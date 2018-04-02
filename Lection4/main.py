'''
На четвертой лекции мы изучили, что такое API,
почему любой уважающий себя сервис имеет собственный
апи и рассмотрели, как встроить Википедию в Пайтон.
'''

#Подключаем модуль Wikipedia API - его мы скачали через pip
import wikipedia

#И сразу выведем короткую инфу по запросу "Wikipedia"
print wikipedia.summary("Wikipedia")

'''
В консоли будет такое:
Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited,
multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...
'''


#Не знаете, что конкретно нужно? Сделаем поиск по ключевому слову!
wikipedia.search("Barack")

'''
Вот такой список результатов получим:
[
    u'Barak (given name)',
    u'Barack Obama',
    u'Barack (brandy)',
    u'Presidency of Barack Obama',
    u'Family of Barack Obama',
    u'First inauguration of Barack Obama',
    u'Barack Obama presidential campaign, 2008',
    u'Barack Obama, Sr.',
    u'Barack Obama citizenship conspiracy theories',
    u'Presidential transition of Barack Obama'
]
'''

#Вытянем в отдельную переменную 'ny' целую страницу из Википедии
ny = wikipedia.page("New York")
#Какой заголовок у страницы?
ny.title
#А ссылка?
ny.url
#Содержимое статьи?
ny.content


#А теперь получим инфу о Facebook. Но одним предложением. И на французском.
wikipedia.set_lang("fr")
wikipedia.summary("Facebook", sentences = 1)
#Запросто!
# Facebook est un service de réseautage social en li
