import threading
import time
import os
import random

#colours
"\033[1;30m"  # Gray
"\033[1;31m"  # Red
"\033[1;32m"  # Green
"\033[1;33m"  # Yellow
"\033[1;34m"  # Blue
"\033[1;35m"  # Magenta
"\033[1;36m"  # Cyan
"\033[1;37m"  # White
"\033[0m"     # Reset / Default

def compute_gwa(grade, i):
    print(f"\033[1;36m{animals} [Thread] Subject {i}: grade = {grade}\033[0m")

art = """
\033[33m
    T     ⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
    E     ⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
    A    ⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
    M    ⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
    K    ⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
    I   ⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
    R    ⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
    B    ⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
    E    ⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
    L   ⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
    L   ⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\033[0m
"""

print(art)

print("⊱════════════════════════════⊰")
print("\033[1;36m𝐆𝐖𝐀 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐨𝐫 (𝐌𝐔𝐋𝐓𝐈𝐓𝐇(𝐑𝐄𝐀𝐃𝐈𝐍𝐆)☕︎⌨︎︎\033[0m")
print("⊱════════════════════════════⊰")

input("\n\033[1;32mEnter proceed ➣\033[0m")
os.system("clear")

while True:
    n = int(input("\n\033[1;33m◎ How many subjects (max 10)➣ "))
    print("\033[0m")
    if 1 <= n <= 10:
        break
    print("\n\033[1;31mPlease enter a number between 1 and 10 only.㋡\033[0m")
    time.sleep(2)
    os.system("clear")


grades_list = []

os.system("clear")

items = ("𓃠","𓃥","𓃭","𓃟","𓃻")

for i in range(1, n + 1):
    while True:
        animals = random.choice(items)
        n = 5
        
        grade = float(input(f"\033[1;33m{animals} Enter grade for subject {i}: "))
        print("\033[0m")
        if 0 <= grade <= 100:
            grades_list.append(grade)
            break
        print("\n\033[1;31mInvalid grade. Please enter a value between 0 and 100.㋡\033[0m")
        time.sleep(2)
        os.system("clear")

os.system("clear")


print("\033[1;32m❛ ━━━━━━･❪ 𝐑𝐄𝐒𝐔𝐋𝐓𝐒 ❫ ･━━━━━━ ❜ \033[0m\n")
start_time = time.perf_counter()

threads = []
for i, grade in enumerate(grades_list, start=1):
    t = threading.Thread(target=compute_gwa, args=(grade, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


end_time = time.perf_counter()
gwa = sum(grades_list) / len(grades_list)
print("\n━━━━━━━━━━━━")
print(f"\033[1;33mGWA: {gwa:.2f}\033[0m")
print("━━━━━━━━━━━━")
print(f"\033[1;31mExecution Time: {end_time - start_time:.6f} seconds\033[0m")
print("━━━━━━━━━━━━")