from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
import pickle
from selenium.webdriver.common.keys import Keys
import time
from telegram.ext import MessageHandler, Filters
import threading






def tether(update, context):
    open_file = open('tether_price.pkl', "rb")

    Price_list = pickle.load(open_file)

    open_file.close()

    print(update.message.chat.first_name,'     ',update.message.chat.last_name,'    ',update.message.chat.username)
    context.bot.send_message(chat_id=update.effective_chat.id, text='tether:  \n \n  اطلاعات قیمت \n \n  ارز مدرن:     %s   تومان  \n  نوبیتکس:      %s  تومان \n  تترلند:        %s  تومان \n  والکس:     %s  تومان \n  نوبیتکس:      %s  تومان \n  تترلند:        %s  تومان \n  والکس:     %s  تومان \n \n \n  میانگین قیمت:     %d \n  بالاترین قیمت:     %d \n   کمترین قیمت:    %d \n   '%(Price_list[0][1],Price_list[1][1],Price_list[2][1],Price_list[3][1],Price_list[4][1]/4,Price_list[5][0],Price_list[6][0],Price_list[7][0]), timeout=100)






def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="به ربات درستیار ویرا خوش آمدید. برای استفاده از امکانات از منو استفاده کنید.")







try:


    updater = Updater(token='your bot token')
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    ethop_handler = CommandHandler('ethop', options_eth)
    dispatcher.add_handler(ethop_handler)
    btcop_handler = CommandHandler('btcop', options_btc)
    dispatcher.add_handler(btcop_handler)
    tether_handler = CommandHandler('tether', tether)
    dispatcher.add_handler(tether_handler)
    updater.start_polling()


except:
    updater.start_polling()
