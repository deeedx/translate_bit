import sqlite3
import datetime



connection = sqlite3.connect('users.db')

sql = connection.cursor()



sql.execute("create table if not exists BOT_USERS(id integer  PRIMARY KEY AUTOINCREMENT,first_name text, telegram_id text,phone_number text,reg_date DATETIME)")
sql.execute("create table if not exists Use_Word(id integer  PRIMARY KEY AUTOINCREMENT,telegram_id text, text text,trans_text text,reg_date DATETIME)")




def register_user(first_name, telegram_id,phone_number):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = f"INSERT INTO BOT_USERS (first_name,telegram_id, phone_number,reg_date) VALUES (?, ?,?,? )"
    cursor.execute(query, (first_name,telegram_id,phone_number,datetime.datetime.now()))

    connection.commit()
    connection.close()


def check_user(telegram_id):


    connection = sqlite3.connect("users.db")
    sql = connection.cursor()

    user = sql.execute("select telegram_id from BOT_USERS where telegram_id = ?",(telegram_id,)).fetchone()




    if user:
        return True
    else:
        return False


def add_user_word(telegram_id,text,trans_text):

    connection = sqlite3.connect("users.db")
    sql = connection.cursor()

    sql.execute( f"INSERT INTO Use_Word (telegram_id,text,trans_text,reg_date) VALUES (?, ?,?,?)",(telegram_id,text,trans_text,datetime.datetime.now()))

    connection.commit()
    connection.close()


