# *- coding: utf-8 -*

from pony.orm import Database,Required,PrimaryKey,Json
from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)

class Pairs(db.Entity):
    id = PrimaryKey(int)
    group = Required(str)
    even_week = Required(bool,default=True, sql_default='1')
    day_of_week = Required(int)
    ordinal = Required(int)
    lesson = Required(str)
    teacher = Required(str)
    type = Required(str)
    location = Required(str)

class UserState(db.Entity):
    user_id = Required(str,unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)

db.generate_mapping(create_tables=True)
