import pyautogui
import time
# Done Right upto 1000
# Done Left upto 1000
#collected upto 450 right
#Move(486) = 1370 Profile
time.sleep(3)
move = 18
pyautogui.hotkey('alt', 'tab')
time.sleep(3)
for x in range(0,1000000):
    pyautogui.click(1852, 54)
    time.sleep(8)
    pyautogui.press('right')
    # pyautogui.press('left')
    for i in range(0,move):
        pyautogui.press('right')
    pyautogui.press('enter')
    time.sleep(15)
    # pyautogui.click(1706,696)
    # time.sleep(3)
    # pyautogui.moveTo(1385,292)
    # time.sleep(10)
    file1 = open("counter.txt", "a")
    file1.write(str(move)+"\n ")
    file1.close()
    for j in range(0,30):
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(0.25)
    if(move%30==0):
        pyautogui.moveTo(890,1055,1.5)
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(858,1000)
        time.sleep(2)
        pyautogui.moveTo(890,1055,1.5)
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(858,1000)
        time.sleep(2)
        pyautogui.moveTo(890,1055,1.5)
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.click(858,1000)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(2)
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('alt')
        pyautogui.keyDown('f4')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('alt')
        pyautogui.keyUp('f4')
        time.sleep(2)
        pyautogui.click(770,1055)
        time.sleep(10)
        move+=1
    else:
        pyautogui.hotkey('alt', 'f4')
        move+=1
        time.sleep(2)
    if(move==201):
        move=1