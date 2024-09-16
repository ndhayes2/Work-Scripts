#HOW TO USE: 
#When you press run, it will request the estimated time away from computer in minutes. Enter that in the console.
#Immediately after entering that, you have 5 seconds to click into a MS Teams message box. Nothing will be sent
#to anyone, but the best bet is to use your own personal chat. This way no one sees the "typing" bubbles when the 
#script starts messing around.
import pyautogui as pg
import time
import keyboard as kb

print("How long will you be away? Enter your answer in minutes.")
min_away = int(input())
t_end = time.time() + (60*min_away)


print('Begin in 5...')
print('Click into a Teams message box now.')
time.sleep(2)
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print("If you need to end early, click into the console and press ctrl + C.")
print("You can use your PC, but every 10ish seconds the mouse position will reset to the MS Teams box.")

mouse_position = pg.position()
loop_count = 0
while time.time() < t_end:
    pg.click(mouse_position)
    kb.press('space')
    time.sleep(1)
    kb.press('backspace')
    time.sleep(10)
    loop_count += 1

print("End. The loop fired " + str(loop_count) + " times.")