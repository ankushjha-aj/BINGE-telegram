import telebot
import os 

# Retrieve secrets from environment variables
bot_token = os.environ.get('TELEGRAM_TOKEN')
channel_id = os.environ.get('CHANNEL_ID')

# Define multiple messages
messages = [
    'https://photos.app.goo.gl/chxAPKxo3ecffK4KA', 
]

# Create a Telegram bot object
bot = telebot.TeleBot(bot_token)

for message in messages:
  # Send each message to the channel
  bot.send_message(channel_id, message)

print('All messages sent successfully!')
