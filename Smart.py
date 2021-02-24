import cv2
import numpy as np
import imutils
from threading import Timer
import math
import collections
import time


cap=cv2.VideoCapture(0)

lower = {'green': (66, 122, 129), 'yellow': (23, 59, 119)}
upper = {'green': (86, 255, 255), 'yellow': (54, 255, 255)}
x1 = 120
y1 = 165
global a
global b
c=[]
psw=[1,2,3]
u=0
#XoX Variables


xox1=[0,0]

matrix=[[0,0,0],
        [0,0,0],
        [0,0,0]]

# End XOX



def wlcm():
    wlcm0 = cv2.putText(frame, "LOGIN SUCCESSFUL", (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)

    wlcm_name = cv2.putText(frame, "Welcome Umutcan Gungor", (220, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 5)
    wlcm2 = cv2.putText(frame, "Sir,What Do u Want to Do ?", (220, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 112),
                        5)
    quit0 = cv2.putText(frame, "Quit", (400, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 112), 5)
    quit1 = cv2.rectangle(frame, (400, 400), (475, 475), (0, 0, 255), 2)


    xox001 = cv2.putText(frame, "Play XoX", (180, 380), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 112), 5)
    xox002 = cv2.rectangle(frame, (200, 400), (275, 475), (0, 0, 255), 2)




def calc():
    if pixel[0] > 100 and pixel[0] < 190 and pixel[1] > 220 and pixel[1] < 315:
        a = 1
        if len(c) == 0:
            c.append(1)
        elif c[-1] == 1:
            pass
        else:
            c.append(1)
            print(c)





    elif pixel[0] > 250 and pixel[0] < 350 and pixel[1] > 220 and pixel[1] < 315:
        a = 2
        if len(c) == 0:
            c.append(2)
        elif c[-1] == 2:
            pass
        else:
            c.append(2)

        print(c)

    elif pixel[0] > 399 and pixel[0] < 480 and pixel[1] > 220 and pixel[1] < 315:
        a = 3

        if len(c) == 0:
            c.append(3)
        elif c[-1] == 3:
            pass
        else:
            c.append(3)

        print(c)
    elif pixel[0] > 100 and pixel[0] < 195 and pixel[1] > 380 and pixel[1] < 500:
        a = 4
        if len(c) == 0:
            c.append(4)
        elif c[-1] == 4:
            pass
        else:
            c.append(4)

        print(c)


    elif pixel[0] > 250 and pixel[0] < 350 and pixel[1] > 380 and pixel[1] < 500:
        a = 5
        if len(c) == 0:
            c.append(5)
        elif c[-1] == 5:
            pass
        else:
            c.append(5)

        print(c)

    elif pixel[0] > 399 and pixel[0] < 480 and pixel[1] > 380 and pixel[1] < 500:
        a = 6
        if len(c) == 0:
            c.append(6)
        elif c[-1] == 6:
            pass
        else:
            c.append(6)

        print(c)
    elif pixel[0] > 500 and pixel[0] < 600 and pixel[1] > 500 and pixel[1] < 600:
        if len(c) == 0:
            pass
        else:
            del c[-1]
        time.sleep(0.2)


def result(x1):
    for i in c:
        result = cv2.putText(frame, str(i), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)
        x1 += 35

def foo():
    pass
def foo1(yty):
    return 1


def quit():

    if pixel[0] > 400 and pixel[0] < 470 and pixel[1] > 400 and pixel[1] < 470:
        exit()



def winner():

    if matrix[0][0]==1 and matrix[0][1] ==1 and matrix[0][2] ==1:
       cv2.putText(frame,"X IS WINNER !",(300,150),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
    elif matrix[0][0]==1 and matrix[1][0] ==1 and matrix[2][0] ==1:
        cv2.putText(frame,"X IS WINNER !",(300,150),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
    elif  matrix[2][0]==1 and matrix[2][1] ==1 and matrix[2][2] ==1:
        cv2.putText(frame, "X IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
    elif  matrix[0][2]==1 and matrix[1][2] ==1 and matrix[2][2] ==1:
        cv2.putText(frame, "X IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
    elif  matrix[0][0]==1 and matrix[1][1] ==1 and matrix[2][2] ==1:
        cv2.putText(frame,"X IS WINNER !",(300,150),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
    elif  matrix[0][2]==1 and matrix[1][1] ==1 and matrix[2][0] ==1:
        cv2.putText(frame,"X IS WINNER !",(300,150),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
    elif  matrix[0][1]==1 and matrix[1][1] ==1 and matrix[2][1] ==1:
        cv2.putText(frame,"X IS WINNER !",(300,150),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
    elif matrix[0][2] == 1 and matrix[1][2] == 1 and matrix[2][2] == 1:
        cv2.putText(frame, "X IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)


    if matrix[0][0] == 2 and matrix[0][1] == 2 and matrix[0][2] == 2:
        cv2.putText(frame,"O IS WINNER !",(300,150),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
    elif matrix[0][0] == 2 and matrix[1][0] == 2 and matrix[2][0] == 2:
        cv2.putText(frame, "O IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
    elif matrix[2][0] == 2 and matrix[2][1] == 2 and matrix[2][2] == 2:
        cv2.putText(frame, "O IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
    elif matrix[0][2] == 2 and matrix[1][2] == 2 and matrix[2][2] == 2:
        cv2.putText(frame, "O IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
    elif matrix[0][0] == 2 and matrix[1][1] == 2 and matrix[2][2] == 2:
        cv2.putText(frame, "O IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
    elif  matrix[0][2]==2 and matrix[1][1] ==2 and matrix[2][0] ==2:
        cv2.putText(frame, "O IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)
    elif  matrix[0][1]==2 and matrix[1][1] ==2 and matrix[2][1] ==2:
        cv2.putText(frame,"O IS WINNER !",(300,150),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
    elif matrix[0][2] == 2 and matrix[1][2] == 2 and matrix[2][2] == 2:
        cv2.putText(frame, "O IS WINNER !", (300, 150), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 2)



def xox():
    winner()
    line = cv2.line(frame, (200, 250), (700, 250), (0, 0, 255), 5)
    line2 = cv2.line(frame, (330, 150), (330, 500), (0, 0, 255), 5)
    line3 = cv2.line(frame, (200, 400), (700, 400), (0, 0, 255), 5)
    line4 = cv2.line(frame, (550, 150), (550, 500), (0, 0, 255), 5)

    cv2.rectangle(frame,(300,650),(400,750),(0,0,255),2),cv2.putText(frame,"X",(320,630),cv2.FONT_HERSHEY_SIMPLEX,2, (255, 255,0 ),3)
    cv2.rectangle(frame, (500, 650), (600, 750), (0, 0, 255), 2),cv2.putText(frame,"O",(520,630),cv2.FONT_HERSHEY_SIMPLEX,2, (255, 255,0 ),3)
    cv2.rectangle(frame, (700, 650), (800, 750), (0, 0, 255), 2), cv2.putText(frame, "Quit", (710, 630), cv2.FONT_HERSHEY_SIMPLEX, 1,  (255, 255,0 ),3)
    cv2.rectangle(frame, (150, 650), (250, 750), (0, 0, 255), 2), cv2.putText(frame, "Restart", (160, 630),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255,0 ),  3)




    if pixel[0] > 300 and pixel[0] < 400 and pixel[1] > 650 and pixel[1] < 750:
        xox1[0]=1
        xox1[1]= 0

    elif pixel[0] > 500 and pixel[0] < 600 and pixel[1] > 650 and pixel[1] < 750:
        xox1[1] = 1
        xox1[0] = 0
    elif pixel[0] > 700 and pixel[0] < 800 and pixel[1] > 650 and pixel[1] < 750:
        exit()
    elif pixel[0] > 150 and pixel[0] < 250 and pixel[1] > 650 and pixel[1] < 750:
        for i in range(3):
            for j in range(3):
                matrix[i][j]=0





    if xox1[0]==1:
        line = cv2.line(frame, (300, 650), (400, 750), (0, 0, 255), 5)
        line2 = cv2.line(frame, (400, 650), (300, 750), (0, 0, 255), 5)


    elif xox1[1]==1:
        line = cv2.line(frame, (500, 650), (600, 750), (0, 0, 255), 5)
        line2 = cv2.line(frame, (600, 650), (500, 750), (0, 0, 255), 5)

    #X PART
    if pixel[0] > 200 and pixel[0] < 330 and pixel[1] > 150 and pixel[1] < 250 and xox1[0]==1:
        if matrix[0][0] == 2:
            pass
        else:
            matrix[0][0] = 1
    elif pixel[0] > 350 and pixel[0] < 500 and pixel[1] > 150 and pixel[1] < 250 and xox1[0]==1:
        if matrix[0][1] == 2:
            pass
        else:
            matrix[0][1] = 1
    elif pixel[0] > 550 and pixel[0] < 680 and pixel[1] > 150 and pixel[1] < 250 and xox1[0]==1:
        if matrix[0][2] == 2:
            pass
        else:
            matrix[0][2] = 1
    elif pixel[0] > 200 and pixel[0] < 330 and pixel[1] > 250 and pixel[1] < 400 and xox1[0]==1:
        if matrix[1][0] == 2:
            pass
        else:
            matrix[1][0] = 1
    elif pixel[0] > 350 and pixel[0] < 500 and pixel[1] > 250 and pixel[1] < 400 and xox1[0]==1:
        if matrix[1][1] == 2:
            pass
        else:
            matrix[1][1] = 1
    elif pixel[0] > 550 and pixel[0] < 680 and pixel[1] > 250 and pixel[1] < 400 and xox1[0]==1:
        if matrix[1][2] == 2:
            pass
        else:
            matrix[1][2] = 1
    elif pixel[0] > 200 and pixel[0] < 330 and pixel[1] > 400 and pixel[1] < 500and xox1[0]==1:
        if matrix[2][0] == 2:
            pass
        else:
            matrix[2][0] = 1
    elif pixel[0] > 350 and pixel[0] < 500 and pixel[1] > 400 and pixel[1] < 500 and xox1[0]==1:
        if matrix[2][1] == 2:
            pass
        else:
            matrix[2][1] = 1
    elif pixel[0] > 550 and pixel[0] < 680 and pixel[1] > 400 and pixel[1] < 500 and xox1[0]==1:
        if matrix[2][2] == 2:
            pass
        else:
            matrix[2][2] = 1
    #X PART END

    #O PART
    if pixel[0] > 200 and pixel[0] < 330 and pixel[1] > 150 and pixel[1] < 250 and xox1[1]==1:
        if matrix [0][0]==1:
            pass
        else:
            matrix[0][0] = 2

    elif pixel[0] > 350 and pixel[0] < 500 and pixel[1] > 150 and pixel[1] < 250 and xox1[1]==1:
        if matrix[0][1] == 1:
            pass
        else:
            matrix[0][1] = 2
    elif pixel[0] > 550 and pixel[0] < 680 and pixel[1] > 150 and pixel[1] < 250 and xox1[1]==1:
        if matrix[0][2] == 1:
            pass
        else:
            matrix[0][2] = 2
    elif pixel[0] > 200 and pixel[0] < 330 and pixel[1] > 250 and pixel[1] < 400 and xox1[1]==1:
        if matrix[1][0] == 1:
            pass
        else:
            matrix[1][0] = 2
    elif pixel[0] > 350 and pixel[0] < 500 and pixel[1] > 250 and pixel[1] < 400 and xox1[1]==1:
        if matrix[1][1] == 1:
            pass
        else:
            matrix[1][1] = 2
    elif pixel[0] > 550 and pixel[0] < 680 and pixel[1] > 250 and pixel[1] < 400 and xox1[1]==1:
        if matrix[1][2] == 1:
            pass
        else:
            matrix[1][2] = 2
    elif pixel[0] > 200 and pixel[0] < 330 and pixel[1] > 400 and pixel[1] < 500and xox1[1]==1:
        if matrix[2][0] == 1:
            pass
        else:
            matrix[2][0] = 2
    elif pixel[0] > 350 and pixel[0] < 500 and pixel[1] > 400 and pixel[1] < 500 and xox1[1]==1:
        if matrix[2][1] == 1:
            pass
        else:
            matrix[2][1] = 2
    elif pixel[0] > 550 and pixel[0] < 680 and pixel[1] > 400 and pixel[1] < 500 and xox1[1]==1:
        if matrix[2][2] == 1:
            pass
        else:
            matrix[2][2] = 2
    #O PART END

    # X PART LINES
    if matrix[0][0] == 1:
        cv2.line(frame, (200, 160), (300, 240), (0, 0, 255), 2)
        cv2.line(frame, (300, 160), (200, 240), (0, 0, 255), 2)
    if matrix[0][1] == 1:
        cv2.line(frame, (380, 160), (500, 240), (0, 0, 255), 2)
        cv2.line(frame, (500, 160), (380, 240), (0, 0, 255), 2)
    if matrix[0][2] == 1:
        cv2.line(frame, (560, 160), (670, 240), (0, 0, 255), 2)
        cv2.line(frame, (670, 160), (560, 240), (0, 0, 255), 2)
    if matrix[1][0] == 1:
        cv2.line(frame, (200, 250), (330, 400), (0, 0, 255), 2)
        cv2.line(frame, (330, 250), (200, 400), (0, 0, 255), 2)

    if matrix[1][1] == 1:
        cv2.line(frame, (350, 250), (500, 400), (0, 0, 255), 2)
        cv2.line(frame, (500, 250), (350, 400), (0, 0, 255), 2)
    if matrix[1][2] == 1:
        cv2.line(frame, (550, 250), (680, 400), (0, 0, 255), 2)
        cv2.line(frame, (680, 250), (550, 400), (0, 0, 255), 2)
    if matrix[2][0] == 1:
        cv2.line(frame, (200, 400), (330, 500), (0, 0, 255), 2)
        cv2.line(frame, (330, 400), (200, 500), (0, 0, 255), 2)
    if matrix[2][1] == 1:
        cv2.line(frame, (350, 400), (500, 500), (0, 0, 255), 2)
        cv2.line(frame, (500, 400), (350, 500), (0, 0, 255), 2)

    if matrix[2][2] == 1:
        cv2.line(frame, (550, 400), (680, 500), (0, 0, 255), 2)
        cv2.line(frame, (680, 400), (550, 500), (0, 0, 255), 2)
    #X PART LINES END

    # O PART LINES
    if matrix[0][0] == 2:
        cv2.circle(frame, (245, 185), 45, (0, 0, 255), 2)
    if matrix[0][1] == 2:
        cv2.circle(frame, (425, 185), 45, (0, 0, 255), 2)
    if matrix[0][2] == 2:
        cv2.circle(frame, (625, 185), 45, (0, 0, 255), 2)
    if matrix[1][0] == 2:
        cv2.circle(frame, (245, 335), 45, (0, 0, 255), 2)

    if matrix[1][1] == 2:
        cv2.circle(frame, (425, 335), 45, (0, 0, 255), 2)
    if matrix[1][2] == 2:
        cv2.circle(frame, (625, 335), 45, (0, 0, 255), 2)

    if matrix[2][0] == 2:
        cv2.circle(frame, (245, 485), 45, (0, 0, 255), 2)
    if matrix[2][1] == 2:
        cv2.circle(frame, (425, 485), 45, (0, 0, 255), 2)

    if matrix[2][2] == 2:
        cv2.circle(frame, (625, 485), 45, (0, 0, 255), 2)

    #O PART LINES END


def interface():
    # INTERFACE
    rect = cv2.rectangle(frame, (100, 100), (500, 500), (0, 0, 255), 5)
    rect2 = cv2.rectangle(frame, (500, 500), (600, 600), (0, 0, 255), 5)

    line = cv2.line(frame, (100, 200), (500, 200), (0, 0, 255), 5)
    line2 = cv2.line(frame, (225, 200), (225, 500), (0, 0, 255), 5)
    line3 = cv2.line(frame, (375, 200), (375, 500), (0, 0, 255), 5)
    line4 = cv2.line(frame, (100, 350), (500, 350), (0, 0, 255), 5)

    letter1 = cv2.putText(frame, "1", (125, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)
    letter2 = cv2.putText(frame, "2", (250, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)
    letter3 = cv2.putText(frame, "3", (385, 300), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

    letter4 = cv2.putText(frame, "4", (125, 440), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)
    letter5 = cv2.putText(frame, "5", (250, 440), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)
    letter6 = cv2.putText(frame, "6", (385, 440), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

    letter7 = cv2.putText(frame, "C", (525, 570), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

    text1 = cv2.putText(frame, "Enter Password for Login", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)

    # INTERFACE END




while True:
    _, frame=cap.read()
    #frame = cv2.flip(frame, 1)
    frame=imutils.resize(frame,width=1080,height=1080)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, th1 = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)


    interface()

    for key,value in upper.items():
        core = np.ones((9, 9), np.uint8)  # Return a new array of 9x9, filled with ones.
        mask=cv2.inRange(hsv,lower[key],upper[key]) # Mask in Range loower and upper collors
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                                core)  # It is the difference between dilation and erosion of an image.
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, core)
        # find contours in the mask and initialize the current
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        for contour in cnts:
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            cv2.drawContours(frame, [approx], 0, (0, 0, 255), 2)
            x = approx.ravel()[0]  # bütün şekillerin x'deki köşelerini alır
            y = approx.ravel()[1] - 10  # ""

            M = cv2.moments(cnts[0])


            pixel=[(round(M['m10'] / M['m00'])),(round(M['m01'] / M['m00']))]
            print(pixel)
            lower2 =[(100, 220)]
            upper2=[(220, 315)]

            calc()


            result(x1)


            if collections.Counter(psw) == collections.Counter(c):
                if psw[0]==c[0] and psw[1]==c[1] and psw[2]==c[2]:

                    wlcm()

                    if pixel[0] > 400 and pixel[0] < 470 and pixel[1] > 400 and pixel[1] < 470:
                        quit()
                    if pixel[0] > 200 and pixel[0] < 275 and pixel[1] > 400 and pixel[1] < 475:
                       u=1

                    if u ==1:
                        xox()
                        wlcm = foo
                        quit = foo



                    interface = foo
                    result = foo1
                    calc = foo







    #cv2.imshow("mask", res)
    cv2.imshow("img", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break




cap.release()
cv2.destroyAllWindows()