# ChatWithMe Telegram Bot Documentation

ChatWithMe is a Telegram bot that uses the OpenAI API to provide interactive conversations with users. The bot can answer questions, provide information, generate text, and perform other tasks based on user input.

## Requirements

The following Python libraries are required to run the ChatWithMe bot:

- `graphyte==1.7.1`: Library for sending metrics to a Graphite server.
- `gTTS==2.3.1`: Google Text-to-Speech library for generating audio files from text.
- `openai==0.27.0`: Library for interacting with the OpenAI API.
- `python-telegram-bot==13.13`: Library for interacting with the Telegram Bot API.
- `requests==2.28.2`: Library for making HTTP requests.
- `youtube-search==2.1.2`: Library for searching YouTube videos.
- `psutil==5.9.4`: Library for retrieving system metrics.

## Configuration

Before running the ChatWithMe bot, you need to set up the following configuration:

**Environment Variables:**

- `telegram-ChatWMe-bot_Token`: Set this variable to your Telegram Bot Token. This token is required for the bot to authenticate and interact with the Telegram API.
- `OPENAI_API_KEY`: Set this variable to your OpenAI API Key. This key is necessary for the bot to access the OpenAI services and make requests to the OpenAI Playground API.

**Graphite Monitoring (Optional):**

If you want to enable monitoring with Graphite, you can set up the following configuration variables:

- `GRAPHITE_HOST`: The hostname or IP address of the Graphite server.
- `GRAPHITE_PORT`: The port used by the Graphite server.
- `time_period`: The time period (in seconds) between sending metrics to the Graphite server.

> Note: Monitoring with Graphite is optional, and you can exclude this configuration if you don't need it.

## Usage

To use the ChatWithMe bot, follow these steps:

1. Clone the ChatWithMe bot repository from the remote repository URL: [https://github.com/imadBelattar/OpenAi-based-Telegram-bot.git](https://github.com/imadBelattar/OpenAi-based-Telegram-bot.git).

2. Install the required Python libraries mentioned in the "Requirements" section using the following command:

   ```shell
   pip install graphyte==1.7.1 gTTS==2.3.1 openai==0.27.0 python-telegram-bot==13.13 requests==2.28.2 youtube-search==2.1.2 psutil==5.9.4
3. Set the required environment variables:

- `telegram-ChatWMe-bot_Token`: Set this variable to your Telegram Bot Token.
- `OPENAI_API_KEY`: Set this variable to your OpenAI API Key.

4. Run the `chatWithMe.py` script to start the ChatWithMe bot.

Bot Commands:

The ChatWithMe bot supports the following commands:

- `/start`: Start the conversation with the bot.
- `/help`: Get help and instructions.
- Text messages: The bot will respond to any text messages sent to it with appropriate answers or actions.

Additional Notes:

- The `handle_message` function in the code is responsible for handling incoming requests and generating appropriate responses based on the user's input.
- The bot uses the OpenAI Playground API to generate text-based responses to user queries.
- Certain features mentioned in the code, such as retrieving YouTube videos or generating images, are placeholders and can be customized.
