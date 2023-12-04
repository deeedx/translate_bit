import telebot 

import databasess

import buttons

from googletrans import Translator
 

 

token = '6431604835:AAGrD_TKy8x_QmVxSgOj-SZXB0xXSfYypzA'


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):

        result = databasess.check_user(int(message.chat.id)) 
        if result== False:
        
             bot.send_message(message.from_user.id, 'Привет, чтобы начать напишите свой номер.', reply_markup=buttons.buttons())
             bot.register_next_step_handler(message, get_contact)

        else:

             bot.send_message(message.from_user.id, 'Привет это твой персональный переводчик языков выбери что будем переводить!' ,reply_markup =buttons.start_button() )


def get_contact(message):
    if message.contact:
        user_phone = message.contact.phone_number
        first_name = message.contact.first_name
        telegram_id = message.chat.id
        databasess.register_user(first_name,telegram_id,user_phone)
        bot.send_message(message.from_user.id, 'Привет это твой персональный переводчик языков выбери что будем переводить!' ,reply_markup =buttons.start_button() )








@bot.message_handler(content_types=['text'])
def get_language(message):

    def ru(message):
        
        trans = Translator()

        result = trans.translate(message.text,dest='ru').text

        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')

        databasess.add_user_word(message.from_user.id,message.text,result)




    
    def uz(message):
        
        trans = Translator()

        result = trans.translate(message.text,dest='uz').text

        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        databasess.add_user_word(message.from_user.id,message.text,result)

    def us(message):
        
        trans = Translator()

        result = trans.translate(message.text,dest='en').text

        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        databasess.add_user_word(message.from_user.id,message.text,result)
    def cn(message):
        
        trans = Translator()

        result = trans.translate(message.text,dest='zh-CN').text

        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        databasess.add_user_word(message.from_user.id,message.text,result)

    def kr(message):

        trans = Translator()
        
        result = trans.translate(message.text,dest='ko').text
        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        databasess.add_user_word(message.from_user.id,message.text,result)

    def kz(message):

        trans = Translator()
        
        result = trans.translate(message.text,dest='kk').text
        print(result)
        bot.send_message(message.from_user.id, f'Вот перевод:  "{result}"')
        databasess.add_user_word(message.from_user.id,message.text,result)





    if message.text == 'Русский 🇷🇺':
        bot.send_message(message.from_user.id, 'Введите что перевести:')
        bot.register_next_step_handler(message,ru)



    elif message.text == 'Узбекский 🇺🇿':
        
            if message.text =='Узбекский 🇺🇿' :
                bot.send_message(message.from_user.id, 'Введите что перевести:')
                bot.register_next_step_handler(message,uz)

                
                
    

    elif message.text =='Английский 🇬🇧🇺🇸' :
        bot.send_message(message.from_user.id, 'Введите что перевести:')
        bot.register_next_step_handler(message,us)
    

    elif message.text == 'Китайский 🇨🇳':
        bot.send_message(message.from_user.id, 'Введите что перевести:')
        bot.register_next_step_handler(message,cn)



    elif message.text == 'Корейский 🇰🇷':
        bot.send_message(message.from_user.id, 'Введите что перевести:')
        bot.register_next_step_handler(message,kr)


    elif message.text == 'Казахский 🇰🇿':
        bot.send_message(message.from_user.id, 'Введите что перевести:')
        bot.register_next_step_handler(message,kz)




    else:
        bot.send_message(message.from_user.id, 'Выберите внизу язык для перевода!')    
         



bot.polling()                                                                                                                                                                                                                                                       