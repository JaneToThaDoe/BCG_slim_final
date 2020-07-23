import PIL
import os #provides functions for interacting with the operating system
from PIL import ImageFont #PIL = Python Image Library, ImageFont = Loads every Font usable in Python
from PIL import ImageDraw #ImageDraw provides 2d graphics which can be created and edited
from PIL import Image #same as ImageDraw, working with images


#---------------------- welcome message and instructions ----------#
print("Hello !")
print("welcome to BCG the Bussinies card generator")
print(" ")
print(" ") #generating empty rows
print(" ")
print("please chose your color like this : red, orange, yellow, green, blue, violet ")
print(" ")
print(" ")
print(" ")

#-------------- let user choose colors --------------------#

#get user input
tcolor = input('Enter text color : ') #textcolor
bgcolor = input('Enter main color : ') #background color
fgcolor = input('Enter accent color : ') #foreground color

#-------------- create background ----------------------------#
#create white backgrund image
baseX, baseY = 1004, 650 # w x h in pixel,print size of a regular business card 85mm x 55mm , basex and basey = size of image
bg = Image.new('RGB', (baseX, baseY), (bgcolor)) #create new image for background using rgb colors and inputs from above
draw = ImageDraw.Draw(bg) #creates image, I use short form draw to simplify

#create accent image 
topX, topY = 333, 650 # w x h in pixel
top = Image.new('RGB', (topX, topY), (fgcolor)) # color
draw = ImageDraw.Draw(top)

#add accent on top of bg
bg.paste(top)

#save background as base.png
bg.save('BASE.png')

#close image
bg.close()
#image created
#first time saving file
#-------------- write user input on background ----------------------------#
#working on saved file
#open image
img = Image.open('BASE.png')
#base.png is now saved as img
#defines imagedraw, img referrs to base.png
#applying function imagedraw on img (which is base.png to be able to work on the image)
draw = ImageDraw.Draw(img) 

#defining all the fonts, using windows standard fonts
#set font big
bigfont = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 50)

#set font midle
middlefont = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 35)

#set font for samll text
font = ImageFont.truetype(r'C:\Windows\Fonts\ARIALN.TTF', 25)

#get user input
fname = input('Enter your first name : ')
lname = input('Enter your Last name : ')
job = input('Job Titel : ')
mail = input('Enter your E-Mail adress : ')
phone = input('Enter your Telephone number : ')
adr = input('Enter your adress : ')

#draw text on image
#after the user has entered their data, the program writes the given info to the
#defined places, the entered text, in the chosen color in the defined font size
draw.text((390, 100),(fname),(tcolor),font=bigfont)
draw.text((390, 160),(lname),(tcolor),font=bigfont)
draw.text((390, 225),(job),(tcolor),font=middlefont)
draw.text((390, 470),('MAIL : '),(tcolor),font=font)
draw.text((460, 470),(mail),(tcolor),font=font)
draw.text((390, 510),('TEL : '),(tcolor),font=font)
draw.text((460, 510),(phone),(tcolor),font=font)
draw.text((390, 550),('ADR : '),(tcolor),font=font)
draw.text((460, 550),(adr),(tcolor),font=font)

#save background with text
img.save('BASE_edited.png')

#close image
img.close()

#-------------- open background , rotate write url, rotate back ----------------------------#
#The image rotates 90° 
#Then I apply ImageDraw to work on the image
#After that I define the font
#The user enters their data
#calculating the middle of the available space based on the user input
#pasting users text and rotate back to the original position


#open image
img1 = Image.open('BASE_edited.png')

#rotate image 90°
img1 = img1.rotate(-90, PIL.Image.NEAREST, expand = 1)

#loads imagedraw, open img1 "I open imagedraw and work on img1"
draw1 = ImageDraw.Draw(img1)

#set font, has a different font size
urlfont = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 40)

#get user input for url
url = input('Enter your website adress : ')
urltext = url #user input as text

#get the text size and font from row 102 and  define w and h
w, h = draw.textsize(urltext, font=urlfont)

#calculate middle of bg image for text position
x = (650 - w)/2
y = 20

#write user input on image
draw1.text((x, y),(urltext), (tcolor),font=urlfont)

img1 = img1.rotate(90, PIL.Image.NEAREST, expand = 1)


#-------------- delet temp files ----------------------------#
#program deletes the before generated files

os.remove('BASE.png')
os.remove('BASE_edited.png')

#-------------- show an save bussines card ----------------------------#

#the programm opens the generated business card in the defualt image viewer application
#and saves it in the background (same folder as the programm)

img1.show()
img1.save('BCG.png')