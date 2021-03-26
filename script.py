import pyautogui as gui
import time
import webbrowser
import random
import datetime
import schedule

zones = [
  "ARRAYS START AT 1 LMAO",
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

calendarDiff = (37, 25)
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
    return ((((point2[0] - point1[0])**2) + ((point2[1] - point1[1])**2))**0.5)

def click(position, offset = 0):
    gui.moveTo(position[0], position[1], offset + (random.random() / 10), movementTypes[random.randint(0, len(movementTypes) - 1)])
    gui.click(button="left")

def initBrowser(zone):
    webbrowser.open_new(zones[zone])

    while (gui.locateOnScreen('./images/hubLogo.png', confidence=0.90) == None):
        pass

    time.sleep(0.153)
    gui.moveTo(960, 540)
    gui.click(button="left")
    gui.scroll(-2354)

def addParticipant():
    addParticipantButton = gui.center(list(gui.locateAllOnScreen('./images/plus.png', confidence=0.90))[1])
    click(addParticipantButton, 0.1)

def selectCalendarDay(desiredDay, desiredDate):
    monthDif = int(desiredDate.strftime("%m")) - int(datetime.datetime.now().strftime("%m"))
    if (monthDif > 0):
        forwardButton = gui.center(gui.locateOnScreen('./images/forwardButton.png', confidence=0.98))
        gui.moveTo(forwardButton[0], forwardButton[1], 0.1 + (random.random() / 10), movementTypes[random.randint(0, len(movementTypes) - 1)])

        for i in range(monthDif):
            time.sleep(random.random() / 10)
            gui.click(button="left")

    backButton = gui.center(gui.locateOnScreen('./images/backButton.png', confidence=0.95))
    datePosition = (backButton[0] + calendarDiff[0]*int(desiredDate.strftime("%w")), backButton[1] + calendarDiff[1]*(desiredDay // 7) + 60)
    click(datePosition, 0.1)
    
    time.sleep(0.2 + random.random() / 10)
    gui.scroll(-703)

def pressBookingButton(desiredDay, desiredTime, desiredDate):
    bookingButton = None
    datePosition = None

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
            if (datePosition == None):
                backButton = gui.center(gui.locateOnScreen('./images/backButton.png', confidence=0.95))
                datePosition = (backButton[0] + calendarDiff[0]*int(desiredDate.strftime("%w")), backButton[1] + calendarDiff[1]*(desiredDay // 7) + 60)
            
            click(datePosition, 0.1)
            time.sleep(0.7 + random.random() / 10)

    click(bookingButton, 0.1)

def completeBooking():
    while (gui.locateOnScreen('./images/bookingDetails.png', confidence=0.90) == None):
        pass

    click(userButton, 0.1)

    gui.scroll(-607)
    time.sleep(0.089)

    click(acknowledge[0], 0.1)
    click(acknowledge[1])

    click(bookings[0], 0.1)
    click(bookings[1])

    click(membership[0], 0.1)
    click(membership[1])

    click(directives[0], 0.1)
    click(directives[1])

    click(continueButton, 0.1)

    while (gui.locateOnScreen('./images/confirmBookingDetails.png', confidence=0.90) == None):
        pass

    gui.scroll(-645)
    time.sleep(0.11)
    gui.scroll(-613)

    click(agree, 0.1)
    click(robot, 0.1)
    click(complete, 0.1)

def bookClimb():
    desiredZone = 1
    desiredYear = 2021
    desiredDay = 29
    desiredMonth = 3
    desiredTime = "730pm"
    desiredDate = datetime.datetime(desiredYear, desiredMonth, desiredDay)

    initBrowser(desiredZone)
    addParticipant()
    selectCalendarDay(desiredDay, desiredDate)
    pressBookingButton(desiredDay, desiredTime, desiredDate)
    completeBooking()

if __name__ == "__main__":
    cronTime = "12:00"
    schedule.every().day.at(cronTime).do(bookClimb)

    while True:
        schedule.run_pending()
        time.sleep(0.5)