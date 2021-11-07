import random
import time


def text(score):
    f = open("guess_game_record.txt", "a")
    f.write(score + "-correctAnswer")
    f.write('\n')
    f.close()


def cls():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def rules():
    print("Guess the Position of \033[1;31mRED\033[m Color")
    print("\033[1;32m", time.ctime(), "\033[m")
    time.sleep(1.5)
    print("\nImp. Instructions:")
    print(
        "1. You have to identify the position of \033[1;31mRED\033[m Color\n"
        "2. You have \033[1;31m3\033[m seconds to identify the position\n")


def countdown():
    import time
    count = 0
    while True:
        count += 1
        if count == 5:
            break
        else:
            print(f"time left: \033[1;36;41m{4 - count}\033[m sec", end="")
            time.sleep(1)
            print("\r", end="")


def banner():
    print('''
         \033[31m(       )  (          (   (        )            
          )\ ) ( /(  )\ )  *   ))\ ))\ )  ( /(            
         (()/( )\())(()/(` )  /(()/(()/(  )\())           
          /(_)|(_)\  /(_))( )(_))(_))(_))((_)\            
         (_))_| ((_)(_)) (_(_()|_))(_))_|_ ((_)\033[m           
         \033[32m| |_  / _ \| _ \|_   _|_ _| |_ \ \ / /           
         | __|| (_) |   /  | |  | || __| \ V /            
         (_|   \_)_/(_|_\  |_| |___|(|    |_)\033[m     ) (     
         \033[31m)\ ) ( /(  )\ )       *   ))\ ) ( /(  ( /( )\ )  
        (()/( )\())(()/(   ( ` )  /(()/( )\()) )\()|()/(  
         /(_)|(_)\  /(_))  )\ ( )(_))(_)|(_)\ ((_)\ /(_)) 
        (_))   ((_)(_)) _ ((_|_(_()|_))   ((_) _((_|_)) \033[m  
        \033[36m/ __| / _ \| | | | | |_   _|_ _| / _ \| \| / __|  
        \__ \| (_) | |_| |_| | | |  | | | (_) | .` \__ \  
        |___/ \___/|____\___/  |_| |___| \___/|_|\_|___/\033[m  
                                                          ''')


def red():
    print("\033[0;31;41m      \033[m")


def green():
    print("\033[0;32;42m      \033[m")


def cyan():
    print("\033[0;36;46m      \033[m")


def blue():
    print("\033[0;34;44m      \033[m")


def color_position():
    while True:
        try:
            position = int(input("\nEnter the position of \033[1;31mRED\033[m Color :"))
            break
        except ValueError:
            print("\n\t\t \033[1;33mo!o\033[mplease enter integer value only!!!!\n")
    return position


def guess():
    score_card = 0
    list1 = ["blue", "cyan", "green", "red"]
    list = []
    count = 0
    while True:

        count += 1
        if count == 5:
            break
        else:
            print(f"Position No. {count} : ", end="")
        a = random.choice(list1)
        list.append(a)
        if a == "blue":
            list1.remove(a)
            blue()
        elif a == "cyan":
            list1.remove(a)
            cyan()
        elif a == "green":
            list1.remove(a)
            green()
        elif a == "red":
            list1.remove(a)
            red()
    countdown()
    cls()
    if list.index("red") + 1 == color_position():
        time.sleep(0.5)
        print("\n\033[1;32mCongratulation!!!!!\033[m, you WON\n")
        time.sleep(1)
        score_card += 1
        text(str(score_card))
    else:
        print("\nSorry, try Again!!!")


def main():
    play = 0
    while True:
        x = input('to continue with the Game, enter any key.... \n\t\tor\nto exit press "1" > ')
        if x == "1":
            f = open("guess_game_record.txt", "r")
            print(f.readlines())
            f.close()
            print(f"You played {play} times\n\nThank you!!!")
            break
        else:
            play += 1
            guess()


start_time = time.time()
cls()
banner()
rules()
main()
time.sleep(2)
cls()
f = open("guess_game_record.txt", "w")
f.write("")
f.close()
print(f"\nYou spent {int(time.time() - start_time)} seconds in Game")

print("\033[1;32m", time.ctime(), "\033[m")
import socket

print(socket.gethostbyname(socket.gethostname()))
print("Follow us on YouTube     :\033[1;37;41mFORTIFY\033[m\033[1;31m SOLUTIONS\033[m")
print("Also visit us on         :https://www.fortifysolutions.in")
print("Visit our LinkedIn Page  :https://in.linkedin.com/in/fortifysolutions")
