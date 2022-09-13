from tkinter import *
from tkinter.filedialog import *
import os
from fitz import fitz, Rect

pdfpath = 0
imgpath = 0
pdfdir = 0
pdf = None

def openpdfFile():
    global pdfpath
    global pdfdir
    pdffile = askopenfilename(title = "Open File", filetypes = (("Pdf File", "*.pdf"),("모든 파일", "*.*")))
    pdfpath = os.path.dirname(pdffile) + "/"+ os.path.basename(pdffile)
    pdfdir = os.path.dirname(pdffile) + "/" + "result.pdf"
    lb1["text"]=pdfpath
    

def openimgFile():
    global imgpath
    imgfile = askopenfilename(title = "Open File", filetypes = (("png File", "*.png"),("모든 파일", "*.*")))
    imgpath = os.path.dirname(imgfile)+"/"+os.path.basename(imgfile)
    lb2["text"]=imgpath
    
def click_exe():
    global pdfpath
    global imgpath
    pdf = fitz.open(pdfpath)
    img = open(imgpath, "rb").read()
    for i in range(0, pdf.pageCount):
        page = pdf[i]
        w = page.MediaBoxSize[0]
        h = page.MediaBoxSize[1]
        rect = fitz.Rect(0, 0.95*h, 1.8*w, h) # stamp img location setting (x0,y0,x1,y1)
        page.cleanContents()
        page.insertImage(rect, stream=img)    
        print(page.MediaBoxSize[1])
    pdf.save(pdfdir)
    lb3["text"]="Succeed and Saved!"
    lb4["text"]="Saved at " + str(pdfdir)
    
      
top = Tk()
top.title("Automatic Stamp Machine")
top.geometry("600x170")

btn1 = Button(text="1.Select PDF File", command=openpdfFile)
btn2 = Button(text="2.Select IMG File", command=openimgFile)
btn3 = Button(text="3.Merge", command=click_exe)

lb1 = Label(top, text="empty", font=("System, 9"))
lb2 = Label(top, text="empty", font=("System, 9"))
lb3 = Label(top, text="", font=("System, 9"))
lb4 = Label(top, text="", font=("System, 9"))

lb5 = Label(top, text="1. Select pdf file", font=("System, 9"))
lb6 = Label(top, text="2. Select stamp img file(png file)", font=("System, 9"))
lb7 = Label(top, text="3. Click 'Merge' button", font=("System, 9"))
lb8 = Label(top, text="4. Check 'result.pdf' at same directory", font=("System, 9"))

btn1.place(x=250, y=20)
btn2.place(x=250, y=70)
btn3.place(x=250, y=120)

lb1.place(x=350, y=20)
lb2.place(x=350, y=70)
lb3.place(x=350, y=120)
lb4.place(x=350, y=140)

lb5.place(x=5, y=20)
lb6.place(x=5, y=40)
lb7.place(x=5, y=60)
lb8.place(x=5, y=80)

top.mainloop()



