import telebot
import config
import requests
from bs4 import BeautifulSoup as soup
from telebot.types import Message

bot = telebot.TeleBot(config.TOKEN)
    
@bot.message_handler(commands=['start'])
def welcome(message: Message):
    bot.send_message(message.chat.id, 'Добридень, шановний!')

@bot.message_handler(content_types=['text'])
def word_find(message: Message):
    for text in get_word(message.text):
        bot.send_message(message.chat.id, text)

def get_word(word: str) -> list:
    url = f'http://ukrlit.org/slovnyk/{word.lower()}'
    code = requests.get(url).text
    page = soup(code, 'html.parser')
    block = page.find('article', attrs={'class':'word__description'})
    blocks = block.find_all('p')
    blocks.pop()
    return [e.text for e in blocks]

if __name__ == '__main__':
    bot.polling(none_stop=True)
