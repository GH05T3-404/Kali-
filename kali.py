#BANNER 
print("""\033[1;36m
+---------------+
|KALI NO TERMUX |
+---------------+""")
print("""
by: GH05T3-404""")

#KALI LINUX 
import os 
print("""\033[1;35m
X==================================X
X ISSO PODE DEMORA ALGUNS  MINUTOS X
X==================================X\n""")
print("\033[1;92m")
os.system("pkg install wget -y")
os.system("pkg install wget openssl-tool proot -y")
os.system("hash -r")
os.system("wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh")
os.system("bash kali.sh")
os.system("./start-kali.sh")