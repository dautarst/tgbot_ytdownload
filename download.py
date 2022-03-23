@bot.message_handler(commands='download')
def download(message):
    bot.send_message(message.chat.id, "Take me URL")
    url = input(' ')
    dw = YouTube(url)
    dw = dw.streams.get_highest_resolution()
    dw = dw.download()