# Fill me in!
# It seems that the 'global' keyword doesn't work, so I'm using Dicts as workarounds
app.setMaxShapeCount(10000000000000) # Set max shape count
app.background = None #initialize app.background for later

#Text messages, need a linebreak every 39 or so characters
Text01 = """Good day,
This is an edited, improved, and 
enhanced version of the text display
from the last creative assignment.

Changes include:
- Added numbers
- Added many more symbols
- Reduced pixel usage
- Created reusable pixels
- Added an option to change colours
- Added an option to change messages
- Changed the lowercase 'y' slightly
- Improved spacing of letters

Hold down mouse for dark mode!
Press the circle for the next text
Press the square to change text colour
"""

Text02 = """"Kerning is better than ever!

Letter consistency is still pretty 
bad though...
"""

Text03 = """
"Omae wa mou shindeiru"

"N-Nani?!"


      |\    _,,,---,,_
ZZZzz /,`.--'`'    -. ";-;;,__
     |,4-  ) )-,_. ,\ (  `'-'
     '---''(_/--'  `-'\_)
            Art by Felix Lee


Me: "You are the ; to my code <3"

Her: "I code in python"
"""

Text04 = """Go and collect some 
leaves and sticks and arrange
them into your favourite colour.

Blue, Red, Gree-

Green is not a creative colour!
"""

Text05 = """Sphinx of Black Quartz; Judge My Vow!

The quick brown fox jumps over the lazy dog

Cwm fjord bank glyphs vext quiz
"""

Text06 = """A B C D E F G H I J K L M

N O P Q R S T U V W X Y Z


a b c d e f g h i j k l m

n o p q r s t u v w x y z


1 2 3 4 5 6 7 8 9 0


! ? . , ( ) [ ] { } ; : - ' " 

/ | \\ ` _ < > + = """ 

# Create Mapping for Each Character
letterMap = { 
    'A':"0110\n1001\n1001\n1001\n1111\n1001\n1001\n0000\n0000",
    'a':"0000\n0000\n0110\n0001\n0111\n1001\n0111\n0000\n0000",
    'B':"1110\n1001\n1001\n1110\n1001\n1001\n1110\n0000\n0000",
    'b':"1000\n1000\n1000\n1110\n1001\n1001\n1110\n0000\n0000",
    'C':"0110\n1001\n1000\n1000\n1000\n1001\n0110\n0000\n0000",
    'c':"0000\n0000\n0110\n1001\n1000\n1001\n0110\n0000\n0000",
    'D':"1110\n1001\n1001\n1001\n1001\n1001\n1110\n0000\n0000",
    'd':"0001\n0001\n0001\n0111\n1001\n1001\n0111\n0000\n0000",
    'E':"1111\n1000\n1000\n1111\n1000\n1000\n1111\n0000\n0000",
    'e':"0000\n0000\n0110\n1001\n1111\n1000\n0111\n0000\n0000",
    'F':"1111\n1000\n1000\n1111\n1000\n1000\n1000\n0000\n0000",
    'f':"0110\n1001\n1000\n1110\n1000\n1000\n1000\n0000\n0000",
    'G':"0110\n1001\n1000\n1000\n1011\n1001\n0110\n0000\n0000",
    'g':"0000\n0000\n0000\n0111\n1001\n1001\n0111\n0001\n1110",
    'H':"1001\n1001\n1001\n1111\n1001\n1001\n1001\n0000\n0000",
    'h':"1000\n1000\n1000\n1110\n1001\n1001\n1001\n0000\n0000",
    'I':"111\n010\n010\n010\n010\n010\n111\n000\n000",
    'i':"000\n010\n000\n110\n010\n010\n111\n000\n000",
    'J':"1111\n0001\n0001\n0001\n0001\n1001\n0110\n0000\n0000",
    'j':"000\n010\n000\n111\n001\n001\n001\n101\n010",
    'K':"1001\n1001\n1010\n1100\n1010\n1001\n1001\n0000\n0000",
    'k':"1000\n1001\n1001\n1110\n1001\n1001\n1001\n0000\n0000",
    'L':"1000\n1000\n1000\n1000\n1000\n1000\n1111\n0000\n0000",
    'l':"110\n010\n010\n010\n010\n010\n111\n000\n000",
    'M':"10001\n11011\n10101\n10001\n10001\n10001\n10001\n00000\n00000",
    'm':"00000\n00000\n00000\n11110\n10101\n10101\n10101\n00000\n00000",
    'N':"1001\n1001\n1101\n1011\n1001\n1001\n1001\n0000\n0000",
    'n':"0000\n0000\n0000\n1110\n1001\n1001\n1001\n0000\n0000",
    'O':"0110\n1001\n1001\n1001\n1001\n1001\n0110\n0000\n0000",
    'o':"0000\n0000\n0000\n0110\n1001\n1001\n0110\n0000\n0000",
    'P':"1110\n1001\n1001\n1110\n1000\n1000\n1000\n0000\n0000",
    'p':"0000\n0000\n0000\n1110\n1001\n1001\n1110\n1000\n1000",
    'Q':"0110\n1001\n1001\n1001\n1001\n1010\n0101\n0000\n0000",
    'q':"0000\n0000\n0000\n0110\n1001\n1001\n0111\n0001\n0001",
    'R':"1110\n1001\n1001\n1110\n1010\n1001\n1001\n0000\n0000",
    'r':"0000\n0000\n0000\n1011\n1100\n1000\n1000\n0000\n0000",
    'S':"0111\n1000\n1000\n0110\n0001\n0001\n1110\n0000\n0000",
    's':"0000\n0000\n0111\n1000\n0110\n0001\n1110\n0000\n0000",
    'T':"111\n010\n010\n010\n010\n010\n010\n000\n000",
    't':"0100\n0100\n1111\n0100\n0100\n0101\n0010\n0000\n0000",
    'U':"1001\n1001\n1001\n1001\n1001\n1001\n0110\n0000\n0000",
    'u':"0000\n0000\n0000\n1001\n1001\n1001\n0111\n0000\n0000",
    'V':"10001\n10001\n10001\n10001\n10001\n01010\n00100\n00000\n00000",
    'v':"00000\n00000\n00000\n10001\n10001\n01010\n00100\n00000\n00000",
    'W':"10001\n10001\n10001\n10001\n10001\n10101\n01010\n00000\n00000",
    'w':"00000\n00000\n00000\n10001\n10001\n10101\n01010\n00000\n00000",
    'X':"1001\n1001\n1001\n0110\n1001\n1001\n1001\n0000\n0000",
    'x':"0000\n0000\n0000\n1001\n0110\n1001\n1001\n0000\n0000",
    'Y':"1001\n1001\n1001\n0111\n0001\n0001\n1110\n0000\n0000",
    'y':"0000\n0000\n0000\n1001\n1001\n0111\n0001\n1001\n0110",
    'Z':"1111\n0001\n0001\n0110\n1000\n1000\n1111\n0000\n0000",
    'z':"0000\n0000\n1111\n0001\n0110\n1000\n1111\n0000\n0000",
    '1':"11\n01\n01\n01\n01\n01\n01\n00\n00",
    '2':"0110\n1001\n0001\n0010\n0100\n1000\n1111\n0000\n0000",
    '3':"0110\n1001\n0001\n0010\n0001\n1001\n0110\n0000\n0000",
    '4':"0001\n0011\n0101\n1001\n1111\n0001\n0001\n0000\n0000",
    '5':"1111\n1000\n1000\n1110\n0001\n0001\n1110\n0000\n0000",    
    '6':"0110\n1001\n1000\n1110\n1001\n1001\n0110\n0000\n0000",
    '7':"1111\n0001\n0010\n0010\n0100\n0100\n1000\n0000\n0000",
    '8':"0110\n1001\n1001\n0110\n1001\n1001\n0110\n0000\n0000",
    '9':"0110\n1001\n1001\n0111\n0001\n0001\n0001\n0000\n0000",
    '0':"0110\n1001\n1011\n1101\n1001\n1001\n0110\n0000\n0000",
    '   ':"0000000000000000\n0000000000000000\n0000000000000000\n0000000000000000\n0000000000000000\n0000000000000000\n0000000000000000\n0000000000000000\n0000000000000000",
    ' ': "0000\n0000\n00000\n0000\n0000\n0000\n0000\n0000\n0000",
    '!':"0100\n0100\n0100\n0100\n0100\n0000\n0100\n0000\n0000",
    '?':"0110\n1001\n0001\n0010\n0100\n0000\n0100\n0000\n0000",
    '.':"00\n00\n00\n00\n00\n00\n10\n00\n00",
    ',':"00\n00\n00\n00\n00\n00\n10\n10\n00",
    "'":"10\n10\n00\n00\n00\n00\n00\n00\n00",
    '(':"0001\n0010\n0010\n0010\n0010\n0010\n0001\n0000\n0000",
    ')':"1000\n0100\n0100\n0100\n0100\n0100\n1000\n0000\n0000",
    ';':"00\n00\n00\n10\n00\n00\n10\n10\n00",
    ':':"00\n00\n00\n10\n00\n00\n10\n00\n00",
    '-':"000\n000\n000\n111\n000\n000\n000\n000\n000",
    '"':"101\n101\n000\n000\n000\n000\n000\n000\n000",
    '|':"10\n10\n10\n10\n10\n10\n10\n00\n00",
    '\\':"100\n100\n010\n010\n010\n001\n001\n000\n000",
    '/':"001\n001\n010\n010\n010\n100\n100\n000\n000",
    '`':"10\n01\n00\n00\n00\n00\n00\n00\n00",
    '_':"000\n000\n000\n000\n000\n000\n111\n000\n000",
    '<':"0000\n0010\n0100\n1000\n0100\n0010\n0000\n0000\n0000",
    '>':"0000\n0100\n0010\n0001\n0010\n0100\n0000\n0000\n0000",
    '=':"0000\n0000\n1111\n0000\n0000\n1111\n0000\n0000\n0000",
    '+':"00000\n00100\n00100\n11111\n00100\n00100\n00000\n00000\n00000",
    '{':"0001\n0010\n0010\n0100\n0010\n0010\n0001\n0000\n0000",
    '}':"1000\n0100\n0100\n0010\n0100\n0100\n1000\n0000\n0000",
    '[':"0011\n0010\n0010\n0010\n0010\n0010\n0011\n0000\n0000",
    ']':"1100\n0100\n0100\n0100\n0100\n0100\n1100\n0000\n0000"
}
#Initializing dicts
letterEncode1D = {}
letterEncode2D = {}
#Turn Map into Array of Lines
for j in letterMap:
    letterEncode1D[j] = letterMap[j].split('\n')

#Turn Map into 2D Array of each bit for Drawing
for k in letterEncode1D:
    a = [] #creates an array to temporarily store data
    a.append(letterEncode1D[k])
    for l in range(len(a)):
        for m in range(len(a[l])):
            letterEncode2D.setdefault(k, []) 
            letterEncode2D.get(k).append([x for x in a[l][m]])

colour = { #Turning Map Into Colours
    1:'black',
    2:'black',
    3:'red',
    4:'orange',
    5:'yellow',
    6:'green',
    7:'blue',
    8:'violet',
    9:gradient('red', 'orange', 'yellow', 'green', 'blue', 'violet', start='left-top'),
    0:3
}
    
pixels = {} #Create a list of the different pixels to be used

def drawDoc(Text):
    for n in range(len(pixels)):
        pixels[n+1].fill = 'white' 
        pixels[n+1].left = pixels[n+1].top = 0
    #Split the String into an Array of Each Line
    drawLineArray = Text.split('\n')  
     #Creating a 2D Array of each character in the drawing
    drawLetterArray = []
    for i in range(len(drawLineArray)):
        drawLetterArray.append([x for x in drawLineArray[i]])
    #Turning the letters into something drawable.
    encodedLetterArray = []
    for i in range(len(drawLetterArray)):
        encodedLetterArray.append([])
        for j in range(len(drawLetterArray[i])):
            encodedLetterArray[i].append([x for x in letterEncode2D[drawLetterArray[i][j]]])
    ################Drawing the Image
    #Variables
    cy = 10
    cx = 10
    maxPixels = 0
    pixelNo = 0
    letterHeight = 18
    lastLetterWidth = 8
    rainbow = False
    r = 255
    g = 0
    b = 0
    rNeg = False
    gNeg = False
    bNeg = False
    if(colour[1] == colour[9]): rainbow = True
    for w in range(len(encodedLetterArray)): #By Scentence
        for x in range(len(encodedLetterArray[w])): #By Letter
            if rainbow == True: #Create letter rainbow effect by adding and subtracting rgb values
                colour[1] = rgb(r, g, b)
                if b == 255 and g == 0: 
                    if r < 255: r += 15
                    rNeg = False
                elif g == 255 or rNeg == True: 
                    if r > 0: r -= 15
                    rNeg = True
                if r == 255 and b == 0:
                    if g < 255: g += 15
                    gNeg = False
                elif b == 255 or gNeg == True:
                    if g > 0: g -= 15
                    gNeg = True
                if g == 255 and r == 0:
                    if b < 255: b += 15
                    bNeg = False
                elif r == 255 or bNeg == True:
                    if b > 0: b -= 15
                    bNeg = True
            for y in range(len(encodedLetterArray[w][x])): # By Letter Row
                for z in range(len(encodedLetterArray[w][x][y])): # By Letter Pixel
                    encodedLetterArray[w][x][y][z] = int(encodedLetterArray[w][x][y][z]) #turns strings into numbers
                    if(encodedLetterArray[w][x][y][z] != 0): #if not whitespace, add a pixel
                        pixelNo += 1
                        if (pixelNo > len(pixels)): #if images need more pixels than available, add to cap and draw more
                            maxPixels = pixelNo
                            pixels[pixelNo] = Rect(0, 0, 2, 2, fill='white')
                        pixels[pixelNo].left = cx # Set positions and colour of pixels
                        pixels[pixelNo].top = cy
                        pixels[pixelNo].fill = colour[encodedLetterArray[w][x][y][z]]
                    lastLetterWidth = len(encodedLetterArray[w][x][y]) * 2 # find the width of the last letter
                    cx += 2 #shift over a pixel
                cy += 2 #shift down a row
                cx -= lastLetterWidth
            cy -= letterHeight #shift to next letter
            cx += lastLetterWidth + 2
        cy += letterHeight + 2 # shift to next line
        cx = 10
    if rainbow == True: colour[1] = colour[9]

#Creating the actual 'buttons' for colour and text changing
changeColour = Rect(375, 375, 25, 25, fill=colour[1])
colourL = Label('Colour', 350, 385, fill=colour[1])
changeText = Circle(15, 385, 20,  fill='black')
Label('Next', 50, 385)
drawDoc(Text01)
textNumber = {
    1:2
}

def onMousePress(mx, my): #Implementing the onClickEvent for the two changers
    if((mx - changeText.centerX) ** 2 + (my - changeText.centerY) ** 2 <= 20 ** 2): #onClickEvnet of circle
        drawDoc(eval('Text' + str(0) + str(textNumber[1])))
        if (textNumber[1] >= 6):
            textNumber[1] = 1
        else:
            textNumber[1] += 1
    elif(mx > 375 and my > 375): #onClickEvent of Square
        colour[1] = colour[colour[0]]
        if colour[0] >= 9:
            colour[0] = 2
        else:
            colour[0] += 1
        changeColour.fill = colour[1]
        colourL.fill = colour[1]
        drawDoc(eval('Text' + str(0) + str(textNumber[1]-1)))
    else: #General dark mode
        if colour[1] == 'black': colour[1] = 'white'
        app.background = 'black'
        drawDoc(eval('Text' + str(0) + str(textNumber[1] - 1)))
    if((colour[1] == colour[6]) and textNumber[1] == 5):
        colour[1] = colour[2]
        changeColour.fill = colourL.fill = colour[1]
        drawDoc("GREEN IS NOT CREATIVE")
def onMouseRelease(mx, my): #Return to normal after dark mode
    if app.background == 'black':
        colour[1] = colour[colour[0] - 1]
        app.background = None
        drawDoc(eval('Text' + str(0) + str(textNumber[1] - 1)))
    if((colour[1] == colour[6]) and textNumber[1] == 5):
        colour[1] = colour[2]
        changeColour.fill = colourL.fill = colour[1]
        drawDoc("GREEN IS NOT CREATIVE")
