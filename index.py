import xlrd

path = "data/5b.xlsx"

with xlrd.open_workbook(path) as file:
    data = file.sheet_by_index(0)

print(data.nrows)


print("\n"*5)
