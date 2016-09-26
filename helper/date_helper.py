__author__ = 'ajitkumar'


def convert_to_epoch_time(time):
    from datetime import datetime
    return datetime.strptime(time, "%Y-%m-%d %H:%M:%S")

