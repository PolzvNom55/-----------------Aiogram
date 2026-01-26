import os 
from dotenv import load_dotenv
load_dotenv()
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio


'''Синх - отдельно, Асинх, async - вместе сразу отвечает пользователям'''

# answer - чтобы просто отвечал обычно
# reply - чтобы при ответе, еще и упоминал пользователя


 
bot = Bot(token=os.getenv('BOT_Token'))
dp = Dispatcher()

# Dispatcher - это то, благодаря чему бот отвечает
# CommandStart - нужен для того, чтобы давать старт для нашего бота

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer("Бот Активирован! Можете ввести - /help - для информации")

@dp.message(Command('help'))
async def help(message:Message):
    await message.reply("Привет!, Чем я могу помочь? \n - Есть подсказки для вас: \n /start, /help,\n /about -,\n /contact - для ответа контактом,\n /location - геолокация Ош") # Реплай - отвечает на сообщение
    await message.reply("Дополнительный раздел: \n-Пользователь - инф. о человеке, \n- фото - обычное")
    


@dp.message(Command('about'))
async def about(message:Message):
    await message.reply("Школа Курманжан Датка - находится в городе ОШ!") # Реплай - отвечает на сообщение

@dp.message(Command('contact'))
async def contact(message:Message):
    await message.reply_contact(phone_number="+996706403395", last_name='Im', first_name="I") # reply_contact - отвечает контактом

@dp.message(Command('location'))
async def location(message:Message):
    await message.reply_location(latitude="40.51591787118994", longitude="72.80318621740489") # reply_location - отвечает локацией, дает указанную локацию

# latitude=  - ширина 
# longitude=   - долгота

# @dp.message(F.text.lower() == 'Polzovatel') # F - мы его используем, когда бот принимает текст,text вместо command
# async def polzovatel(message:Message):
#     await message.reply("Пользователь - 3 месяца")

@dp.message(F.text.lower() == 'Пользователь') # F - мы его используем, когда бот принимает текст,text вместо command
async def polzovatel(message:Message):
    await message.reply("Пользователь - 3 месяца")



@dp.message(F.text.lower() == 'фото') # F - мы его используем, когда бот принимает текст,text вместо command
async def photo(message:Message):
    await message.reply_photo(photo="https://biodt.eu/sites/default/files/2024-09/Forest%20Biodiversity%20Dynamics.jpg")


# @dp.message(F.sticker)
# async def get_sticker_id(message:Message):
#     await message.answer(f"file_id: \n<code>{message.sticker.file_id}</code>", parse_mode="HTML")


# Для запуска бота: Обязательно писать
async def main():
    await dp.start_polling(bot)
# Нужно заполнить вот эти 4 блока 
asyncio.run(main())


