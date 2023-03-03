from vars import *
import telegram.ext
import os
import openai


authentified_users = {1631515390: "owner"}
password = "2023@@@"
forHelp = 0
Token = os.environ["telegram-ChatWMe-bot_Token"]
openai.api_key = os.environ["OPENAI_API_KEY"]
print(f".......Running ..........ChatWithMe-bot......... by Imad Belattar.")


def start(update, context):
    update.message.reply_text(
        "Hi, how can I assist you ! (if you want answers in arabic, ask like this 'ar your question..')"
    )


def help(update, context):
    global forHelp
    forHelp = forHelp + 1
    if forHelp <= 2:
        update.message.reply_text("there is no help command ok !")
    else:
        update.message.reply_text("not again, you can do better than that")


def handle_message(update, context):
    # Get the message from the user
    global authentified_users
    global password
    user_id = update.effective_user.id
    message = update.message.text.lower()
    if user_id in authentified_users:
        # check if the intended answer would be in arabic by checking the request question
        if message.startswith("ar "):
            message = message.replace("ar ", "")
            request = f"'{message}', give your answer in Arabic language only Arabic"
        else:
            request = f"'{message}'"
        if request in yourOwner:
            answer = "my owner is Mr. Imad belattar"
        elif request in aboutTheOwner:
            answer = owner
        else:
            # Call the OpenAI Playground API to get a response
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=request,
                max_tokens=256,
                top_p=1,
                n=1,
                stop=None,
                temperature=0.7,
                frequency_penalty=0,
                presence_penalty=0,
            )
            answer = response.choices[0].text.strip()
        if authentified_users[user_id] == "owner":
            user_id = "Imad Belattar"
        print(" ")
        print(f"     ID : {user_id}")
        print(f"   ******  question is : {request}")
        print(f"   ******  answer is : {answer}")
        update.message.reply_text(answer)
    else:
        if message == password:
            authentified_users[user_id] = "yes"
            answer = f"Great! let's begin"
            #  print(f"{answer}")
            update.message.reply_text(answer)
        else:
            answer = f"Password is required to start the conversation :"
            # print(f"{answer}")
            update.message.reply_text(answer)


updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
