import pyautogui as pg
import numpy as np
import time as tt
import datetime as dt
import argparse as ag
import os

def norm(x, y):
    return np.sqrt(x**2 + y**2)

def clickFilm(x, y):
    sX, sY = pg.size()
    scr = norm(sX, sY)
    curX, curY = pg.position()
    dist = norm(x - curX, y - curY)
    time = dist / scr / 2 + np.random.normal() / 10
    pg.moveTo(x, y, time)
    tt.sleep(0.2)
    pg.click()

def logIn(usernamePos, passwordPos):
    clickFilm(usernamePos[0], usernamePos[1])
    username = "mejl"
    password = "hasło"
    for e in username:
        pg.write(e, interval=abs(np.random.normal(10, 1) / 1000))
    clickFilm(passwordPos[0], passwordPos[1])
    for e in password:
        pg.write(e, interval=abs(np.random.normal(10, 1) / 1000))
    pg.press('enter')

def logOut(buttonPos):
    clickFilm(buttonPos[0], buttonPos[1])

def main():
    path = os.path.dirname(__file__)
    films = np.load(os.path.join(path, "films.npy"))
    config = np.load(os.path.join(path, "config.npy"))
    x = films[0]
    y = films[1]
    xConfig = config[0]
    yConfig = config[1]
    epsilon = np.random.randint(40)
    c = 1
    while(c == 1):
        if dt.datetime.now().hour == 8 and dt.datetime.now().minute == 28 and dt.datetime.now().second >= 16 + epsilon:
            c = 0
            pg.press('ctrl')
            tt.sleep(0.7)
            logIn((xConfig[0], yConfig[0]), (xConfig[1], yConfig[1]))
            clickFilm(xConfig[3], yConfig[3])  # guzik z następnym dniem
            tt.sleep(100 - epsilon)
            for i in range(len(x)):
                clickFilm(x[i], y[i])
                print(x[i], y[i])
            tt.sleep(abs(np.random.normal(4, 1)))
            logOut((xConfig[2], yConfig[2]))
            print("end")

if __name__ == "__main__":
    main()
