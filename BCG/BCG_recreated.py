import PIL
import os #provides functions for interacting with the operating system
from PIL import ImageFont #PIL = Python Image Library, ImageFont = Loads every Font usable in Python
from PIL import ImageDraw #ImageDraw provides 2d graphics which can be created and edited
from PIL import Image #same as ImageDraw, working with images
#-----------------------welcome user and instructions--------------
print("Hello !")
print("welcome to BCG the Business card generator")
print(" ")
print(" ") #generating empty rows
print(" ")
print("please chose your color like this : red, orange, yellow, green, blue, violet ")
print(" ")
print(" ")
print(" ")
#-----------------------let user chose colors------------------------
#define inputs and give order
tcolor = input('Enter text color:')
bgcolor = input('Enter background color:')
acolor = input('Enter accent color:')
#------------------------create backgound------------------------
#measure the card w x h in pixels
basex, basey = 1004 , 650 #width and height
bg = Image.new('RGB', (basex, basey), (bgcolor)) #create new image for background using rgb colors and inputs from above
draw = ImageDraw.Draw(bg)  #creates image, I use short form draw to simplify


#----------------create accent image-------------

topx, topy = 333, 650
top = Image.new('RGB', (topx, topy),(acolor))
draw = ImageDraw.Draw(top)
#-----------------add accent on top of bg-------------
#paste on bg the top
bg.paste(top)
#safe background as base.png
bg.save('base.png')
#close it
bg.close()
#image created
#first time saving file
#---------------------write user image on background---------------
#working on saved file
#open image
img = Image.open ('base.png')
#base.png is now saved as img
#defines imagedraw, img referrs to base.png
#applying function imagedraw on img (which is base.png to be able to work on the image)

draw = ImageDraw.Draw(img) 
#base.png is now saved as img
#defines image, img is base.png
#defining all the fonts with standart windows fonts
bigfont =ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 50)
midfont =ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 35)
smallfont =ImageFont.truetype(r'C:\Windows\Fonts\ARIALN.TTF', 25)

#get user input
fname = input('Enter your first name : ')
lname = input('Enter your Last name : ')
job = input('Job Titel : ')
mail = input('Enter your E-Mail adress : ')
phone = input('Enter your Telephone number : ')
adr = input('Enter your adress : ')

#get user input

draw.text((390, 100),(fname),(tcolor),font=bigfont)
draw.text((390, 160),(lname),(tcolor),font=bigfont)
draw.text((390, 225),(job),(tcolor),font=midfont)
draw.text((390, 470),('MAIL : '),(tcolor),font=smallfont)
draw.text((460, 470),(mail),(tcolor),font=smallfont)
draw.text((390, 510),('TEL : '),(tcolor),font=smallfont)
draw.text((460, 510),(phone),(tcolor),font=smallfont)
draw.text((390, 550),('ADR : '),(tcolor),font=smallfont)
draw.text((460, 550),(adr),(tcolor),font=smallfont)

#safe backgound with text

img.save('BASE_edited.png')

#close it

img.close()
#-------------- open background , rotate write url, rotate back ----------------------------#
#The image rotates 90° 
#Then I apply ImageDraw to work on the image
#After that I define the font
#The user enters their data
#calculating the middle of the available space based on the user input
#pasting users text and rotate back to the original position
#open image
img1 = Image.open('base_edited.png')
#rotate 90°

img1 = img1.rotate (-90, PIL.Image.NEAREST, expand = 1) 

#loads imagedraw, open img1 "I open imagedraw and work on img1"
draw1 = ImageDraw.Draw(img1) 

#set new font for url
urlfont =ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 40)

#get user input for url
url = input('Enter your website adress : ')

urltext = url

#get the text size and font from row 102 and  define w and h
w, h = draw.textsize(urltext, font=urlfont)

#calculate middle of bg image for text position
x = (650 -w)/2
y = 120

#write user input on image
draw1.text((x,y), (urltext), (tcolor), font = urlfont)

#rotate back
img1 = img1.rotate(90, PIL.Image.NEAREST, expand = 1)

#-------------- delet temp files ----------------------------#

#program deletes the before generated files
os.remove('base.png')
os.remove('base_edited.png')

#-------------- show an save bussines card ----------------------------#

#the programm opens the generated business card in the defualt image viewer application
#and saves it in the background (same folder as the programm)

img1.show()
img1.save('bcg.png')
