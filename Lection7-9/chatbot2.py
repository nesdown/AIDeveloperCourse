# -*- coding: utf-8 -*-
# А это - бот, который учится на основе списка
from chatterbot import ChatBot


# Здесь все как в прошлом примере, кроме пары нюансов...
bot = ChatBot(
    'Default Response Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

# Список заготовок для обучения
bot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

# Основной рабочий цикл
while True:
    question = input('Ask me sth! -')
    response = bot.get_response(question)
    print(response)