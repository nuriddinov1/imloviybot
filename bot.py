import logging
from aiogram import Bot,Dispatcher,executor,types
from wordCheck import checkWord,reposted
from transliterate import transliterate
API_TOKEN="6325909055:AAGVfaW5SIYK1a8MUrfprSsYQQ7xY_ZxoJQ"
logging.basicConfig(level=logging.INFO)
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    startText="Hush kelibsiz!\nBu yerda siz o'zbek tilidagi so'zlari imloviy tekshirib olishingiz mumkin.\n[albatta hozircha👌,keyinchalik esa so'zlarni izohini ham topishingiz mumkin!]"
    await message.reply(startText)
@dp.message_handler(commands=["help"])
async def help(message:types.Message):
    helpText="1. Siz biror so'z yozing\n2. Va bu so'zni to'g'ri yoki noto'g'ri ekanligini tekshiring\n\nto'g'ri=✔\nnoto'g'ri=❌"
    await message.reply(helpText)
@dp.message_handler()
async def check_and_send(message:types.Message):
    try:
        request = transliterate(message.text,"cyrillic")
        repost = list(checkWord(request)['matches'])
        if reposted(request)==True or checkWord(request)['aviable']==True:
            request=transliterate(request,"latin")
            res = f"✅ {request}"
            await message.reply(res)
        else:
            lang=transliterate(message.text,"latin")
            res = f"❌ {lang}\n\n"
            for char in repost:
                t=transliterate(char,"latin")
                res += f"✅ {t}\n"
            await message.reply(res)
    except:
        errorText=f"❌ {message.text} - bunday so'z topilmadi!"
        await message.reply(errorText)


if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)