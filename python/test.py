import openpyxl


wb = openpyxl.load_workbook("2021sbjct.xlsx")
sheet = wb.worksheets[0]

dic = []
dic2 = {}
n = 0

for row in sheet.rows:
    pass


def find(v):
    print(dic2[v])
    print(dic[dic2[v]])
    return dic[dic2[v]]


def find_all():
    print(dic)
    return dic


def find_num(v):
    for key, value in dic2.items():
        if value == v:
            print(key)
            return key
    return -1
