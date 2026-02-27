from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import asyncio

TOK = "ВАШ_ТОКЕН"

bot = Bot(token='TOK')
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='Направления'),
KeyboardButton(text='контакты')], 
[KeyboardButton(text='о нас')]]

keyboardz = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,
input_field_placeholder='Выберите кнопку', one_time_keyboard=True)
#-----------------------------------------------------------------


courses_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Курсы')
# KeyboardButton(text=''), 
# KeyboardButton(text='')
    ]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку', 
one_time_keyboard=True)



courses = {
    "Backend": {
    'desk': 'Backend - это внутрення часть сайта, серверная логика и базы данных.',
    "price": '4500 сом в месяц', 
    "duration": '7 месяцев'},

    'Frontend': {
    "desk": "Frontend - это визуальная часть сайта, интерфейсы и взаимодействия с пользователем.",
    "price": '4000 сом в месяц',
    "duration": '5 месяцев'},

    "English": {
    "desk": 'Изучаем английский язык до уверенного уровня!',
    "price": '3500 сом в месяц',
    "duration": '6 месяцев'},

    "Продленка": {
    "desk": 'Дети делают домашнюю работу с учителем и развивающиеся задания',
    "price": '3000 сом в месяц',
    "duration": '2 месяца'},

    "Арифметика": {
    "desk": 'Развитие быстрого счета, логики, внимания и памяти',
    "price": '4000 сом в месяц',
    "duration": '6 месяцев'}
}


@dp.message(CommandStart())
async def about_start(message: types.Message):
    await message.answer("Добро пожаловать в StarTum!\nВыберите раздел:", reply_markup=keyboardz) 

@dp.message(F.text == 'о нас')
async def Command_F1(message: types.Message):
    await message.answer("StarTum - образовательный центр профессий для детей и подростков", reply_markup=keyboardz) 


@dp.message(F.text == 'контакты')
async def Command_F2(message: types.Message):
    await message.reply_contact(phone_number="+996706403395", last_name='A', first_name="S")
    await message.answer("Адрес - Город ОШ\nУлица: Ленин проспект 47")


@dp.message(F.text == 'Направления')
async def about_f_strokes(message: types.Message):
    await message.reply('Выберите любой курс:', reply_markup=courses_keyboard) 


@dp.message(F.text.in_({'привет', 'првет', 'здравствуй', 'хай', 'здравствуйте'}))
async def about_in(message: types.Message):
    await message.reply("Привет") 


@dp.message(F.text.in_({'назад', 'НАЗАД', 'Назад'}))
async def Command_back(message: types.Message):
    await message.reply('Главное меню:', reply_markup=keyboardz)
    


@dp.message()
async def show_menu(message: types.Message):
    if message.text == 'Курсы':
        data = courses['Backend']
        await message.answer(f'{data['desk']}\nЦена = {data['price']}\n Время = {data['duration']}') 
    elif message.text == 'Курсы':
        data = courses['Frontend']
        await message.answer(f'{data['desk']}\nЦена = {data['price']}\n Время = {data['duration']}') 
    elif message.text == 'Курсы':
        data = courses['English']
        await message.answer(f'{data['desk']}\nЦена = {data['price']}\n Время = {data['duration']}') 


@dp.message()
async def Command_None(message: types.Message):
    await message.reply('Я вас не понял, введите "Назад" для выхода в гл. меню') 

async def main():
    await dp.start_polling(bot)
asyncio.run(main())
