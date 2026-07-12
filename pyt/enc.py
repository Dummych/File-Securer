from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from pathlib import Path
import base64
from visuals import timer, deb_print

BASE_DIR = Path(__file__).parent  

def check_folder(dir_pth):
    files = [item for item in dir_pth.iterdir() if item.is_file() and item.name != ".gitkeep"]    
    for file in files:
        dir_pth = dir_pth / file
        with open(dir_pth, "rb") as f:
            raw_data = f.read()
        yield file, raw_data
        dir_pth.unlink(missing_ok=True)         

def to_enc(name, u_files):
    recent_file = name.stem # Ключ
    recent_suff = name.suffix # Значение
    u_files[recent_file] = recent_suff # Изменение
    return name.stem + ".enc"

def to_norm(name, u_files):
    return Path(name).stem + u_files[Path(name).stem]


def derive_key(psw: str, salt: bytes) -> bytes:
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return base64.urlsafe_b64encode(kdf.derive(psw.encode()))

def get_key(psw, enc_salt):
    global fer
    key = derive_key(psw, enc_salt)  
    fer = Fernet(key)

def encrypt_data(user, u_files, pth):
    u_pth = BASE_DIR.parent / "data" / user
    if pth == None:    
            folder = BASE_DIR.parent / "enc" 
            has_files = any(f.is_file() for f in folder.iterdir())
            if has_files:    
                for file, data in check_folder(folder):
                    file = Path(file)
                    raw_data = data
                    encrypt_data_func(u_pth, u_files, file, raw_data)
            elif not has_files:
                deb_print("dir_none", Path(folder).name)
    else:
        file = Path(pth)    
        if file.exists():    
            with open(file, "rb") as f:
                raw_data = f.read()
            encrypt_data_func(u_pth, u_files, file, raw_data)
            file.unlink(missing_ok=True)
        else:
            deb_print("dir_pth_error", None)
           
@timer
def encrypt_data_func(u_pth, u_files, file, raw_data):   
        deb_print("enc_in", file.name)
        enc_data = fer.encrypt(raw_data)
        enc_file = to_enc(file, u_files)
        f_pth = u_pth / enc_file
        with open(f_pth, "wb") as f_enc:
            f_enc.write(enc_data)
        deb_print("enc_out", file.name)       

def decrypt_data(user, u_files, pth):
    folder = BASE_DIR.parent / "data" / user
    if pth == None:
        dir = BASE_DIR.parent / "dec"
        has_files = any(f.is_file() for f in folder.iterdir())
        if has_files:    
            decrypt_data_func(u_files, folder, dir)
        elif not has_files:
            deb_print("dir_none", Path(folder).name)
    else:
        dir = Path(pth)
        if dir.exists():
            decrypt_data_func(u_files, folder, dir)
        elif not dir.exists():
            deb_print("dir_pth_error", None)

@timer
def decrypt_data_func(u_files, folder, dir_pth):
    for file, raw_data in check_folder(folder):
        deb_print("dec_in", Path(file).name)
        enc_data = raw_data
        dec_data = fer.decrypt(enc_data)
        n_file = to_norm(file, u_files)
        u_files.pop(Path(file).stem)
        f_pth = dir_pth / n_file
        with open(f_pth, "wb") as f_dec:
            f_dec.write(dec_data)
        deb_print("dec_out", Path(file).name) 






          