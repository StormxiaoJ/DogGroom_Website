import sqlite3
import threading
from datetime import *
import smtplib


def send(email_address):
    content = 'Hello ,the email is from Tom Dog Groom. \nPlease notice that Your dog cleaning service will arrive on time tomorrow.'
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()
    mail.starttls()
    mail.login('DogGroomEO8', 'DogGroomEO8!')
    mail.sendmail('DogGroomEO8', email_address, content)
    mail.close()


def get_emaillist():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    emaillist = []
    for row in c.execute(
            'SELECT date, starttime, email  FROM DogGroom_appointment INNER JOIN Account_user WHERE DogGroom_appointment.client_id = Account_user.id'):
        if tobemailed(row[0], row[1]):
            emaillist.append(row)

    return emaillist


def tobemailed(datestr, timestr):
    # datestr = 2018-05-21
    # timestr = 15:30
    y, m, d = int(datestr[:4]), int(datestr[5:7]), int(datestr[8:])
    h, mm = int(timestr[:2]), int(timestr[3:])
    scheduletime = datetime(y, m, d, h, mm, 0)
    _nowtime = str(datetime.now())
    yn, mn, dn, hn, mmn = int(_nowtime[:4]), int(_nowtime[5:7]), int(_nowtime[8:10]), int(_nowtime[11:13]), int(
        _nowtime[14:16])
    nowtime = datetime(yn, mn, dn, hn, mmn, 0)
    ttlsnds = (scheduletime - nowtime).total_seconds()
    if ttlsnds <= 24 * 3600:
        return True


def send_email():
    sent_list = []
    while True:
        mlist = get_emaillist()
        for m in mlist:
            if m not in sent_list:
                print(m)
                send(m)
                sent_list.append(m)
                break


if __name__ == '__main__':
    thr = threading.Thread(target=send_email)
    thr.start()