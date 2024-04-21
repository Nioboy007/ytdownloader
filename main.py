import os 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import Client, filters,emoji
from pyrogram.types import Message
import os
import math
from Plugins.commands import commands
import time
import requests
from pytube import YouTube
import time
from helpers.progress import TimeFormatter, humanbytes, format_bytes, progress_for_pyrogram
import pytube
import urllib.request
import re
from helpers.thumbnail import take_screen_shot
from pytube import Playlist
from pytube.exceptions import AgeRestrictedError


from pytube.innertube import InnerTube

# Modify the client used by InnerTube
InnerTube._default_clients['ANDROID_MUSIC'] = InnerTube._default_clients['ANDROID']



START_TEXT, HELP_TEXT, UPLOAD_START, ABOUT_TEXT, START_BUTTONS, result_buttons, HELP_BUTTONS, ABOUT_BUTTONS, SOURCE_TEXT, SOURCE_BUTTONS, result_text = commands()

HB = Client(
    "YOUTUBE Bot",
    bot_token=os.environ.get("BOT_TOKEN", "6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU"),
    api_id=int(os.environ.get("API_ID", "10471716")),
    api_hash=os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")
)

VIDEO_REGEX = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/|(?:youtube\.com\/shorts\/))(?P<video_id>[a-zA-Z0-9_-]{11})'
PLAYLIST_REGEX = r'(.*)youtube.com/(.*)[&|?]list=(?P<playlist>[^&]*)(.*)'
start_time = time.time()




@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )







# Handler for YouTube video URLs
@HB.on_message(filters.regex(VIDEO_REGEX))
async def ytdl(_, message):
    try:
        # Use authenticated credentials for YouTube requests
        yt = YouTube(message.text)

        # Extract video information
        thumb = yt.thumbnail_url
        length = yt.length
        video_title = yt.title
        thumb_extension = ".jpeg"
        custom_thumb_filename = f"{video_title}{thumb_extension}"
        thumb_filename, _ = urllib.request.urlretrieve(thumb, custom_thumb_filename)
        ythd = yt.streams.get_highest_resolution()
        ytlow = yt.streams.get_by_resolution(resolution='360p')
        file = yt.streams.filter(only_audio=True).first()
        ytaudio = yt.streams.filter(only_audio=True).first()
        download = ytaudio.download(filename=f"{str(yt.title)}")
        rename = os.rename(download, f"{str(yt.title)}.mp3")
        audio_size = f"{int(format_bytes(ytaudio.filesize)[0]):.2f}{format_bytes(ytaudio.filesize)[1]}"
        hd = f"{int(format_bytes(ythd.filesize)[0]):.2f}{format_bytes(ythd.filesize)[1]}"
        low = f"{int(format_bytes(ytlow.filesize)[0]):.2f}{format_bytes(ytlow.filesize)[1]}"

        # Prepare inline keyboard buttons
        result_buttons2 = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('🎬720P ' + ' ⭕️ ' + hd, callback_data='high'),
                InlineKeyboardButton('🎬 360p ' + '⭕️ ' + low, callback_data='360p')
            ], [
                InlineKeyboardButton('🎧 AUDIO ' + '⭕️ ' + audio_size, callback_data='audio')
            ], [
                InlineKeyboardButton('🖼THUMBNAIL🖼', callback_data='thumbnail')
            ]]
        )

        # Send video thumbnail with caption and inline keyboard
        await message.reply_photo(
            photo=thumb_filename,
            caption="🎬 TITLE : " + yt.title + "\n\n📤 UPLOADED : " + yt.author + "\n\n📢 CHANNEL LINK " + f'https://www.youtube.com/channel/{yt.channel_id}',
            reply_markup=result_buttons2,
            quote=True,
        )

    except AgeRestrictedError as e:
        # Handle age-restricted videos
        error_message = "This video is age-restricted and cannot be accessed without logging in."
        print(f"Error occurred: {error_message}")
        await message.reply_text(error_message)
    except Exception as e:
        # Handle other exceptions
        error_message = f"An error occurred: {str(e)}"
        print(f"Error occurred: {error_message}")
        await message.reply_text("An unexpected error occurred while processing the video.")



@HB.on_callback_query()
async def cb_data(bot, update):
   
    if update.data == 'high':
        try:
            await HB.send_video(
                chat_id=update.message.chat.id,
                video=ythd.download(),
                caption=result_text,
                duration=length,
                thumb=thumb_filename,  # Use the downloaded thumbnail file
                reply_markup=result_buttons,
                progress=progress_for_pyrogram,
                progress_args=(
                    UPLOAD_START,
                    update.message,
                    start_time
                )
            )
            await update.message.delete()
        except Exception as e:
            error_message = f"Error occurred: {str(e)}"
            await HB.send_message(
                chat_id=update.message.chat.id,
                text="**😔 1080P QUALITY IS NOT AVAILABLE\n CHOOSE ANY OTHER QUALITIES**"
            )
            await HB.send_message(
                chat_id=update.message.chat.id,
                text=error_message
            )

    elif update.data == '360p':
        try:
            await HB.send_video(
                chat_id=update.message.chat.id,
                video=ytlow.download(),
                caption=result_text,
                duration=length,
                reply_markup=result_buttons,
                thumb=thumb_filename,  # Use the downloaded thumbnail file
                progress=progress_for_pyrogram,
                progress_args=(
                    UPLOAD_START,
                    update.message,
                    start_time
                )
            )
            await update.message.delete()
        except Exception as e:
            error_message = f"Error occurred: {str(e)}"
            await HB.send_message(
                chat_id=update.message.chat.id,
                text="**😔 360P QUALITY IS NOT AVAILABLE \n CHOOSE ANY OTHER QUALITIES**"
            )
            await HB.send_message(
                chat_id=update.message.chat.id,
                text=error_message
            )

    elif update.data == 'audio':
        try:
            await HB.send_audio(
                chat_id=update.message.chat.id,
                audio=f"{str(yt.title)}.mp3",
                caption=result_text,
                duration=yt.length,
                reply_markup=result_buttons,
                progress=progress_for_pyrogram,
                progress_args=(
                    UPLOAD_START,
                    update.message,
                    start_time
                )
            )
            await update.message.delete()
        except Exception as e:
            error_message = f"Error occurred: {str(e)}"
            await HB.send_message(
                chat_id=update.message.chat.id,
                text="**Error occurred while sending audio**"
            )
            await HB.send_message(
                chat_id=update.message.chat.id,
                text=error_message
            )

    elif update.data == 'thumbnail':
        try:
            await HB.send_photo(
                chat_id=update.message.chat.id,
                photo=thumb,
                caption="**JOIN @TELSABOTS**"
            )
            await update.message.delete()
        except Exception as e:
            error_message = f"Error occurred: {str(e)}"
            await HB.send_message(
                chat_id=update.message.chat.id,
                text="**Error occurred while sending thumbnail**"
            )
            await HB.send_message(
                chat_id=update.message.chat.id,
                text=error_message
            )

    elif update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await update.message.delete()


@HB.on_message(filters.regex(PLAYLIST_REGEX))
async def ytdl(_, update):
   purl=update.text
   pyt = Playlist(purl)
  
   for video in pyt.videos:
    phd =video.streams.get_highest_resolution()
    
    await  HB.send_video(
            chat_id = update.chat.id, 
            caption=(f"⭕️ PLAYLIST : "+ pyt.title + "\n📥 DOWNLOADED " + "\n✅ JOIN @TELSABOTS" ),
            video = phd.download(),
            
    )
print("Private Botz On the Run HOHOHO *LOL 😂")
HB.run()
