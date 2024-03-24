import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import PySimpleGUI as sg
import os
def generate_key(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"salt",
        iterations=100000
    )
    return Fernet(base64.urlsafe_b64encode(kdf.derive(password.encode())))

def encrypt_file(file_path, password):
    f = generate_key(password)

    with open(file_path, 'rb') as infile:
        original_data = infile.read()

    encrypted_data = f.encrypt(original_data)

    with open(file_path, 'wb') as outfile:
        outfile.write(encrypted_data)

def decrypt_file(file_path, password):
    f = generate_key(password)

    with open(file_path, 'rb') as infile:
        encrypted_data = infile.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(file_path, 'wb') as outfile:
        outfile.write(decrypted_data)

def change_file_extension(file_path, new_extension):
    base_name = os.path.splitext(file_path)[0]
    new_file_path = f"{base_name}.{new_extension}"

    if os.path.exists(new_file_path):
        os.remove(new_file_path)

    os.rename(file_path, new_file_path)

layout = [
        [sg.Button("Расшифровать", button_color=("white", "green"), font=("Helvetica", 14), key="-DEC-")],
        [sg.Text("", key="-OUTPUT-", font=("Helvetica", 12), text_color="red")],
    ]

window = sg.Window("Decrypt Otchet.txt", layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-DEC-":
        file_path = "Otchet.txt"

        if os.path.isfile(file_path):
            password = "-JUB_em5E-V5yc0k2YlqP6"
            decrypt_file(file_path, password)
            change_file_extension(file_path, 'xlsx')
            window["-OUTPUT-"].update("Успешно")
        else:
            window["-OUTPUT-"].update("Файл не найден")
window.close()