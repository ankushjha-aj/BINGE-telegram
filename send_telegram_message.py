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


def send_to_telegram(new_msg, prev_msg_file="prev_msg.txt"):
    try:
        # Read previous message (if the file exists)
        if os.path.exists(prev_msg_file):
            with open(prev_msg_file, "r") as f:
                prev_msg = f.read().strip()
        else:
            prev_msg = None

        # Compare messages
        if new_msg != prev_msg:
            # Send to Telegram... (your existing code)

            # Write the new message to file
            with open(prev_msg_file, "w") as f:
                f.write(new_msg)
        else:
            logging.info("No new message to send.")

    except FileNotFoundError:
        logging.warning(f"File not found: {prev_msg_file}. Creating a new one.")
        with open(prev_msg_file, "w") as f:
            f.write(new_msg)

    except telebot.apihelper.ApiException as e:
        logging.error(f"Telegram API Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


# --- Main Execution ---
if __name__ == "__main__":
    # Get the new message (you'll adapt how this is obtained)
    new_msg = 'https://photos.app.goo.gl/abcdefg123df'  
    send_to_telegram(new_msg, prev_msg_file)
