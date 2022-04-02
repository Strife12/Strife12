import os
import random
import shutil

import config.settings


# функция выбора файла из заданой папки. Создание его копии для работы и отправка исходного фото в архив
def choose_file():
    print("Начинаем выбор файла...")
    files = os.listdir(srcdir)
    file_name = random.choice(files)
    filename = str(srcdir+file_name)
    tempname = 
    shutil.copy(filename, tempname)
    shutil.move(filename, dscdir+file_name)
    print("Выбор файла завершен")

# функция выбора подписи по заданым параметрам с условиями наличия (отсутствия) заданых ключевых слов в названии файла.
# берется название файла, отгрызается расширение, полученая строка проверяется на наличие стоп-слов и при необходимости заменяется на случайную строку из файла
def choose_caption():
    print ("Выбор описания")
    file_caption = str(file_name)[:-4]
    default_caption = random.choice(open(r"default_captions.txt").readlines())
    caption = file_caption
    if "undefined" or "rdt_20" or "daily" or "i made" in str(file_caption):
        caption = default_caption
    print("Описание выбрано")

# функция подготовки данных к публикации
def posting_preparation():
    print("Подготовка публикации")
    bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    filename = str(tempfile)
    file = open(f"{tempfile}", 'rb')
    caption =str(caption)
    document = open(f"{filename}", 'rb')
    print("Подготовка завершена")
    
# функция одиночного постинка (картинка с подписью) в telegram канал   
def single_posting():
    print("Начинаем одиночный постинг")
    async def main():

    await bot.send_photo(channel_ID, photo=file, caption=caption)
    await bot.send_message(admins, text = "На канале "+channel+" опубликован файл "+filename+" \n В папке осталось "+filesremain+" файлов")
    
# функция двойного постинга (картинка с подписью и файл) в telegram канал 
def double_posting():
    print("Начинаем двойной постинг")
    async def main():

    await bot.send_photo(channel_ID, photo=file, caption=caption)
    await bot.send_document(channel_ID, document=document)
    await bot.send_message(admins, text = "На канале "+channel+" осталось "+filesremain+" файлов")

# запуск постинга
def run_posting():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


    print("Файл успешно опубликован")
    
# отправка отчета о проделаной работе    
def send_feedback():


    print("Работа бота завершена. Ожидание нового запуска. ")