import tkinter.filedialog
from tkinter import *
import tkinter
import pygame
from PIL import Image
import imghdr


class FileHandler(object):

    def __init__(self):

        self.file = ""

    def fileConvert(file):
        # opens a file, converts it to rgb, resizes it to 16x16, saves it, and returns the downsized image
        if file == "wrongtype":
            image = Image.open(str("images/smokey.gif")).convert("RGB")
            image = image.resize((16, 16))
            image.save("images/smokeyscaled.png")
        else:
            image = Image.open(str(file)).convert("RGB")
            image = image.resize((16, 16))
            image.save("images/smokeyscaled.png")

        return image

    def screenshot(surface, file):
        typeDictionary = {
            "success": "image saved successfully",
            "failed": "image not saved",
        }
        try:
            pygame.image.save(surface, file)
            print(typeDictionary.get("success"))
        except:
            print(typeDictionary.get("failed"))

    def askFile():
        # asks user to select a file, checks if file is a png or gif or not
        image = tkinter.filedialog.askopenfilename()

        if (
            imghdr.what(image) != "gif" and imghdr.what(image) != "png"
        ):  # outside concept
            return "wrongtype"
        else:
            return image
