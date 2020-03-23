# Environmental analysis of COVID-19 infection rates


## Downloading data

The directory `/scripts` contains python scripts for downloading ERA5 atmospheric reanalysis data and COVID-19 clinical data.

### Downloading ERA5 reanalysis data

[ERA5 documentation](https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation)

[Near-surface meterological variables in ERA5](https://cds.climate.copernicus.eu/cdsapp#!/dataset/derived-near-surface-meteorological-variables?tab=overview)

Some variables of interest:

Variable | Units | API name for python script
-- | -- | -- |
Altitude | meters | `grid_point_altitude`
Temperature | Kelvin | `near_surface_air_temperature`
Specific humidity | kg water / kg air | `near_surface_specific_humidity`
Pressure | Pascals | `surface_air_pressure`
Rainfall | kg-meters^2 / s | `rainfall_flux`
            
