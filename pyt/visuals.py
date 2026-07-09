from pathlib import Path
from time import time
def main_art():
    print(r"""
=========================================================
   ______ _ _        _____
  |  ____(_) |      / ____|
  | |__   _| | ___ | (___   ___  ___ _   _ _ __ ___
  |  __| | | |/ _ \ \___ \ / _ \/ __| | | | '__/ _ \
  | |    | | |  __/ ____) |  __/ (__| |_| | | |  __/
  |_|    |_|_|\___||_____/ \___|\___|\__,_|_|  \___|

               File Secure
               Build: stable 0.1.0
=========================================================
""")    

def main_help():
    print("""
==============================================

/reg <login> <password>
    Регистрация нового пользователя.

/login <login> <password>
    Вход в существующий аккаунт.

/info_list
    Показать список названий всех сохранённых файлов.

/info_enc <path_to_file>
    Путь до файла опционален. Если его не указать, то поиск файлов будет автоматически воспроизведён из папки "enc".

/info_dec <path_to_dir>
    Путь до папки для расшифрованных файлов опционален. Если его не указать, то расшифрованные файлы автоматически попадут в папку "dec".                                       

/info_del <name>
    Удалить файл по его названию.

/help
    Показать эту справку.

/exit
    Завершить работу программы.

==============================================
""")
    
def timer(func):
    def wrapper(*args, **kwargs):
        begin = time()
        res = func(*args, **kwargs)
        end = time() - begin
        print("[TIME] Процесс выполнен. Затрачено времени:", end, "секунд")
        return res
    return wrapper    

def deb_print(value, obj):
    var = True
    if value == "enc_in":
        flag = "[ENC]"
        if var == True:
           print(flag, "Принят файл", obj)
        elif var == False:
            print(flag, "Принят файл", obj)
    elif value == "enc_out":
        flag = "[ENC]"
        if var == True:
           print(flag, "Зашифрован файл", obj)
        elif var == False:
            print(flag, "Зашифрован файл", obj)    
    elif value == "dec_in":
        flag = "[DEC]"
        if var == True:
           print(flag, "Принят файл", obj)
        elif var == False:
            print(flag, "Принят файл", obj) 
    elif value == "dec_out":
        flag = "[DEC]"
        if var == True:
            print(flag, "Дешифрован файл", obj)
        elif var == False:
            print(flag, "Дешифрован файл", obj) 
    elif value == "dir_none":
        flag = "[DIR]"         
        if var == True:
            print(flag, "Папка", obj, "в данный момент пуста")
        elif var == True:
            print(flag, "Папка", obj, "в данный момент пуста")  
    elif value == "dir_pth_error":
        flag = "[DIR]" 
        if var == True:
            print(flag, "Файл по такому пути не найден, попробуйте ещё раз")
        elif var == True:
            print(flag, "Файл по такому пути не найден, попробуйте ещё раз")          
