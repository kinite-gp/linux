import time
from model.config import SLEEP_TIME
from model.scripts import play
from os import system
from pyautogui import keyDown, keyUp, press

keys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']


def controller(value, start_time):
    print(value)
    if (time.time() - start_time) > SLEEP_TIME:
        play("end")
        print("sleeped")
        return False
    elif "sleep" and "snow" and "boy" in value:
        play("unsuccess")
        print("sleeped")
        return False   
    
    # action bluetooth
     
    elif "blue" and "start" in value:
        play("accept")
        system("sudo systemctl start bluetooth")
        play("success")
    elif "blue" and "stop" in value:
        play("accept")
        system("sudo systemctl stop bluetooth")
        play("success")
        
    
    
    elif "show" in value:
        # show desktop
        
        if "desktop" in value:
            keyDown("win")
            press("d")
            keyUp("win")
            
         
    
    # move and go to workspace
    
    elif "go" and "windows" and "up" in value:
        play("accept")
        keyDown("alt")
        keyDown("ctrl")
        press("up")
        keyUp("alt")
        keyUp("ctrl")    
    elif "go" and "windows" and "down" in value:
        keyDown("alt")
        play("accept")
        keyDown("ctrl")
        press("down")
        keyUp("alt")
        keyUp("ctrl")
    elif "go" and "windows" and "right" in value:
        play("accept")
        keyDown("alt")
        keyDown("ctrl")
        press("right")
        keyUp("alt")
        keyUp("ctrl")    
    elif "go" and "windows" and "left" in value:
        play("accept")
        keyDown("alt")
        keyDown("ctrl")
        press("left")
        keyUp("alt")
        keyUp("ctrl")
       
    # take a screenshoot
    
    elif "screen" and "shot" in value:
        press("prtscr")
        
    elif "lock" and "screen" or "computer" or "system" in value:
        keyDown("win")
        press("l")
        keyUp("win")
    
    elif "open" or "run" or "launch" in value:
        
        # run terminal
        
        if "terminal" in value:
            keyDown("ctrl")
            keyDown("alt")
            press("t")
            keyUp("ctrl")
            keyUp("alt")
            
        # run browser
        
        elif "browser" in value:
            keyDown("ctrl")
            keyDown("alt")
            press("w")
            keyUp("ctrl")
            keyUp("alt")
            