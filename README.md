# Исследовательский проект для предмета "Количественные методы исследования"

Датасет взят с ресурса [www.swipestats.io](https://www.swipestats.iohttps://www.swipestats.io/research/research). Он содержит подробную информацию о 1200 пользователях Tinder: их сообщения, агрегированные данные о сообщениях, данные о свайпах и лайках за период 10.11.2014-10.11.2021. 

Для тестирования гипотез будем использовать сокращённую версию датасета, в которой поля, содержащие временные признаки сделаем 2 агрегации: сумма и количество дней с не пустыми значениями.

## Как пользоваться?
Пока все эксперименты находятся в `Experiment/experiment.ipynb`, в будущем будет более приемлемое оформление.

## Какие гипотезы хочется проверить

1. Существует зависимость между возрастом пользователя и возрастным фильтром, который они устанавливают для потенциальных партнеров.
2. Активности (например, количество лайков и сообщений) между мужчинами и женщинами отличаются.
3. Наличие подключенного аккаунта Instagram/Spotify увеличивает количество сообщений/совпадений/лайков.
4. Знак зодиака пользователя не влияет на количестве сообщений/совпадений/лайков.

## Таблица типов данных и шкал измерений для всех полей

| Название поля                                               | Тип данных | Шкала измерения | Пояснение                                                                                                              |
|-------------------------------------------------------------|------------|-----------------|------------------------------------------------------------------------------------------------------------------------|
| `__v`                                                       | int64      | Относительная   | Версия документа, используется для управления версиями в базах данных.                                                 |
| `_id`                                                       | object     | Номинальная     | Уникальный идентификатор, используется для определения записей.                                                  |
| `conversationsMeta.averageConversationLength`               | float64    | Относительная   | Средняя длина разговоров.                                 |
| `conversationsMeta.averageConversationLengthInDays`         | float64    | Относительная   | Средняя длина разговоров в днях, показывает длительность общения.                                                       |
| `conversationsMeta.longestConversation`                     | int64      | Относительная   | Длина самого долгого разговора.                               |
| `conversationsMeta.longestConversationInDays`               | float64    | Относительная   | Самый долгий разговор в днях.                                          |
| `conversationsMeta.medianConversationLength`                | int64      | Относительная   | Медианная длина разговоров.                                          |
| `conversationsMeta.medianConversationLengthInDays`          | float64    | Относительная   | Медианная длина разговоров в днях.                                        |
| `conversationsMeta.nrOfConversations`                       | int64      | Относительная   | Общее количество разговоров.                                  |
| `conversationsMeta.nrOfGhostingsAfterInitialMessage`        | int64      | Относительная   | Количество случаев, когда после первого сообщения не последовало ответа.   |
| `conversationsMeta.nrOfOneMessageConversations`             | int64      | Относительная   | Количество разговоров с одним сообщением.                                |
| `conversationsMeta.percentOfOneMessageConversations`        | float64    | Относительная   | Процент разговоров с одним сообщением.                   |
| `user.ageFilterMax`                                         | int64      | Относительная   | Максимальный возраст интереса пользователя.                        |
| `user.ageFilterMin`                                         | int64      | Относительная   | Минимальный возраст интереса пользователя.                         |
| `user.birthDate`                                            | object     | Интервальная    | Дата рождения пользователя.                                                         |
| `user.cityName`                                             | object     | Номинальная     | Название города проживания пользователя.                                   |
| `user.country`                                              | object     | Номинальная     | Страна проживания пользователя.                                        |
| `user.createDate`                                           | object     | Интервальная    | Дата создания профиля.                                             |
| `user.education`                                            | object     | Номинальная     | Уровень образования.                                        |
| `user.educationLevel`                                       | object     | Порядковая      | Уровень достигнутого образования.             |
| `user.gender`                                               | object     | Номинальная     | Пол пользователя.                                                 |
| `user.genderFilter`                                         | object     | Номинальная     | Пол, на который пользователь настроен фильтр.                                   |
| `user.instagram`                                            | bool       | Номинальная     | Наличие подключения к Instagram, бинарная переменная (да/нет).                                                         |
| `user.jobs`                                                 | object     | Номинальная     | Работа пользователя.                                        |
| `user.schools`                                              | object     | Номинальная     | Школы, которые посещал пользователь.                   |
| `user.spotify`                                              | object     | Номинальная     | Статус подключения к Spotify, бинарная переменная (да/нет).                                                            |
| `Total_appOpens`                                            | float64    | Относительная   | Общее количество открытий приложения.                              |
| `DaysWith_appOpens`                                         | int64      | Относительная   | Количество дней, когда приложение было открыто.                                |
| `Total_matches`                                             | float64    | Относительная   | Общее количество совпадений.                          |
| `DaysWith_matches`                                          | int64      | Относительная   | Количество дней с совпадениями.                          |
| `Total_messagesReceived`                                    | float64    | Относительная   | Общее количество полученных сообщений.                    |
| `DaysWith_messagesReceived`                                 | int64      | Относительная   | Количество дней, когда пользователь получал сообщения.                          |
| `Total_messagesSent`                                        | float64    | Относительная   | Общее количество отправленных сообщений.                         |
| `DaysWith_messagesSent`                                     | int64      | Относительная   | Количество дней, когда отправлялись сообщения.                  |
| `Total_swipeLikes`                                          | float64    | Относительная   | Общее количество лайков, выданных пользователем.     |
| `DaysWith_swipeLikes`                                       | int64      | Относительная   | Количество дней, когда пользователь ставил лайки.                     |
| `Total_swipePasses`                                         | float64    | Относительная   | Общее количество отказов/пропусков.                               |
| `DaysWith_swipePasses`                                      | int64      | Относительная   | Количество дней, когда пользователь делал свайпы влево.                          |
