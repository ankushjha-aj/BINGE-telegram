import os
import telebot
import logging

# Logging setup for better error tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize prev_msg from a file or default
prev_msg_file = "prev_msg.txt"  # Use a file to store prev_msg

# Load previous message from the file
if os.path.exists(prev_msg_file):
    with open(prev_msg_file, "r") as f:
        prev_msg = f.read().strip()
else:
    prev_msg = None


def send_to_telegram(new_msg, prev_msg_file=prev_msg_file):
    """
    Sends a new message to Telegram and updates the previous message record.
    """

    bot_token = '6384770295:AAH_FlqDRXL49GM8eR5yH_WJ-K24Dsm5B4g'
    channel_id = '-1001715673902'

    if not bot_token or not channel_id:
        logging.error("Missing TELEGRAM_TOKEN or CHANNEL_ID environment variables!")
        return

    try:
        if new_msg != prev_msg:
            bot = telebot.TeleBot(bot_token) 

            sent_message = bot.send_message(channel_id, new_msg)
            logging.info(f"Message sent successfully: {sent_message.message_id}")

            # Update the previous message file
            with open(prev_msg_file, "w") as f:
                f.write(new_msg)
        else:
            logging.info("No new message to send.")

    except telebot.apihelper.ApiException as e:
        logging.error(f"Telegram API Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


# --- Main Execution ---
# Replace this with the actual message URL
new_msg = 'Hello This is telegram Automated msg'

send_to_telegram(new_msg, prev_msg_file)
print('Script completed!')
