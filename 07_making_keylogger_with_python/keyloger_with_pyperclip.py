"""
sudo apt-get install xclip  (Required to work with pyperclip)
"""
import pyperclip
import time


def main():
    alist = []
    while True:
        if pyperclip.paste() != "None":
            value = pyperclip.paste()
            if value not in alist:
                alist.append(value)

            print(alist)

            time.sleep(1)

if __name__ == "__main__":
    main()