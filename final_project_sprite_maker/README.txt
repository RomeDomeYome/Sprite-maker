To run/use:

Run the main.py file.

It will automatically load a picture of smokey. Feel free to try out any non-moving gifs or pngs.
These will be the only file types it will accept.

To add your own image, click the upload image button and it will automatically format it for you.

To clear the canvas, click the clear canvas button to reveal a basic grid of all the pixels.

To save the image, click the save image button.
It will automatically save as newSprite.png and overwrite a previous save of the same name.
Rename your sprite before saving a new one to avoid overwriting.

For some reason, the program might not quit when pressing the close window button.
You may have to close the main.py file in idle to exit.

Requiremnts met:

Two classes
-Gamescreen in screen.py
-FileHandler in filehandler.py

3 Methods
-Gamescreen
    -update()
    -clickButton()
    -updateCanvas
    -uploadImage()
-FileHandler
    -fileConvert()
    -screenshot()
    -askFile()

List
-Gamescreen
    -uploadImage()
        -rgbList[]
        -rectList[]

Dictionary
-FileHandler
    -screenshot()
        -typeDictionary{}

3 Modules used in class
-screen.py
    -tkinter
    -pygame
    -PIL

Pulls data by taking an image and converting it to a grid of rects
-FileHandler
    -askFile()
    -fileConvert()
-Gamescreen
    -uploadImage()

Try/Except
-FileHandler
    -screenshot()
        -uses try/except to check if a screenshot was saved

If/else and for loop
-Gamescreen
    -clickButton()
        -uses for loop to loop through all events queued in pygame.event
        -uses if/else to check which button/rect was clicked
-plus many others throughout the program

Data entry validation
-FileHandler
    -askFile()
        -uses imghdr.what() to see the file type of the image. Must be gif or png
            -rejects the file and uploads smokey.png instead and displays an error message

Python concept not explored in class
-tkinter colorchooser
    -Gamescreen
        -clickButton()
-imghdr
    -FileHandler
        -askFile()