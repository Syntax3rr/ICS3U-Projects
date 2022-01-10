# Fill me in!
drawing01 = """00010000001000000000000
00121000012100000000000
00123111132100000000110
01322332322310000001221
01222222222210000001221
13222222222231111000131
12212212212223232100121
12422121224223232211131
12222222222222222221210
12222222222222222221210
12222222222222222222100
13222222222222222222100
13222222222222222222100
13222222222222222223100
01322222222222222231000
00132332322232332310000
00012112111112112100000
00011001100011001100000"""

drawing02 = """00000000000000000000000
00100000010000000000000
00110000011000000000000
00121111123100000000000
01322332322310000000110
01222222222210000001221
13222222222231111001221
12212212212223232100131
12422121224223232211321
12222222222222222221210
12222222222222222221210
12222222222222222222100
13222222222222222222100
13222222222222222222100
13222222222222222223100
01322222222222222231000
00132111211121112110000
00011001100011001100000"""

# Assign Numbers to a Colour
colour = { 
    0:'white',
    1:rgb(0, 0, 10),
    2:rgb(180, 180, 180),
    3:rgb(120, 120, 120),
    4:rgb(255, 120, 200)
}
    
    
    
def drawImage(drawing):
    #Split the String into an Array of Each Line
    drawLineArray = drawing.split('\n')  

    #Height and Width of the Final Image in Blocks
    pictureHeight = len(drawLineArray)
    pictureWidth = len(drawLineArray[0])

    #Canvas Size for Pictures with Different Aspect Ratios
    if (pictureHeight > pictureWidth):
        pixelSize = (400 - (400 % pictureHeight)) / pictureHeight
        canvasLeft = (400 - (pixelSize * pictureWidth)) / 2
        canvasTop = (400 - (pixelSize * pictureHeight)) / 2
    else:
        pixelSize = (400 - (400 % pictureWidth)) / pictureWidth
        canvasLeft = (400 - (pixelSize * pictureWidth)) / 2
        canvasTop = (400 - (pixelSize * pictureHeight)) / 2
    
    #Creating a 2D Array of each character in the drawing
    drawPixelArray = []
    for i in range(pictureHeight):
        drawPixelArray.append([x for x in drawLineArray[i]])
    
    ################Drawing the Image
    #Variables
    cy = canvasTop
    cx = canvasLeft
    Rect(0, 0, 400, 400)
    for y in range(len(drawPixelArray)):
        for x in range(len(drawPixelArray[0])):
            drawPixelArray[y][x]=int(drawPixelArray[y][x])
            Rect(cx, cy, pixelSize + 1, pixelSize +1, fill=colour[drawPixelArray[y][x]]) # +1 to prevent gaps
            cx += pixelSize
        cx = canvasLeft
        cy += pixelSize

n = random()
print(n)
if (n >= 0.5):
    drawImage(drawing01)
elif (n <= 0.4):
    drawImage(drawing02)
else:
    Circle(300, 140, 70, fill=colour[2]) # tail
    Circle(310, 140, 50, fill=colour[0])
    Polygon(365, 90, 215, 150, 280, 0, fill=colour[0])
    Circle(335, 120, 31, fill=colour[2])
   
    Circle(140, 140, 100, fill=colour[2]) #body
    Circle(250, 200, 80, fill=colour[2])
    Rect(40, 140, 30, 110, fill=colour[2])
    Circle(70, 250, 30, fill=colour[2])
    Rect(70, 120, 180, 160, fill=colour[2])
    
    Circle(95, 115, 8) #face
    Circle(165, 115, 8)
    Circle(138, 135, 10)
    Circle(123, 135, 10)
    Circle(138, 135, 5, fill=colour[2])
    Circle(123, 135, 5, fill=colour[2])
    Polygon(110, 140, 135, 60, 150, 140, 131, 130, fill=colour[2])
    
    Rect(235, 130, 20, 10, fill=colour[3])
    Circle(245, 140,10, fill=colour[3])
    Circle(245, 130, 10, fill=colour[3])
    Rect(265, 135, 20, 5, fill=colour[3])
    Circle(275, 140,10, fill=colour[3])
    Circle(275, 135, 10, fill=colour[3])
    
    Rect(115, 50, 10, 10, fill=colour[3])
    Circle(120, 60, 5, fill=colour[3])
    Circle(120, 52, 5, fill=colour[3])

    Rect(140, 49, 10, 10, fill=colour[3])
    Circle(145, 59, 5, fill=colour[3])
    Circle(145, 51, 5, fill=colour[3])
    x=65
    for j in range(4):
        Rect(x, 270, 30, 20, fill=colour[2])
        Circle(x + 15, 290, 15, fill=colour[2])
        x += 45
        if j == 1:
            x += 30
    Polygon(55, 90, 55, 35, 105, 50, fill=colour[2])
    Polygon(160, 50, 200, 30, 205, 65, fill=colour[2])
