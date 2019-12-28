import requests
import time
from config import *

'''Функция,выполняющая GET-запрос к указанному адресу, 
а при необходимости повторять запрос указанное число раз 
по алгоритму экспоненциальной задержки
'''
def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос
    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    delay = 1
    counter = 0
    while counter < max_retries:
        response = requests.get(url, timeout = timeout)
        if response.status_code == CONNECTED:
            break
        sleep(delay)

        # calculate next delay
        delay = min(delay * backoff_factor, timeout)
        delay = delay + normalvariate(delay)
    return response


def get_friends(user_id, fields):
    """ Вернуть данныe о друзьях пользователя
    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = get(query, backoff_factor=2,timeout=100).json()
    return response