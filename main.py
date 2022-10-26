import requests



response = requests.get("https://api.telegram.org/bot5643026358:AAGyYJMh4pyXal1SQI0-6gV1bX2MF-pwamw/getUpdates")
bot = response.json()
length = len(bot["result"])

while True:
    response = requests.get("https://api.telegram.org/bot5643026358:AAGyYJMh4pyXal1SQI0-6gV1bX2MF-pwamw/getUpdates")

    bot = response.json()
    recieved_text = bot["result"][len(bot["result"]) - 1]["message"]["text"]

    if len(bot["result"]) == length + 1:
        length  =  length + 1
        send_message = requests.get(f"https://api.telegram.org/bot5643026358:AAGyYJMh4pyXal1SQI0-6gV1bX2MF-pwamw/sendMessage?chat_id=395454426&text={recieved_text}")


