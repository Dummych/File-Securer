from visuals import main_art, deb_print, main_help, lang_change
import json as j
import os
import enc
from pathlib import Path
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
ph = PasswordHasher()

BASE_DIR = Path(__file__).parent 

with open(BASE_DIR.parent / "json" / "users.json", "r") as Ufile:
    user_dict = j.load(Ufile)


logged = False
c_user = None
c_psw = None
c_key = None
c_files = None


   
def create_user(log, psw):
    if bool(log):
        hash_ = ph.hash(psw)
        salt = os.urandom(16)
        user_dict[log] = {"enc_salt": salt.hex(), "hash_": hash_, "files": {}}
        u_dir = BASE_DIR.parent / "data" / log
        u_dir.mkdir(parents=True, exist_ok=True)
        dump_user(user_dict)  
        return True
    return False    

def valid_user(log, psw):
    global c_user
    global c_psw
    global c_key
    global logged
    global c_files
    if log in user_dict.keys():
        try:
            ph.verify(user_dict[log]["hash_"], psw)
        except VerifyMismatchError:
            return False
        c_user = log
        c_psw = psw
        c_key = enc.get_key(psw, bytes.fromhex(user_dict[log]["enc_salt"]))
        c_files = user_dict[log]["files"]
        logged = True
        return True
    return False    

def valid_str(data, data2):
    data_list = [data, data2]
    total = 0
    for i in data_list:
        if bool(i):
            total += 1
    if total == 2:
        return True
    return False        

def dump_user(Udict):
    pth = BASE_DIR.parent / "json" / "users.json"

    with open(pth, "r") as Ufile:
        users = j.load(Ufile)
    users = Udict
    with open(pth, "w") as Ufile:
        j.dump(users, Ufile, indent=4, ensure_ascii=False) 


def str_parcer(str_list):
    if not str_list:
        return False
    str_list = str_list.split()
    l = len(str_list)
    if l > 3:
        return False
    comm = str_list[0]
    if comm[0] == "/":     
        global cmd
        global arg1
        global arg2 
        if l == 3:
            cmd, arg1, arg2 = str_list[0], str_list[1], str_list[2]       
        elif l == 2:
            cmd, arg1 = str_list[0], str_list[1]  
        elif l == 1:
            cmd = str_list[0]    
    else:
        deb_print("command_error_uknown", None)  

def info_enc(log, c_files, pth):                         
    enc.encrypt_data(log, c_files, pth) # Словарь меняется в to_enc
    dump_user(user_dict)

def info_dec(log, c_files, pth):
    enc.decrypt_data(log, c_files, pth) 
    dump_user(user_dict) 

main_art()

deb_print("help_message", None)

while True:

    str_list = input(">>> ")

    cmd = None
    arg1 = None
    arg2 = None
    
    str_parcer(str_list)

      
    if cmd == "/login":
        log = arg1
        psw = arg2
        val = valid_str(log, psw) 
        if val:
            res = valid_user(log, psw)
            if res:
                deb_print("login_success", None)
            if not res:
                deb_print("login_failed", None) 
        if not val:
            deb_print("login_args_error", None)          
     
    elif cmd == "/reg":
        log = arg1 
        psw = arg2
        val = valid_str(log, psw)
        if val:
            res = create_user(log, psw)
            if res:    
                deb_print("reg_success", None)
            if not res:
                deb_print("reg_failed", None)
        if not val:
            deb_print("reg_args_error", None)           

    elif cmd == "/show_Udict":
        print("Debug: ", user_dict) 

    elif cmd == "/info_list":
        if logged:
            start = 0
            for key, value in user_dict[c_user]["files"].items():
                start += 1
                item = key + value
                print(str(start) + ".", item)
        elif not logged:
            deb_print("login_required", None) 
    

    elif cmd == "/info_enc":
            if logged:
                pth = arg1
                info_enc(c_user, c_files, pth)
            elif not logged:
                deb_print("login_required", None)   

    elif cmd == "/info_dec":
        if logged:
            pth = arg1
            info_dec(c_user, c_files, pth)
        elif not logged:
            deb_print("login_required", None)    
                

    elif cmd == "/clear_u":
        folder = BASE_DIR.parent / "data" / c_user
        folder.rmdir()
        user_dict = {}
        dump_user(user_dict)          
       
    elif cmd == "/help":
        if arg1 == None:
            main_help()
        else:
            deb_print("command_no_args", None)    
    
    elif cmd == "/exit": 
        if arg1 == None:
            break
        else:
            deb_print("command_no_args", None) 

    elif cmd == "/lang":
        lang = arg1
        lang_change(arg1)
    else:
        deb_print("command_error_unknown", None)   
     