import pydirectinput
from PIL import Image, ImageGrab
import time
import random
import pyautogui
from datetime import datetime

BLUE = (0,149,246)

# Box is the region of all of the follow boxes
BoxX = 550
BoxY = 240
width = 120
totalHeight = 300
individualHeight = 40
# Take care, 2 value tuples are coordinates while 3 value are color rgb values

def hasFollow(imagePath):
    im = Image.open(imagePath)
    pix = im.load()
    for y in range(int(BoxY), int(BoxY + totalHeight)):
        for x in range(int(BoxX), int(BoxX + width)):
            value = pix[x, y]
            if value == BLUE:
                return [True, (x,y)]
    
    return [False, value]

def clickFollow(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time_sleepRand = round(random.uniform(5, 7), 2)
    time.sleep(time_sleepRand)
    screenshot = ImageGrab.grab()
    screenshot.save('insta-image.png', 'PNG')

def scrollDown():
    pydirectinput.press('down')
    pydirectinput.press('down')
    pydirectinput.press('down')


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    followCount = 0
    screenshot = ImageGrab.grab()
    screenshot.save('insta-image.png', 'PNG')
    time_sleepRand = round(random.uniform(5, 7), 2)
    time.sleep(time_sleepRand)
    random_follow = random.randint(10, 25)
    random_time = random.randint(2600,2700)
    while followCount < random_follow:
        if hasFollow('insta-image.png')[0]:
            clickFollow(hasFollow('insta-image.png')[1][0], hasFollow('insta-image.png')[1][1]) # x and y coordinates
            followCount += 1
            screenshot = ImageGrab.grab()
            screenshot.save('insta-image.png', 'PNG')
        else:
            scrollDown()
            screenshot = ImageGrab.grab()
            screenshot.save('insta-image.png', 'PNG')
    print(f"followed {followCount} people by: {current_time}")
    time.sleep(random_time)

