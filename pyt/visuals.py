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
        deb_print("timer_succes", end)
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
            deb_print("lang_unknown_error")  
    else:
        deb_print("lang_unknown_error")   

def deb_print(value, obj=None):
    global lang

    for flag, messages in deb_dict[lang].items():
        if value in messages:
            print(flag, messages[value].format(obj=obj))
            return

deb_dict = {
    "RU": {
        "[ENC]": {
            "enc_in": "Принят файл {obj}",
            "enc_out": "Зашифрован файл {obj}"
        },

        "[DEC]": {
            "dec_in": "Принят файл {obj}",
            "dec_out": "Дешифрован файл {obj}"
        },

        "[DIR]": {
            "dir_none": "Папка {obj} в данный момент пуста",
            "dir_pth_error": "Файл/папка по такому пути не найден(а), попробуйте ещё раз"
        },

        "[CMD]": {
            "command_error_unknown": "Ошибка: неизвестная команда",
            "command_no_args": "Эта команда не принимает аргументов. Попробуйте ещё раз",

            "login_success": "Вы успешно вошли!",
            "login_failed": "Логин или пароль неверны, попробуйте ещё раз",
            "login_args_error": "Ошибка: неправильные аргументы, попробуйте /login <login> <password>",

            "reg_success": "Профиль создан успешно!",
            "reg_failed": "Ошибка создания профиля, попробуйте ещё раз",
            "reg_args_error": "Ошибка: неправильные аргументы, попробуйте /reg <login> <password>",

            "login_required": "Вам нужно войти в профиль для использования этой команды",

            "lang_unknown_error": "Неизвестное значение языка. Попробуйте ещё раз.",
            "lang_changed": "Язык сменён. Текущий язык: {obj}",

            "help_message": "Введите /help для получения справки."
        },

        "[TIME]": {
            "timer_success": "Процесс выполнен. Затрачено времени: {obj} секунд."
        }
    },

    "EN": {
        "[ENC]": {
            "enc_in": "Received file {obj}",
            "enc_out": "Encrypted file {obj}"
        },

        "[DEC]": {
            "dec_in": "Received file {obj}",
            "dec_out": "Decrypted file {obj}"
        },

        "[DIR]": {
            "dir_none": "Directory {obj} is currently empty",
            "dir_pth_error": "File or directory not found. Please try again."
        },

        "[CMD]": {
            "command_error_unknown": "Error: unknown command",
            "command_no_args": "This command does not accept any arguments. Please try again.",

            "login_success": "Successfully logged in!",
            "login_failed": "Incorrect login or password. Please try again.",
            "login_args_error": "Error: invalid arguments. Try /login <login> <password>",

            "reg_success": "Profile created successfully!",
            "reg_failed": "Failed to create profile. Please try again.",
            "reg_args_error": "Error: invalid arguments. Try /reg <login> <password>",

            "login_required": "You need to log in to use this command.",

            "lang_unknown_error": "Unknown language value. Please try again.",
            "lang_changed": "Language changed. Current language: {obj}",

            "help_message": "Type /help for help."
        },

        "[TIME]": {
            "timer_success": "Process completed. Time taken: {obj} seconds."
        }
    }
}