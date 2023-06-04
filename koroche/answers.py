from asyncio import sleep
from bot import bot

@bot.message_handler(commands=['start'])
def start(msg):
    user_id = msg.from_user.id
    bot.send_message(user_id,  'Здравствуйте,чтобы пользоваться ботом подпишитесь на мои каналы')

@bot.message_handler(connands=['parse'])
def parse(msg):
    user_id = msg.from_user.id
    bot.send_message(user_id, 'Введите количество видео которое хотите получить с каждого канала. До 30.')
    bot.register_next_step_handler_by_chat_id(user_id, get_numb)


def get_numb(msg):
    content = msg.text
    user_id = msg.from_user.id
    bot.send_message(user_id, 'Пожалуйста подождите,идёт обработка…')
    try:
        data = parse.parser(int(content))
        for i in data:
            for k in i:
                sleep(0.5)
                bot.send_message(user_id, k)

    except:
        bot.send_message(user_id, 'WARNING')

    
    