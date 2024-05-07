import tkinter as tk
from PIL import Image , ImageTk
import csv
from datetime import date
import time
import numpy as np
import cv2
from tkinter.filedialog import askopenfilename
import os
from tkinter import messagebox as ms
import shutil
#from skimage import measure
#import Train_FDD_cnn as TrainM
global fn

#==============================================================================
root = tk.Tk()
root.state('zoomed')

root.title("Fake Image Video Detection System")

current_path = str(os.path.dirname(os.path.realpath('__file__')))

basepath=current_path  + "\\" 

#==============================================================================
#==============================================================================

img = Image.open(basepath + "GUI4.jpg")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()

bg = img.resize((w,h),Image.ANTIALIAS)

bg_img = ImageTk.PhotoImage(bg)

bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=0)

heading = tk.Label(root,text="Fake Image Video Detection System",width=28,font=("Times New Roman",30,'bold'),bg="white",fg="black")
heading.place(x=100,y=42)
     
def show_FDD_video(video_path):
    ''' Display FDD video with annotated bounding box and labels '''
    from keras.models import load_model
    
    # video_path=r"D:\Alka_python_2019_20\FDD_Main\Video_File\fall-01.mp4"
    img_cols, img_rows = 64,64
    
    FALLModel=load_model(r'fake_event.h5')    #video = cv.VideoCapture(video_path);
    
    video = cv2.VideoCapture(video_path)
        
    # video = cv2.VideoCapture(0)

    if (not video.isOpened()):
        print("{} cannot be opened".format(video_path))
        # return False

    font = cv2.FONT_HERSHEY_SIMPLEX
    green = (0, 255, 0)
    red = (0, 0, 255)
    # orange = (0, 127, 255)
    line_type = cv2.LINE_AA
    i=1
    
    while True:
        ret, frame = video.read()
        
        if not ret:
            break
        img=cv2.resize(frame,(img_cols, img_rows),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.array(img)
        
        X_img = img.reshape(-1, img_cols, img_rows, 1)
        X_img = X_img.astype('float32')
        
        X_img /= 255
        
        predicted =FALLModel.predict(X_img)

        if predicted[0][0] < 0.5:
            predicted[0][0] = 0
            predicted[0][1] = 1
            label = 1
        else:
            predicted[0][0] = 1
            predicted[0][1] = 0
            label = 0
          
        frame_num = int(i)  #.iloc[:1,0])
        # label = int(annotations['label'][i])
        label_text = ""
        
        color = (255, 255, 255)
        
        if  label == 1 :
            label_text = "Fake Image Detected"
            color = red
        else:
            label_text = "Normal Image Detected"
            color = green

        frame = cv2.putText(
            frame, "Frame: {}".format(frame_num), (5, 30),
            fontFace = font, fontScale = 1, color = color, lineType = line_type
        )
        frame = cv2.putText(
            frame, "Label: {}".format(label_text), (5, 60),
            fontFace = font, fontScale =1, color = color, lineType = line_type
        )

        i=i+1
        cv2.imshow('FDD', frame)
        if cv2.waitKey(30) == 27:
            break

    video.release()
    cv2.destroyAllWindows()
       
    
def Video_Verify():
    
    global fn
    
#    fn=r"D:\Alka_python_2019_20\Alka_python_2019_20\Video Piracy\Piracy_Preserving\result.mp4"
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                               filetypes=[("all files", "*.*")])

    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)
            
    if Sel_F!= 'mp4':
        print("Select Video File!!!!!!")
    else:
        
        # frame_display = tk.LabelFrame(root, text=" --Display-- ", width=400, height=500, bd=5, font=('times', 10, ' bold '),bg="white",fg="red")
        # frame_display.grid(row=0, column=0, sticky='nw')
        # frame_display.place(x=920, y=190)

        
        # lbl2 = tk.Label(frame_display, text="Status", font=('times', 15,' bold '),width=30,bg="white",fg="black")
        # lbl2.place(x=0, y=300)

        show_FDD_video(fn)
        # run_video(fn,520, 190,400,500)   
#============================================================================================================
def upload():
     
    global fn

    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                               filetypes=[("all files", "*.*")])

    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)
            
    if Sel_F!= 'mp4':
        print("Select Video File!!!!!!")
        ms.showerror('Oops!', 'Select Video File!!!!!!')
    else:
        ms.showinfo('Success!', 'Video Uploaded Successfully !')
        return fn
def convert():
#    global fn
    #a=upload(fn)
    cam = cv2.VideoCapture(fn)
    try:
          
        # creating a folder named data
        if not os.path.exists('images'):
            os.makedirs('images')
      
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of images')
      
    # frame
    currentframe = 0
      
    while(True):
          
        # reading from frame
        ret,frame = cam.read()
      
        if ret:
            # if video is still left continue creating images
            name = './images/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
      
            # writing the extracted images
            cv2.imwrite(name, frame)
      
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
      
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
    ms.showinfo('Success!', 'Video converted into frames Successfully !')

def CLOSE():
    root.destroy()
    
   
###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            

button5 = tk.Button(root,command = upload, text="Upload Video", width=22,font=("Times new roman", 17, "bold"),bg="grey80",fg="black")
button5.place(x=100,y=150)

button1 = tk.Button(root,command = convert, text="Convert Video To Frames", width=22,font=("Times new roman", 17, "bold"),bg="grey80",fg="black")
button1.place(x=100,y=250)

button2 = tk.Button(root,command = Video_Verify, text="Detect Fake Video", width=22,font=("Times new roman", 17, "bold"),bg="grey80",fg="black")
button2.place(x=100,y=350)


close = tk.Button(root,command = CLOSE, text="Exit", width=22,font=("Times new roman", 17, "bold"),bg="red",fg="white")
close.place(x=100,y=450)


root.mainloop()






