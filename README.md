# SeisCruST

SeisCruST is a database of spot measurements of global seismic continental crustal structure.

This repository contains continental crustal thickness and seismic velocity estimates derived from 
controlled source seismic refraction (wide-angle) and reflection profiles, and passive source receiver 
function analyses.

For a detailed description of the contents of this database please refer to Stephenson et al. (2024).

## Contents

- `CRUSTAL_THICKNESS/`: This directory contains data files related to crustal thickness.
  - `seisCRUST.csv`: Crustal thickness data table. The structure of the file is as follows:

      | Column Name | Description |
      |-------------|-------------|
      | LONG        | Longitude |
      | LAT         | Latitude |
      | MOHO_DEPTH  | Depth of the Moho discontinuity |
      | VP/VS       | Ratio of P-wave to S-wave velocities |
      | METHOD      | Method used to obtain the data |
      | SUB-METHOD  | Sub-method used to obtain the data |
      | AUTHOR      | Author of the data |
      | V_PROFILE(Y/N) | Indicates if a velocity profile is available (Y) or not (N) |
      | LOCATION    | General geographic location where the data were obtained |
      | SUB_LOCATION | More specific geographic location where the data were obtained |

  - `QC.py`: A skeleton python3 program for checking for basic quality issues in the
               the database.

- `CRUSTAL_STRUCTURE/`: This directory contains data related to crustal structure, organized by geographic region and method. Each region directory contains various files and further subdirectories as follows:

  - `ARABIA/`, `EUROPE/`, `HUDSON_BAY/`, `IRAN/`, `N_AFRICA/`, `SE_ASIA/`, `S_AMERICA/`, `USGS_GSC/`, ... : Each of these directories represents a specific geographic region.  The `USGS_GSC` directory contains velocity profiles derived from the United States Geological Survey Global Seismic Catalog (USGS GSC) Inside each region directory, you will find:

    - `Vs`, `vs_rho_stephenson`, `vs_rho_stephenson_T_DEPENDENT`, `vs_rho_brocher`, `Vp`, `vp_rho_stephenson`, `vp_rho_brocher`, `vp_rho_stephenson_T_DEPENDENT`... : These files contain various data related to seismic velocities and converted densities.  Please see Stephenson et al. (2024) and [SMV2rho](https://github.com/sstephenson2/SMV2rho) for details on the methods used to convert to density.  Inside these directories you will find the method name of the seismic approach used to estimate the velocity structure:

    - `RECEIVER_FUNCTION/`, `REVERSED_REFRACTION/`... : These directories represent the method used to obtain the data. Inside each method directory, there is a `DATA/` directory which contains the actual data files (.dat suffix). The structure of these data files is as follows:

      ```
      profile_name
      lon lat
      moho_depth
      vs1 -z1
      vs2 -z2
      .    .
      .    .
      .    .
      ```

      Where `profile_name` is the name of the seismic profile, `lon` and `lat` are the longitude and latitude of the profile, `moho_depth` is the depth of the Moho discontinuity, and `vs1`, `vs2`, `-z1`, `-z2` are the seismic velocities and depths at various points.

## Data Sources

The data in this repository is derived from seismic refraction, reflection, and receiver function studies. 
Original sources can be found in [References.tex](References.tex).

A significant minority of crustal thickness constraints and around three quarters of velocity profiles
are taken from the United States Geological Survey's Global Seismic Catalog ([Mooney et al., 2023](https://www.sciencedirect.com/science/article/pii/S0012825223001824)).  
We do not include all data from the USGS GSC database and encourage users to explore that database as well.

## Usage

Simply download the database!

We request that users reference this database and the primary authors of the studies whose data is used.
Users are welcome to add to the database so long as the database and primary sources are referenced as well.

Data derived from the Global Seismic Catalog of the United States Geological Survey used in this database
is accompanied by the reference code provided in the original database.  Please refer to ([Mooney et al., 2023](https://www.sciencedirect.com/science/article/pii/S0012825223001824)) for further details.

We encourage users to use the data in conjunction with [SMV2rho](https://github.com/sstephenson2/SMV2rho), a 
tool for loading and processing velocity profiles and for converting them to density using various approaches.  
Please see the documentation in SMV2rho and in Stephenson et al. (2024) for further details.

## Contributing

If you would like to contribute to this database, please contact the authors.  We welcome contributions
to `SeisCruST` and would be delighted if you choose to upload your spot measurements and 1D velocity
profiles!

## License

This project is licensed under the CC-By Creative Commons licence.