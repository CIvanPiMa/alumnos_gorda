import datetime
import xlrd


def make_students_dict(path, dict_data={}):
    """
    Given the .xlsx file takes the students data in the first sheet and puts them in a dict 
    """

    with xlrd.open_workbook(path) as file:
        # Takes the first sheet in the file
        data = file.sheet_by_index(0)

    dict_data_names = ['sexo', 'fecha', 'peso', 'talla', ]

    sanitaizer = {
        0: sanitaize_sex,
        2: sanitaize_date,
        3: sanitaize_number,
        4: sanitaize_number,
    }

    for row in range(1, data.nrows):

        name = sanitaize_name(data.cell_value(row, 1))
        if name in dict_data:
            continue

        student_data = []
        for col in range(5):
            if col == 1:
                continue
            value = data.cell_value(row, col)
            clean_value = sanitaizer[col](value)
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
    if type(number) == float:
        return number
    return None


def sanitaize_name(name):

    name = name.strip().replace('\n', ' ').title()

    if len(name) == 0:
        return None

    return name


def sanitaize_sex(sex):

    sex = sex.strip().lower()

    if len(sex) < 1:
        return None

    return sex
