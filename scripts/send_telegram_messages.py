import os
import telebot
import logging

# Logging setup for better error tracking
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_to_telegram(new_msg, prev_msg=None):
    """
    This function sends a new message to a Telegram channel if it's different from the previous message.
    
    Args:
        new_msg (str): The new message to send.
        prev_msg (str, optional): The previous message for comparison. Defaults to None.
    """
    
    # Retrieve secrets securely from environment variables
    bot_token = os.getenv('TELEGRAM_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')

    if not bot_token or not channel_id:
        logging.error("Missing TELEGRAM_TOKEN or CHANNEL_ID environment variables!")
        return

    try:
        # Check if the new message is different
        if new_msg != prev_msg:
            bot = telebot.TeleBot(bot_token)
            
            # Send the message
            sent_message = bot.send_message(channel_id, new_msg)
            
            logging.info(f"Message sent successfully: {sent_message.message_id}")
        else:
            logging.info("No new message to send.")
    except telebot.apihelper.ApiException as e:
        logging.error(f"Telegram API Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# --- Main Execution ---
# Replace these with the actual message URLs
prev_msg = 'https://photos.app.goo.gl/chxAPKxo3ecffK4KA' 
new_msg = 'https://photos.app.goo.gl/abcdefg12345'  # Make sure this is different for testing

send_to_telegram(new_msg, prev_msg)

print('Script completed!')










# import telebot

# # Retrieve secrets from environment variables
# bot_token = os.environ.get('TELEGRAM_TOKEN')
# channel_id = os.environ.get('CHANNEL_ID')

# prev_msg = 'https://photos.app.goo.gl/chxAPKxo3ecffK4KA'
# new_msg = 'https://photos.app.goo.gl/chxAPKxo3ecffK4KA'
# messages = None
# if prev_msg != new_msg:
#     messages = [
#         new_msg,
#     ]

#     # Create a Telegram bot object
#     bot = telebot.TeleBot(bot_token)

#     for message in messages:
#         # Send each message to the channel
#         bot.send_message(channel_id, message)

# print('All messages sent successfully!')




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
