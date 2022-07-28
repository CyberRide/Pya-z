import os
import subprocess
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
print("")
print(colored (0,0,255, "██████╗░██╗░░░██╗░█████╗░░░░░░░███████╗"))
print(colored (0,0,255, "██╔══██╗╚██╗░██╔╝██╔══██╗░░░░░░╚════██║"))
print(colored (0,0,255, "██████╔╝░╚████╔╝░███████║█████╗░░███╔═╝"))
print(colored (0,0,255, "██╔═══╝░░░╚██╔╝░░██╔══██║╚════╝██╔══╝░░"))
print(colored (0,0,255, "██║░░░░░░░░██║░░░██║░░██║░░░░░░███████╗"))
print(colored (0,0,255, "╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚══════╝"))
print(colored (0,0,255, "Made by: CyberRide"))
print(colored (0,0,255, "github: https://github.com/CyberRide"))
print(colored(255, 0, 0,"PyA-Z is a simple python mini A-Z projects""\n"))
print(colored(139,0,139,"[A] Alarm Clock             ""[K] ??                      ""[U] ??")) 
print(colored(139,0,139,"[B] Battery Notification    ""[L] Leap Year               ""[V] ??"))   
print(colored(139,0,139,"[C] Countdown Timer         ""[M] Movie Scraper           ""[W] Wifi Password"))
print(colored(139,0,139,"[D] Digital Clock           ""[N] Number Guessing         ""[X] XKCD Downloader"))
print(colored(139,0,139,"[E] Encrypt Text            ""[O] Organize Folder         ""[Y] Youtube Downloader"))
print(colored(139,0,139,"[F] Find Ip                 ""[P] PDF to MP3              ""[Z] Zip Brute"))
print(colored(139,0,139,"[G] Game                    ""[Q] QR Code                 ""[OK] To Exit"     ))
print(colored(139,0,139,"[H] Hello                   ""[R] Random Password         "     ))
print(colored(139,0,139,"[I] Internet Checker        ""[S] Shutdown Device         "     ))
print(colored(139,0,139,"[J] ??                      ""[T] Text To Speech          "     ))

if __name__ == "__main__":
    while True:
        try:
            valc = input(colored(255, 0, 0,"Input Option A-Z "))
            d=valc.lower()
            if d == "a":
                import os
                os.system("python3 .project/.alarm.py")
            elif d == "b":
                import os
                os.system("python3 .project/.battery.py")
            elif d == "c":
                import os
                os.system("python3 .project/.countdown.py")
            elif d == "d":
                import platform
                import os
                if platform.system() == "Windows":
                    os.system("python3 .project/.digital.py")
                elif platform.system() == "Linux" or platform.system() == "Linux2" or platform.system() == "Darwin":
                    os.system("python3 .project/.digital.py")
                else:
                    print("Os not supported!")
            elif d == "e":
                import os
                os.system("python3 .project/.encode.py")
            elif d == "f":
                import platform
                import os
                if platform.system() == "Windows":
                    os.system("ipconfig")
                elif platform.system() == "Linux" or platform.system() == "Linux2" or platform.system() == "Darwin":
                    os.system("ifconfig")
                else:
                    print("Os not supported!")
            elif d == "g":
                import os
                os.system("python3 .project/.game.py")
            elif d == "h":
                import os
                os.system("python3 .project/.hello.py")
            elif d == "i":
                import os 
                os.system("python3 .project/.internet.py")
            # elif d == "j":
            # elif d == "k":
            elif d == "l":
                import os
                import platform
                os.system('python3 .project/.leapyear.py')
            elif d == "m":
                import os
                os.system('python3 .project/.movie.py')
            elif d == "n":
                import os
                os.system('python3 .project/.number.py')
            elif d == "o":
                import os
                os.system('python3 .project/.organize.py')
            # elif d == "p":
            elif d == "q":
                import os
                os.system('python3 .project/.qrcode.py')
            # elif d == "q":
            # elif d == "r":
            elif d == "s":
                import os
                import platform
                os.system('python3 .project/.shut.py')
            elif d == "t":
                import os
                os.system('python3 .project/.text.py')
            elif d == "p":
                import os
                os.system('python3 .project/.pdf-mp3.py')
            elif d == "w":
                import os
                os.system('python3 .project/.wifi.py')
            elif d == "x":
                import os
                num = int(input('Enter Any Number '))
                os.system('python3 .xkcd.py -l', num)
            elif d == "y":
                import os
                os.system('python3 .project/.youtube.py')
            elif d == "z":
                import os
                os.system('python3 .project/.zip.py')

            elif d =="ok":
                exit()
            else:
                print("Invalid Input Please Try Again")
        except ValueError:
                print("Error: Invalid Number!")
              