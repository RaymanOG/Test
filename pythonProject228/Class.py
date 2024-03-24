import openpyxl



class TheoryDB:

    def __init__(self, lvl: str, global_them=None):
        self.lvl = lvl
        self.global_them = global_them

    @staticmethod
    def __fail(name_fail):
        with open(name_fail, 'r', encoding='utf-8') as f:
            return f.read()

    def __thema(self):
        wb = openpyxl.load_workbook(rf'.\Theory\{self.lvl}\razdel.xlsx')
        ws = wb.active
        themy = {}
        for row in ws.values:
            themy[row[0]] = row[1], row[2]
        return themy

    def full_opisanie(self):
        lst = []
        for i in self.__thema().values():
            lst.append(i[0])
        return lst

    def text(self, global_them):
        try:
            if self.global_them is None:
                self.global_them = global_them
            return self.__fail(rf'.\Theory\{self.lvl}\{self.global_them}.txt')
        except FileNotFoundError:
            return "Файл с текстом не найден"
        except Exception as e:
            return f"Произошла ошибка: {str(e)}"

    def image(self, global_them):
        if self.global_them is None:
            self.global_them = global_them
        try:
            return self.__thema()[self.global_them][1]
        except KeyError:
            return "Изображение не найдено"
        except TypeError:
            return "Ошибка формата изображения"


A1 = TheoryDB('A1')
print(A1.image(1))