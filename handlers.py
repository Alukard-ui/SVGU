# *- coding: utf-8 -*

import re
from models import Pairs
from pony.orm import db_session,select
import datetime

@db_session
def group_handler_Schedule(text):
    text = 'Уважаемы товарищи предлагаю ознакомистся с планом занятий на текуший день и завтра\n' \
           'Ваша группа ИС/б-21-3-о\n\n' \
           'На сегодня\n\n'
    _day = datetime.datetime.today().weekday()+1
    week = int(datetime.date.today().strftime("%V")) % 2 == 0
    text += sort(_day,week)
    text += 'На завтра\n\n'
    text += sort(_day+1,week)
    return text


def sort(_day,week):
    if _day == 7:
        return "пар нет"
    astext =''
    even = select(u.id for u in Pairs if u.day_of_week == _day)
    for i in even:
        Pairss = Pairs.get(id=i)
        if Pairss.even_week == week:
            if  Pairss.ordinal == 1:
                astext += "8:30 ~ 10:00\n1."
            elif Pairss.ordinal == 2:
                astext += "10:10 ~ 11:40\n2."
            elif Pairss.ordinal == 3:
                astext += "11:50 ~ 13:20\n3."
            elif Pairss.ordinal == 4:
                astext += "14:00 ~ 15:30\n4."
            elif Pairss.ordinal == 5:
                astext += "15:40 ~ 17:10\n5."
            elif Pairss.ordinal == 6:
                astext += "17:20 ~ 18:50\n6."
            elif Pairss.ordinal == 7:
                astext += "19:00 ~ 20:30\n7."
            astext +=  Pairss.lesson+'\n'+'  '+Pairss.teacher+'\n  '+Pairss.type+' в '+Pairss.location+'\n\n'
    return astext
