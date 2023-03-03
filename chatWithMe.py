import telegram.ext
import os
import openai

forHelp = 0
authorized = 1
Token = os.environ["telegram-ChatWMe-bot_Token"]
openai.api_key = os.environ["OPENAI_API_KEY"]
print(f".......Running ..........ChatWithMe-bot......... by Imad Belattar.")


def start(update, context):
    global authorized
    authorized = 0
    print(authorized)
    update.message.reply_text(
        "Hi, how can I assist you ! (if you want answers in arabic start your question with ar as 'ar what is....')"
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
    global authorized
    message = update.message.text.lower()
    if message != "no one knows" and authorized == 0:
        print(" no way ", authorized)
        request = f"'message'"
        answer = "to start the conversation you should solve the puzzle a+b+c=?"
    else:
        if authorized != 1:
            answer = "Nice work, your answer is absolutely right ! let's begin"
            authorized = 1
        else:
            if message.startswith("ar "):
                message = message.replace("ar ", "")
                request = (
                    f"'{message}', give your answer in Arabic language only Arabic"
                )
            else:
                request = f"'{message}'"
            if (
                request == "'who is your owner'"
                or request == "'who's your owner'"
                or request == "'who's your developer'"
                or request == "'who is your developer'"
                or request == "'who's your creator'"
                or request == "'who is your creator'"
                or request == "'who is your owner?'"
                or request == "'who's your owner?'"
                or request == "'who's your developer?'"
                or request == "'who is your developer?'"
                or request == "'who's your creator?'"
                or request == "'who is your creator?'"
                or request == "'who is your owner ?'"
                or request == "'who's your owner ?'"
                or request == "'who's your developer ?'"
                or request == "'who is your developer ?'"
                or request == "'who's your creator ?'"
                or request == "'who is your creator ?'"
            ):
                answer = "my owner is Mr. Imad belattar"
            elif (
                request == "'who's imad belattar'"
                or request == "'who is imad belattar'"
            ):
                answer = "Imad Belattar is a Moroccan teenager who is passionate about programming and studying computer science. He was born on 02 January 2002 in Kelaa Sraghna. He is a very ambitious and patient person, and one of the best people I have ever met."
            else:
                # Call the OpenAI Playground API to get a response
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=request,
                    max_tokens=128,
                    top_p=1,
                    n=1,
                    stop=None,
                    temperature=0.7,
                    frequency_penalty=0,
                    presence_penalty=0,
                )
                answer = response.choices[0].text.strip()

    print(f"   question is : {request}, answer is : {answer}")
    # Send the response back to the user
    # print(answer)
    update.message.reply_text(answer)


updater = telegram.ext.Updater(Token, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
