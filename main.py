import requests

text = ""


send = requests.get("https://api.telegram.org/bot5643026358:AAGyYJMh4pyXal1SQI0-6gV1bX2MF-pwamw/sendMessage?chat_id=395454426&text=hello")
response = requests.get("https://api.telegram.org/bot5643026358:AAGyYJMh4pyXal1SQI0-6gV1bX2MF-pwamw/getUpdates")

bot = response.json()


print(bot)

#
# if text == "hi":
#     #respond to the text


