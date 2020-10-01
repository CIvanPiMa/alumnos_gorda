import datetime
import xlrd


def make_students_dict(path):

    with xlrd.open_workbook(path) as file:
        data = file.sheet_by_index(0)

    dict_data_names = ['fecha', 'peso', 'talla', ]
    dict_data = {}

    sanitaizer = {
        4: sanitaize_date,
        5: sanitaize_number,
        6: sanitaize_number,
    }

    for j in range(1, data.ncols):
        student_data = []
        name = sanitaize_name(data.cell_value(j, 3))

        if name in dict_data:
            continue

        for i in range(4, 7):
            value = data.cell_value(j, i)
            clean_value = sanitaizer[i](value)
            student_data.append(clean_value)

        dict_data[name] = dict(zip(dict_data_names, student_data))

    return dict_data


def sanitaize_date(str_date):
    try:
        return datetime.datetime.strptime(str_date, '%d/%m/%Y').date()
    except:
        return None


def sanitaize_number(number):
    number = number
    if type(number) == float and number > 3:
        return number
    return None


def sanitaize_name(name):
    if len(name) < 10:
        return None

    name = name.strip()
    name = name.replace('\n', ' ')
    name = name.capitalize()

    return name
