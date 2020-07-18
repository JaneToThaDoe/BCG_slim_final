from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image 
import PIL
import os 


#---------------------- welcome message and instructions ----------#
print("Hello !")
print("welcome to BCG the Bussinies card generator")
print(" ")
print(" ")
print(" ")
print("pleas chose your color like this : red, orange, yellow, green, blue, violet ")
print(" ")
print(" ")
print(" ")

#-------------- let user choose colors --------------------#

#get user input
tcolor = input('Enter text color : ')
bgcolor = input('Enter main color : ')
fgcolor = input('Enter accent color : ')

#-------------- create background ----------------------------#
#creat white backgrund image
baseX, baseY = 1004, 650 # w x h in pixel
bg = Image.new('RGB', (baseX, baseY), (bgcolor)) # color
draw = ImageDraw.Draw(bg)

#creat accent image
topX, topY = 333, 650 # w x h in pixel
top = Image.new('RGB', (topX, topY), (fgcolor)) # color
draw = ImageDraw.Draw(top)

#add accent on top
bg.paste(top)

#save background
bg.save('BASE.png')

#close image
bg.close()

#-------------- write user input on background ----------------------------#

#open image
img = Image.open('BASE.png')

#defines imagedraw
draw = ImageDraw.Draw(img)


#set font big
bigfont = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 50)

#set font midle
middlefont = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 35)

#set font samll text
font = ImageFont.truetype(r'C:\Windows\Fonts\ARIALN.TTF', 25)

#get user input
fname = input('Enter your first name : ')
lname = input('Enter your Last name : ')
job = input('Job Titel : ')
mail = input('Enter your E-Mail adress : ')
phone = input('Enter your Telephone number : ')
adr = input('Enter your adress : ')

#draw text on image
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

#-------------- open background , roatte write url, rotate back ----------------------------#

#open image
img1 = Image.open('BASE_edited.png')

#rotate image 90 
img1 = img1.rotate(-90, PIL.Image.NEAREST, expand = 1)

#defines imagedraw
draw1 = ImageDraw.Draw(img1)

#set font
urlfont = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 40)

#text position
bounding_box = [650, 80, 0, 0]
x1, y1, x2, y2 = bounding_box  # For easy readin

#get user input for url#
url = input('Enter your website adress : ')
urltext = url

#get text size
w, h = draw.textsize(urltext, font=urlfont)

#calculate middle of bg image for text position
x = (x2 - x1 - w)/2 + x1
y = (y2 - y1 - h)/2 + y1

#write user input on imeage
draw1.text((x, y),(urltext), (tcolor),font=urlfont)

img1 = img1.rotate(90, PIL.Image.NEAREST, expand = 1)


#-------------- delet temp files ----------------------------#

#delete file
os.remove('BASE.png')

#delete file
os.remove('BASE_edited.png')

#-------------- show an save bussines card ----------------------------#

#save image#
img1.show()
img1.save('BCG.png')