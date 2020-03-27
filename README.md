# Environmental analysis of COVID-19 transmission rates
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hdrake/covid-environmental-factors/master)

---
## Repository structure

`/scripts/` contains bash and python scripts for downloading ERA5 atmospheric reanalysis data and COVID-19 clinical data.

`/data/` contains processed data and is a placeholder directory that holds raw data files too large to be version-controlled.

`/notebooks/` contains the key python notebooks used for pre-processing, analysis, and plotting.

#### Notebook naming conventions
We use the following prefix conventions for naming notebooks:
- `0_`  for pre-processing locally-downloaded raw data (large > 10 GB) and producing locally-saved interim data (10 MB < medium < 10 GB)
- `1_`  for analysis of raw and interim data and producing plot-ready processed data (small < 10 Mb, pushed to github)
- `2_`  post-processing and making publication-quality plots (saved in `/figures/`)
- `T_`  testing and code development (avoid using in `master` branch)

---
## Programming environment

The python packages necessary for running the python scripts and jupyter notebooks included here are listed in the `environment.yml` file. We recommend using [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) to install these packages using the command:
```bash
conda env update -f environmental.yml
```
and activating the environment with
```bash
conda activate covid-weather
```

---
## Downloading raw data

#### Downloading JHU CSSE COVID-19 epidemiological data

The [`/scripts/get_covid19_data.sh`](https://github.com/COVID-Weather/covid-environmental-factors/blob/master/scripts/get_covid19_data.sh) script clones the JHU CSSE dataset into the `/data/` folder.

#### Downloading ERA5 reanalysis data

Our scripts use the [Climate Data Store (CDS) API](https://cds.climate.copernicus.eu/#!/home) and require an account. [These instructions](https://cds.climate.copernicus.eu/api-how-to) describe how to configure your account key and use the python app, which is installed via `pip install cdsapi`.

[ERA5 documentation](https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation)

[Near-surface meterological variables in ERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview) (and [quality-controlled bias corrected fields through 2018](https://cds.climate.copernicus.eu/cdsapp#!/dataset/derived-near-surface-meteorological-variables?tab=overview))

Some variables of interest:

Variable | Units | API name for python script
-- | -- | -- |
Altitude | meters | `grid_point_altitude`
Temperature | Kelvin | `near_surface_air_temperature`
Specific humidity | kg water / kg air | `near_surface_specific_humidity`
Pressure | Pascals | `surface_air_pressure`
Rainfall | kg-meters^2 / s | `rainfall_flux`
            
[Instructions](https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation#ERA5:datadocumentation-Computationofnear-surfacehumidityandsnowcover) for computing the near-surface specific and relative humidities, which are not archived diagnostics, from the near-surface temperature, dew point temperature, and surface pressure.

---
## Contributor guidelines

Contributors to this repository should use the following workflow to ease collaboration:
1) [Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) the repository
2) Create [a new branch](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches) with a name that reflects your intended contribution
3) Make local changes to your branch, following the repository structure and naming conventions
4) Add, commit, and push the local changes to your branch to your fork
5) Open a pull request and request review from a relevant co-contributor
6) Celebrate as your changes are approved by a reviewer and merged into the master branch!
