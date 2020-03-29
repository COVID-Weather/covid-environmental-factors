import cdsapi, os

c = cdsapi.Client()

# ERA5 reanalysis data will be downloaded into ../data
datadir = os.path.join('..', 'data/raw/environmental')
cmd = f"mkdir -p {datadir}"
os.system(cmd)

prefix = 'thermodynamic_variables'
pathprefix = os.path.join(datadir, prefix)

env_prefix = 'environmental_variables'
env_pathprefix = os.path.join(datadir, env_prefix)

# Download temperature, pressure, and dewpoint temperature to permit humidity calculation
thermodynamic_variables = ['2m_dewpoint_temperature', '2m_temperature', 'surface_pressure']
environmental_variables = ['downward_uv_radiation_at_the_surface', 'surface_solar_radiation_downwards', 'total_precipitation', 'total_sky_direct_solar_radiation_at_surface']

# Download data every day in the specified months
every_day = ["{:02d}".format(i) for i in range(32)]

# Download hourly data in the specified days
every_hour = ["{:02d}:00".format(i) for i in range(24)]
every_two_hours = ["{:02d}:00".format(i) for i in range(0, 24, 2)]
frequency = every_hour # change this to download less-frequent data

# Send requests via the CDS API to download data for 2019 and 2020.
#
# Setup instructions here: https://cds.climate.copernicus.eu/api-how-to
#
# Global data is downloaded for 11/2019 to 03/2020.

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2019',
                   'month': ['11'],
                    'time': frequency,
                     'day': every_day}, '{}_11_2019.nc'.format(pathprefix))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2019',
                   'month': ['12'],
                    'time': frequency,
                     'day': every_day}, '{}_12_2019.nc'.format(pathprefix))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2020',
                   'month': ['01'],
                    'time': frequency,
                     'day': every_day}, '{}_01_2020.nc'.format(pathprefix))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2020',
                   'month': ['02'],
                    'time': frequency,
                     'day': every_day}, '{}_02_2020.nc'.format(pathprefix))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2020',
                   'month': ['03'],
                    'time': frequency,
                     'day': every_day}, '{}_03_2020.nc'.format(pathprefix))


### Environmental variables
c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': environmental_variables,
                    'year': '2019',
                   'month': ['11'],
                    'time': frequency,
                     'day': every_day}, '{}_11_2019.nc'.format(env_pathprefix))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': environmental_variables,
                    'year': '2019',
                   'month': ['12'],
                    'time': frequency,
                     'day': every_day}, '{}_12_2019.nc'.format(env_pathprefix))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': environmental_variables,
                    'year': '2020',
                   'month': ['01'],
                    'time': frequency,
                     'day': every_day}, '{}_01_2020.nc'.format(env_pathprefix))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': environmental_variables,
                    'year': '2020',
                   'month': ['02'],
                    'time': frequency,
                     'day': every_day}, '{}_02_2020.nc'.format(env_pathprefix))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': environmental_variables,
                    'year': '2020',
                   'month': ['03'],
                    'time': frequency,
                     'day': every_day}, '{}_03_2020.nc'.format(env_pathprefix))
