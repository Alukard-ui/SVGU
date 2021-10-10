group_id = '207172656'
token = "2817673542770220aeddbcb48f49b49616f2a417f030931d8be658b74c52692099bb1e15621ec4f285367"

INTENTS = [
    {
        'name': 'Help',
        'tokens': ('?вождь', '?help'),
        'scenario': None,
        'answer': 'Помощь по использованию бота:'
                  '\n\n Пока есть только расписание, для того чтобы оно появилось надо написать ?расписание или ?пары'
    },
    {
        'name':'Schedule',
        'tokens':('?расписание','?пары'),
        'scenario': None,
        'answer':None,
        'group_handler':'group_handler_Schedule'
    },
    {
    'name':'room',
        'tokens':('?аудитория','?ауд'),
        'scenario': None,
        'answer':None,
        'group_handler':'group_handler_room'
    }
]

SCENARIOS = {
    'laboratoryWork': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Введи свой курс',
                'failure_text': 'Курс не обнаружен',
                'handler': 'handler_class',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введи номер лабораторной работы',
                'failure_text': 'Лабораторная работа не обнаружена',
                'handler': 'handler_numberLab',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Вам нужна лабороторная работа №{numberLab} для {class} курса, {first_name}?',
                'failure_text': 'Ответь да',
                'handler': 'handler_link',
                'next_step': 'step4'
            },
            'step4': {
                'text': 'Вот ссылки на лабораторную работу №{numberLab} для {class} курса\n'
                        '{oldPiggyBank} - Копилка стариков\n'
                        '{newPiggyBank} - копилка\n'
                        '{IOFPiggyBank} - копилка №2',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }
    }
}

DEFAULT_ANSWER = 'Я хз'

DB_CONFIG = dict(
    provider='sqlite',
    filename='pairs.db'
)
