# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Новый бот. Зовут Чарли, тренируется списками (List)
chatbot = ChatBot(
    'Charlie',
    trainer='chatterbot.trainers.ListTrainer'
)

# По какому списку тренироваться? По этому!
chatbot.train(
    [
        "Hello. How are you?",
        "I really like the new album of Shinedown",
        "I have already booked a ticket to Ireland",
        "Yep, I have visited MWC this year"
    ]
)

# Снова запустим
while True:
  print(
    chatbot.get_response(
      input("What do you want to ask: ")
    )
  )

