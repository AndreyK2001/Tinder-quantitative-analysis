import pandas as pd

data = pd.read_csv("../Datasets/profiles_2021-11-10.csv")

# Датасет содержит подробную информацию о 1200 пользователях Tinder: их сообщения, агрегированные данные о сообщениях, данные о свайпах и лайках за период 10.11.2014-10.11.2021.


def aggregation(data: pd.DataFrame, field_name: str) -> pd.DataFrame:
    # Идентификация колонок с данными по дням
    columns = [col for col in data.columns if col.startswith(field_name)]

    # Расчёт суммарного количества признака и количества дней с признаком
    data[f"Total_{field_name}"] = data[columns].sum(axis=1)
    data[f"DaysWith_{field_name}"] = data[columns].notna().sum(axis=1)
    return data.drop(columns=columns)


def dropper(data: pd.DataFrame, field_name: str) -> pd.DataFrame:
    # Идентификация колонок с данными по дням
    columns = [col for col in data.columns if col.startswith(field_name)]
    return data.drop(columns=columns)


data = data.drop(columns=["conversations", "userId", "user.interestedIn"])

data = aggregation(data, "appOpens")
data = aggregation(data, "matches")
data = dropper(data, "messages.received")  # поля дублируются
data = dropper(data, "messages.sent")  # поля дублируются
data = aggregation(data, "messagesReceived")
data = aggregation(data, "messagesSent")
data = dropper(data, "swipes.likes")
data = dropper(data, "swipes.passes")
data = aggregation(data, "swipeLikes")
data = aggregation(data, "swipePasses")

data.to_csv("../Datasets/short_data.csv")
