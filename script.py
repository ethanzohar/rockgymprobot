import pyautogui as gui
import time
import webbrowser
import random
import datetime

zones = [
  "",
  "https://app.rockgympro.com/b/?&bo=3ba4229e839f48d08bff7026ebb507e0",
  "https://app.rockgympro.com/b/?&bo=bd099f5a7306411ba1cfe4cfc6b85e49",
  "https://app.rockgympro.com/b/?&bo=16d922aa60754e2d8f7dee10054da1de"
]

movementTypes = [
    gui.easeInQuad,
    gui.easeOutQuad,
    gui.easeInOutQuad,
    gui.easeInBounce,
    gui.easeInElastic
]

desiredYear = 2021
desiredDay = 26
desiredMonth = 3
desiredTime = "4pm"

desiredDate = datetime.datetime(desiredYear, desiredMonth, desiredDay)

calendarStart = (509, 896)
calendarDiff = (37, 25)
calendarNextMonth = (725, 832)

addParticipantButton = (888, 869)

userButton = (538, 630)
acknowledge = [(565, 442), (544, 502)]
bookings = [(656, 567), (695, 618)]
membership = [(660, 784), (666, 846)]
directives = [(632, 889), (636, 949)]
continueButton = (643, 947)
agree = (499, 663)
robot = (494, 775)
complete = (655, 860)

def distance(point1, point2):
    return ((((point2[0] - point1[0])**2) + ((point2[1] - point1[1])**2) )**0.5)

def initBrowser():
    webbrowser.open_new(zones[3])
    gui.moveTo(960, 540)
    gui.click(button="left")

    while (gui.locateOnScreen('./images/hubLogo.png', confidence=0.90) == None):
        pass

    gui.scroll(-850)

def addParticipant():
    gui.moveTo(addParticipantButton[0], addParticipantButton[1], 0.2 + (random.random() / 10), movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

def selectCalendarDay():
    monthDif = int(desiredDate.strftime("%m")) - int(datetime.datetime.now().strftime("%m"))
    if (monthDif > 0):
        gui.moveTo(calendarNextMonth[0], calendarNextMonth[1], 0.2 + (random.random() / 10), movementTypes[random.randint(0, len(movementTypes) - 1)])

        for i in range(monthDif):
            time.sleep(random.random() / 10)
            gui.click(button="left")

    calendarPosition = (calendarStart[0] + calendarDiff[0]*int(desiredDate.strftime("%w")), calendarStart[1] + calendarDiff[1]*(desiredDay // 7))
    gui.moveTo(calendarPosition[0], calendarPosition[1], 0.2 + (random.random() / 10), movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")
    time.sleep(0.2 + random.random() / 10)
    gui.scroll(-703)

def pressBookingButton():
    bookingButton = None
    newCalendarStart = None

    while bookingButton == None:
        timeslot = None
        confidence = 0.95
        while (timeslot == None and confidence >= 0.7):
            timeslot = gui.locateOnScreen('./images/' + desiredTime + '.png', confidence=confidence)
            confidence -= 0.05

        if timeslot == None:
            raise Exception("unable to find timeslot")

        selectButtons = list(gui.locateAllOnScreen('./images/select.png', confidence=0.95))
        minDist = float('inf')
        for button in selectButtons:
            dist = distance(gui.center(button), gui.center(timeslot))
            if (dist < minDist):
                minDist = dist
                bookingButton = button

        if (bookingButton == None):
            if (newCalendarStart == None):
                backButton = gui.center(gui.locateOnScreen('./images/backButton.png', confidence=0.95))
                newCalendarStart = (backButton[0] + calendarDiff[0]*int(desiredDate.strftime("%w")), backButton[1] + calendarDiff[1]*(desiredDay // 7) + 60)
            
            gui.moveTo(newCalendarStart[0], newCalendarStart[1], 0.2 + (random.random() / 10), movementTypes[random.randint(0, len(movementTypes) - 1)])
            gui.click(button="left")
            time.sleep(0.7 + random.random() / 10)

    gui.moveTo(bookingButton[0], bookingButton[1], 0.2 + (random.random() / 10), movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

def completeBooking():
    while (gui.locateOnScreen('./images/bookingDetails.png', confidence=0.90) == None):
        pass

    gui.moveTo(userButton[0], userButton[1], 0.219873245, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    time.sleep(0.046)
    gui.scroll(-607)

    gui.moveTo(acknowledge[0][0], acknowledge[0][1], 0.19234523456, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(acknowledge[1][0], acknowledge[1][1], 0.082342435, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(bookings[0][0], bookings[0][1], 0.18973543957813900938, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(bookings[1][0], bookings[1][1], 0.0672893109, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(membership[0][0], membership[0][1], 0.30879134573129845, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(membership[1][0], membership[1][1], 0.1092458134795, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(directives[0][0], directives[0][1], 0.23498511289734, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(directives[1][0], directives[1][1], 0.0523123059, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(continueButton[0], continueButton[1], 0.2333421123, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    while (gui.locateOnScreen('./images/confirmBookingDetails.png', confidence=0.90) == None):
        pass

    gui.scroll(-645)
    time.sleep(0.11)
    gui.scroll(-613)

    gui.moveTo(agree[0], agree[1], 0.22343425209181, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(robot[0], robot[1], 0.2343523049578, movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

    gui.moveTo(complete[0], complete[1], 0.1532145907130496, movementTypes[random.randint(0, len(movementTypes) - 1)])
    # gui.click(button="left")

if __name__ == "__main__":
    initBrowser()
    addParticipant()
    selectCalendarDay()
    pressBookingButton()
    time.sleep(0.7 + random.random() / 10)
    completeBooking()