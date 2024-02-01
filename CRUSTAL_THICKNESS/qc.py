#!/usr/bin/env python3

# This simple script is used to clean the seisCRUST database.  It is not 
# intended to be an exhaustive QC, but rather a skeleton to catch some of 
# the more obvious errors that may have been introduced during the 
# compilation of the database.

# Users are encouraged to use this script as a template for their own QC if
#  they add new data to the seisCRUST database.

#  steps are as follows:
#  1. Convert all data to numeric values, coercing various different NaN fields
#     to NaN if unable to directly convert into NaN
#  2. Catch data input errors with misplaced decimal point
#  3. Check for direct duplications
#  4. Remove direct duplications
#  5. Save QC'd database

# Other QC steps that could be added:
#  1. Check for duplicate entries that are not direct duplicates.  For example,
#     if the reference string is almost identical, but not quite, then this
#     could be a duplicated entry.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load in data
crust_df = pd.read_csv("seisCRUST_thickness.csv")

# convert data to numeric values, coercing various different NaN fields to NaN
#   if unable to directly convert into NaN
H_Na_corrected = pd.to_numeric(crust_df["MOHO_DEPTH"], errors='coerce')
K_Na_corrected = pd.to_numeric(crust_df["VP/VS"], errors='coerce')
lat_Na_corrected = pd.to_numeric(crust_df["LAT"], errors='coerce')
lon_Na_corrected = pd.to_numeric(crust_df["LONG"], errors='coerce')

# catch data input errors with misplaced decimal point
condition = K_Na_corrected > 100
print(f"correcting \n\n {K_Na_corrected.loc[condition]} \n\n to \n\n {K_Na_corrected.loc[condition] / 100}\n")
K_Na_corrected.loc[condition] = K_Na_corrected.loc[condition] / 100

# catch data input errors with misplaced decimal point
condition = K_Na_corrected > 10
print(f"correcting \n\n {K_Na_corrected.loc[condition]} \n\n to \n\n {K_Na_corrected.loc[condition] / 10}\n")
K_Na_corrected.loc[condition] = K_Na_corrected.loc[condition] / 10

# recombine dataframe and check for direct duplications
crust_df_Na_corrected = pd.concat([lon_Na_corrected, 
                                   lat_Na_corrected, 
                                   H_Na_corrected, 
                                   K_Na_corrected,
                                   crust_df["METHOD"],
                                   crust_df["SUB-METHOD"],
                                   crust_df["AUTHOR"],
                                   crust_df["V_PROFILE(Y/N)"],
                                   crust_df["LOCATION"],
                                   crust_df["SUB_LOCATION"]], axis = 1)

# Check for duplicates.  Note that this may remove a very small number of
#    data where there is truly a duplicated measurement.  Users should
#    check for this and manually add these data back in if necessary or
#    write a new QC procedure.
n_duplicates = crust_df_Na_corrected.duplicated().sum()
print(f"\n dropping {n_duplicates} duplicated entries \n")

# remove duplicates
crust_df_Na_corrected_no_duplicates = crust_df_Na_corrected.drop_duplicates().replace('-', np.nan)

print(f"database has {len(crust_df_Na_corrected_no_duplicates)} entries \n")

# plot a scatterplot of moho depth and vp/vs
sns.scatterplot(data=crust_df_Na_corrected_no_duplicates, x="MOHO_DEPTH", y="VP/VS")
plt.show()

# save QC'd database
crust_df_Na_corrected_no_duplicates.to_csv("seisCRUST_thickness_QC.csv", index=False, na_rep="-")