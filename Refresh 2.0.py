import pyautogui
import time

#Profile Selector = 18
#Scroll Click 24 per set

#Continous Refresh of 210 tabs need scroll click 7

#Refresh 30 Times
def refresh():
    for i in range(0,30):
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(0.125)

#Use Super F4 to close and reopen Brave
def forceCloseWindow():
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
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('f4')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('f4')
    time.sleep(2)
    pyautogui.click(770,1055)
    time.sleep(10)
    pyautogui.moveTo(890,1055,1.5)
    pyautogui.click(button='right')
    time.sleep(2)
    pyautogui.click(858,1000)
    time.sleep(2)
    for i in range(0,30):
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(0.25)

#Save Last Opened Profile Data
def saveToFile(rightCount,scrollClickCount):
    if(rightCount==0):
        rightCount=23
    else:
        rightCount=rightCount-1
    file1 = open("CountData.txt", "a")
    file1.write("Right Count = "+ str(rightCount) + " \t" + "Scroll Click Count = " + str(scrollClickCount) +"\n")
    file1.close()

#To refresh First 18
def refreshFirstSet():
    for first18 in range(1,19):
        pyautogui.click(1852, 54)
        time.sleep(8)
        pyautogui.press('right')
        time.sleep(0.5)
        for i in range(0,first18):
            pyautogui.press('right')
        pyautogui.press('enter')
        time.sleep(10)
        # donateTips()
        refresh()
        pyautogui.hotkey('alt', 'f4')
        time.sleep(2)

#To Claim Rewards
def claimRewards():
    pyautogui.click(1706,696)                   #Click Claim My Rewards
    time.sleep(3)
    pyautogui.moveTo(1385,292)                  #Move Cursor to Triangle
    time.sleep(10)
    
#Donate Tips
def donateTips():
    # refresh()
    pyautogui.hotkey('ctrl','l')
    time.sleep(0.25)
    pyautogui.write('https://pmstextiles.netlify.app/')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(1615,60)                    #Click Rewards Icon
    time.sleep(3)
    pyautogui.click(1582,470)                   #Click Close Backup Panel
    time.sleep(2)
    pyautogui.click(1380,500)                   #Click Send Tip
    time.sleep(2)
    pyautogui.click(1680,600)                   #Click Send
    time.sleep(2)
    pyautogui.click(1870,115)                   #Click Close
    time.sleep(2)
    pyautogui.hotkey('ctrl','t')
    time.sleep(3)
    pyautogui.hotkey('ctrl','tab')
    time.sleep(3)
    pyautogui.hotkey('ctrl','w')
    time.sleep(3)

def main():
    #Continue refresh from Right count = 3 and ScrollCount = 4
    # Right Count = 10 	Scroll Click Count = 36 Continue Claim Rewards From Here
    multiTabCount=0
    rightCount=0
    scrollClickCount=40
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(2)

    for mainLoop in range(0,10000000):

        # # For Continuous Refresh
        if(scrollClickCount==40):
            scrollClickCount=1
            refreshFirstSet()

        pyautogui.click(1852, 54)                   #Click Profile Selector
        time.sleep(5)
        for i in range(0,scrollClickCount):
            pyautogui.click(1860, 1010)
            time.sleep(0.1)
        pyautogui.moveTo(1690,90)
        time.sleep(1)
        if(rightCount==0):
            pyautogui.press('enter')
            time.sleep(4)
        else:
            for x in range(0,rightCount):
                pyautogui.press('right')
            pyautogui.press('enter')
            time.sleep(4)
        rightCount+=1
        if(rightCount==24):
            rightCount=0
            scrollClickCount+=1
        # donateTips()
        # claimRewards()
        refresh()
        multiTabCount+=1
        saveToFile(rightCount,scrollClickCount)
        if(multiTabCount%25==0):
            forceCloseWindow()
        else:    
            pyautogui.hotkey('alt', 'f4')
            time.sleep(2)

if __name__ == "__main__":
    main()