import openpyxl
def tilt(a:int, b:str):
    wb = openpyxl.load_workbook('ляляля.xlsx')
    ws = wb.active
    slowar = {}
    slowar2 = {}
    for i in ws.values:
        slowar[i[0]] = [i[1]]
        slowar2[i[0]] = i[2]
    if a in slowar:
        if b == slowar2[a]:
            return("Верно")
        else:
            return("Переделывай")
    else:
        return("Нет такого")

a = int(input("Номер предложения: "))
b = input("Ваш ответ: ")

print(tilt(a, b))

