import pyautogui as pg
import numpy as np
import keyboard as kb
import argparse as ag

def getFilms():
    x = [0]
    y = [0]
    while(True):
        if(kb.is_pressed('y')):
            tempx, tempy = pg.position()
            if tempx != x[-1] and tempy != y[-1]:
                x.append(tempx)
                y.append(tempy)
                print(tempx, tempy)
        if(kb.is_pressed('n')):
            out = np.zeros((2, len(x)))
            out[0] = x
            out[1] = y
            return out[:, 1:]

def main():
    parser = ag.ArgumentParser()
    parser.add_argument('-c', '--config', help='Create config file with position of buttons and text fields', action='store_true')
    args = parser.parse_args()
    films = getFilms()
    if args.config:
        np.save("config.npy", films)
    else:
        np.save("films.npy", films)

if __name__ == "__main__":
    main()
