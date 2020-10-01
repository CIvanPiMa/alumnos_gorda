import os
from utils import *
from imc import *

os.chdir('./data')
files = [file for file in os.listdir() if file[-1] == 'x']

dict_data = {}
for file in files:
    dict_data = {**dict_data, **make_students_dict(file)}

for name, data in dict_data.items():
    imc, interp = interpret_imc_kids(
        data['talla'], data['peso'], data['fecha'], 'm')
    dict_data[name] = {**dict_data[name], **{'imc': imc, 'interp': interp}}

for name, data in dict_data.items():
    mesage = print(name, *data.values(), sep=',')
