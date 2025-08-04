import os
import subprocess
import aiofiles
from pyrogram import Client, filters
from pyrogram.types import Message
import os import subprocess import aiofiles from pyrogram import Client, filters from pyrogram.types import Message
API_ID = 21702672  # 🔁 Replace with your actual API ID API_HASH = "your_api_hash_here"  # 🔁 Replace with your actual API hash BOT_TOKEN = "your_bot_token_here"  # 🔁 Replace with your actual bot token

bot = Client("classplus_uploader_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

"🔧 Function to download and send video from .m3u8 link"

async def download_and_send_video(link, chat_id, bot, index): try: output_file = f"video_{index}.mp4" cmd = f'ffmpeg -i "{link}" -c copy -loglevel quiet "{output_file}"' subprocess.run(cmd, shell=True)

if os.path.exists(output_file):
        await bot.send_video(chat_id=chat_id, video=open(output_file, 'rb'))
        os.remove(output_file)
    else:
        await bot.send_message(chat_id, f"❌ Download failed: {link}")
except Exception as e:
    await bot.send_message(chat_id, f"⚠️ Error downloading video: {e}")

📥 Handle .txt file upload

@bot.on_message(filters.document & filters.private) async def upload_course_txt(message: Message): try: file = await message.download() chat_id = message.chat.id await message.reply_text("⏳ Uploading course, please wait...", quote=True)

index = 1
    async with aiofiles.open(file, mode='r') as f:
        async for line in f:
            if line.strip().startswith("http") and ".m3u8" in line:
                await download_and_send_video(line.strip(), chat_id, bot, index)
                index += 1

    await message.reply_text("✅ Course upload complete.")
except Exception as e:
    await message.reply_text(f"❌ Error: {e}")

▶️ Start the bot

bot.run()

