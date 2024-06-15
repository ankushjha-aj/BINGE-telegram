import telebot

# Replace with your bot's API token
bot_token = '6384770295:AAH_FlqDRXL49GM8eR5yH_WJ-K24Dsm5B4g'

# Replace with the channel ID
channel_id = '-1002236190456'

# Define multiple messages
messages = [
    'This is the first message.',
    'This is the second message with some additional information.',
    'This is the final message for now.'
]

# Create a Telegram bot object
bot = telebot.TeleBot(bot_token)

for message in messages:
  # Send each message to the channel
  bot.send_message(channel_id, message)

print('All messages sent successfully!')
