import pyautogui
import os
import time

#Setup environment
ImageFolder = os.getcwd() + os.sep + 'img' + os.sep
Width, Height = pyautogui.size()
Screen = (0, 0, Width-1, Height-1)

#Define functions

def wait_for(img, region = Screen, time_out = 10):
    img_path = ImageFolder + img
    location = None
    start_time = time.time()

    while (location == None):
        try:
            elapsed = time.time() - start_time
            if elapsed > time_out:
                return location

            location = pyautogui.locateOnScreen(img_path)
        except Exception as e:
            print(e)
    return location

def click_on(img, region = Screen):
    img_path = ImageFolder + img
    location = None

    try:
        location = pyautogui.locateCenterOnScreen(img_path)
        pyautogui.click(location)
    except Exception as e:
        print(e)
    return location

#Main program
if __name__ == '__main__':
    print('#' * 50)
    print(f'Image Folder: {ImageFolder}')
    print(f'Screen Region: {Screen}')
    print('#' * 50)

    time.sleep(2)

    location = wait_for('Button_City.png')
    print(location)
    location = click_on('Button_City.png')
    print(location)
    location = wait_for('Button_Shop.png')
    print(location)
    location = click_on('Button_Shop.png')
    print(location)