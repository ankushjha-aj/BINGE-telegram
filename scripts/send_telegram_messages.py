import telebot
import os
import json

# Retrieve secrets from environment variables
bot_token = os.environ.get('TELEGRAM_TOKEN')
channel_id = os.environ.get('CHANNEL_ID')

# Define a persistent storage location
PERSISTENCE_FILE = 'last_messages.json'

# Function to load previously sent messages
def load_previous_messages():
  try:
    with open(PERSISTENCE_FILE, 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    return []

# Function to save the current messages
def save_current_messages(messages):
  with open(PERSISTENCE_FILE, 'w') as f:
    json.dump(messages, f)

# Define the messages list
messages = [
  'This is the first message.',
  'This is the second message to check automation'  # Modify or add new messages here
]

# Load previously sent messages
previous_messages = load_previous_messages()

# Identify new messages
new_messages = [message for message in messages if message not in previous_messages]

# Create a Telegram bot object
bot = telebot.TeleBot(bot_token)

# Send only new messages
if new_messages:
  for message in new_messages:
    bot.send_message(channel_id, message)
    print(f"Sent new message: {message}")
  save_current_messages(messages)  # Update the persistence file with the current messages
else:
  print("No new messages found.")


# import telebot
# import os 

# # Retrieve secrets from environment variables
# bot_token = os.environ.get('TELEGRAM_TOKEN')
# channel_id = os.environ.get('CHANNEL_ID')

# # # Replace with your bot's API token
# # bot_token = '6384770295:AAH_FlqDRXL49GM8eR5yH_WJ-K24Dsm5B4g'

# # # Replace with the channel ID
# # channel_id = '-1002236190456'

# # Define multiple messages
# messages = [
#     'This is the first message.',
#     'This is the second message with some additional information.',
#     'This is the final message for now.'
# ]

# # Create a Telegram bot object
# bot = telebot.TeleBot(bot_token)

# for message in messages:
#   # Send each message to the channel
#   bot.send_message(channel_id, message)

# print('All messages sent successfully!')
