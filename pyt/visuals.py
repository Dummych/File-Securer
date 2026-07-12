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
    global lang
    
    if lang == "RU":
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

/lang <value>
    RU Русский
    EN English
/exit
    Завершить работу программы.

==============================================
""")
        
    elif lang == "EN":
        print("""
==============================================

/reg <login> <password>
    Register a new user.

/login <login> <password>
    Log in to an existing account.

/info_list
    Show a list of all saved file names.

/info_enc <path_to_file>
    The file path is optional. If omitted, files will be searched automatically in the "enc" directory.

/info_dec <path_to_dir>
    The output directory is optional. If omitted, decrypted files will be saved automatically to the "dec" directory.

/info_del <name>
    Delete a file by its name.

/help
    Display this help message.

/lang <value>
    RU Русский
    EN English

/exit
    Exit the program.

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

lang = "EN" 

def lang_change(n_lang):
    global lang
    langs = ["RU", "EN"]
    if n_lang != None:
        if n_lang in langs:
            lang = n_lang
            deb_print("lang_changed", n_lang)
        else:
            deb_print("lang_unknown_error", None)  
    else:
        deb_print("lang_unknown_error", None)   

def deb_print(value, obj):
    global lang

    if value == "enc_in":
        flag = "[ENC]"
        if lang == "RU":
            print(flag, "Принят файл", obj)
        elif lang == "EN":
            print(flag, "Received file", obj)

    elif value == "enc_out":
        flag = "[ENC]"
        if lang == "RU":
            print(flag, "Зашифрован файл", obj)
        elif lang == "EN":
            print(flag, "Encrypted file", obj)

    elif value == "dec_in":
        flag = "[DEC]"
        if lang == "RU":
            print(flag, "Принят файл", obj)
        elif lang == "EN":
            print(flag, "Received file", obj)

    elif value == "dec_out":
        flag = "[DEC]"
        if lang == "RU":
            print(flag, "Дешифрован файл", obj)
        elif lang == "EN":
            print(flag, "Decrypted file", obj)

    elif value == "dir_none":
        flag = "[DIR]"
        if lang == "RU":
            print(flag, "Папка", obj, "в данный момент пуста")
        elif lang == "EN":
            print(flag, "Directory", obj, "is currently empty")

    elif value == "dir_pth_error":
        flag = "[DIR]"
        if lang == "RU":
            print(flag, "Файл/папка по такому пути не найден(а), попробуйте ещё раз")
        elif lang == "EN":
            print(flag, "File or directory not found. Please try again.")
    
    elif value == "command_error_unknown":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Ошибка: неизвестная команда")
        elif lang == "EN":
            print(flag, "Error: unknown command")

    elif value == "command_no_args":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Эта команда не требует аргументов. Попробуйте еще раз")
        elif lang == "EN":
            print(flag, "This command does not accept any arguments. Please try again.")            

    elif value == "login_success":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Вы успешно вошли!")
        elif lang == "EN":
            print(flag, "Successfully logged in!")

    elif value == "login_failed":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Логин или пароль неверны, попробуйте ещё раз")
        elif lang == "EN":
            print(flag, "Incorrect login or password. Please try again.")

    elif value == "login_args_error":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Ошибка: неправильные аргументы, попробуйте /login <login> <password>")
        elif lang == "EN":
            print(flag, "Error: invalid arguments. Try /login <login> <password>")

    elif value == "reg_success":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Профиль создан успешно!")
        elif lang == "EN":
            print(flag, "Profile created successfully!")

    elif value == "reg_failed":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Ошибка создания профиля, попробуйте ещё раз")
        elif lang == "EN":
            print(flag, "Failed to create profile. Please try again.")

    elif value == "reg_args_error":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Ошибка: неправильные аргументы, попробуйте /reg <login> <password>")
        elif lang == "EN":
            print(flag, "Error: invalid arguments. Try /reg <login> <password>")

    elif value == "login_required":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Вам нужно войти в профиль для использования этой команды")
        elif lang == "EN":
            print(flag, "You need to log in to use this command.")

    elif value == "lang_unknown_error":
        flag = "[CMD]"
        print(flag, "Unknown language value. Please try again.")

    elif value == "lang_changed":
        flag = "[CMD]"
        if lang == "RU":
            print(flag, "Язык сменён. Текущий язык:", obj)
        elif lang == "EN":
            print(flag, "Language changed. Current language:", obj)         

    elif value == "help_message":
        flag = "[CMD]"
        print(flag, "Type /help for manual.")

    elif value == "timer_succes":
        flag = "[TIME]"
        if lang == "RU":
            print(flag, "Процесс выполнен. Затрачено времени:", obj, "секунд")
        elif lang == "EN":
            print(flag, "Process completed. Time taken:", obj, "seconds.")         

