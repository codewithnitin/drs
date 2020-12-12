
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils



stream = cv2.VideoCapture("DRS.mp4")

flag = True
def play(speed):
    global flag
    frame = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)

    grabbed, frame = stream.read()

    # if not grabbed:
    #     exit()
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, anchor=tkinter.NW, image=frame)

    if flag:
        canvas.create_text(580, 30, fill = "black", font = "Times 20 bold", text = "Decision Pending")
    flag = not flag

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("decision_pending.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, anchor = tkinter.NW, image = frame)

    time.sleep(4)

    frame = cv2.cvtColor(cv2.imread("sponser.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, anchor=tkinter.NW, image=frame)

    time.sleep(2)

    if decision == "out":
        decision_img = "out.jpeg"

    else:
        decision_img = "not_out.jpeg"

    frame = cv2.cvtColor(cv2.imread(decision_img), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, anchor=tkinter.NW, image=frame)





def out():
    thread = threading.Thread(target = pending, args= ("out", ))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

SET_WIDTH = 700
SET_HEIGHT = 465

window = tkinter.Tk()
window.title("CodeWithNitinThirdUmpireDecisionReviewSystemKit")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpeg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
Photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW, image = Photo)
canvas.pack()



btn = tkinter.Button(window, text = "<< Previous (Fast)", width = 50, command = partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text = "<< Previous (Slow)", width = 50, command = partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text = "   Next (Slow) >>", width = 50, command = partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text = "   Next (Fast) >>", width = 50, command = partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text = "   Give Not Out", width = 50, command = not_out)
btn.pack()

btn = tkinter.Button(window, text = "   Give Out", width = 50, command = out)
btn.pack()


window.mainloop()





