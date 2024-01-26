from logging import exception
from pathlib import WindowsPath
from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np #we use numpy as it gives 88% better performance

class trainData:
    def __init__(self,root): #calling constructor; root is the root window..base window...the first window or the home page
        self.root=root #initialising self
        self.root.title("Attendance System With Face Recognition") #giving title to root window
        self.root.geometry("1x1+0+0") #setting screen size for root window
        #self.root.geometry(None)
        self.train_classifier()                    

    def train_classifier(self):
        #data_dr=(r"C:\Users\santo\OneDrive\Documents\PythonFiles\Python_Projects\Attendance_System\imageSamples")
        data_dr=(r"imageSamples")
        path=[os.path.join(data_dr,file) for file in os.listdir(data_dr)]
        #print(path)
        faces=[] # this will contain the px of images
        ids=[] # this will contain the path of images

        for image in path:
            img=Image.open(image).convert('L') #to convert image into grey scale
            imageNp=np.array(img,'uint8')
            id=int((os.path.split(image)[1].split('.')[0]).split('_')[1])
            faces.append(imageNp)
            
            ids.append(id)
            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13 # 13 is for enter key
            
        #print(ids)
        ids=np.array(ids)
        #return np.array(ids),faces
        #ids, faces = train_classifier()

        #=======================Train the classifier and save==================
        
        clf = cv2.face.LBPHFaceRecognizer_create()  # clf is lbph classifier     
        #lbph_classifier=cv2.face.createLBPHFaceRecognizer() 
        #ids = np.array(ids)
        clf.train(faces,ids)        
        clf.write("TrainDataClassifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training of DataSets completed") 

if __name__=="__main__":
    root=Tk()
    obj=trainData(root)
    root.mainloop()