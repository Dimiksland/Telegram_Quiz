@bot.message_handler(commands=['quiz'])
def cmd_quiz(message: Message):
    bot.send_message(message.chat.id, 'Сколько дней в году?')
    bot.send_message(message.chat.id, 'Варианты ответа: 1.120, 2.365, 3.1000')
    bot.register_next_step_handler(message, get_quiz)
  
def get_quiz(message: Message):
    mess = message.text
    if mess == '1' or mess == '120':
        bot.reply_to(message, 'Не правильно!')
    elif mess == '2' or mess == '365':
        bot.reply_to(message, 'Правильно!')
    elif mess == '3' or mess == '1000':
        bot.reply_to(message, 'Не правильно!')
