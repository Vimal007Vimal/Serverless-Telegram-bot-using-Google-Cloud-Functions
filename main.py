import os
import telegram

bot = telegram.Bot(token=os.environ["7272129084:AAGVNP52FelFIXA7EGtjXsTMmeiIl9TPb1E"])


def webhook(request):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=update.message.text)
    return "ok"
