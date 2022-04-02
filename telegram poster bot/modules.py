import os
import random
import shutil

import config.settings


# функция выбора файла из заданой папки
def choose_file():
    print("Начинаем выбор файла...")
    files = os.listdir(srcdir)
    file_name = random.choice(files)
    filename = str(srcdir+file_name)
    tempname = 
    shutil.copy(filename, tempname)
    shutil.move(filename, dscdir+file_name)
    print("Выбор файла завершен")

# функция выбора подписи по заданым параметрам с условиями наличия (отсутствия) заданых ключевых слов в названии файла
def choose_caption():
    print ("Выбор описания")
    file_caption = str(file_name)[:-4]
    default_caption = random.choice(open(r"config/default_captions.txt").readlines())
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
    print("Подготовка завершена")
    
# функция одиночного постинка (картинка с подписью) в telegram канал   
def single_posting():
    print("Начинаем одиночный постинг")
    
# функция двойного постинга (картинка с подписью и файл) в telegram канал 
def double_posting():
    print("Начинаем двойной постинг")

# запуск постинга
def run_posting():

    print("Файл успешно опубликован")
    
# отправка отчета о проделаной работе    
def send_feedback():