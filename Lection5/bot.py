# -*- config: utf-8 -*-

#Импортировали файл конфигураций
import config

#Импортировали модуль для Телеграм - это наше API
import telebot

#Создали "прототип" апи (есть чертеж машины, а есть модель)
bot = telebot.TeleBot(config.token)

#Создали хэндлер - "секретяря", который перехватит
#Неожиданные сообщения пользователя
@bot.message_handler(content_types=["text"])

#Как сказать секретарю, что делать?
#Создать для него функцию! Вот эта "ловит" новое сообщение из Телеграм
def repeat_all_message(message):
    #А когда "словила", разбивает сообщение на "отправителя" - message.chat.id,
    #И на текст сообщения - message.text
    bot.send_message(message.chat.id, message.text)
    
'''
А вот так заставить бота "общаться с пользователем":
def answer_questions(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Привет, как дела?")
    if message.text == "Как дела?":
        bot.send_message(message.chat.id, "Отлично, а у тебя?")
'''


#Какая "должность" у нашего файла? Если он главный (main), то запустим бота
if __name__ == '__main__':
    #Бот, запустись! (не_останавливаться = Правда)
    bot.polling(none_stop=True)
