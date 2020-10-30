import os
import time
def main():
    str1='歡迎來到前鋒學習Python\nxxxxxxxxxxxxxx'
    while True:
        os.system('cls')
        print(str1)
        time.sleep(0.5)
        str1=str1[1:]+str1[0]

if __name__ == '__main__':
    main()