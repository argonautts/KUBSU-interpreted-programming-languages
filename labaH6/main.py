import csv
from translate import Translator
from datetime import *
from dateutil.parser import parse

FIRST_PATH = '4-1.csv'
SECOND_PATH = '4-2.csv'

# Найти количество неудачных попыток прохождения теста, которые
# выполнялись позже заданной даты. Вывести список людей, не прошедших тест.

def main():
    with open(FIRST_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_first = list(reader)
    with open(SECOND_PATH, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data_second = list(reader)

    unsuccessfulAttempt = 0
    fio = []
    d2, m2, y2 = [int(x) for x in input("Enter date(DD/MM/YYYY) : ").split('/')]
    # 05/04/2017
    # 17/05/2017
    resultUser = date(y2, m2, d2)
    c = 0

    for row in data_first:
        c += 1
        print("[", c, "/ 82 ]", " loading...")
        surname = row["Фамилия"]
        name = row["Имя"]
        data = row["Завершено"]
        mark = row["Оценка/10,00"]
        mark = mark.replace(',', '.')

        if data != '-' and data != '':
            translator = Translator(from_lang="ru", to_lang="en")
            dataTranslate = translator.translate(data)
            dataParse = parse(dataTranslate)
            strDataParse = str(dataParse)
            resultStrData = strDataParse[:11] + strDataParse[19:]
            y1, m1, d1 = [int(x) for x in resultStrData.split('-')]
            resultCsv = date(y1, m1, d1)

            if resultCsv > resultUser:
                if mark == '-':
                    unsuccessfulAttempt += 1
                    fio.append(surname + " " + name)
                elif float(mark) < 8.0:
                    unsuccessfulAttempt += 1
                    fio.append(surname + " " + name)

        elif data == '-' or data == '':
            if mark == '-':
                unsuccessfulAttempt += 1
                fio.append(surname + " " + name)
            elif float(mark) < 8.0:
                unsuccessfulAttempt += 1
                fio.append(surname + " " + name)


    for row in data_second:
        c += 1
        print("[", c, "/ 82 ]", " loading...")
        surname = row["Фамилия"]
        name = row["Имя"]
        data = row["Завершено"]
        mark = row["Оценка/100,00"]
        mark = mark.replace(',', '.')

        if data != '-' and data != '':
            translator = Translator(from_lang="ru", to_lang="en")
            dataTranslate = translator.translate(data)
            dataParse = parse(dataTranslate)
            strDataParse = str(dataParse)
            resultStrData = strDataParse[:11] + strDataParse[19:]
            y1, m1, d1 = [int(x) for x in resultStrData.split('-')]
            resultCsv = date(y1, m1, d1)

            if resultCsv > resultUser:
                if mark == '-':
                    unsuccessfulAttempt += 1
                    fio.append(surname + " " + name)
                elif float(mark) < 75.00:
                    unsuccessfulAttempt += 1
                    fio.append(surname + " " + name)

        elif data == '-' or data == '':
            if mark == '-':
                unsuccessfulAttempt += 1
                fio.append(surname + " " + name)
            elif float(mark) < 75.00:
                unsuccessfulAttempt += 1
                fio.append(surname + " " + name)


    print("Количество неудачных попыток: ", unsuccessfulAttempt)
    print("Не прошли тест: ", fio)


if __name__ == '__main__':
    main()
