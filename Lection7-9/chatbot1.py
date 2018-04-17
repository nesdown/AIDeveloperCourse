# -*- coding: utf-8 -*-

#Подключаем библиотеку чат-бота
from chatterbot import ChatBot

"""
This example shows how to create a chat bot that
will learn responses based on an additional feedback
element from the user.
"""

# Создаем новый объект чат-бота
# Чертеж авто на стене -> Собранная модель со своими параметрами
bot = ChatBot(
    #Название
    'Feedback Learning Bot',
    #Адаптер памяти
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #Адаптер логики
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    #Адаптер ввода - из терминала
    input_adapter='chatterbot.input.TerminalAdapter',
    #Адаптер вывода - в терминал
    output_adapter='chatterbot.output.TerminalAdapter'
)

#Для "бортового журнала" берем номер беседы
CONVERSATION_ID = bot.storage.create_conversation()

#Просим пользователя что-то ввести.
#Нейросеть обработает ввод, вытянет из контекстной
#группы ответ... И спросит пользователя, правилен ли он.
#Если нет, то нейросеть "развернется", переформировав
#контекстные группы, а также семантические веса и расстояния
#Если да - просто запомнит диалог и сохранит контекст
def get_feedback():
    from chatterbot.utils import input_function

    text = input_function()

    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')
        return get_feedback()


print('Type something to begin...')

# The following loop will execute each time the user enters input
#Бесконечный цикл, в который склеены все предыдущие фукнции
while True:
    try:
        input_statement = bot.input.process_input_statement()
        statement, response = bot.generate_response(input_statement, CONVERSATION_ID)
        print('\n Is "{}" this a coherent response to "{}"? \n'.format(response, input_statement))

        if get_feedback():
            bot.learn_response(response, input_statement)
            # Update the conversation history for the bot
            # It is important that this happens last, after the learning step
            bot.storage.add_to_conversation(CONVERSATION_ID, statement, response)

        bot.output.process_response(response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break