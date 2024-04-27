import os
import telebot
from telebot import types
from instaloader import Instaloader, Post
from collections import deque

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token obtained from BotFather
bot = telebot.TeleBot('7109762613:AAHxuPrt4LQi5oPa6BlTJNYhKpX4RBuFDyA')

# Define the directory for downloading reels
DOWNLOADS_DIR = 'downloads'

# Replace 'senpaiii10' with the username of the target user
TARGET_USERNAME = 'senpaiii10'

# Instaloader instance
L = Instaloader()

# Provide your Instagram username and password here
INSTAGRAM_USERNAME = 'wrongboy411'
INSTAGRAM_PASSWORD = 'Adiahh'

# Queue to store messages to be processed
message_queue = deque()

# Function to download Instagram post or reel
def download_post(link):
    try:
        # Download the post or reel
        post = Post.from_shortcode(L.context, link.split('/')[-2])
        L.download_post(post, target=DOWNLOADS_DIR)

        # Get filename of downloaded post or reel
        filename = post.date_utc.strftime("%Y-%m-%d_%H-%M-%S") + "_UTC.mp4"
        return filename, post.title
    except Exception as e:
        raise e


# Define the '/help' command handler
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "**𝙍𝙚𝙚𝙡𝙤𝙜𝙧𝙖𝙢 𝙃𝙚𝙡𝙥**\n\n"
        "𝙏𝙤 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙖 𝙧𝙚𝙚𝙡, 𝙨𝙞𝙢𝙥𝙡𝙮 𝙨𝙚𝙣𝙙 𝙩𝙝𝙚 𝙡𝙞𝙣𝙠 𝙤𝙛 𝙩𝙝𝙚 𝙧𝙚𝙚𝙡 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙩𝙤 𝙩𝙝𝙞𝙨 𝙗𝙤𝙩. 𝙊𝙣𝙘𝙚 𝙮𝙤𝙪'𝙫𝙚 𝙨𝙚𝙣𝙩 𝙩𝙝𝙚 𝙡𝙞𝙣𝙠, 𝙨𝙞𝙩 𝙗𝙖𝙘𝙠 𝙖𝙣𝙙 𝙬𝙖𝙩𝙘𝙝 𝙩𝙝𝙚 𝙢𝙖𝙜𝙞𝙘 𝙝𝙖𝙥𝙥𝙚𝙣! 𝙏𝙝𝙚 𝙗𝙤𝙩 𝙬𝙞𝙡𝙡 𝙝𝙖𝙣𝙙𝙡𝙚 𝙩𝙝𝙚 𝙧𝙚𝙨𝙩 𝙛𝙤𝙧 𝙮𝙤𝙪.\n\n"
        "*𝙀𝙭𝙖𝙢𝙥𝙡𝙚:*\n"
        "𝙎𝙚𝙣𝙙: https://www.instagram.com/reel/XXXXXXXXXXXX/\n\n"
        "𝙄𝙛 𝙮𝙤𝙪 𝙚𝙣𝙘𝙤𝙪𝙣𝙩𝙚𝙧 𝙖𝙣𝙮 𝙞𝙨𝙨𝙪𝙚𝙨 𝙤𝙧 𝙣𝙚𝙚𝙙 𝙛𝙪𝙧𝙩𝙝𝙚𝙧 𝙖𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙘𝙚, 𝙛𝙚𝙚𝙡 𝙛𝙧𝙚𝙚 𝙩𝙤 𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙩𝙝𝙚 𝙗𝙤𝙩 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧."
    )
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')





# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))
# Construct the file path for filee.jpg
filee_path = os.path.join(script_directory, 'filee.jpg')

# Define a handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == "private":
        send_lightning_bolt(message)
        send_private_welcome(message)
    elif message.chat.type == "group" or message.chat.type == "supergroup":
        send_group_welcome(message)

# Function to send ⚡ in private chat
def send_lightning_bolt(message):
    bot.send_message(message.chat.id, "⚡")

# Function to send welcome message and inline buttons in private chat
def send_private_welcome(message):
    first_name = message.from_user.first_name
    welcome_message = f"𝙃𝙚𝙮 <a href='https://t.me/{message.from_user.username}'>{first_name}</a>, 𝙬𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙍𝙚𝙚𝙡𝙤𝙜𝙧𝙖𝙢! 🎉\n\n𝙍𝙚𝙚𝙡𝙤𝙜𝙧𝙖𝙢 𝙞𝙨 𝙮𝙤𝙪𝙧 𝙜𝙤-𝙩𝙤 𝙗𝙤𝙩 𝙛𝙤𝙧 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢 𝙧𝙚𝙚𝙡𝙨. 𝙎𝙞𝙢𝙥𝙡𝙮 𝙨𝙚𝙣𝙙 𝙢𝙚 𝙩𝙝𝙚 𝙡𝙞𝙣𝙠 𝙩𝙤 𝙩𝙝𝙚 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢 𝙧𝙚𝙚𝙡, 𝙖𝙣𝙙 𝙄'𝙡𝙡 𝙩𝙖𝙠𝙚 𝙘𝙖𝙧𝙚 𝙤𝙛 𝙩𝙝𝙚 𝙧𝙚𝙨𝙩. 𝙀𝙣𝙟𝙤𝙮 𝙝𝙖𝙨𝙨𝙡𝙚-𝙛𝙧𝙚𝙚 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙖𝙣𝙙 𝙠𝙚𝙚𝙥 𝙚𝙭𝙥𝙡𝙤𝙧𝙞𝙣𝙜 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢'𝙨 𝙚𝙭𝙘𝙞𝙩𝙞𝙣𝙜 𝙘𝙤𝙣𝙩𝙚𝙣𝙩!"
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(types.InlineKeyboardButton("𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧", url=f"https://t.me/{TARGET_USERNAME}"),
                        types.InlineKeyboardButton("𝘼𝙗𝙤𝙪𝙩", callback_data="About"))
    bot.send_photo(message.chat.id, open(filee_path, 'rb'), caption=welcome_message, reply_markup=inline_keyboard, parse_mode='HTML')

# Function to send welcome message and inline buttons in group chat
def send_group_welcome(message):
    welcome_message = "𝙃𝙚𝙮 𝙩𝙝𝙚𝙧𝙚! 𝙄 𝙖𝙢 𝙍𝙚𝙚𝙡𝙤𝙜𝙧𝙖𝙢, 𝙮𝙤𝙪𝙧 𝙪𝙡𝙩𝙞𝙢𝙖𝙩𝙚 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢 𝙧𝙚𝙚𝙡 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙚𝙧 𝙗𝙤𝙩. 🤖\n\n𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙍𝙚𝙚𝙡𝙤𝙜𝙧𝙖𝙢 ! 🎉\n\n𝙒𝙞𝙩𝙝 𝙍𝙚𝙚𝙡𝙤𝙜𝙧𝙖𝙢, 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙚𝙖𝙨𝙞𝙡𝙮 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢 𝙧𝙚𝙚𝙡𝙨 𝙝𝙖𝙨𝙨𝙡𝙚-𝙛𝙧𝙚𝙚. 𝙅𝙪𝙨𝙩 𝙨𝙝𝙖𝙧𝙚 𝙩𝙝𝙚 𝙡𝙞𝙣𝙠 𝙩𝙤 𝙩𝙝𝙚 𝙧𝙚𝙚𝙡 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙, 𝙖𝙣𝙙 𝙄'𝙡𝙡 𝙙𝙤 𝙩𝙝𝙚 𝙧𝙚𝙨𝙩 𝙛𝙤𝙧 𝙮𝙤𝙪. 𝙄𝙩'𝙨 𝙩𝙝𝙖𝙩 𝙨𝙞𝙢𝙥𝙡𝙚!\n\n𝙁𝙚𝙚𝙡 𝙛𝙧𝙚𝙚 𝙩𝙤 𝙚𝙭𝙥𝙡𝙤𝙧𝙚 𝙩𝙝𝙚 𝙛𝙚𝙖𝙩𝙪𝙧𝙚𝙨 𝙖𝙣𝙙 𝙡𝙚𝙩 𝙢𝙚 𝙠𝙣𝙤𝙬 𝙞𝙛 𝙮𝙤𝙪 𝙣𝙚𝙚𝙙 𝙖𝙣𝙮 𝙖𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙘𝙚 !"
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(types.InlineKeyboardButton("𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧", url=f"https://t.me/{TARGET_USERNAME}"),
                        types.InlineKeyboardButton("𝘼𝙗𝙤𝙪𝙩", callback_data="About"))
    bot.send_photo(message.chat.id, open(filee_path, 'rb'), caption=welcome_message, reply_markup=inline_keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "About":
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        about_message = """
        🤖 **𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙍𝙚𝙚𝙡𝙤𝙜𝙧𝙖𝙢!**

        *𝙈𝙤𝙙𝙪𝙡𝙚𝙨 𝙐𝙨𝙚𝙙:*
        1. 𝙏𝙚𝙡𝙚𝙗𝙤𝙩
        2. 𝙄𝙣𝙨𝙩𝙖𝙡𝙤𝙖𝙙𝙚𝙧

        *𝙑𝙚𝙧𝙨𝙞𝙤𝙣𝙨:*
        - 𝙏𝙚𝙡𝙚𝙗𝙤𝙩: 12.0.0
        - 𝙄𝙣𝙨𝙩𝙖𝙡𝙤𝙖𝙙𝙚𝙧𝙩: 𝙇𝙖𝙩𝙚𝙨𝙩 𝙑𝙚𝙧𝙨𝙞𝙤𝙣
        
        *𝘾𝙤𝙣𝙣𝙚𝙘𝙩𝙚𝙙 𝙬𝙞𝙩𝙝 𝙄𝙣𝙨𝙩𝙖 𝙖𝙘𝙘𝙤𝙪𝙣𝙩*
        
        *☠️𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧☠️:*
        - <a href='https://t.me/senpaiii10'>    𝘼𝘼𝘿𝙄𝙄𝙄 👾</a>
        """
        bot.edit_message_caption(chat_id=chat_id, message_id=message_id, caption=about_message, parse_mode='HTML')
        back_button = types.InlineKeyboardButton("𝘽𝙖𝙘𝙠", callback_data="Back")
        inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
        inline_keyboard.add(back_button)
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=inline_keyboard)
    elif call.data == "Back":
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        if call.message.chat.type == "private":
            send_private_welcome_edited(chat_id, message_id)
        elif call.message.chat.type == "group" or call.message.chat.type == "supergroup":
            send_group_welcome_edited(chat_id, message_id)

# Function to send the edited welcome message in private chat
def send_private_welcome_edited(chat_id, message_id):
    welcome_message = "Hey there, welcome to Reelogram! 🎉\n\nReelogram is your go-to bot for downloading Instagram reels. Simply send me the link to the Instagram reel, and I'll take care of the rest. Enjoy hassle-free downloading and keep exploring Instagram's exciting content!"
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(types.InlineKeyboardButton("𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧", url=f"https://t.me/{TARGET_USERNAME}"),
                        types.InlineKeyboardButton("𝘼𝙗𝙤𝙪𝙩", callback_data="About"))
    bot.edit_message_caption(chat_id=chat_id, message_id=message_id, caption=welcome_message, reply_markup=inline_keyboard)

# Function to send the edited welcome message in group chat
def send_group_welcome_edited(chat_id, message_id):
    welcome_message = "Hey there! I am Reelogram, your ultimate Instagram reel downloader bot. 🤖\n\nWelcome to Reelogram ! 🎉\n\nWith Reelogram, you can easily download Instagram reels hassle-free. Just share the link to the reel you want to download, and I'll do the rest for you. It's that simple!\n\nFeel free to explore the features and let me know if you need any assistance !"
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(types.InlineKeyboardButton("𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧", url=f"https://t.me/{TARGET_USERNAME}"),
                        types.InlineKeyboardButton("𝘼𝙗𝙤𝙪𝙩", callback_data="About"))
    bot.edit_message_caption(chat_id=chat_id, message_id=message_id, caption=welcome_message, reply_markup=inline_keyboard)



# Function to handle Instagram link messages
@bot.message_handler(regexp=r'https://www.instagram.com/(reel)/[A-Za-z0-9_-]+/')
def handle_instagram_link(message):
    try:
        # Send "Please wait" message instantly
        wait_message = bot.send_message(message.chat.id, "🦎 𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 𝙬𝙝𝙞𝙡𝙚 𝙬𝙚 𝙥𝙧𝙤𝙘𝙚𝙨𝙨 𝙮𝙤𝙪𝙧 𝙧𝙚𝙦𝙪𝙚𝙨𝙩...")

        # Add the message to the queue along with the "Please wait" message
        message_queue.append((message, wait_message))

        # If this is the only message in the queue, process it
        if len(message_queue) == 1:
            process_next_message()

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

# Function to process the next message in the queue
def process_next_message():
    try:
        if message_queue:
            message, wait_message = message_queue[0]

            # Extract link from the message
            link = message.text.strip()

            # Download the post or reel
            filename, title = download_post(link)

            # Extract reel title from the message
            post = Post.from_shortcode(L.context, link.split('/')[-2])
            reel_title = post.caption

            # Delete the "Please wait" message
            bot.delete_message(message.chat.id, wait_message.message_id)

            # Send a message with the reel title indicating that the reel is being downloaded
            downloading_message = bot.send_message(message.chat.id, f"☁ 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 - {reel_title}")

            # Send the downloaded video back to the user
            video_path = os.path.join(DOWNLOADS_DIR, filename)
            with open(video_path, 'rb') as video_file:
                sent_video = bot.send_video(message.chat.id, video_file)

            # Delete the downloaded video from PC only if it has been sent successfully
            os.remove(video_path)

            # Delete non-.mp4 files from the 'downloads' directory
            for file in os.listdir(DOWNLOADS_DIR):
                if not file.endswith(".mp4"):
                    os.remove(os.path.join(DOWNLOADS_DIR, file))
            
            # Delete the "Reel title Downloading..." message
            bot.delete_message(message.chat.id, downloading_message.message_id)

            # Remove the processed message from the queue
            message_queue.popleft()

            # Process the next message if available
            if message_queue:
                process_next_message()

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")



# Log in using the provided Instagram username and password
L.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

# Polling to keep the bot running
bot.polling()