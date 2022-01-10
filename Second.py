# Fill me in!
app.setMaxShapeCount(10000000000000)

Text01 = """Hello,
This is some sample text.
This took a really long time to make,
so I hope you like it!
Regards,
Dan

(P.S. What's your favourite show?
I'm currenty enjoying Scrubs.
it's somewhat akin to a doctor drama)"""

Text02 = """Kerning? What the heck is kerning?
Keming, Kerning, it's all the same."""

Text03 = """I can't leave blank lines.
 
 
Can I?





Hey I guess I can!"""

Text04 = "Is this really creative?"

Text05 = "Sphinx of Black Quartz; Judge My Vow!"

Text06 = """A B C D E F G H I J K L M
N O P Q R S T U V W X Y Z

a b c d e f g h i j k l m
n o p q r s t u v w x y z

! ? . , ( ) ;"""
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
    'I':"1110\n0100\n0100\n0100\n0100\n0100\n1110\n0000\n0000",
    'i':"0000\n0100\n0000\n1100\n0100\n0100\n1110\n0000\n0000",
    'J':"1111\n0001\n0001\n0001\n0001\n1001\n0110\n0000\n0000",
    'j':"0000\n0100\n0000\n1110\n0010\n0010\n0010\n1010\n0100",
    'K':"1001\n1001\n1010\n1100\n1010\n1001\n1001\n0000\n0000",
    'k':"1000\n1001\n1001\n1110\n1001\n1001\n1001\n0000\n0000",
    'L':"1000\n1000\n1000\n1000\n1000\n1000\n1111\n0000\n0000",
    'l':"1100\n0100\n0100\n0100\n0100\n0100\n1110\n0000\n0000",
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
    'T':"1110\n0100\n0100\n0100\n0100\n0100\n0100\n0000\n0000",
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
    'y':"0000\n0000\n0000\n1001\n1001\n0111\n0001\n0001\n1110",
    'Z':"1111\n0001\n0001\n0110\n1000\n1000\n1111\n0000\n0000",
    'z':"0000\n0000\n1111\n0001\n0110\n1000\n1111\n0000\n0000",
    ' ': "0000\n0000\n00000\n0000\n0000\n0000\n0000\n0000\n0000",
    '!':"0100\n0100\n0100\n0100\n0100\n0000\n0100\n0000\n0000",
    '?':"0110\n1001\n0001\n0010\n0100\n0000\n0100\n0000\n0000",
    '.':"0000\n0000\n0000\n0000\n0000\n0000\n1000\n0000\n0000",
    ',':"0000\n0000\n0000\n0000\n0000\n0000\n1000\n1000\n0000",
    "'":"1000\n1000\n0000\n0000\n0000\n0000\n0000\n0000\n0000",
    '(':"0001\n0010\n0010\n0010\n0010\n0010\n0001\n0000\n0000",
    ')':"1000\n0100\n0100\n0100\n0100\n0100\n1000\n0000\n0000",
    ';':"0000\n0000\n1000\n0000\n0000\n0000\n1000\n1000\n0000"
}
letterEncode1D = {}
letterEncode2D = {}
#Turn Map into Array of Lines
for key in letterMap:
    letterEncode1D[key] = letterMap[key].split('\n')

#Turn Map into 2D Array for Drawing
for k in letterEncode1D:
    a = []
    a.append(letterEncode1D[k])
    for l in range(len(a)):
        for m in range(len(a[l])):
            letterEncode2D.setdefault(k, [])
            letterEncode2D.get(k).append([x for x in a[l][m]])


colour = { #Turning Map Into Something Usable
    0:'white',
    1:'black'
}
    
    
def drawDoc(Text):
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
    letterHeight = 18
    lastLetterWidth = 8
    for w in range(len(encodedLetterArray)): #By Scentence
        for x in range(len(encodedLetterArray[w])): #By Letter
            for y in range(len(encodedLetterArray[w][x])): # By Letter Row
                for z in range(len(encodedLetterArray[w][x][y])): # By Letter Pixel
                    encodedLetterArray[w][x][y][z] = int(encodedLetterArray[w][x][y][z])
                    Rect(cx, cy, 2, 2, fill=colour[encodedLetterArray[w][x][y][z]])
                    lastLetterWidth = len(encodedLetterArray[w][x][y]) * 2
                    cx += 2
                cy += 2
                cx -= lastLetterWidth
            cy -= letterHeight
            cx += 10
        cy += letterHeight
        cx = 10
        
r = randrange(0, 20, 1)
print(r)
if(r == 0):
    drawDoc(Text01)
elif(r <= 11):
    drawDoc(Text02)
elif(r == 12):
    drawDoc(Text03)
elif(r == 13):
    drawDoc(Text04)
elif(r == 14):
    drawDoc(Text05)
elif(r >= 15):
    drawDoc(Text06)
