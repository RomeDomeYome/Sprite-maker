import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
from screen import GameScreen
import pygame


def gameloop(g):

    keepGoing = g.update()

    return keepGoing


def main():

    height = 750
    width = 1000

    g = GameScreen(width, height)

    play = True

    while play:

        play = gameloop(g)
    pygame.quit()


if __name__ == "__main__":
    main()
