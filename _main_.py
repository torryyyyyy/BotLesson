import requests
import pprint

with open('token.txt') as f:
    token = f.read()

# получить информацию по всем событиям / апдейтам
endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
res = requests.get(endPoint).json()['result']
pprint.pprint(res)

userInfo = dict()
for i in res:
    chatid = i['message']['chat']['id']
    userName = i['message']['chat']['first_name']
    if 'text' in i['message']:
        userText = i['message']['text']
    userInfo[chatid] = [userName, userText]

print(userInfo)

# отправление сообщения в чат
endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
for user in userInfo:
    mes= f'Привет, {userInfo[user][0]}!'
    params = {'chat_id': user, 'text': mes}
    res = requests.get(endPoint, params=params)




