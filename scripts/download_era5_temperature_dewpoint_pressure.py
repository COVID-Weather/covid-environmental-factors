import cdsapi

c = cdsapi.Client()

filepath = '../data/thermodynamic_variables'

thermodynamic_variables = ['2m_dewpoint_temperature', '2m_temperature', 'surface_pressure']

every_two_hours = ["{:02d}:00".format(i) for i in range(0, 24, 2)]
every_hour = ["{:02d}:00".format(i) for i in range(24)]
every_day = ["{:02d}".format(i) for i in range(32)]

# Sent requests via the CDS API to download data for 2019 and 2020
# Setup instructions here: https://cds.climate.copernicus.eu/api-how-to
c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2019',
                   'month': ['11'],
                    'time': every_hour,
                     'day': every_day}, '{}_11_2019.nc'.format(filepath))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2019',
                   'month': ['12'],
                    'time': every_hour,
                     'day': every_day}, '{}_12_2019.nc'.format(filepath))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2020',
                   'month': ['01'],
                    'time': every_hour,
                     'day': every_day}, '{}_01_2020.nc'.format(filepath))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2020',
                   'month': ['02'],
                    'time': every_hour,
                     'day': every_day}, '{}_02_2020.nc'.format(filepath))

c.retrieve('reanalysis-era5-single-levels', 
           {'product_type': 'reanalysis',
                  'format': 'netcdf',
                'variable': thermodynamic_variables,
                    'year': '2020',
                   'month': ['03'],
                    'time': every_hour,
                     'day': every_day}, '{}_03_2020.nc'.format(filepath))
