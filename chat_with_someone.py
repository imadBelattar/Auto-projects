import telegram.ext
import os
import requests

Token = os.environ["telegram-ChatWMe-bot_Token"]
# Get the user's message
response = "start"


# the user messages updates handler
def handle_message(update, context):
    user_id = update.effective_chat.id
    UserName = update.effective_user.full_name
    message = update.message.text.lower()
    if user_id != -1001673155233:
        print(f"   user {UserName} not allowed said : {message}")
        answer = "fuck off man I don't want to talk with you today 😒😠"
        update.message.reply_text(answer)

    else:
        print(f"   user {UserName} said : {message}")
        answer = input("Enter your message to the user: ")
        update.message.reply_text(answer)


updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
