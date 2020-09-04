import cv2 # importing cv2 liberary
import webbrowser
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\user\tesseract\tesseract.exe'
from PIL import Image
import tkinter as tk
from tkinter import messagebox


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
root.withdraw()
MsgBox = tk.messagebox.showinfo ('INSTRUCTIONS','Press SPACEBAR to capture image \n Press ESC after capturing image\n\n\n Please wait a moment....')
root.destroy()
root.mainloop()


cam = cv2.VideoCapture(0)

count = 0

while True:
    ret, img = cam.read()

    cv2.imshow("Test", img)

    if not ret:
        break

    k=cv2.waitKey(1)

    if k%256==27:
        #For Esc key
        print("Close")
        break
    elif k%256==32:
        #For Space key

        print("Image "+str(count)+"saved")
        file='D:/python/images/img'+str(count)+'.jpg'
        
        cv2.imwrite(file, img)
        count +=1

cam.release
cv2.destroyAllWindows



imgy = Image.open(r'D:\python\images\img'+str((count-1))+'.jpg')
text = tess.image_to_string(imgy)

#print(text)

urlstring=text.split()

url="https://www.goodreads.com/search?utf8=%E2%9C%93&query="+urlstring[0]+' '+urlstring[1]+' '+urlstring[2]+' '+urlstring[3]
webbrowser.open(url)

