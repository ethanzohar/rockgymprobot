import keyboard
import pyautogui as gui
import time

userButton = (538, 630)
acknowledge = [(565, 442), (544, 502)]
bookings = [(656, 567), (695, 618)]
membership = [(660, 784), (666, 846)]
directives = [(632, 889), (636, 949)]
continueButton = (643, 947)
agree = (499, 663)
robot = (494, 775)
complete = (655, 860)

keyboard.start_recording()
keyboard.wait("a")

gui.moveTo(userButton[0], userButton[1], 0.219873245, gui.easeOutQuad)
gui.click(button="left")

time.sleep(0.046)
gui.scroll(-607)

gui.moveTo(acknowledge[0][0], acknowledge[0][1], 0.19234523456, gui.easeOutQuad)
gui.click(button="left")

gui.moveTo(acknowledge[1][0], acknowledge[1][1], 0.082342435, gui.easeInBounce)
gui.click(button="left")

gui.moveTo(bookings[0][0], bookings[0][1], 0.18973543957813900938, gui.easeOutQuad)
gui.click(button="left")

gui.moveTo(bookings[1][0], bookings[1][1], 0.0672893109, gui.easeInElastic)
gui.click(button="left")

gui.moveTo(membership[0][0], membership[0][1], 0.30879134573129845, gui.easeOutQuad)
gui.click(button="left")

gui.moveTo(membership[1][0], membership[1][1], 0.1092458134795, gui.easeOutQuad)
gui.click(button="left")

gui.moveTo(directives[0][0], directives[0][1], 0.23498511289734, gui.easeInBounce)
gui.click(button="left")

gui.moveTo(directives[1][0], directives[1][1], 0.0523123059, gui.easeInElastic)
gui.click(button="left")

gui.moveTo(continueButton[0], continueButton[1], 0.2333421123, gui.easeInBounce)
gui.click(button="left")

time.sleep(0.823)
gui.scroll(-645)
time.sleep(0.11)
gui.scroll(-613)

gui.moveTo(agree[0], agree[1], 0.22343425209181, gui.easeOutQuad)
gui.click(button="left")

gui.moveTo(robot[0], robot[1], 0.2343523049578, gui.easeOutQuad)
gui.click(button="left")

gui.moveTo(complete[0], complete[1], 0.1532145907130496, gui.easeOutQuad)
gui.click(button="left")

keyboard.stop_recording()
