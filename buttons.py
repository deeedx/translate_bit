from telebot.types import ReplyKeyboardMarkup,KeyboardButton


def buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    share_contact = KeyboardButton('Поделиться номером',request_contact=True)

    kb.add(share_contact)

    return kb






    


def start_button():

    kb = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)

    ru = KeyboardButton('Русский 🇷🇺')
    uz = KeyboardButton('Узбекский 🇺🇿')
    us = KeyboardButton('Английский 🇬🇧🇺🇸')
    cn = KeyboardButton('Китайский 🇨🇳')
    kr = KeyboardButton('Корейский 🇰🇷')  
    kz = KeyboardButton('Казахский 🇰🇿')  

    kb.row(ru)
    kb.add(uz,us)
    kb.row(kz)
    kb.add(cn,kr)

   


    return kb
