import pyautogui
import time

time.sleep(2)
profileNumber = 3509
pyautogui.hotkey('alt', 'tab')
time.sleep(3)
for i in range(0,1000):
    pyautogui.click(1852, 54) #Click profile
    time.sleep(10)
    pyautogui.press('up') #Select Add
    time.sleep(1.5)
    pyautogui.press('enter') #Open Create New Profile
    time.sleep(45)
    pyautogui.typewrite(str(profileNumber)) #Enter Profile Number
    time.sleep(2)
    profileNumber+=1
    pyautogui.click(840, 960) #Deselect Create Shortcut
    time.sleep(2)
    pyautogui.click(1480, 960) #Click Done
    time.sleep(45)
    pyautogui.click(1700, 660) #Click "Start Using Rewards"
    time.sleep(5)
    pyautogui.click(1600, 60) #Click Rewards Icon
    time.sleep(10)
    pyautogui.click(1490, 240) #Click Reward Settings
    time.sleep(10)
    pyautogui.click(1015, 930) #Turn Off Auto COntribute 
    time.sleep(2)
    pyautogui.click(935, 430) #Ad Settings
    time.sleep(2)
    pyautogui.click(680, 515) #Select No of ads option
    time.sleep(2)
    pyautogui.click(665, 860) #Select 10 per hour
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'r') #Refresh
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w') #Close Tab
    time.sleep(3)
    for j in range(0,25):
        pyautogui.hotkey('ctrl', 'r') #Refresh
        time.sleep(0.18)
    time.sleep(3)
    pyautogui.hotkey('alt', 'f4') #Close Window
    time.sleep(5)