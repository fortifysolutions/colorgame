import random
import time


def text(score):
    f = open("guess_game_record.txt", "a")
    f.write(score)
    f.close()


def cls():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def rules():
    print("Guess the Position of \033[1;31mRED\033[m Color")
    time.sleep(1.5)
    print(" Imp. Instructions:")
    print(
        "1. You have to identify the position of \033[1;31mRED\033[m Color\n"
        "2. Time: You have \033[1;31m3\033[m seconds to identify the positions\n")


def countdown():
    import time
    count = 0
    while True:
        count += 1
        if count == 5:
            break
        else:
            print(f"time left: {4 - count} sec", end="")
            time.sleep(1)
            print("\r", end="")


def banner():
    print('''
                                                             ,----,                                                
                             ,----..                   ,/   .`|                                                
                   ,---,.   /   /   \  ,-.----.      ,`   .'  :   ,---,    ,---,.                              
                 ,'  .' |  /   .     : \    /  \   ;    ;     /,`--.' |  ,'  .' |       ,---,                  
               ,---.'   | .   /   ;.  \;   :    \.'___,/    ,' |   :  :,---.'   |      /_ ./|                  
               |   |   .'.   ;   /  ` ;|   | .\ :|    :     |  :   |  '|   |   .',---, |  ' :                  
               :   :  :  ;   |  ; \ ; |.   : |: |;    |.';  ;  |   :  |:   :  : /___/ \.  : |                  
               :   |  |-,|   :  | ; | '|   |  \ :`----'  |  |  '   '  ;:   |  |-,.  \  \ ,' '                  
               |   :  ;/|.   |  ' ' ' :|   : .  /    '   :  ;  |   |  ||   :  ;/| \  ;  `  ,'                  
               |   |   .''   ;  \; /  |;   | |  \    |   |  '  '   :  ;|   |   .'  \  \    '                   
               '   :  '   \   \  ',  / |   | ;\  \   '   :  |  |   |  ''   :  '     '  \   |                   
               |   |  |    ;   :    /  :   ' | \.'   ;   |.'   '   :  ||   |  |      \  ;  ;                   
               |   :  \     \   \ .'   :   : :-'     '---'     ;   |.' |   :  \       :  \  \                  
               |   | ,'      `---`     |   |.'                 '---'   |   | ,'        \  ' ;                  
               `----'        ,--,      `---'             ,----,        `----'           `--`                   
                ,----..   ,---.'|                      ,/   .`|            ,----..            ,--.             
  .--.--.      /   /   \  |   | :                    ,`   .'  :   ,---,   /   /   \         ,--.'|  .--.--.    
 /  /    '.   /   .     : :   : |            ,--,  ;    ;     /,`--.' |  /   .     :    ,--,:  : | /  /    '.  
|  :  /`. /  .   /   ;.  \|   ' :          ,'_ /|.'___,/    ,' |   :  : .   /   ;.  \,`--.'`|  ' :|  :  /`. /  
;  |  |--`  .   ;   /  ` ;;   ; '     .--. |  | :|    :     |  :   |  '.   ;   /  ` ;|   :  :  | |;  |  |--`   
|  :  ;_    ;   |  ; \ ; |'   | |__ ,'_ /| :  . |;    |.';  ;  |   :  |;   |  ; \ ; |:   |   \ | :|  :  ;_     
 \  \    `. |   :  | ; | '|   | :.'||  ' | |  . .`----'  |  |  '   '  ;|   :  | ; | '|   : '  '; | \  \    `.  
  `----.   \.   |  ' ' ' :'   :    ;|  | ' |  | |    '   :  ;  |   |  |.   |  ' ' ' :'   ' ;.    ;  `----.   \ 
  __ \  \  |'   ;  \; /  ||   |  ./ :  | | :  ' ;    |   |  '  '   :  ;'   ;  \; /  ||   | | \   |  __ \  \  | 
 /  /`--'  / \   \  ',  / ;   : ;   |  ; ' |  | '    '   :  |  |   |  ' \   \  ',  / '   : |  ; .' /  /`--'  / 
'--'.     /   ;   :    /  |   ,/    :  | : ;  ; |    ;   |.'   '   :  |  ;   :    /  |   | '`--'  '--'.     /  
  `--'---'     \   \ .'   '---'     '  :  `--'   \   '---'     ;   |.'    \   \ .'   '   : |        `--'---'   
                `---`               :  ,      .-./             '---'       `---`     ;   |.'                   
                                     `--`----'                                       '---'                     
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
            position = int(input("Enter the position of \033[1;31mRED\033[m Color :"))
            break
        except ValueError:
            print(" o!o please enter integer value only!!!!")
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
        print("congratulation!!!!!, you WON")
        score_card += 1
        text(str(score_card))
    else:
        print("Sorry, try Again!!!")


def main():
    play = 0
    while True:
        x = input('to continue with the Game, enter any key.... \nor\n to exit press "1" > ')
        if x == "1":
            f = open("guess_game_record.txt","r")
            print(f.readlines())
            f.close()
            print(f"You played {play} times\n\nThank you!!!")
            break
        else:
            play += 1
            guess()


start_time = time.time()
rules()
main()
time.sleep(2)
cls()
print(f"\nYou spent {int(time.time() - start_time)} seconds in Game")
