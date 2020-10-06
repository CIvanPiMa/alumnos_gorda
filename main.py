import os
from utils import *
from imc import *

if __name__ == '__main__':

    os.chdir('./data')
    files = [file_name for file_name in os.listdir() if '.xlsx' in file_name]

    # All the students data {student_name: {sexo:char, fecha:datetype, ...}, ...}
    dict_data = {}
    for file in files:
        dict_data = {**dict_data, **make_students_dict(file)}

    for name, data in dict_data.items():
        imc, interp = interpret_imc_kids(
            data['talla'], data['peso'], data['fecha'], data['sexo']
        )
        # Join all the data in one dict
        dict_data[name] = {**dict_data[name], **{'imc': imc, 'interp': interp}}

    # print the data in a pretty CSV way
    for name, data in dict_data.items():
        mesage = print(name, *data.values(), sep=',')
