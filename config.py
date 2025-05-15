from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyro import validate_session

# ضع القيم الخاصة بك هنا مباشرة
APP_ID = 20621590
# ضع هنا الـ APP_ID الخاص بك كرقم صحيح
APP_HASH = "a7e91275d681fefd4b2453b158b254ec"
# ضع هنا الـ APP_HASH كسلسلة نصية
ss = "AgE6qRYAIBiOkzpeaN8STpFiuthQsBSsrLD8duzw_xVJkCiCg72vfp4ZH_q6sksuK6SrM8FatuTi9xS5xwtbGoebxdxRtuelj3iMWpdmZBND_HhqpxdvT2Ekcs5siWaJbGR1OIbiK0DKVu1o_5KGUTO1QVeie2tv2Ld7uuQxZ6N8SyKmm7T-6yo_95h9uHjschdyr-4QuoKEIsiugnhsmLrb7Rqaptq4xgMlgaKa3pILvNL-cBEWwcOLqidKsefmUItfgGJBLGoiubtbrjH1HgriaMxX4MSAVXHGQUvwH-yv0ty_hu8-WwXShAduWnIngqvAu8YavI7ghO39Ub_4bgqyOGvZLAAAAAG1qpZ3AA="
  # ضع هنا الـ String Session كنص

# التحقق من صحة الجلسة
session = validate_session(ss)

# إنشاء العميل
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# إذا كنت تستخدم بوت، يمكنك تفعيل الأسطر التالية:
# BOT_USERNAME = "your_bot_username"
# token = "your_bot_token"
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()
