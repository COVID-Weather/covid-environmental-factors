import cdsapi

c = cdsapi.Client()

filepath_2019 = '../data/thermodynamic_variables_2019.nc'
filepath_2020 = '../data/thermodynamic_variables_2020.nc'

thermodynamic_variables = ['2m_dewpoint_temperature', '2m_temperature', 'surface_pressure']

every_two_hours = [
                   '00:00', '02:00', '04:00',
                   '06:00', '08:00', '10:00',
                   '12:00', '14:00', '16:00',
                   '18:00', '20:00', '22:00',
                  ]

every_day = [
             '01', '02', '03',
             '04', '05', '06',
             '07', '08', '09',
             '10', '11', '12',
             '13', '14', '15',
             '16', '17', '18',
             '19', '20', '21',
             '22', '23', '24',
             '25', '26', '27',
             '28', '29', '30',
             '31',
             ]

# Sent requests via the CDS API to download data for 2019 and 2020
# Setup instructions here: https://cds.climate.copernicus.eu/api-how-to
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
              'format': 'netcdf',
            'variable': thermodynamic_variables,
                'year': '2020',
               'month': ['01', '02', '03'],
                'time': every_two_hours,
                 'day': every_day,
    },
    filepath_2019)


c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
              'format': 'netcdf',
            'variable': thermodynamic_variables,
                'year': '2019',
               'month': ['11', '12'],
                'time': every_two_hours,
                 'day': every_day,
    },
    filepath_2020)
