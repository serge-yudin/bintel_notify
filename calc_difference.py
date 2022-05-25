#!/usr/bin/python3
''' A simple telegram message notification program about current price of
choosen Coin compared to price of purchase
Installation pip install binance-connector
 '''
import requests
from binance.spot import Spot

from text_to_img import create_img

from credentials import TOKEN
from db import DB


class MyTeleBot:
    def __init__(self, TOKEN):
        self.__token = TOKEN

    def send_text(self, msg, chat_id):
        url = f'https://api.telegram.org/bot{self.__token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={msg}'
        res = requests.get(url)
        return res

    def send_photo(self, text_on_img, chat_id):
        url = f'https://api.telegram.org/bot{self.__token}/sendPhoto?chat_id={chat_id}'
        photo = create_img(text_on_img)
        res = requests.post(url, files={'photo': photo})
        return res


if __name__ == '__main__':
    chat_id = ''  # Telegram chat id
    coin = "LUNA"
    pair = "BUSD"  # avg_price request is composed by {coin}{pair}
    client = Spot()  # binance client
    buy_price = 0  # luna buy price
    amount_of_coins = 0  #

    db = DB()
    txt = {'percents': 0, 'cur_price': 0, 'positive': True}
    cur_price = float(client.avg_price(f'{coin}{pair}')['price'])
    last_price = db.get_last_price(coin)[1]
    if not last_price:
        last_price = cur_price
        db.add_new_coin(coin, cur_price)
    txt['percents'] = abs(round(((cur_price - last_price) / last_price) * 100, 2))
    txt['positive'] = cur_price > last_price
    txt['cur_price'] = f'{cur_price:.8f}'
    if abs(txt['percents']) >= 5:
        bot = MyTeleBot(TOKEN)
        bot.send_photo(txt, chat_id)
        db.update_price(coin, cur_price)
        if buy_price and amount_of_coins:
            cur_balance = round((cur_price * amount_of_coins) - (buy_price * amount_of_coins), 2)
            txt['cur_price'] = f'{cur_balance}$'
            bot.send_photo(txt, chat_id)
