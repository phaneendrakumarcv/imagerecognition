# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:08:16 2019

@author: phaneendra
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import img2pdf
import PyPDF2



license=cv2.imread("licenseplate.jpg")


pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

licenserecg=cv2.CascadeClassifier('opencv-master\data\haarcascades\haarcascade_russian_plate_number.xml')

def fetch_license(image):
    
    licenserecg_copy=license.copy()
    
    license_rects= licenserecg.detectMultiScale(licenserecg_copy,1.2,10)
    
    for x,y,w,h in license_rects:
        cv2.rectangle(licenserecg_copy,(x,y),(x+w,y+h),(0,0,255),10)
        
    cv2.imshow('cropped',licenserecg_copy)
    cv2.waitKey(0)
    roi = license[y:y+h,x:x+w]
    cv2.imwrite("roi.png",roi)
    
    im=Image.open("roi.png").convert("RGBA")
    bg=Image.new("RGBA",im.size,(255,255,255))
    x,y=im.size
    bg.paste(im,(0,0,x,y),im)
    bg.save("roi.png",quality=95)
    
    
#    pdf="roi.pdf"
#    roiimage=Image.open("roi.png")
#    pdf_bytes=img2pdf.convert(roiimage.filename)
#    pdffile=open(pdf,"wb")
#    pdffile.write(pdf_bytes)
#    roiimage.close()
#    pdffile.close()
    
    licensenumber=pytesseract.image_to_string(Image.open("roi.png"))
    
    if(len(licensenumber)==0):
        print("data not found in tesseract")
        roi_pdf=open('roi.pdf',"rb")
        read_pdf=PyPDF2.PdfFileReader(roi_pdf)
        n_o_p=read_pdf.getNumPages()
        page=read_pdf.getPage(0)
        licensenumber=page.extractText()
    
    print(licensenumber)
    
    
    

#        
#    
# 
#    
#    
#    return licenserecg_copy

result=fetch_license(licenserecg)

#cv2.imshow('license',result)
#
#cv2.waitKey(0)

