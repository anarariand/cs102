from datetime import date
from typing import Optional
from api import *

def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей
    Возраст считается как медиана среди возраста всех друзей пользователя
    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    friends = get_friends(user_id, 'bdate')
    ages = []
    for friend in friends['response']['items']:
        try:
            age = calculate_age(friend['bdate'])
            ages.append(age)
        except:
            pass
    if len(ages) % 2:
        return ages[len(ages) // 2]
    else:
        return (ages[len(ages) // 2] + ages[len(ages) // 2 + 1]) // 2


def calculate_age(bd):
    bd = bd.split('.')
    year = int(bd[2])
    month = int(bd[1])
    day = int(bd[0])
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age


if __name__ == '__main__':
    print(age_predict(user_id))
