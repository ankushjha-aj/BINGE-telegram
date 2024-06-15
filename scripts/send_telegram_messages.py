import telebot
import os
import json
from difflib import SequenceMatcher

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

# Function to save the current messages (only when new messages are sent)
def save_current_messages(messages):
  if new_messages:  # Save only if new messages were sent
    with open(PERSISTENCE_FILE, 'w') as f:
      json.dump(messages, f)

# Define the messages list (modify as needed)
messages = [
  'This is the first message.',
  'This is the second message.',
  'This might be a slightly modified message (check for typos or spaces)'
]

# Load previously sent messages
previous_messages = load_previous_messages()

# Function to compare messages (consider customizing the similarity threshold)
def message_similar(message1, message2):
  matcher = SequenceMatcher(None, message1, message2)
  ratio = matcher.quick_ratio()
  return ratio >= 0.95  # Adjust threshold for desired similarity (0.95 for slight changes)

# Identify only new messages based on content similarity
new_messages = [message for message in messages if not any(message_similar(m, prev) for prev in previous_messages)]

# Create a Telegram bot object
bot = telebot.TeleBot(bot_token)

# Send only new messages (avoid unnecessary triggers)
if new_messages:
  for message in new_messages:
    bot.send_message(channel_id, message)
    print(f"Sent new message: {message}")
  save_current_messages(messages)  # Update persistence file only for new messages
else:
  print("No new messages found (based on content similarity).")

# import telebot
# import os 

# # Retrieve secrets from environment variables
# bot_token = os.environ.get('TELEGRAM_TOKEN')
# channel_id = os.environ.get('CHANNEL_ID')

# # Define multiple messages
# messages = [
#     'https://photos.app.goo.gl/chxAPKxo3ecffK4KA',
# ]

# # Create a Telegram bot object
# bot = telebot.TeleBot(bot_token)

# for message in messages:
#   # Send each message to the channel
#   bot.send_message(channel_id, message)

# print('All messages sent successfully!')
