__author__ = 'ajitkumar'


def read_input_from_file(file_name):
    with open(file_name) as _file:
        lines = _file.read().splitlines()
    lines = [line.split(",") for line in lines]
    lines = [[int(line[0]), line[1].strip(), line[2].strip(), line[3].strip(), int(line[4]), float(line[5])] for line in lines]
    return lines

