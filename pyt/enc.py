from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from pathlib import Path
import base64
from visuals import timer, deb_print

BASE_DIR = Path(__file__).parent  

def check_folder(dir_pth):
    files = [item for item in dir_pth.iterdir() if item.is_file()]    
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

@timer
def encrypt_data_func(u_pth, u_files, folder):   
    for file, raw_data in check_folder(folder):
        file = Path(file)
        deb_print("enc_in", file.name)
        enc_data = fer.encrypt(raw_data)
        enc_file = to_enc(file, u_files)
        f_pth = u_pth / enc_file
        with open(f_pth, "wb") as f_enc:
            f_enc.write(enc_data)
        deb_print("enc_out", file.name)       

@timer
def encrypt_data_pth_func(file, u_pth, u_files):
    deb_print("enc_in", file)
    with open(file, "rb") as f:
        raw_data = f.read()
    enc_data = fer.encrypt(raw_data)
    enc_file = to_enc(file, u_files)
    f_pth = u_pth / enc_file
    with open(f_pth, "wb") as f_enc:
        f_enc.write(enc_data)
    deb_print("enc_out", file.name)    

def encrypt_data(user, u_files, pth):
    u_pth = BASE_DIR.parent / "data" / user
    if pth == None:    
            folder = BASE_DIR.parent / "enc" 
            has_files = any(f.is_file() for f in folder.iterdir())
            if has_files:    
                encrypt_data_func(u_pth, u_files, folder)
            elif not has_files:
                deb_print("dir_none", Path(folder).name)
    else:
        file = Path(pth)    
        if file.exists():    
            encrypt_data_pth_func(file, u_pth, u_files)
   
        else:
            deb_print("dir_pth_error", None)
           


@timer    
def decrypt_data(user, u_files, pth):
    folder = BASE_DIR.parent / "data" / user
    for file, raw_data in check_folder(folder):
        deb_print("dec_in", Path(file).name)
        enc_data = raw_data
        dec_data = fer.decrypt(enc_data)
        n_file = to_norm(file, u_files)
        u_files.pop(Path(file).stem)
        f_pth = BASE_DIR.parent / "dec" / n_file
        with open(f_pth, "wb") as f_dec:
            f_dec.write(dec_data)
        deb_print("dec_out", Path(file).name)           
          