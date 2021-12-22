import datetime
import businesstimedelta
def calculation(start_date, expansion, num_of_char, lang):

    price_one_eng = 0.12
    price_one_ru_ukr = 0.05
    char_in_hour_eng = 333
    char_in_hour_ru_ukr = 1333


    price = 0
    time = 0


    if lang == 'eng':
        price = float(num_of_char) * price_one_eng
        hours = round(0.5 + float(num_of_char) / char_in_hour_eng)

        if price < 120:
            price = 120
        else:
            price

        if hours < 1:
            hours = 1
        else:
            hours

    else:
        price = float(num_of_char) * price_one_ru_ukr
        hours = round(0.5 + float(num_of_char) / char_in_hour_ru_ukr)

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

    workday = businesstimedelta.WorkDayRule(
        start_time=datetime.time(10),
        end_time=datetime.time(19),
        working_days=[0, 1, 2, 3, 4])

    start_weekday = start_date.weekday()
    deadline = start_date + businesstimedelta.BusinessTimeDelta(workday, hours=hours)
    deadline_weekday = deadline.weekday()
    format_deadline = format(deadline, "%y-%m-%d %H:%M")

    return {'deadline': format_deadline,
            'cost': price,
            'hours': hours
            }

def test_calculation_1():
    # start tuesday 01/07/21 at 09:59
    # deadline tuesday 01/07/21 at 11:00
    start_date = datetime.datetime(2021, 7, 1, 9, 59)
    assert calculation(start_date,'doc', '1000', 'рус') == {'deadline': '21-07-01 11:00',
                                                 'cost': 50.0,
                                                 'hours':1
    }

def test_calculation_2():
    # start tuesday 01/07/21 at 19:00
    # deadline friday 02/07/21 at 14:00
    start_date = datetime.datetime(2021, 7, 1, 19, 00)
    assert calculation(start_date,'doc', '1200', 'eng') == {'deadline': '21-07-02 14:00',
                                                 'cost': 144.0,
                                                 'hours':4
    }

def test_calculation_3():
    # start friday 02/07/21 at 20:45
    # deadline monday 05/07/21 at 14:48
    # format "txt" ---> +20% to cost and hours
    start_date = datetime.datetime(2021, 7, 2, 20, 45)
    assert calculation(start_date,'txt', '1200', 'eng') == {'deadline': '21-07-05 14:48',
                                                 'cost': 172.8,
                                                 'hours': 4.8
    }

def test_calculation_4():
    # start tuesday 01/07/21 at 18:19
    # deadline monday 02/07/21 at 15:19
    # format "txt" ---> +20% to cost and hours
    start_date = datetime.datetime(2021, 7, 1, 18, 19)
    assert calculation(start_date,'txt', '5600', 'укр') == {'deadline': '21-07-02 15:19',
                                                 'cost': 336.0,
                                                 'hours': 6.0
    }

