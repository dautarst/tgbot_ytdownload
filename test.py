from numpy import put
import telebot
from selenium import webdriver
from time import sleep
from pytube import YouTube
import requests

driver = webdriver.Chrome()

token = '5218803979:AAHyNMKHTUsHtFpyrDQ3uQcDQNL9x2onpYY'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Wake up, Samurai! We have a videos to search! /search to start searching YT videos")


@bot.message_handler(commands=['search'])
def search(message):
    msg = bot.send_message(message.chat.id, "What are we looking for? Enter the text!")
    bot.register_next_step_handler(msg, search_videos)

@bot.message_handler(commands=['download'])
def download(message):
    yd = bot.send_message(message.chat.id, "Give me YT video URL!")
    bot.register_next_step_handler(yd, ytdl)



def search_videos(message):
    bot.send_message(message.chat.id, "Scanning space in progress!")
    video_link = 'https://www.youtube.com/results?search_query=' + message.text
    driver.get(video_link)
    sleep(3)
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 10:
            break

def ytdl(message):
    link = message.text
    yt = YouTube(link)
    video_name = yt.title+str('.mp4')
    ys = yt.streams.get_highest_resolution()
    puty = 'C:/Users/kukus/Desktop/botYTDL'
    ys = ys.download(puty)
    bot.send_message(message.chat.id, "Download complete!")
    video_open = open(video_name, 'rb')
    bot.send_video(message.chat.id, video_open)
    
    

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "/search to searching videos on YouTube")

bot.polling()

