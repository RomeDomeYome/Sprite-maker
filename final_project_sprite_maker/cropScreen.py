import tkinter.filedialog
from tkinter import *
from tkinter import colorchooser
import pygame
from PIL import Image
import tkinter
from tkinter import filedialog
from filehandler import FileHandler
from cropper import CroppingTool


class CropScreen(object):

    def __init__(self, w, h, image):

        pygame.init()

        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Sprite Maker")
        self.cropImage = image
        self.font = pygame.font.SysFont("arial", 24)
        self.buttonFont = pygame.font.SysFont("arial", 14)

        self.cropImageResizedWidth = 750
        self.cropImageResizedHeight = 0
        self.xOffset = 125
        self.yOffset = 50

        # cropImage = pygame.image.load(image)
        self.cropRect = pygame.Rect(0, 0, 500, 500)

        self.cropImage = Image.open(str(self.cropImage)).convert("RGB")
        self.cropImageDimensions = self.cropImage.size
        self.cropImageWidth = self.cropImageDimensions[0]
        self.cropImageHeight = self.cropImageDimensions[1]

        # if an image is in portrait mode, rotate it 90 degress
        if self.cropImageHeight > self.cropImageWidth:
            self.cropImage = self.cropImage.transpose(method=Image.Transpose.ROTATE_90)
            self.cropImage.save("images/userImage.gif")
            self.cropImage = Image.open("images/userImage.gif").convert("RGB")

            self.cropImageDimensions = self.cropImage.size
            self.cropImageWidth = self.cropImageDimensions[0]
            self.cropImageHeight = self.cropImageDimensions[1]

        # constraining the image to at most 750px for width and 550px for height
        if self.cropImageHeight > 550 and self.cropImageWidth < 750:

            print("height over 550")
            self.cropImageHeight = 550
            self.cropImageDimensionRatio = self.cropImageWidth / self.cropImageHeight
            self.cropImageWidth = int(
                self.cropImageHeight * self.cropImageDimensionRatio
            )

        elif self.cropImageHeight < 550 and self.cropImageWidth > 750:
            print("width over 750")
            self.cropImageWidth = 750
            self.cropImageDimensionRatio = self.cropImageWidth / self.cropImageHeight
            self.cropImageHeight = int(
                self.cropImageWidth * self.cropImageDimensionRatio
            )
        elif self.cropImageHeight > 550 and self.cropImageWidth > 750:
            print("height over 550 and Width over 750")
            self.cropImageWidth = 750
            self.cropImageDimensionRatio = self.cropImageWidth / self.cropImageHeight
            print(self.cropImageDimensionRatio)
            self.cropImageHeight = int(
                self.cropImageWidth * self.cropImageDimensionRatio
            )
            print(self.cropImageHeight)
            if self.cropImageHeight > 550:
                print("height still over 550")
                self.cropImageHeight = 550
                self.cropImageDimensionRatio = (
                    self.cropImageWidth / self.cropImageHeight
                )
                self.cropImageWidth = int(
                    self.cropImageHeight * self.cropImageDimensionRatio
                )
        # accounts for images under both of the constraints. sets the width to 750 then rechecks all the size dimensions
        else:
            self.cropImageWidth = 750
            self.cropImageDimensionRatio = self.cropImageHeight / self.cropImageWidth
            self.cropImageHeight = int(
                self.cropImageWidth * self.cropImageDimensionRatio
            )
            if self.cropImageHeight > 550 and self.cropImageWidth < 750:

                print("upscaled height over 550")
                self.cropImageHeight = 550
                self.cropImageDimensionRatio = (
                    self.cropImageWidth / self.cropImageHeight
                )
                self.cropImageWidth = int(
                    self.cropImageHeight * self.cropImageDimensionRatio
                )

            elif self.cropImageHeight < 550 and self.cropImageWidth > 750:
                print("upscaled width over 750")
                self.cropImageWidth = 750
                self.cropImageDimensionRatio = (
                    self.cropImageHeight / self.cropImageWidth
                )
                self.cropImageHeight = int(
                    self.cropImageWidth * self.cropImageDimensionRatio
                )
            elif self.cropImageHeight > 550 and self.cropImageWidth > 750:
                print("upscaled height over 550 and self.cropImageWidth over 750")
                self.cropImageWidth = 750
                self.cropImageDimensionRatio = (
                    self.cropImageHeight / self.cropImageWidth
                )
                self.cropImageHeight = int(
                    self.cropImageWidth * self.cropImageDimensionRatio
                )
                if self.cropImageHeight > 550:
                    self.cropImageHeight = 550
                    self.cropImageDimensionRatio = (
                        self.cropImageWidth / self.cropImageHeight
                    )
                    self.cropImageWidth = int(
                        self.cropImageHeight * self.cropImageDimensionRatio
                    )
        self.cropImage = self.cropImage.resize(
            (self.cropImageWidth, self.cropImageHeight)
        )
        print(
            "scaled height", self.cropImageResizedWidth * self.cropImageDimensionRatio
        )
        print(self.cropImage.size)

        self.cropImage.save("images/userImage.gif")

        self.scaledCropImage = pygame.image.load("images/userImage.gif")

        self.yOffset = ((550 - self.cropImageHeight) / 2) + 50
        self.screen.blit(self.scaledCropImage, (self.xOffset, self.yOffset))

        self.leftButton = pygame.Rect(60, 400, 100, 50)
        self.rightButton = pygame.Rect(200, 400, 100, 50)
        self.squeezeButton = pygame.Rect(200, 475, 100, 50)
        self.cropButton = pygame.Rect(60, 475, 100, 50)
        self.screenshotRect = pygame.Rect(0, 0, 2, 2)

        self.screenshotSurface = self.screen.subsurface(self.screenshotRect)
        """
        pygame.draw.rect(self.screen, (128, 128, 128), self.leftButton)
        pygame.draw.rect(self.screen, (128, 128, 128), self.rightButton)
        pygame.draw.rect(self.screen, (128, 128, 128), self.squeezeButton)
        pygame.draw.rect(self.screen, (128, 128, 128), self.cropButton)
        
        leftButtonText = self.buttonFont.render("Upload Image", True, (0, 0, 0))
        self.screen.blit(leftButtonText, (75, 415))
        rightButtonText = self.buttonFont.render("Clear Canvas", True, (0, 0, 0))
        self.screen.blit(rightButtonText, (215, 415))
        squeezeButtonText = self.buttonFont.render("Pick Color", True, (0, 0, 0))
        self.screen.blit(squeezeButtonText, (215, 490))
        cropButtonText = self.buttonFont.render("Save Image", True, (0, 0, 0))
        self.screen.blit(cropButtonText, (75, 490))
        """

    def update(self):
        # updates the screen
        imageCropped = False
        pygame.display.update()
        self.clickButton()

        return imageCropped

    def clickButton(self):
        # checks for mouse clicks and checks if the click is inside any available rects
        for event in pygame.event.get():
            pass
