#!/usr/bin/env python3

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

# check for duplicates.  Note that this may remove a very small number of
#    data where there is truly a duplicated measurement.
n_duplicates = crust_df_Na_corrected.duplicated().sum()
print(f"\n dropping {n_duplicates} duplicated entries")

crust_df_Na_corrected_no_duplicates = crust_df_Na_corrected.drop_duplicates().replace('-', np.nan)


