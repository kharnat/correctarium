import datetime
import businesstimedelta

expansion = input("Введите расширение файла: ")
num_of_char = float(input("Введите количество символов: "))
lang = input("Введите язык текста(eng, рус или укр): ")

price_one_eng = 0.12
price_one_ru_ukr = 0.05
char_in_hour_eng = 333
char_in_hour_ru_ukr = 1333

price = 0
time = 0

if lang == 'eng':
    price = num_of_char * price_one_eng
    hours = round(0.5 + num_of_char / char_in_hour_eng)

    if price < 120:
        price = 120
    else:
        price

    if hours < 1:
        hours = 1
    else:
        hours

else:
    price = num_of_char * price_one_ru_ukr
    hours = round(0.5 + num_of_char / char_in_hour_ru_ukr)

    if price < 50:
        price = 50
    else:
        price

    if hours < 1:
        hours = 1
    else:
        hours

if expansion not in ['doc', 'docx', 'rtf']:
    price = price + price * 0.2
    hours = hours + hours * 0.2

print('Стоимость текста равна ' + str(price) + 'грн')
print('Количество часов работы равно ' + str(hours))

workday = businesstimedelta.WorkDayRule(
    start_time=datetime.time(10),
    end_time=datetime.time(19),
    working_days=[0, 1, 2, 3, 4])
start_date = datetime.datetime.today()
start_weekday = start_date.weekday()
deadline = start_date + businesstimedelta.BusinessTimeDelta(workday, hours=hours)
deadline_weekday = deadline.weekday()

format_start_date = format(start_date, "%d/%m/%y %H:%M")
format_deadline = format(deadline, "%d/%m/%y %H:%M")

print(format_start_date, "Weekday: ", start_weekday)
print(format_deadline, "Weekday: ", deadline_weekday)
