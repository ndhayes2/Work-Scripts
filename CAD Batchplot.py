import keyboard
import time
import pyautogui
import datetime

#INSTRUCTIONS
#1. Open all drawings to plot in AutoCAD
#2. Plot one to the folder you want them to appear in, then delete the plotted drawing. This sets the plotter's file path
#3. Change the drawing_number variable below to the amount of drawings to be plotted.
#4. Select the FIRST drawing to print (farthest to the left in the drawing tabs)
#5. Run the script, then immediately click into AutoCAD (best to click the top of the CAD window)


#The script will plot each drawing, clicking into the AutoCAD window between each plot so the commands can be entered
#While this is running, you can't use your computer for anything else until it finishes.
#Do not use this without meticulous setup, it could wreck a project if anything goes wrong.

drawing_number = 22

def batchplot():
    time.sleep(2)

    current_mouse_position = pyautogui.position()
    keyboard.write('plot')
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('enter')

    time.sleep(2)
    keyboard.press_and_release('enter')
    time.sleep(4)
    pyautogui.click(current_mouse_position)
    keyboard.press_and_release('ctrl + tab')


start_time = time.time()
print('Beginning in 3 seconds...')
time.sleep(3)
print("Begin.")
for i in range(0, drawing_number):
    batchplot()
    percent = ((i+1)/drawing_number) * 100
    x = i+1
    print(f'Drawing number {x} completed. {percent:.2f}%% complete.')
end_time = time.time()
elapsed_time = round(end_time - start_time)
elapsed_time = str(datetime.timedelta(seconds= elapsed_time))
print('End.')
print(elapsed_time)
