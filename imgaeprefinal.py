from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import time
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("C:\\Users\\praneeth\\AppData\\Local\\Programs\\Python\\Python36\\resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()
x=""
logo = ImageTk.PhotoImage(Image.open(root.filename).resize((250, 250), Image.ANTIALIAS))
w = Label(root, image=logo)
w.pack()
predictions, percentage_probabilities = prediction.predictImage(root.filename, result_count=5)
for index in range(len(predictions)):
    x+=predictions[index]+" : "+str( percentage_probabilities[index])+"\n"

w = Label(root, text=x)
w.pack()
