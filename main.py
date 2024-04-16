import smtplib as sm
import datetime as dt
import pandas as pd
import random

HOST_EMAIL = 'dz.danylo@gmail.com'
HOST_PASS = 'sahu imqp pdui ikos'
TEMPLATES_FILES = ['msg_templates/letter_1.txt', 'msg_templates/letter_2.txt', 'msg_templates/letter_3.txt']

bd_data = pd.read_csv('birthdays.csv')
now_day = dt.datetime.now().day
now_month = dt.datetime.now().month
people = bd_data[(bd_data.day == now_day) & (bd_data.month == now_month)]

if not people.empty:
    for index, row in people.iterrows():
        with open(random.choice(TEMPLATES_FILES)) as file:
            message = file.read().replace('[NAME]', row['name'].strip())

        with sm.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=HOST_EMAIL, password=HOST_PASS)
            connection.sendmail(
                from_addr=HOST_EMAIL,
                to_addrs=row.email,
                msg=f'Subject:Happy birthday!\n\n{message}')
