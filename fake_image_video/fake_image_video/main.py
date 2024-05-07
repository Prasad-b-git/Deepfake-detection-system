# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:24:42 2024

@author: COMPUY
"""


import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
'''import detection_emotion_practice as validate'''
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Fake Image Video Detection System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = image2.resize((w ,h ), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  



# image2 = Image.open('bg2.jpg')
# image2 = image2.resize((900, 800), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=800, y=0)  # , relwidth=1, relheight=1)

# label_l1 = tk.Label(root, text="Deep Fake Detection",font=("Helvetica", 20, 'bold'),
# background="black",fg="cyan", width=20, height=2)
# label_l1.place(x=920, y=40)


# , relwidth=1, relheight=1)
#
# label_l1 = tk.Label(root, text="Fake Image Video Detection System",font=("Times New Roman", 35, 'bold'),
#                     background="#000000", fg="Magenta", width=50, height=1)
# label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)

# image2 = Image.open('logo3.png')
# image2 = image2.resize((100, 100), Image.ANTIALIAS)
# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=1100, y=160)     


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# def reg():
#     from subprocess import call
#     call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","GUI_Master1.py"])
    
def window():
  root.destroy()


button4 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 17, ' bold '), bg="Red", fg="white")
button4.place(x=80, y=200)


root.mainloop()