import cv2
from cvzone.HandTrackingModule import HandDetector
import pyttsx3


class Calculator:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw_button(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (125, 125, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 70), cv2.FONT_HERSHEY_PLAIN,
                    2, (50, 50, 50), 2)

    def click(self, x, y, img):
        if self.pos[0] < x < self.pos[0] + self.width and \
                self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),
                          (self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN,
                        5, (0, 0, 0), 5)
            return True
        else:
            return False


# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("Please wait! The virtual calculator is starting")
engine.runAndWait()

# Define the Calculator Buttons
buttons = [['7', '8', '9', 'C'],
           ['4', '5', '6', '*'],
           ['1', '2', '3', '+'],
           ['0', '-', '/', '='],
           ['(', ')', '.', 'del']]

button_list = []
for x in range(4):
    for y in range(5):
        xpos = x * 100 + 700
        ypos = y * 100 + 100
        button_list.append(Calculator((xpos, ypos), 100, 100, buttons[y][x]))

equation = ''
counter = 0

# Webcam Setup
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 1080)  # Height
detector = HandDetector(detectionCon=0.9, maxHands=1)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame from the webcam.")
        break  # Exit the loop if frame capture fails

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    # Draw buttons
    for button in button_list:
        button.draw_button(img)

    # Check for Hand and Button Click
    if hands:
        lmList = hands[0]['lmList']
        # Ensure that we only pass the 2D coordinates (x, y) to findDistance
        x1, y1 = lmList[8][0:2]  # Tip of the index finger
        x2, y2 = lmList[12][0:2]  # Tip of the middle finger
        length, info, img = detector.findDistance((x1, y1), (x2, y2), img)

        x, y = lmList[8][0:2]  # Update x and y to only use 2D coordinates

        if length < 50 and counter == 0:
            for i, button in enumerate(button_list):
                if button.click(x, y, img):
                    myValue = button.value  # Correct button value
                    if myValue == '=':
                        try:
                            equation = str(eval(equation))
                        except:
                            engine.say("Syntax Error")
                            engine.runAndWait()
                            equation = 'Syntax Error'
                    elif equation == 'Syntax Error':
                        equation = ''
                    elif myValue == 'C':
                        equation = ''
                    elif myValue == 'del':
                        equation = equation[:-1]
                    else:
                        equation += myValue
                    counter = 1

    # To avoid multiple clicks
    if counter != 0:
        counter += 1
        if counter > 10:
            counter = 0

    # Display the final answer
    cv2.rectangle(img, (700, 20), (1100, 100), (175, 125, 155), cv2.FILLED)
    cv2.rectangle(img, (700, 20), (1100, 100), (50, 50, 50), 3)
    cv2.putText(img, equation, (710, 80), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    cv2.putText(img, 'VIRTUAL CALCULATOR -->', (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow("Virtual Calculator", img)
    cv2.moveWindow("Virtual Calculator", 0, 0)

    # Close the webcam when 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
