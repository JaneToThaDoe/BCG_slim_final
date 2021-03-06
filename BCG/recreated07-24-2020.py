import PIL
import os #provides functions for interacting with the operating system
from PIL import ImageFont #PIL = Python Image Library, ImageFont = Loads every Font usable in Python
from PIL import ImageDraw #ImageDraw provides 2d graphics which can be created and edited
from PIL import Image #same as ImageDraw, working with images

#greeting user and giving instructions

print("Hi!")
print("")
print("")
print("Welcome to the Business Card Generator!")
print("")
print("")
print("Please chose your color like this: orange, yellow, red, white, blue, red, violet")
print("")
print("")
print("You will first chose your background color, then the text color and then the colored accent on your card. ")


#define input and give order

bgcolor=input('Enter your background color:')
tcolor=input('Enter your text color:')
acolor=input('Enter your accent color:')

#create background

baseX, baseY = 1004 , 650
bg=Image.new ('RGB', (baseX, baseY), (bgcolor))
draw = ImageDraw.Draw(bg)

#create accent image

topX, topY = 333 , 650
top=Image.new('RGB', (topX, topY), (acolor))
draw=ImageDraw.Draw(top)

#paste image on top of bg

bg.paste(top)

#save backgound as base.png
bg.save('base.png')

#close saved file
bg.close()

#working on saved file. open image

img=Image.open('base.png')

#base.png is now saved as img
#defines imagedraw, img referrs to base.png
#applying function imagedraw on img (which is base.png to be able to work on the image)
draw=ImageDraw.Draw(img)

#base.png is now saved as img
#defines image, img is base.png
#defining all the fonts with standart windows fonts
bigfont = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 50)
midfont = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 35)
smallfont = ImageFont.truetype(r'C:\Windows\Fonts\ARIALN.TTF', 25)
#urlfont = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 40)

fname = input('Enter your first name : ')
lname = input('Enter your Last name : ')
position = input('Enter your position : ')
mail = input('Enter your E-Mail adress : ')
phone = input('Enter your Telephone number : ')
adr = input('Enter your adress : ')

#get user input

draw.text((390, 100),(fname),(tcolor),font=bigfont)
draw.text((390, 160),(lname),(tcolor),font=bigfont)
draw.text((390, 225),(position),(tcolor),font=midfont)
draw.text((390, 470),('MAIL : '),(tcolor),font=smallfont)
draw.text((460, 470),(mail),(tcolor),font=smallfont)
draw.text((390, 510),('TEL : '),(tcolor),font=smallfont)
draw.text((460, 510),(phone),(tcolor),font=smallfont)
draw.text((390, 550),('ADR : '),(tcolor),font=smallfont)
draw.text((460, 550),(adr),(tcolor),font=smallfont)

#save backgound with text
img.save('BASE_edited.png')

#close it

img.close()

#rotate image 90° 

img1=Image.open('BASE_edited.png')
img1=img1.rotate(-90, PIL.Image.NEAREST, expand = 1 )


#Then I apply ImageDraw to work on the image
draw1=ImageDraw.Draw(img1)

urlfont = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 40)


#The user enters their data
url=input('Enter your URL:')

#write user input on image
#draw1.text((x,y), (url), (tcolor), font = urlfont)

#get the text size and font from row 102 and  define w and h
w, h = draw.textsize(url, font=urlfont)

#calculating the middle of the available space based on the user input
x = (650 -w)/2
y = 120

#write user input on image
draw1.text((x,y), (url), (tcolor), font = urlfont)

#pasting users text and rotate back to the original position
img1=img1.rotate(90, PIL.Image.NEAREST, expand = 1)

#program deletes the before generated files
os.remove('base.png')
os.remove('BASE_edited.png')


#the programm opens the generated business card in the defualt image viewer application
#and saves it in the background (same folder as the programm)

img1.show()
img1.save('bcg.png')

