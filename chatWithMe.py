from vars import *
import telegram.ext
import os
import openai
import requests
from gtts import gTTS
from io import BytesIO
from youtube_search import YoutubeSearch
from pytube import YouTube


# allowing the owner of the bot to access the services without using the password
authentified_users = {1631515390: "owner"}
password = "imad@"
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


# the search music function
def send_video_of_song(name, chat_id, bot_token):
    # Search for the song on YouTube
    results = YoutubeSearch(name, max_results=1).to_dict()

    if results:
        # Get the URL of the first search result
        video_url = f"https://www.youtube.com/watch?v={results[0]['id']}"

        # Download the video
        video = YouTube(video_url)
        video_file = video.streams.get_by_resolution("720p").download()

        # Send the video to the user using the Telegram Bot API
        bot = telegram.Bot(token=bot_token)
        bot.send_video(chat_id=chat_id, video=open(video_file, "rb"))

        # Remove the temporary file
        os.remove(video_file)

        return f"🎥 🎶 🔊 Here's a video of {name}!"
    else:
        return f"😔 Sorry, I couldn't find {name} on YouTube."


def handle_message(update, context):
    # Get the message from the user
    global authentified_users
    global password
    user_id = update.effective_user.id
    UserName = update.effective_user.full_name
    message = update.message.text.lower()

    if user_id in authentified_users:
        if message.startswith("vid "):
            message = message.replace("vid ", "")
            answer = send_video_of_song(message, update.message.chat_id, Token)
            update.message.reply_text(answer)
            return

        # test if the user is requesting an image or a texted response
        if message.startswith("image "):
            message = message.replace("image ", "")
            prompt = f"Generate an image of {message}"
            response = openai.Image.create(
                model="image-alpha-001",
                prompt=prompt,
                n=1,
                size="512x512",
                response_format="url",
            )
            image_url = response["data"][0]["url"]
            # Download the image and save it to a local file
            image_name = f"{message}.jpg"
            image_path = os.path.join("uploads", image_name)
            with open(image_path, "wb") as f:
                f.write(requests.get(image_url).content)
            # Send the image to the user
            update.message.reply_photo(open(image_path, "rb"))
            return
        # check if the intended answer would be in arabic by checking the request question
        if message.startswith("ar "):
            message = message.replace("ar ", "")
            request = f"'{message}', give answer in Arabic language"
        else:
            request = f"'{message}'"
        if request in yourOwner:
            answer = "my owner is Mr. Imad belattar"
        elif request in aboutTheOwner:
            answer = owner
        elif message.startswith("sound "):
            message = message.replace("sound ", "")
            # Call the OpenAI Playground API to get a response
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=message,
                max_tokens=256,
                top_p=1,
                n=1,
                stop=None,
                temperature=0.7,
                frequency_penalty=0,
                presence_penalty=0,
            )
            answer = response.choices[0].text.strip()
            # convert the answer to an audio file using gTTS
            tts = gTTS(answer)
            audio_file = BytesIO()
            tts.write_to_fp(audio_file)
            audio_file.seek(0)
            # send the audio file to the user
            context.bot.send_voice(chat_id=user_id, voice=audio_file)
            return
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
        print(" ")
        print(f"     User : {UserName}")
        print(f"   ******  question is : {request}")
        print(f"   ******  answer is : {answer}")
        update.message.reply_text(answer)
    else:
        if message == password:
            authentified_users[user_id] = "yes"
            answer = f"Great! Mr. {UserName} let's begin"
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
