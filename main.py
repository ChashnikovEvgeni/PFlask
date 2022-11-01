import os
import threading

MENU = [
    ["Консольное приложение", "asm2204/st27/console_app.py"],
    ["Web-приложение", "asm2204/st27/web_app.py"],
]



def menu():
    print("------------------------------")
    for i, item in enumerate(sorted(MENU)):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())


try:
    while True:
        try:
            app = sorted(MENU)[menu()][1]
            if os.system("python3 " + app):
                os.system("python " + app)
        except KeyboardInterrupt:
            pass
except Exception as ex:
    print(ex, "\nbye")


