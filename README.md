# SeisCruST

SeisCruST is a database of spot measurements of global seismic continental crustal structure.

This repository contains continental crustal thickness and seismic velocity estimates derived from 
controlled source seismic refraction (wide-angle) and reflection profiles, and passive source receiver 
function analyses.

For a detailed description of the contents of this database please refer to Stephenson _et al._ (2024).

To contribute data, bug fixes or any other changes, plese see the ***Contributing*** section below.

## Contents

#### Crustal thickness files

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
  - `EARS.csv`:  [Global Earthscope Automated Receiver Survey](http://ds.iris.edu/dms/products/ears/) database.  Note this data is not used in Stephenson _et al._ (2024) but is provided here for completeness.  Data was accessed in June 2022.

#### Crustal velocity and density files

- `CRUSTAL_STRUCTURE/`: This directory contains data related to crustal structure, organized by geographic region and method. Each region directory contains various files and further subdirectories as follows:

        ```
        CRUSTAL_STRUCTURE
        ├── ARABIA
        │   ├── Vp
        │   │   └── RECEIVER_FUNCTION
        │   │       └── CALCULATED_brocher
        │   ├── Vs
        │   │   └── RECEIVER_FUNCTION
        │   │       └── DATA
        │   ├── vs_rho_brocher
        │   │   └── RECEIVER_FUNCTION
        │   └── vs_rho_stephenson_T_DEPENDENT
        │       └── RECEIVER_FUNCTION
        ├── EUROPE
        ├── HUDSON_BAY
        ├── IRAN
        ├── N_AFRICA
        ├── SE_ASIA
        ├── S_AMERICA
        └── USGS_GSC
        ```

  - `ARABIA/`, `EUROPE/`, `HUDSON_BAY/`, `IRAN/`, `N_AFRICA/`, `SE_ASIA/`, `S_AMERICA/`, `USGS_GSC/`, ... : Each of these directories represents a specific geographic region.  The `USGS_GSC` directory contains velocity profiles derived from the United States Geological Survey Global Seismic Catalog (USGS GSC) Inside each region directory, you will find:

    - `Vs`, `vs_rho_stephenson`, `vs_rho_stephenson_T_DEPENDENT`, `vs_rho_brocher`, `Vp`, `vp_rho_stephenson`, `vp_rho_brocher`, `vp_rho_stephenson_T_DEPENDENT`... : These files contain various data related to seismic velocities and converted densities.  Please see Stephenson et al. (2024) and [SMV2rho](https://github.com/sstephenson2/SMV2rho) for details on the methods used to convert to density.  Inside these directories you will find the method name of the seismic approach used to estimate the velocity structure.

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

      There may also be a `CALCULATED_brocher` directory within the `Vp` directory.  This directory contains profiles where `Vp` has been calcualted from the `Vs` profile using [Brocher's (2005)](https://pubs.geoscienceworld.org/ssa/bssa/article-abstract/95/6/2081/146858/Empirical-Relations-between-Elastic-Wavespeeds-and) approach.

#### Bulk crustal property files

- `BULK_CRUSTAL_PROPERTIES`: This directory contains various data files related to bulk crustal properties. Each file represents a specific type of data or method. The files in this directory are:

  - `av_dens_depth_function_T_DEPENDENT.dat`: average contintneal crustal density as a function of depth within the crust as calculated using [`SMV2rho`](https://github.com/sstephenson2/SMV2rho).  Nate the suffix `'T_DEPENDENT'` indicates that they were calculated using the temperature-dependent implementation of this approach.  Please see  [`SMV2rho`](https://github.com/sstephenson2/SMV2rho) and Stephenson _et al._ (2024) for more information.
  - `av_vp_depth_function_T_DEPENDENT.dat`: average contintneal crustal $V_P$ velocity as a function of depth within the crust
  - `av_vp_vs_rho_all_stephenson_T_DEPENDENT.dat`: location, crustal thickness and bulk velocity and density calculated using the temperature-dependent version of the Stephenson _et al._ density conversion.  Please see documentation in [`SMV2rho`](https://github.com/sstephenson2/SMV2rho) and Stephenson _et al._ (2024) for more details.  Columns are:

      | Column Name | Description |
      |-------------|-------------|
      | station     | Station identifier |
      | lon         | Longitude |
      | lat         | Latitude |
      | moho        | Depth of the Moho discontinuity |
      | av_vp       | Average P-wave velocity |
      | av_vs       | Average S-wave velocity |
      | av_rho      | Average density |

  - `av_vs_depth_function_T_DEPENDENT.dat`: average contintneal crustal $V_S$ velocity as a function of depth within the crust
  - `bulk_rho_tc_function_T_DEPENDENT.dat`: Average bulk density as a function of crustal thickness as calculated using the temperature-dependent implementation of [`SMV2rho`](https://github.com/sstephenson2/SMV2rho).
  - `bulk_vp_tc_function_T_DEPENDENT.dat`: Average bulk $V_P$ velocity as a function of crustal thickness.
  - `bulk_vs_tc_function_T_DEPENDENT.dat`: Average bulk $V_S$ velocity as a function of crustal thickness.

#### Referencing files

- `REFERENCES`: This directory contains all references used to compile `SeisCruST`.  Please refer to this reference list for the primary source of any data that you choose to use in your work.  Original studies must be cited as a condition of use of this database.
  -  `SeisCruST_citations.bib`: list of references in BibTeX format.
  -  `SeisCruST_citations.md`: list of citations in markdown.

## Data Sources

The data in this repository is derived from seismic refraction, reflection, and receiver function studies. 
Original sources can be found in [References.tex](References.tex).

A significant minority of crustal thickness constraints and around three quarters of velocity profiles
are taken from the United States Geological Survey's Global Seismic Catalog ([Mooney et al., 2023](https://www.sciencedirect.com/science/article/pii/S0012825223001824)).  
We do not include all data from the USGS GSC database and encourage users to explore that database as well.

## Usage

Simply download the database!

We recommend cloning the database using git

```
git clone https://github.com/sstephenson2/SeisCRUST.git $directory
```

We request that users reference this database and the primary authors of the studies whose data is used.
Users are welcome to add to the database so long as the database and primary sources are referenced as well.  
If you add to the database, we would reccommend that you consider contributing your data to the respository!  See ***Contributing*** below for more information.

Data derived from the Global Seismic Catalog of the United States Geological Survey used in this database
is accompanied by the reference code provided in the original database.  Please refer to ([Mooney et al., 2023](https://www.sciencedirect.com/science/article/pii/S0012825223001824)) for further details.

We encourage users to use the data in conjunction with [SMV2rho](https://github.com/sstephenson2/SMV2rho), a 
tool for loading and processing velocity profiles and for converting them to density using various approaches.  
Please see the documentation in SMV2rho and in Stephenson et al. (2024) for further details.

## Contributing

If you would like to contribute to this database, please contact the authors. We welcome contributions to `SeisCruST` and would be delighted if you choose to upload your spot crustal thickness measurements and 1D velocity profiles!

If you're ready to contribute, here's how you can do it:

1. **Fork the repository**: Click the 'Fork' button at the top right of this page and clone your forked repository to your local machine.

2. **Create a new branch**: From your terminal, create a new branch for the data addition, bug fix or feature you want to work on. You can create a new branch with `git checkout -b branch-name`.

3. **Make your changes**: Make the changes you want to contribute. Whether it is adding new data, fixing a bug, improving documentation, or adding a new feature, we really appreciate feedback, new data and improvements!

4. **Commit your changes**: Once you're done, commit your changes with `git commit -m "Your detailed commit message"`.  Please add as much information as possible to your commit messages.

5. **Push your changes**: Push your changes to your forked repository with `git push origin branch-name`.

6. **Create a pull request**: Go to your forked repository on GitHub and click the 'New pull request' button. Fill out the form and then submit the pull request.

We will take a look at your pull request as soon as we can!

## License

This project is licensed under a CC-BY Creative Commons licence.