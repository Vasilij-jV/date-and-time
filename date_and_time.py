# -*- confit: utf-8 -*-
from datetime import datetime


class SuperDate(datetime):
    _number_month = {
        'Winter': [1, 2, 3],
        'Spring': [4, 5, 6],
        'Summer': [7, 8, 9],
        'Autumn': [10, 11, 12]
    }
    _time_interval = {
        'Morning': [6, 7, 8, 9, 10, 11],
        'Day': [12, 13, 14, 15, 16, 17],
        'Evening': [18, 19, 20, 21, 22, 23],
        'Night': [24, 1, 2, 3, 4, 5]
    }

    def get_season(self):
        for season, number_month in SuperDate._number_month.items():
            if super().month in number_month:
                return season

    def get_time_of_day(self):
        for interval, times in SuperDate._time_interval.items():
            if super().hour in times:
                return interval


superdate = SuperDate(year=2024, month=4, day=16, hour=16)
print(superdate.get_season())
print(superdate.get_time_of_day())
