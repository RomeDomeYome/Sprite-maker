import tkinter.filedialog
from tkinter import *
from tkinter import colorchooser
import pygame
from PIL import Image
import tkinter
from tkinter import filedialog
from filehandler import FileHandler
from cropper import CroppingTool
from cropScreen import CropScreen


class GameScreen(object):

    def __init__(self, w, h):

        pygame.init()

        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Sprite Maker")

        self.font = pygame.font.SysFont("arial", 24)
        self.buttonFont = pygame.font.SysFont("arial", 14)

        self.mouseColor = (0, 0, 0)

        self.colorAndRectList = self.uploadImage(None)

        self.uploadButton = pygame.Rect(60, 400, 100, 50)
        self.clearCanvasButton = pygame.Rect(200, 400, 100, 50)
        self.pickColorButton = pygame.Rect(200, 475, 100, 50)
        self.saveImageButton = pygame.Rect(60, 475, 100, 50)
        self.screenshotRect = pygame.Rect(0, 0, 2, 2)
        self.cropRect = pygame.Rect(0, 0, 0, 0)

        self.screenshotSurface = self.screen.subsurface(self.screenshotRect)

        pygame.draw.rect(self.screen, (128, 128, 128), self.uploadButton)
        pygame.draw.rect(self.screen, (128, 128, 128), self.clearCanvasButton)
        pygame.draw.rect(self.screen, (128, 128, 128), self.pickColorButton)
        pygame.draw.rect(self.screen, (128, 128, 128), self.saveImageButton)

        uploadButtonText = self.buttonFont.render("Upload Image", True, (0, 0, 0))
        self.screen.blit(uploadButtonText, (75, 415))
        clearCanvasButtonText = self.buttonFont.render("Clear Canvas", True, (0, 0, 0))
        self.screen.blit(clearCanvasButtonText, (215, 415))
        pickColorButtonText = self.buttonFont.render("Pick Color", True, (0, 0, 0))
        self.screen.blit(pickColorButtonText, (215, 490))
        saveImageButtonText = self.buttonFont.render("Save Image", True, (0, 0, 0))
        self.screen.blit(saveImageButtonText, (75, 490))

        pygame.draw.rect(self.screen, (0, 0, 0), self.cropRect)
        self.cropSurface = self.screen.subsurface(self.cropRect)

    def update(self):
        # updates the screen
        keepGoing = True
        pygame.display.update()
        self.clickButton()

        return keepGoing

    def clickButton(self):
        # checks for mouse clicks and checks if the click is inside any available rects
        for event in pygame.event.get():
            if (
                self.uploadButton.collidepoint(pygame.mouse.get_pos())
                and event.type == pygame.MOUSEBUTTONDOWN
            ) == True:
                self.colorAndRectList = self.uploadImage("func")
                print("color and list: ", self.colorAndRectList)
            elif (
                self.pickColorButton.collidepoint(pygame.mouse.get_pos())
                and event.type == pygame.MOUSEBUTTONDOWN
            ) == True:
                color = colorchooser.askcolor()  # outside concept
                self.mouseColor = color[0]
                print(self.mouseColor)
            elif (
                self.clearCanvasButton.collidepoint(pygame.mouse.get_pos())
                and event.type == pygame.MOUSEBUTTONDOWN
            ) == True:
                self.colorAndRectList = self.uploadImage("clear")
                print("color and list: ", self.colorAndRectList)
            elif (
                self.saveImageButton.collidepoint(pygame.mouse.get_pos())
                and event.type == pygame.MOUSEBUTTONDOWN
            ) == True:
                self.screenshotRect = pygame.Rect(20, 35, 320, 320)
                self.screenshotSurface = self.screen.subsurface(self.screenshotRect)
                FileHandler.screenshot(self.screenshotSurface, "images/newSprite.png")
                self.screenshotRect = pygame.Rect(0, 0, 2, 2)
                self.screenshotSurface = self.screen.subsurface(self.screenshotRect)
            elif (event.type == pygame.MOUSEBUTTONDOWN) == True:
                count = 0
                for rect in self.colorAndRectList[1]:
                    if (
                        rect.collidepoint(pygame.mouse.get_pos())
                        and event.type == pygame.MOUSEBUTTONDOWN
                    ) == True:
                        rectColorList = self.colorAndRectList[0]
                        rectColorList[count] = self.mouseColor
                        self.colorAndRectList = self.updateCanvas(
                            rectColorList, self.colorAndRectList[1]
                        )
                    count += 1
            else:
                pass

    def updateCanvas(self, rgbList, rectList):
        # draws the canvas after changes have been made
        count = 0
        x = 20
        y = 20
        for rectY in range(16):
            for rectX in range(16):
                pygame.draw.rect(self.screen, rgbList[count], rectList[count])
                count += 1
                x += 20
            y += 20
            x = 20
        return [rgbList, rectList]

    def crop(self, cropRect, image):

        c = CropScreen(1000, 750, image)

        imageCropped = False

        while imageCropped == False:

            imageCropped = self.cropLoop(c)

    def cropLoop(self, c):
        cropInProgress = c.update()
        return cropInProgress

    def uploadImage(self, image):
        """takes in an image, scales it down to 16x16, saves as a png,
        then creates a list of pixel colors, uses pixel color list to create a grid of rects
        """

        if image == None:
            self.image = FileHandler.fileConvert("images/smokey.png")
        elif image == "func":
            self.image = FileHandler.askFile()
            self.image = self.crop(self.cropRect, self.image)
            print(self.image, "THIS IS THE FILE NAME")
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 300, 35))

            if self.image == "wrongtype":
                self.uploadImage(None)
                errorText = self.font.render(
                    "Error: Wrong File Type", True, (255, 255, 255)
                )
                self.screen.blit(errorText, (10, 6))
            elif self.image == "":
                self.uploadImage(None)
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 300, 35))

            else:
                self.image = FileHandler.fileConvert(self.image)
                self.pygameImage = pygame.image.load("images/smokeyscaled.png")
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 300, 35))

        elif image == "clear":

            self.image = FileHandler.fileConvert("images/blank_canvas.png")
            self.pygameImage = pygame.image.load("images/blank_canvas_resized.png")
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 300, 35))

        rgbList = []
        rectList = []

        for y in range(16):
            for x in range(16):
                (r, g, b) = self.image.getpixel((x, y))
                rgbList.append((r, g, b))
        x = 20
        y += 20
        count = 0

        for rectY in range(16):
            for rectX in range(16):
                rectList.append(pygame.Rect(x, y, 20, 20))
                pygame.draw.rect(self.screen, rgbList[count], rectList[count])
                count += 1
                x += 20
            y += 20
            x = 20
        return [rgbList, rectList]
