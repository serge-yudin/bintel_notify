import sqlite3
# from os import getcwd


class DB:
    db_uri = "crypto.db"

    def __init__(self):
        self.con = sqlite3.connect(self.db_uri)
        self.cur = self.con.cursor()

    def get_last_price(self, coin):
        sql = 'Select * from prices where coin=?'
        res = self.cur.execute(sql, (coin,))
        return res.fetchone()

    def update_price(self, coin, price):
        sql = 'update prices set price=? where coin=?'
        self.cur.execute(sql, (price, coin))
        self.con.commit()

    def add_new_coin(self, coin, price):
        sql = 'insert into prices(coin, price) values(?,?)'
        self.cur.execute(sql, (coin, price))
        self.con.commit()

    def get_all_prices(self):
        sql = 'select * from prices'
        res = self.cur.execute(sql)
        return res.fetchall()

    def __del__(self):
        self.con.commit()
        self.con.close()
