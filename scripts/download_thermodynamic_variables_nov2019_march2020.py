import cdsapi

c = cdsapi.Client()

single_level_variables = [
                          '2m_dewpoint_temperature', 
                          '2m_temperature', 
                          'surface_pressure'
                         ]

pressure_level = '1000' # download only specific humidity for now

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

all_day = [
           '00:00', '01:00', '02:00',
           '03:00', '04:00', '05:00',
           '06:00', '07:00', '08:00',
           '09:00', '10:00', '11:00',
           '12:00', '13:00', '14:00',
           '15:00', '16:00', '17:00',
           '18:00', '19:00', '20:00',
           '21:00', '22:00', '23:00',
          ]

time_frame = {
              '2019': {
                        '10': every_day,
                        '11': every_day[:30],
                        '12': every_day
                       },

              '2020': {
                        '1': every_day,
                        '2': every_day[:29],
             #           '3': every_day[:20]
                       }
              }

for year, month_days in time_frame.items():
    for month, days in month_days.items():
        c.retrieve(
            'reanalysis-era5-single-levels',
            {
             'product_type': 'reanalysis',
                   'format': 'netcdf',
                 'variable': single_level_variables,
                     'year': year,
                    'month': month,
                      'day': days,
                     'time': all_day    
                },
            '../data/single_level_data_{}_{}.nc'.format(year, month))


        c.retrieve(
            'reanalysis-era5-pressure-levels',
            {
               'product_type': 'reanalysis',
                     'format': 'netcdf',
                   'variable': 'specific_humidity',
             'pressure_level': pressure_level,
                       'year': year,
                      'month': month,
                        'day': days,
                       'time': all_day    
            },
            '../data/pressure_level_{}_data_{}_{}.nc'.format(year, month))
