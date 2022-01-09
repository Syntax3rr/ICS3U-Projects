# Fill me in!
import math
app.setMaxShapeCount(10000000000000) # Set max shape count
app.background = rgb(225,225,225) #set app.background to light grey
app.stepsPerSecond = 30 #tries to run at 30 fps
#All Global Variables
app.counterMenu = 0
app.counterMsgs = 0
app.counterMsgLen = 0
app.state = 'start'
app.menuSelect = -1
app.level = 0
app.blockSize = 0
app.canvasLeft = 0
app.canvasTop = 0
app.playerSpawn = Rect(0, 0, 1, 1, opacity = 0)
app.levelScrollX = False
app.levelScrollY = False
app.levelOffsetOn = False
app.levelOffsetX = 0
app.levelOffsetY = 0
app.levelOffsetMax = 600
app.points = Label(0, 15, 15, font='monospace', visible = False)
app.PGun = Group()
app.PGun.setting = None
app.bluePortal = app.orangePortal = None
app.PGun.blueShot = None
app.PGun.orangeShot = None
app.hp = Rect(0, 0, 1, 1, fill = rgb(255, 50, 50), opacity = 95)

app.info = Group(Rect(0, 0, 400, 400, fill = 'black', opacity = 80))

app.message = [
    "Welcome To My Game!",
    "This is Less of A Game",
    "And More of A Proof of Concept.",
    "Because of Time Restrictions,",
    "There are Still a Lot of Bugs",
    "And A Myriad of Issues,",
    "The Worst Of Which Is The Moving Bullet",
    "Which Causes Copious Amounts of Lag.",
    "Note: The Goal is to Leave the Level.",
    "Portals can be Placed on White Blocks.",
    "Use the Mouse to Look Around", 
    "and Click to Place Portals.", 
    "Hold Q and Use the Mouse to Scroll.",
    "Anyhow, Enjoy!",
    "To Start, Press Escape"]
    
app.msgLabels = [Label('', 200, 20, font='monospace', size = 20, bold = True,  fill = 'white'), 
Label('', 200, 60, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 80, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 120, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 140, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 160, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 180, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 200, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 240, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 260, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 280, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 300, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 320, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 340, font='monospace', size = 15,  fill = 'white'),
Label('', 200, 380, font='monospace', size = 15,  fill = 'white')]

for i in range(len(app.msgLabels)):
    app.info.add(app.msgLabels[i])

app.info.visible = False

app.escapeMenu = Group(
    Rect(0, 0, 400, 400, fill = 'white', opacity = 90),
    Label("Paused", 200, 56, size = 40, bold = True, font = 'monotype'),
    Rect(112, 112, 176, 56, fill = None, border = 'black'),
    Label("Continue", 200, 140, size = 20, font = 'monotype'),
    Rect(112, 170, 176, 56, fill = None, border = 'black'),
    Label("Controls", 200, 200, size = 20, font = 'monotype'),
    Rect(112, 228, 176, 56, fill = None, border = 'black'),
    Label("Level Select", 200, 258, size = 20, font = 'monotype'))
app.escapeMenu.select = Rect(112, 112, 176, 56, opacity = 10)
app.escapeMenu.add(app.escapeMenu.select)

app.escapeMenu.visible = False

app.currKeybinds = [
    ['w', 'up', 'space'], #up
    ['s', 'down'], #down
    ['a', 'left'], #left
    ['d', 'right'], #right
    ['f', '/'], #swtich
    ['g', '.'], #clear
    ['m', 'q'], #camera
    ['escape']] #escape

app.currKeybindsDisplay = [
    [Label(app.currKeybinds[0][0], 150, 100, font = 'monospace'), Label(app.currKeybinds[0][1], 250, 100, font = 'monospace'), Label(app.currKeybinds[0][2], 350, 100, font = 'monospace')],
    [Label(app.currKeybinds[1][0], 150, 140, font = 'monospace'), Label(app.currKeybinds[1][1], 250, 140, font = 'monospace')],
    [Label(app.currKeybinds[2][0], 150, 180, font = 'monospace'), Label(app.currKeybinds[2][1], 250, 180, font = 'monospace')],
    [Label(app.currKeybinds[3][0], 150, 220, font = 'monospace'), Label(app.currKeybinds[3][1], 250, 220, font = 'monospace')],
    [Label(app.currKeybinds[4][0], 150, 260, font = 'monospace'), Label(app.currKeybinds[4][1], 250, 260, font = 'monospace')],
    [Label(app.currKeybinds[5][0], 150, 300, font = 'monospace'), Label(app.currKeybinds[5][1], 250, 300, font = 'monospace')],
    [Label(app.currKeybinds[6][0], 150, 340, font = 'monospace'), Label(app.currKeybinds[6][1], 250, 340, font = 'monospace')],
    [Label(app.currKeybinds[7][0], 150, 380, font = 'monospace')]]

app.keybinding = Group(
    Rect(0, 0, 400, 400, fill = 'lightGrey', opacity = 90),
    Rect(100, 80, 400, 400, fill = 'white', opacity = 90),
    Line(100, 40, 100, 400),
    Line(200, 40, 200, 400),
    Line(300, 40, 300, 400),
    Label('C  O  N  T  R  O  L  S', 200, 20, font = 'monospace', bold = True, size = 25),
    Label('Action', 50, 60, font = 'monospace', size = 15),
    Label('Button 1', 150, 60, font = 'monospace', size = 15),
    Label('Button 2', 250, 60, font = 'monospace', size = 15),
    Label('Button 3', 350, 60, font = 'monospace', size = 15),
    Label('up', 50, 100, font = 'monospace'),
    Label('down', 50, 140, font = 'monospace'),
    Label('left', 50, 180, font = 'monospace'),
    Label('right', 50, 220, font = 'monospace'),
    Label('switch portals', 50, 260, font = 'monospace'),
    Label('clear portals', 50, 300, font = 'monospace'),
    Label('camera pan', 50, 340, font = 'monospace'),
    Label('escape', 50, 380, font = 'monospace'))

for i in range(9):
    app.keybinding.add(Line(0, 40 + 40 * i, 400, 40 + 40 * i))

for i in range(len(app.currKeybindsDisplay)):
    for j in range(len(app.currKeybindsDisplay[i])):
        app.keybinding.add(app.currKeybindsDisplay[i][j])

app.keybinding.visible = False

app.mouseX = 0
app.mouseY = 0
app.pressAnyKeyToStart = Label("Press Any Key To Start", 187.5, 330, size=25, font='monospace')

Menu = """##################################################################################################################
##oo###o##oo####oooo###oooo###oooooo#oooooo#oooooo#####oo###oo##oo#oo##oo###oo##oo#oooooo#oo##oo##################
##o#o#o#o#o#o###oooo###oooo###oooooo#oooooo#oooooo#####oo###oo##oo#oo##oo###oo##oo#oooooo#oo##oo##################
##oo##o#o#oo####oo##oo#oo##oo#oo#####oo#####oo#######oo##oo#ooo#oo#oo##oo###oo##oo#oo#####oo##oo##################
##o####o##o#o###oo##oo#oo##oo#oooo###oooooo#oooooo###oo##oo#ooo#oo###oo#####oooo###oooo#####oo####################
################oooo###oooo###oooo#######oo#####oo###oooooo#oo#ooo###oo#####oooo###oooo#####oo####################
##ooo##o##o#####oooo###oooo###oo#########oo#####oo###oooooo#oo#ooo###oo#####oo##oo#oo#######oo####################
###o##o#o#o#####oo#####oo##oo#oooooo#oooooo#oooooo###oo##oo#oo##oo###oo#####oo##oo#oooooo###oo####################
###o##ooo#o#####oo#####oo##oo#oooooo#oooooo#oooooo###oo##oo#oo##oo###oo#####oo##oo#oooooo###oo####################
###o##o#o#ooo#####################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################"""

Level00 = """###############################
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#ooooooooooooooooooooooooooooo#
#oooooooooooooooooooooooo@oooo#
#ooooooooooooooooooooooooooooo#
oooooooooooooooooooooooooooooo#
###############################"""

Level01 = """%%%%%%%%%%%%%%%%
%oooooooooooooo%
%oooooooooooooo%
%#ooooooooooooo%
ooooooooooooooo%
%%%ooo$oooooooo%
%oo$ooooooooooo%
%oooooooooooooo%
%oooooooooooooo%
%oooooooooooooo%
%oooooooooooooo%
%ooooooooooo$%o%
#oooooooooooooo%
#oooooooooooooo%
#o$oooooo%%oooo%
#oooooooooooooo%
#oooooooooooooo%
#oooooooooo#$oo#
#oooooooooo%%%o#
#oooooooooooooo%
#@ooooooooooooo%
#ooooooo$oooooo%
##wwwwww#wwwww##
################"""

Level02 = """##############%%%%%%%%%%%%%%%%
#oooooooooo##oooooooooooooooo%
#o@ooyoo$oooooooooooooooooooo%
#oooo$oooooooooooo%%%%%%%%%%o%
######wooooooooooo%###ooooooo%
#o$ooowooooooooooo%oooooooooo%
######w#####oooooo%oooooo#####
####oowooooooooooo%$ooooooooo#
####$#w#####oooooo%######oooo#
%$oooowooooooooooo%oooooooooo#
%ooooowooooooooooo%oooxooooo$#
##%%%owooooooooooo%ooooooo####
#ooooowooooooooooo%oo###ooooo#
#wwwwww#oooooooooo%ooooooooooo
#wwwwww########wwwwwwwwwwwwww#
##############################"""

# Save Mapping for the Level
currentLevelMap = []

# Create Mapping for The Character
Player = Group()

Player.XOld = 0
Player.YOld = 0

Player.dX = 0
Player.dY = 0
Player.dXOld = 0
Player.dYOld = 0

Player.rotateAngleOld = 0

Player.relX = 0
Player.relY = 0
Player.relXOld = 0
Player.relYOld = 0

Player.touchGround = False
Player.touchGroundOld = False

Player.touchCeiling = False
Player.touchCeilingOld = False

Player.touchLeft = False
Player.touchLeftOld = False

Player.touchRight = False
Player.touchRightOld = False

Player.maxSpeed = 500
Player.maxRun = 120
Player.maxJump = 100

Player.state = 'standing'

Player.lookAngle = 0 
Player.rotateAngle = 0

Player.widthPercent = 0.5
Player.heightPercent = 0.9
Player.jacket = 'orange'
Player.hp = 50

#Create a group of the entire level
antiList = {}
blockList = {}
acidList = {}
coinList = {}
dangerList = {}
currentLevelBlocks = Group()


def levelSelect():
    selection = app.getTextInput("Choose a level to go to: 0, 1, 2, or type 'custom' to make your own!")
    if(selection == '0'):
        onKeyPress(app.currKeybinds[7][0])
        drawLevel(Level00)
        drawPlayer()
        playerRespawn()
        onStep()
        onKeyPress(app.currKeybinds[5][0])
    elif(selection == '1'):
        onKeyPress(app.currKeybinds[7][0])
        drawLevel(Level01)
        drawPlayer()
        playerRespawn()
        onStep()
        onKeyPress(app.currKeybinds[5][0])
    elif(selection == '2'):
        onKeyPress(app.currKeybinds[7][0])
        drawLevel(Level02)
        drawPlayer()
        playerRespawn()
        onStep()
        onKeyPress(app.currKeybinds[5][0])
    elif(selection.lower() == 'custom'):
        mapOutput = ''
        mapInput = app.getTextInput("Type in a levelMap, seperating each line with a space. # is for a block, o is for air, % is for a no portal block, w is for acid, @ is for the spawnpoint, $ is for a coin (TIP. Design one in a word processor first) (WARNING: THIS MAY BREAK EVERYTHING IF YOU INPUT SOMETHING WRONG)   Ex. '###### #oooo# #o@oo# #oooo# ######'").rstrip(" \n  ")
        mapArray = mapInput.split(' ')
        for i in range(len(mapArray) - 1):
            mapOutput += mapArray[i] + '\n'
        mapOutput += mapArray[len(mapArray) -1]
        onKeyPress(app.currKeybinds[7][0])
        drawLevel(mapOutput)
        drawPlayer()
        playerRespawn()
        onStep()
        onKeyPress(app.currKeybinds[5][0])
    else: return 0

def drawPlayer():
    Player.clear()
    Player.add(Rect(0, 0, Player.widthPercent * app.blockSize, Player.heightPercent / 3 * app.blockSize, fill = 'white'))
    Player.add(Rect(0, Player.heightPercent / 3 * app.blockSize,  Player.widthPercent * app.blockSize, Player.heightPercent * 2 / 3 * app.blockSize, fill = Player.jacket))
    
    app.PGun.clear()
    app.PGun.add(Rect(Player.right, Player.centerY, app.blockSize * 0.3, app.blockSize * 0.2))
    app.PGun.setting = Rect(Player.right + app.blockSize * 0.18, Player.centerY, app.blockSize * 0.08, app.blockSize * 0.2, fill = rgb(0, 120, 255)) #rgb(250, 100, 0) rgb(0, 120, 255)
    app.PGun.add(app.PGun.setting) 

    app.bluePortal = Line(0, 0, app.blockSize, 0, fill = rgb(0, 150, 255), visible = False)
    app.orangePortal = Line(0, 0, app.blockSize, 0, fill = rgb(250, 100, 0), visible = False)
    app.bluePortal.dir = app.orangePortal.dir = None
    
    app.bluePortal.antiCollision = Group()
    app.bluePortal.antiCollision.clear()
    app.bluePortal.antiCollision.obj = Rect(app.blockSize * 0.2, 0, app.blockSize, app.blockSize * 1.2, fill = rgb(225, 225, 225))
    app.bluePortal.antiCollision.bottomBlock = Rect(app.blockSize * 0.2, app.blockSize * 1.2, app.blockSize, app.blockSize * 0.2, fill = 'white')
    app.bluePortal.antiCollision.leftBlock = Rect(0, app.blockSize * 0.2, app.blockSize * 0.2, app.blockSize, fill = 'white')
    app.bluePortal.antiCollision.rightBlock = Rect(app.blockSize * 1.2, app.blockSize * 0.2, app.blockSize * 0.2, app.blockSize, fill = 'white')
    app.bluePortal.antiCollision.add(app.bluePortal.antiCollision.obj)
    app.bluePortal.antiCollision.add(app.bluePortal.antiCollision.bottomBlock)
    app.bluePortal.antiCollision.add(app.bluePortal.antiCollision.leftBlock)
    app.bluePortal.antiCollision.add(app.bluePortal.antiCollision.rightBlock)
    
    app.orangePortal.antiCollision = Group()
    app.orangePortal.antiCollision.clear()
    app.orangePortal.antiCollision.obj = Rect(app.blockSize * 0.2, 0, app.blockSize, app.blockSize * 1.2, fill = rgb(225, 225, 225))
    app.orangePortal.antiCollision.bottomBlock = Rect(app.blockSize * 0.2, app.blockSize * 1.2, app.blockSize, app.blockSize * 0.2, fill = 'white')
    app.orangePortal.antiCollision.leftBlock = Rect(0, app.blockSize * 0.2, app.blockSize * 0.2, app.blockSize, fill = 'white')
    app.orangePortal.antiCollision.rightBlock = Rect(app.blockSize * 1.2, app.blockSize * 0.2, app.blockSize * 0.2, app.blockSize, fill = 'white')
    app.orangePortal.antiCollision.add(app.orangePortal.antiCollision.obj)
    app.orangePortal.antiCollision.add(app.orangePortal.antiCollision.bottomBlock)
    app.orangePortal.antiCollision.add(app.orangePortal.antiCollision.leftBlock)
    app.orangePortal.antiCollision.add(app.orangePortal.antiCollision.rightBlock)
    
    app.PGun.blueShot = Rect(0, 0, app.blockSize * 0.1, app.blockSize * 0.1, fill = rgb(0, 150, 255), opacity = 90, visible = False)
    app.PGun.orangeShot = Rect(0, 0, app.blockSize * 0.1, app.blockSize * 0.1, fill = rgb(250, 100, 0), opacity = 90, visible = False)
    app.PGun.blueShot.YOld = app.PGun.blueShot.XOld = None
    app.PGun.orangeShot.YOld = app.PGun.orangeShot.XOld = None
    currentLevelBlocks.add(app.bluePortal)
    currentLevelBlocks.add(app.orangePortal)
    
    currentLevelBlocks.add(app.bluePortal.antiCollision)
    app.bluePortal.antiCollision.visible = False
    
    currentLevelBlocks.add(app.orangePortal.antiCollision)
    app.orangePortal.antiCollision.visible = False

    Player.centerX = app.playerSpawn.centerX 
    Player.centerY = app.playerSpawn.centerY
    
    Player.relX = Player.centerX - currentLevelBlocks.centerX
    Player.relY = Player.centerY - currentLevelBlocks.centerY
    
    Player.maxSpeed = app.blockSize * 30
    Player.maxRun = app.blockSize * 5
    Player.maxJump = app.blockSize * 4
    
    app.hp.width = app.blockSize * 4
    app.hp.height = app.blockSize / 2
    app.hp.top = 0
    app.hp.right = 400
    app.hp.toBack()

def playerRespawn():
    Player.hp = 50
    
    Player.dX = Player.dY = 0
    Player.dXOld = Player.dYOld = 0
    
    Player.lookAngle = 0 
    Player.rotateAngle = 0
    Player.rotateAngleOld = 0
    
    Player.touchGround = False
    Player.touchGroundOld = False
    Player.touchCeiling = False
    Player.touchCeilingOld = False
    Player.touchLeft = False
    Player.touchLeftOld = False
    Player.touchRight = False
    Player.touchRightOld = False
    Player.state = 'standing'
    
    currentLevelBlocks.centerX += 200 - app.playerSpawn.centerX
    currentLevelBlocks.centerY += 200 - app.playerSpawn.centerY
    
    if(currentLevelBlocks.left > app.canvasLeft): currentLevelBlocks.left = app.canvasLeft
    if(currentLevelBlocks.right < 400 - app.canvasLeft): currentLevelBlocks.right = 400 - app.canvasLeft
    if(currentLevelBlocks.top > app.canvasTop): currentLevelBlocks.top = app.canvasLeft
    if(currentLevelBlocks.bottom < 400 - app.canvasTop): currentLevelBlocks.bottom = 400 - app.canvasTop
    Player.centerX = app.playerSpawn.centerX 
    Player.centerY = app.playerSpawn.centerY
    
    Player.relX = Player.centerX - currentLevelBlocks.centerX
    Player.relY = Player.centerY - currentLevelBlocks.centerY
    
    onKeyPress(app.currKeybinds[5][0])
    
def drawLevel(level):
    app.level = level
    currentLevelBlocks.clear()
    currentLevelMap = []
    app.playerSpawn.centerX = app.playerSpawn.centerY = 0
    
    #Split the String into an Array of Each Line
    drawLineArray = level.split('\n')  

    #Height and Width of the Final Image in Blocks
    levelHeight = len(drawLineArray)
    levelWidth = len(drawLineArray[0])
    
    #Canvas Size for levels with Different Aspect Ratios
    if(levelWidth > levelHeight): 
        app.blockSize = blockSize = (400 - (400 % levelHeight)) / levelHeight
    elif(levelWidth < levelHeight): 
        app.blockSize = blockSize = (400 - (400 % levelWidth)) / levelWidth
    else: 
        app.blockSize = blockSize = (400 - (400 % levelHeight)) / levelHeight

     #Creating a 2D Array of each character in the level
    for i in range(levelHeight):
        currentLevelMap.append([x for x in drawLineArray[i]])    
        
    if(blockSize < 20 and currentLevelMap[0][0] != 'U'):
        blockSize = 20
    
    if(levelWidth > levelHeight):
        canvasLeft = (400 - (blockSize * levelHeight)) / 2
        canvasTop = (400 - (blockSize * levelHeight)) / 2
    elif(levelWidth < levelHeight):
        canvasLeft = (400 - (blockSize * levelWidth)) / 2
        canvasTop = (400 - (blockSize * levelWidth)) / 2
    else:
        canvasLeft = 0
        canvasTop = 0
        
    app.canvasLeft = canvasLeft
    app.canvasTop = canvasTop
    
    ################Drawing the Image
    #Variables
    antiList.clear()
    blockList.clear()
    acidList.clear()
    coinList.clear()
    dangerList.clear()
    cy = canvasTop
    cx = canvasLeft
    blockNo = 0
    coinNo = 0
    coinMax = 0
    #Rect(0, 0, 400, 400)
    for a in range(len(currentLevelMap)):
        for b in range(len(currentLevelMap[a])):
            currBlock = currentLevelMap[a][b]
            #Detects what block to draw and what to do accordingly
            if(currBlock in ['#', 'U']):
                blockList[blockNo] = Rect(cx, cy, blockSize, blockSize, fill = 'white')
                currentLevelBlocks.add(blockList[blockNo])
            elif(currBlock == '%'):
                antiList[blockNo] = Rect(cx, cy, blockSize, blockSize, fill = 'darkGrey')
                currentLevelBlocks.add(antiList[blockNo])
            elif(currBlock == 'w'):
                if(currentLevelMap[a-1][b] == 'w' or currentLevelMap[a-1][b] == '#'):
                    acidList[blockNo] = Rect(cx, cy, blockSize, blockSize, fill = rgb(30,240,60))
                else:
                    acidList[blockNo] = Rect(cx, cy + blockSize * 0.3, blockSize, blockSize * 0.7, fill = rgb(30,240,60))
                currentLevelBlocks.add(acidList[blockNo])
            elif(currBlock == '$'):
                coin = Rect(cx + blockSize * 0.4, cy + blockSize * 0.3, blockSize * 0.2, blockSize * 0.4, fill="yellow")
                coin.startY = coin.centerY - (canvasTop + levelHeight/2 * blockSize)
                coin.startX = coin.centerX - (canvasLeft + levelWidth/ 2 * blockSize)
                coin.offset = (random() - 0.5) / 8
                coin.dir = randrange(-1, 2, 2)
                coin.centerY += coin.offset * blockSize
                coinList[blockNo] = coin
                currentLevelBlocks.add(coinList[blockNo])
            elif(currBlock == '@'):
                app.playerSpawn.centerX = cx + blockSize/2
                app.playerSpawn.centerY = cy + blockSize/2
                currentLevelBlocks.add(app.playerSpawn)
            elif(currBlock in ['x', 'y']):
                danger = Rect(cx + blockSize * 0.35, cy + blockSize * 0.35, blockSize * 0.3, blockSize * 0.3, fill = 'cyan', border = 'aqua', borderWidth = blockSize * 0.05)
                danger.spawnX = danger.centerX - (canvasLeft + len(currentLevelMap[0]) / 2 * blockSize)
                danger.spawnY = danger.centerY - (canvasTop + len(currentLevelMap) / 2 * blockSize)
                danger.XOld = danger.centerX
                danger.YOld = danger.centerY
                danger.dir = randrange(-1, 2, 2)
                if(currBlock == 'x'):
                    danger.dX = randrange(int(app.blockSize * 5), int(app.blockSize * 15))
                    danger.dY = 0
                    danger.spawnAxis = 'x'
                elif(currBlock == 'y'):
                    danger.dY = randrange(int(app.blockSize * 5), int(app.blockSize * 15))
                    danger.dX = 0
                    danger.spawnAxis = 'y'
                dangerList[blockNo] = danger
                currentLevelBlocks.add(danger)
            blockNo += 1
            cx += blockSize
        cx = canvasLeft
        cy += blockSize
    currentLevelBlocks.left = app.playerSpawn.centerX
    currentLevelBlocks.top =  app.playerSpawn.centerY
    if(currentLevelBlocks.left > 0): currentLevelBlocks.left = 0
    if(currentLevelBlocks.right < 400): currentLevelBlocks.right = 400
    if(currentLevelBlocks.top > 0): currentLevelBlocks.top = 0
    if(currentLevelBlocks.bottom < 400): currentLevelBlocks.bottom = 400
    
def updatePortalAntiCollision(portal, bypass):
    if(app.bluePortal.visible and app.orangePortal.visible and not portal.antiCollision.visible):
        if(portal.dir == 'bottom' and ((Player.top <= portal.bottom and Player.left > portal.left and Player.right < portal.right) or bypass == True)):
            portal.antiCollision.centerY = portal.centerY + app.blockSize / 2
            portal.antiCollision.centerX = portal.centerX
            portal.antiCollision.visible = True 
            portal.antiCollision.rotateAngle = 0
            if(portal == app.bluePortal and not bypass):
                updatePortalAntiCollision(app.orangePortal, True)
            elif(portal == app.orangePortal and not bypass): 
                updatePortalAntiCollision(app.bluePortal, True)
        elif(portal.dir == 'top' and ((Player.bottom >= portal.top and Player.left > portal.left and Player.right < portal.right) or bypass == True)):
            portal.antiCollision.centerY = portal.centerY - app.blockSize / 2
            portal.antiCollision.centerX = portal.centerX
            portal.antiCollision.visible = True
            portal.antiCollision.rotateAngle = 180
            if(portal == app.bluePortal and not bypass):
                updatePortalAntiCollision(app.orangePortal, True)
            elif(portal == app.orangePortal and not bypass): 
                updatePortalAntiCollision(app.bluePortal, True)
        elif(portal.dir == 'left' and ((Player.right >= portal.left and Player.bottom <= portal.bottom and Player.top > portal.top) or bypass == True)):
            portal.antiCollision.centerX = portal.centerX - app.blockSize / 2
            portal.antiCollision.centerY = portal.centerY
            portal.antiCollision.visible = True
            portal.antiCollision.rotateAngle = 90
            if(portal == app.bluePortal and not bypass):
                updatePortalAntiCollision(app.orangePortal, True)
            elif(portal == app.orangePortal and not bypass): 
                updatePortalAntiCollision(app.bluePortal, True)
        elif(portal.dir == 'right' and ((Player.left <= portal.right and Player.bottom <= portal.bottom and Player.top > portal.top) or bypass == True)):
            portal.antiCollision.centerX = portal.centerX + app.blockSize / 2
            portal.antiCollision.centerY = portal.centerY
            portal.antiCollision.visible = True
            portal.antiCollision.rotateAngle = 270
            if(portal == app.bluePortal and not bypass):
                updatePortalAntiCollision(app.orangePortal, True)
            elif(portal == app.orangePortal and not bypass): 
                updatePortalAntiCollision(app.bluePortal, True)
        else:
            portal.antiCollision.visible = False
        portal.antiCollision.toFront()
    
def collision(obj):
    if(obj == Player):
        Player.touchCeiling = False
        Player.touchGround = False
        Player.touchLeft = False
        Player.touchRight = False
        
        app.bluePortal.toFront()
        app.orangePortal.toFront()
        if(app.bluePortal.visible == True and app.orangePortal.visible == True):
            if(app.bluePortal.hitsShape(Player) and ((app.bluePortal.dir == 'bottom' and Player.centerY > app.bluePortal.centerY and Player.left > app.bluePortal.left and Player.right < app.bluePortal.right) or (app.bluePortal.dir == 'top' and Player.centerY < app.bluePortal.centerY and Player.left > app.bluePortal.left and Player.right < app.bluePortal.right) or (app.bluePortal.dir == 'left' and Player.centerX < app.bluePortal.centerX and Player.bottom <= app.bluePortal.bottom and Player.top > app.bluePortal.top) or (app.bluePortal.dir == 'right' and Player.centerX > app.bluePortal.centerX and Player.bottom <= app.bluePortal.bottom and Player.top > app.bluePortal.top))):
                playerPortalOffsetX = Player.centerX - app.bluePortal.centerX
                playerPortalOffsetY = Player.centerY - app.bluePortal.centerY
                Player.centerX = app.orangePortal.centerX
                Player.centerY = app.orangePortal.centerY
                Player.relX = Player.centerX - currentLevelBlocks.centerX
                Player.relY = Player.centerY - currentLevelBlocks.centerY
                updatePortalAntiCollision(app.bluePortal, False)
                if(app.bluePortal.dir == 'bottom'):
                    if(app.orangePortal.dir == 'bottom'):
                        Player.centerX += playerPortalOffsetX
                        Player.dY *= -1
                        Player.dY -= Player.dY * 0.08
                        Player.rotateAngle += 180
                    elif(app.orangePortal.dir == 'top'):
                        Player.centerX += playerPortalOffsetX
                    elif(app.orangePortal.dir == 'left'):
                        Player.centerY += playerPortalOffsetX
                        temp = Player.dX
                        Player.dX = Player.dY * 1.5
                        Player.dY = temp
                        Player.rotateAngle += 270
                    elif(app.orangePortal.dir == 'right'):
                        Player.centerY += playerPortalOffsetX
                        temp = Player.dX
                        Player.dX = -Player.dY * 1.5
                        Player.dY = temp
                        Player.rotateAngle += 90
                if(app.bluePortal.dir == 'top'):
                    if(app.orangePortal.dir == 'bottom'):
                        Player.centerX += playerPortalOffsetX
                    elif(app.orangePortal.dir == 'top'):
                        Player.centerX += playerPortalOffsetX
                        Player.dY *= -1
                        Player.rotateAngle += 180
                    elif(app.orangePortal.dir == 'left'):
                        Player.centerY += playerPortalOffsetX
                        temp = Player.dX
                        Player.dX = -Player.dY
                        Player.dY = temp
                        Player.rotateAngle += 90
                    elif(app.orangePortal.dir == 'right'):
                        Player.centerY += playerPortalOffsetX
                        temp = Player.dX
                        Player.dX = Player.dY
                        Player.dY = temp
                        Player.rotateAngle += 270
                if(app.bluePortal.dir == 'left'):
                    if(app.orangePortal.dir == 'bottom'):
                        Player.centerX += playerPortalOffsetY
                        temp = Player.dY
                        Player.dY = Player.dX
                        Player.dX = temp
                        Player.rotateAngle += 270
                    elif(app.orangePortal.dir == 'top'):
                        Player.centerX += playerPortalOffsetY
                        temp = Player.dY
                        Player.dY = -Player.dX
                        Player.dX = temp
                        Player.rotateAngle += 90
                    elif(app.orangePortal.dir == 'left'):
                        Player.centerY += playerPortalOffsetY
                        Player.dX *= -1
                    elif(app.orangePortal.dir == 'right'):
                        Player.centerY += playerPortalOffsetY
                if(app.bluePortal.dir == 'right'):
                    if(app.orangePortal.dir == 'bottom'):
                        Player.centerX += playerPortalOffsetY
                        temp = Player.dY
                        Player.dY = -Player.dX
                        Player.dX = temp
                        Player.rotateAngle += 90
                    elif(app.orangePortal.dir == 'top'):
                        Player.centerX += playerPortalOffsetY
                        temp = Player.dY
                        Player.dY = Player.dX
                        Player.dX = temp
                        Player.rotateAngle += 270
                    elif(app.orangePortal.dir == 'left'):
                        Player.centerY += playerPortalOffsetY
                    elif(app.orangePortal.dir == 'right'):
                        Player.centerY += playerPortalOffsetY
                        Player.dX *= -1
                        
            elif(app.orangePortal.hitsShape(Player) and ((app.orangePortal.dir == 'bottom' and Player.centerY > app.orangePortal.centerY and Player.left > app.orangePortal.left and Player.right < app.orangePortal.right) or (app.orangePortal.dir == 'top' and Player.centerY < app.orangePortal.centerY and Player.left > app.orangePortal.left and Player.right < app.orangePortal.right) or (app.orangePortal.dir == 'left' and Player.centerX < app.orangePortal.centerX and Player.bottom <= app.orangePortal.bottom and Player.top > app.orangePortal.top) or (app.orangePortal.dir == 'right' and Player.centerX > app.orangePortal.centerX and Player.bottom <= app.orangePortal.bottom and Player.top > app.orangePortal.top))):
                playerPortalOffsetX = Player.centerX - app.orangePortal.centerX
                playerPortalOffsetY = Player.centerY - app.orangePortal.centerY
                Player.centerX = app.bluePortal.centerX
                Player.centerY = app.bluePortal.centerY
                Player.relX = Player.centerX - currentLevelBlocks.centerX
                Player.relY = Player.centerY - currentLevelBlocks.centerY
                updatePortalAntiCollision(app.orangePortal, False)
                if(app.orangePortal.dir == 'bottom'):
                    if(app.bluePortal.dir == 'bottom'):
                        Player.centerX += playerPortalOffsetX
                        Player.dY *= -1
                        Player.dY -= Player.dY * 0.08
                        Player.rotateAngle += 180
                    elif(app.bluePortal.dir == 'top'):
                        Player.centerX += playerPortalOffsetX
                    elif(app.bluePortal.dir == 'left'):
                        Player.centerY += playerPortalOffsetX
                        temp = Player.dX
                        Player.dX = Player.dY * 1.5
                        Player.dY = temp
                        Player.rotateAngle += 270
                    elif(app.bluePortal.dir == 'right'):
                        Player.centerY += playerPortalOffsetX
                        temp = Player.dX
                        Player.dX = -Player.dY * 1.5
                        Player.dY = temp
                        Player.rotateAngle += 90
                if(app.orangePortal.dir == 'top'):
                    if(app.bluePortal.dir == 'bottom'):
                        Player.centerX += playerPortalOffsetX
                    elif(app.bluePortal.dir == 'top'):
                        Player.centerX += playerPortalOffsetX
                        Player.dY *= -1
                        Player.rotateAngle += 180
                    elif(app.bluePortal.dir == 'left'):
                        Player.centerY += playerPortalOffsetX
                        temp = Player.dX
                        Player.dX = -Player.dY
                        Player.dY = temp
                        Player.rotateAngle += 90
                    elif(app.bluePortal.dir == 'right'):
                        Player.centerY += playerPortalOffsetX
                        temp = Player.dX
                        Player.dX = Player.dY
                        Player.dY = temp
                        Player.rotateAngle += 270
                if(app.orangePortal.dir == 'left'):
                    if(app.bluePortal.dir == 'bottom'):
                        Player.centerX += playerPortalOffsetY
                        temp = Player.dY
                        Player.dY = Player.dX
                        Player.dX = temp
                        Player.rotateAngle += 270
                    elif(app.bluePortal.dir == 'top'):
                        Player.centerX += playerPortalOffsetY
                        temp = Player.dY
                        Player.dY = -Player.dX
                        Player.dX = temp
                        Player.rotateAngle += 90
                    elif(app.bluePortal.dir == 'left'):
                        Player.centerY += playerPortalOffsetY
                        Player.dX *= -1
                    elif(app.bluePortal.dir == 'right'):
                        Player.centerY += playerPortalOffsetY
                if(app.orangePortal.dir == 'right'):
                    if(app.bluePortal.dir == 'bottom'):
                        Player.centerX += playerPortalOffsetY
                        temp = Player.dY
                        Player.dY = -Player.dX
                        Player.dX = temp
                        Player.rotateAngle += 90
                    elif(app.bluePortal.dir == 'top'):
                        Player.centerX += playerPortalOffsetY
                        temp = Player.dY
                        Player.dY = Player.dX
                        Player.dX = temp
                        Player.rotateAngle += 270
                    elif(app.bluePortal.dir == 'left'):
                        Player.centerY += playerPortalOffsetY
                    elif(app.bluePortal.dir == 'right'):
                        Player.centerY += playerPortalOffsetY
                        Player.dX *= -1
                        
            updatePortalAntiCollision(app.bluePortal, False)    
            updatePortalAntiCollision(app.orangePortal, False)
                    
    elif(obj.fill == 'cyan'):
        if(app.bluePortal.visible == True and app.orangePortal.visible == True):
            if(app.bluePortal.hitsShape(obj)):
                objOffsetX = obj.centerX - app.bluePortal.centerX
                objOffsetY = obj.centerY - app.bluePortal.centerY
                
                obj.centerX = app.orangePortal.centerX
                obj.centerY = app.orangePortal.centerY
                if(app.bluePortal.dir == 'bottom'):
                    if(app.orangePortal.dir == 'bottom'):
                        obj.centerX += objOffsetX
                        obj.bottom = app.orangePortal.top - 1
                        obj.dY *= -1
                    elif(app.orangePortal.dir == 'top'):
                        obj.centerX += objOffsetX
                        obj.top = app.orangePortal.bottom + 1
                    elif(app.orangePortal.dir == 'left'):
                        obj.centerY += objOffsetX
                        obj.left = app.orangePortal.right + 1
                        temp = obj.dX
                        obj.dX = obj.dY
                        obj.dY = temp
                    elif(app.orangePortal.dir == 'right'):
                        obj.centerY += objOffsetX
                        obj.right = app.orangePortal.left - 1
                        temp = obj.dX
                        obj.dX = -obj.dY
                        obj.dY = temp
                if(app.bluePortal.dir == 'top'):
                    if(app.orangePortal.dir == 'bottom'):
                        obj.centerX += objOffsetX
                        obj.bottom = app.orangePortal.top - 1
                    elif(app.orangePortal.dir == 'top'):
                        obj.centerX += objOffsetX
                        obj.top = app.orangePortal.bottom + 1
                        obj.dY *= -1
                    elif(app.orangePortal.dir == 'left'):
                        obj.centerY += objOffsetX
                        obj.left = app.orangePortal.right + 1
                        temp = obj.dX
                        obj.dX = -obj.dY
                        obj.dY = temp
                    elif(app.orangePortal.dir == 'right'):
                        obj.centerY += objOffsetX
                        obj.right = app.orangePortal.left - 1
                        temp = obj.dX
                        obj.dX = obj.dY
                        obj.dY = temp
                if(app.bluePortal.dir == 'left'):
                    if(app.orangePortal.dir == 'bottom'):
                        obj.centerX += objOffsetY
                        obj.bottom = app.orangePortal.top - 1
                        temp = obj.dY
                        obj.dY = obj.dX
                        obj.dX = temp
                    elif(app.orangePortal.dir == 'top'):
                        obj.centerX += objOffsetY
                        obj.top = app.orangePortal.bottom + 1
                        temp = obj.dY
                        obj.dY = -obj.dX
                        obj.dX = temp
                    elif(app.orangePortal.dir == 'left'):
                        obj.centerY += objOffsetY
                        obj.left = app.orangePortal.right + 1
                        obj.dX *= -1
                    elif(app.orangePortal.dir == 'right'):
                        obj.centerY += objOffsetY
                        obj.right = app.orangePortal.left - 1
                if(app.bluePortal.dir == 'right'):
                    if(app.orangePortal.dir == 'bottom'):
                        obj.centerX += objOffsetY
                        obj.bottom = app.orangePortal.top - 1
                        temp = obj.dY
                        obj.dY = -obj.dX
                        obj.dX = temp
                    elif(app.orangePortal.dir == 'top'):
                        obj.centerX += objOffsetY
                        obj.top = app.orangePortal.bottom + 1
                        temp = obj.dY
                        obj.dY = obj.dX
                        obj.dX = temp
                    elif(app.orangePortal.dir == 'left'):
                        obj.centerY += objOffsetY
                        obj.left = app.orangePortal.right + 1
                    elif(app.orangePortal.dir == 'right'):
                        obj.centerY += objOffsetY
                        obj.right = app.orangePortal.left - 1
                        obj.dX *= -1
                        
            elif(app.orangePortal.hitsShape(obj)):
                objOffsetX = obj.centerX - app.orangePortal.centerX
                objOffsetY = obj.centerY - app.orangePortal.centerY
                
                obj.centerX = app.bluePortal.centerX
                obj.centerY = app.bluePortal.centerY
                if(app.orangePortal.dir == 'bottom'):
                    if(app.bluePortal.dir == 'bottom'):
                        obj.centerX += objOffsetX
                        obj.bottom = app.bluePortal.top - 1
                        obj.dY *= -1
                    elif(app.bluePortal.dir == 'top'):
                        obj.centerX += objOffsetX
                        obj.top = app.bluePortal.bottom + 1
                    elif(app.bluePortal.dir == 'left'):
                        obj.centerY += objOffsetX
                        obj.left = app.bluePortal.right + 1
                        temp = obj.dX
                        obj.dX = obj.dY
                        obj.dY = temp
                    elif(app.bluePortal.dir == 'right'):
                        obj.centerY += objOffsetX
                        obj.right = app.bluePortal.left - 1
                        temp = obj.dX
                        obj.dX = -obj.dY
                        obj.dY = temp
                if(app.orangePortal.dir == 'top'):
                    if(app.bluePortal.dir == 'bottom'):
                        obj.centerX += objOffsetX
                        obj.bottom = app.bluePortal.top - 1
                    elif(app.bluePortal.dir == 'top'):
                        obj.centerX += objOffsetX
                        obj.top = app.bluePortal.bottom + 1
                        obj.dY *= -1
                    elif(app.bluePortal.dir == 'left'):
                        obj.centerY += objOffsetX
                        obj.left = app.bluePortal.right + 1
                        temp = obj.dX
                        obj.dX = -obj.dY
                        obj.dY = temp
                    elif(app.bluePortal.dir == 'right'):
                        obj.centerY += objOffsetX
                        obj.right = app.bluePortal.left - 1
                        temp = obj.dX
                        obj.dX = obj.dY
                        obj.dY = temp
                if(app.orangePortal.dir == 'left'):
                    if(app.bluePortal.dir == 'bottom'):
                        obj.centerX += objOffsetY
                        obj.bottom = app.bluePortal.top - 1
                        temp = obj.dY
                        obj.dY = obj.dX
                        obj.dX = temp
                    elif(app.bluePortal.dir == 'top'):
                        obj.centerX += objOffsetY
                        obj.top = app.bluePortal.bottom + 1
                        temp = obj.dY
                        obj.dY = -obj.dX
                        obj.dX = temp
                    elif(app.bluePortal.dir == 'left'):
                        obj.centerY += objOffsetY
                        obj.left = app.bluePortal.right + 1
                        obj.dX *= -1
                    elif(app.bluePortal.dir == 'right'):
                        obj.centerY += objOffsetY
                        obj.right = app.bluePortal.left - 1
                if(app.orangePortal.dir == 'right'):
                    if(app.bluePortal.dir == 'bottom'):
                        obj.centerX += objOffsetY
                        obj.bottom = app.bluePortal.top - 1
                        temp = obj.dY
                        obj.dY = -obj.dX
                        obj.dX = temp
                    elif(app.bluePortal.dir == 'top'):
                        obj.centerX += objOffsetY
                        obj.top = app.bluePortal.bottom + 1
                        temp = obj.dY
                        obj.dY = obj.dX
                        obj.dX = temp
                    elif(app.bluePortal.dir == 'left'):
                        obj.centerY += objOffsetY
                        obj.left = app.bluePortal.right + 1
                    elif(app.bluePortal.dir == 'right'):
                        obj.centerY += objOffsetY
                        obj.right = app.bluePortal.left - 1
                        obj.dX *= -1
        obj.visibleOld = obj.visible
        currentLevelBlocks.remove(obj)
    
    for i in range(int(obj.width + 1)): #bottom
        bottomBlock = currentLevelBlocks.hitTest(obj.left + i, obj.bottom)
        if(bottomBlock == app.bluePortal.antiCollision):
            bottomBlock = app.bluePortal.antiCollision.hitTest(obj.left + i, obj.bottom)
        elif(bottomBlock == app.orangePortal.antiCollision):
            bottomBlock = app.orangePortal.antiCollision.hitTest(obj.left + i, obj.bottom)
        if(bottomBlock != None):
            if(obj == Player):
                if(bottomBlock in [app.bluePortal, app.orangePortal]):
                    if(app.bluePortal.visible != app.orangePortal.visible):
                        if(Player.YOld <= bottomBlock.top):
                            Player.touchGround = True
                            Player.bottom = bottomBlock.top
                            Player.relY = Player.centerY - currentLevelBlocks.centerY
                        if(Player.dYOld > 0):
                            Player.dY = 0
                if(bottomBlock.fill in ["white", "darkGrey"]):
                    if(Player.YOld <= bottomBlock.top):
                        Player.touchGround = True
                        Player.bottom = bottomBlock.top
                        Player.relY = Player.centerY - currentLevelBlocks.centerY
                        if(Player.dYOld > 0):
                            Player.dY = 0
                if(bottomBlock.fill == rgb(30, 240, 60)):
                    Player.hp -= 100 / app.stepsPerSecond
                if(bottomBlock.fill == 'cyan'):
                    Player.hp -= 25
                    bottomBlock.visible = False
                    bottomBlock.cooldown = randrange(1, 4)
                if(bottomBlock.fill == 'yellow'):
                    app.points.value += 50
                    if(Player.hp <= 45):
                        Player.hp += 5
                    elif(Player.hp != 50):
                        Player.hp == 50
                    currentLevelBlocks.remove(bottomBlock)
            elif(obj in [app.PGun.blueShot, app.PGun.orangeShot]):
                if(bottomBlock.fill == 'white'):
                    if(obj.YOld <= bottomBlock.top or (obj.YOld == None and Player.YOld <= bottomBlock.top)):
                        obj.dX = obj.dY = 0
                        obj.bottom = bottomBlock.top - 1
                        obj.visible = False
                        for j in range(int((app.blockSize + 1) // 2)):
                            for k in [1, -1]:
                                test1 = currentLevelBlocks.hitTest(obj.centerX - app.blockSize // 2  + (j * k), obj.bottom + 1)
                                test2 = currentLevelBlocks.hitTest(obj.centerX + app.blockSize // 2  + (j * k), obj.bottom + 1)
                                test3 = currentLevelBlocks.hitTest(obj.centerX - app.blockSize // 2  + (j * k), obj.bottom - 1)
                                test4 = currentLevelBlocks.hitTest(obj.centerX + app.blockSize // 2  + (j * k), obj.bottom - 1)
                                if(test1 != None and test2 != None):
                                    if(test1.fill in ['white', obj.fill] and test2.fill in ['white', obj.fill]):
                                        if((test3 in [None, app.bluePortal, app.orangePortal] or test3.fill == 'cyan') and (test4 in [None, app.bluePortal, app.orangePortal] or test4.fill == 'cyan')):
                                            if(obj == app.PGun.blueShot and test3 != app.orangePortal and test4 != app.orangePortal):
                                                app.bluePortal.x1 = obj.centerX - app.blockSize // 2  + (j * k)
                                                app.bluePortal.x2 = obj.centerX + app.blockSize // 2  + (j * k)
                                                app.bluePortal.y1 = app.bluePortal.y2 = bottomBlock.top + 1
                                                app.bluePortal.dir = 'bottom'
                                                app.bluePortal.visible = True
                                            elif(obj == app.PGun.orangeShot and test3 != app.bluePortal and test4 != app.bluePortal):
                                                app.orangePortal.x1 = obj.centerX - app.blockSize // 2  + (j * k)
                                                app.orangePortal.x2 = obj.centerX + app.blockSize // 2  + (j * k)
                                                app.orangePortal.y1 = app.orangePortal.y2 = bottomBlock.top + 1
                                                app.orangePortal.dir = 'bottom'
                                                app.orangePortal.visible = True
                                            break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                elif(bottomBlock.fill in ["darkGrey", "pink"]):
                    obj.dX = obj.dY = 0
                    obj.visible = False
                    break
            elif(obj.fill == 'cyan'):
                if((bottomBlock.fill in ['white', 'darkGrey'] or (bottomBlock in [app.bluePortal, app.orangePortal] and app.bluePortal.visible != app.orangePortal.visible)) and obj.YOld <= bottomBlock.top):
                    obj.bottom = bottomBlock.top - 1
                    obj.dir = -1
                elif(bottomBlock.fill == rgb(30, 240, 60)):
                    obj.visibleOld = False
                    obj.cooldown = randrange(1, 4)
                    app.points.value += 10
                elif(bottomBlock.fill == 'cyan'):
                    obj.visibleOld = False
                    obj.cooldown = -100
                    bottomBlock.visible = False
                    bottomBlock.cooldown = -100
                    app.points.value += 30
                    
    for i in range(int(obj.height + 1)): #left
        leftBlock = currentLevelBlocks.hitTest(obj.left, obj.top + i)
        if(leftBlock == app.bluePortal.antiCollision):
            leftBlock = app.bluePortal.antiCollision.hitTest(obj.left, obj.top + i)
        elif(leftBlock == app.orangePortal.antiCollision):
            leftBlock = app.orangePortal.antiCollision.hitTest(obj.left, obj.top + i)
        if(leftBlock != None):
            if(obj == Player):
                if(leftBlock in [app.bluePortal, app.orangePortal]):
                    if(app.bluePortal.visible != app.orangePortal.visible):
                        if(Player.XOld > leftBlock.right):
                            Player.touchLeft = True
                            Player.left = leftBlock.right
                            Player.relX = Player.centerX - currentLevelBlocks.centerX
                        if(Player.dXOld < 0):
                            Player.dX = 0
                if(leftBlock.fill in ["white", "darkGrey"]):
                    if(Player.XOld > leftBlock.right):
                        Player.touchLeft = True
                        Player.left = leftBlock.right
                        Player.relX = Player.centerX - currentLevelBlocks.centerX
                        if(Player.dXOld < 0):
                            Player.dX = 0
                if(leftBlock.fill == rgb(30, 240, 60)):
                    Player.hp -= 100 / app.stepsPerSecond
                if(leftBlock.fill == 'cyan'):
                    Player.hp -= 25
                    leftBlock.visible = False
                    leftBlock.cooldown = randrange(1, 4)
                if(leftBlock.fill == 'yellow'):
                    app.points.value += 50
                    currentLevelBlocks.remove(leftBlock)
                    if(Player.hp <= 45):
                        Player.hp += 5
                    elif(Player.hp != 50):
                        Player.hp == 50
            elif(obj in [app.PGun.blueShot, app.PGun.orangeShot]):
                if(leftBlock.fill == 'white'):
                    if(obj.XOld > leftBlock.right or (obj.XOld == None and Player.XOld > leftBlock.right)):
                        obj.dX = obj.dY = 0
                        obj.left = leftBlock.right + 1
                        obj.visible = False
                        for j in range(int((app.blockSize + 1) // 2)):
                            for k in [1, -1]:
                                test1 = currentLevelBlocks.hitTest(leftBlock.right - 1, obj.centerY - app.blockSize // 2  + (j * k))
                                test2 = currentLevelBlocks.hitTest(leftBlock.right - 1, obj.centerY + app.blockSize // 2  + (j * k))
                                test3 = currentLevelBlocks.hitTest(leftBlock.right + 1, obj.centerY - app.blockSize // 2  + (j * k))
                                test4 = currentLevelBlocks.hitTest(leftBlock.right + 1, obj.centerY + app.blockSize // 2  + (j * k))
                                if(test1 != None and test2 != None):
                                    if(test1.fill in ['white', obj.fill] and test2.fill in ['white', obj.fill]):
                                        if((test3 in [None, app.bluePortal, app.orangePortal] or test3.fill == 'cyan') and (test4 in [None, app.bluePortal, app.orangePortal] or test4.fill == 'cyan')):
                                            if(obj == app.PGun.blueShot and test3 != app.orangePortal and test4 != app.orangePortal):
                                                app.bluePortal.y1 = obj.centerY - app.blockSize // 2  + (j * k)
                                                app.bluePortal.y2 = obj.centerY + app.blockSize // 2  + (j * k)
                                                app.bluePortal.x1 = app.bluePortal.x2 = leftBlock.right
                                                app.bluePortal.dir = 'left'
                                                app.bluePortal.visible = True
                                            if(obj == app.PGun.orangeShot and test3 != app.bluePortal and test4 != app.bluePortal):
                                                app.orangePortal.y1 = obj.centerY - app.blockSize // 2  + (j * k)
                                                app.orangePortal.y2 = obj.centerY + app.blockSize // 2  + (j * k)
                                                app.orangePortal.x1 = app.orangePortal.x2 = leftBlock.right
                                                app.orangePortal.dir = 'left'
                                                app.orangePortal.visible = True
                                            break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                if(leftBlock.fill in ["darkGrey", "pink"]):
                    obj.dX = obj.dY = 0
                    obj.visible = False
                    break
            elif(obj.fill == 'cyan'):
                if((leftBlock.fill in ['white', 'darkGrey'] or (leftBlock in [app.bluePortal, app.orangePortal] and app.bluePortal.visible != app.orangePortal.visible)) and obj.XOld > leftBlock.right):
                    obj.left = leftBlock.right + 1
                    obj.dir = 1
                elif(leftBlock.fill == rgb(30, 240, 60)):
                    obj.visibleOld = False
                    obj.cooldown = randrange(1, 4)
                    app.points.value += 10
                elif(leftBlock.fill == 'cyan'):
                    obj.visibleOld = False
                    obj.cooldown = -100
                    leftBlock.visible = False
                    leftBlock.cooldown = -100
                    app.points.value += 30
                    
    for i in range(int(obj.height + 1)): #right
        rightBlock = currentLevelBlocks.hitTest(obj.right, obj.top + i)
        if(rightBlock == app.bluePortal.antiCollision):
            rightBlock = app.bluePortal.antiCollision.hitTest(obj.right, obj.top + i)
        elif(rightBlock == app.orangePortal.antiCollision):
            rightBlock = app.orangePortal.antiCollision.hitTest(obj.right, obj.top + i)
        if(rightBlock != None):
            if(obj == Player):
                if(rightBlock in [app.bluePortal, app.orangePortal]):
                    if(app.bluePortal.visible != app.orangePortal.visible):
                        if(Player.XOld < rightBlock.left):
                            Player.touchRight = True
                            Player.right = rightBlock.left
                            Player.relX = Player.centerX - currentLevelBlocks.centerX
                        if(Player.dXOld > 0):
                            Player.dX = 0
                if(rightBlock.fill in ["white", "darkGrey"]):
                    if(Player.XOld < rightBlock.left):
                        Player.touchRight = True
                        Player.right = rightBlock.left
                        Player.relX = Player.centerX - currentLevelBlocks.centerX
                        if(Player.dX > 0):
                            Player.dX = 0
                if(rightBlock.fill == rgb(30, 240, 60)):
                    Player.hp -= 100 / app.stepsPerSecond
                if(rightBlock.fill == 'cyan'):
                    Player.hp -= 25
                    rightBlock.visible = False
                    rightBlock.cooldown = randrange(1, 4)
                if(rightBlock.fill == 'yellow'):
                    app.points.value += 50
                    currentLevelBlocks.remove(rightBlock)
                    if(Player.hp <= 45):
                        Player.hp += 5
                    elif(Player.hp != 50):
                        Player.hp == 50
            elif(obj in [app.PGun.blueShot, app.PGun.orangeShot]):
                if(rightBlock.fill == 'white'):
                    if(obj.XOld < rightBlock.left or (obj.XOld == None and Player.XOld < rightBlock.left)):
                        obj.dX = obj.dY = 0
                        obj.right = rightBlock.left - 1
                        obj.visible = False
                        for j in range(int((app.blockSize + 1) // 2)):
                            for k in [1, -1]:
                                test1 = currentLevelBlocks.hitTest(rightBlock.left + 1, obj.centerY - app.blockSize // 2  + (j * k))
                                test2 = currentLevelBlocks.hitTest(rightBlock.left + 1, obj.centerY + app.blockSize // 2  + (j * k))
                                test3 = currentLevelBlocks.hitTest(rightBlock.left - 1, obj.centerY - app.blockSize // 2  + (j * k))
                                test4 = currentLevelBlocks.hitTest(rightBlock.left - 1, obj.centerY + app.blockSize // 2  + (j * k))
                                if(test1 != None and test2 != None):
                                    if(test1.fill in ['white', obj.fill] and test2.fill in ['white', obj.fill]):
                                        if((test3 in [None, app.bluePortal, app.orangePortal] or test3.fill == 'cyan') and (test4 in [None, app.bluePortal, app.orangePortal] or test4.fill == 'cyan')):
                                            if(obj == app.PGun.blueShot and test3 != app.orangePortal and test4 != app.orangePortal):
                                                app.bluePortal.y1 = obj.centerY - app.blockSize // 2  + (j * k)
                                                app.bluePortal.y2 = obj.centerY + app.blockSize // 2  + (j * k)
                                                app.bluePortal.x1 = app.bluePortal.x2 = rightBlock.left
                                                app.bluePortal.dir = 'right'
                                                app.bluePortal.visible = True
                                            if(obj == app.PGun.orangeShot and test3 != app.bluePortal and test4 != app.bluePortal):
                                                app.orangePortal.y1 = obj.centerY - app.blockSize // 2  + (j * k)
                                                app.orangePortal.y2 = obj.centerY + app.blockSize // 2  + (j * k)
                                                app.orangePortal.x1 = app.orangePortal.x2 = rightBlock.left
                                                app.orangePortal.dir = 'right'
                                                app.orangePortal.visible = True
                                            break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                if(rightBlock.fill in ["darkGrey", "pink"]):
                    obj.dX = obj.dY = 0
                    obj.visible = False
                    break
            elif(obj.fill == 'cyan'):
                if((rightBlock.fill in ['white', 'darkGrey'] or (rightBlock in [app.bluePortal, app.orangePortal] and app.bluePortal.visible != app.orangePortal.visible)) and obj.XOld < rightBlock.left):
                    obj.right = rightBlock.left - 1
                    obj.dir = -1
                elif(rightBlock.fill == rgb(30, 240, 60)):
                    obj.visibleOld = False
                    obj.cooldown = randrange(1, 4)
                    app.points.value += 10
                elif(rightBlock.fill == 'cyan'):
                    obj.visibleOld = False
                    obj.cooldown = -100
                    rightBlock.visible = False
                    rightBlock.cooldown = -100
                    app.points.value += 30

    for i in range(int(obj.width + 1)): #top
        topBlock = currentLevelBlocks.hitTest(obj.left + i, obj.top - 1)
        if(topBlock == app.bluePortal.antiCollision):
            topBlock = app.bluePortal.antiCollision.hitTest(obj.left + i, obj.top - 1)
        if(topBlock == app.orangePortal.antiCollision):
            topBlock = app.orangePortal.antiCollision.hitTest(obj.left + i, obj.top - 1)
        if(topBlock != None):
            if(obj == Player):
                if(topBlock in [app.bluePortal, app.orangePortal]):
                    if(app.bluePortal.visible != app.orangePortal.visible):
                        if(Player.YOld <= topBlock.bottom):
                            Player.touchCeiling = True
                            Player.top = topBlock.bottom
                            Player.relY = Player.centerY - currentLevelBlocks.centerY
                        if(Player.dYOld < 0):
                            Player.dY = 0
                if(topBlock.fill in ["white", "darkGrey"]):
                    if(Player.YOld >= topBlock.bottom):
                        Player.touchCeiling = True
                        Player.top = topBlock.bottom
                        Player.relY = Player.centerY - currentLevelBlocks.centerY
                        if(Player.dYOld < 0):
                            Player.dY = 0
                if(topBlock.fill == rgb(30, 240, 60)):
                    Player.hp -= 100 / app.stepsPerSecond
                if(topBlock.fill == 'cyan'):
                    Player.hp -= 25
                    topBlock.visible = False
                    topBlock.cooldown = randrange(1, 4)
                if(topBlock.fill == 'yellow'):
                    app.points.value += 50
                    currentLevelBlocks.remove(topBlock)
                    if(Player.hp <= 45):
                        Player.hp += 5
                    elif(Player.hp != 50):
                        Player.hp == 50
            elif(obj in [app.PGun.blueShot, app.PGun.orangeShot]):
                if(topBlock.fill == 'white'):
                    if(obj.YOld >= topBlock.bottom or (obj.YOld == None and Player.YOld >= topBlock.bottomBlock)):
                        obj.dX = obj.dY = 0
                        obj.top = topBlock.bottom + 1
                        obj.visible = False
                        for j in range(int((app.blockSize + 1) // 2)):
                            for k in [1, -1]:
                                test1 = currentLevelBlocks.hitTest(obj.centerX - app.blockSize // 2  + (j * k), topBlock.bottom - 1)
                                test2 = currentLevelBlocks.hitTest(obj.centerX + app.blockSize // 2  + (j * k), topBlock.bottom - 1)
                                test3 = currentLevelBlocks.hitTest(obj.centerX - app.blockSize // 2  + (j * k), topBlock.bottom + 1)
                                test4 = currentLevelBlocks.hitTest(obj.centerX + app.blockSize // 2  + (j * k), topBlock.bottom + 1)
                                if(test1 != None and test2 != None):
                                    if(test1.fill in ['white', obj.fill] and test2.fill in ['white', obj.fill]):
                                        if((test3 in [None, app.bluePortal, app.orangePortal] or test3.fill == 'cyan') and (test4 in [None, app.bluePortal, app.orangePortal] or test4.fill == 'cyan')):
                                            if(obj == app.PGun.blueShot and test3 != app.orangePortal and test4 != app.orangePortal):
                                                app.bluePortal.x1 = obj.centerX - app.blockSize // 2  + (j * k)
                                                app.bluePortal.x2 = obj.centerX + app.blockSize // 2  + (j * k)
                                                app.bluePortal.y1 = app.bluePortal.y2 = topBlock.bottom
                                                app.bluePortal.dir = 'top'
                                                app.bluePortal.visible = True
                                            if(obj == app.PGun.orangeShot and test3 != app.bluePortal and test4 != app.bluePortal):
                                                app.orangePortal.x1 = obj.centerX - app.blockSize // 2  + (j * k)
                                                app.orangePortal.x2 = obj.centerX + app.blockSize // 2  + (j * k)
                                                app.orangePortal.y1 = app.orangePortal.y2 = topBlock.bottom
                                                app.orangePortal.dir = 'top'
                                                app.orangePortal.visible = True
                                            break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                if(topBlock.fill in ["darkGrey", "pink"]):
                    obj.dX = obj.dY = 0
                    obj.visible = False
                    break
            elif(obj.fill == 'cyan'):
                if((topBlock.fill in ['white', 'darkGrey'] or (topBlock in [app.bluePortal, app.orangePortal] and app.bluePortal.visible != app.orangePortal.visible)) and obj.YOld < topBlock.bottom):
                    obj.top = topBlock.bottom + 1
                    obj.dir = 1
                elif(topBlock.fill == rgb(30, 240, 60)):
                    obj.visibleOld = False
                    obj.cooldown = randrange(1, 4)
                    app.points.value += 10
                elif(topBlock.fill == 'cyan'):
                    obj.visibleOld = False
                    obj.cooldown = randrange(1, 4)
                    topBlock.visible = False
                    topBlock.cooldown = -100
                    app.points.value += 30
                
    app.bluePortal.antiCollision.visible = app.orangePortal.antiCollision.visible = False
    if(obj != Player and obj.fill == 'cyan'):
        currentLevelBlocks.add(obj)
        obj.visible = obj.visibleOld

def onKeyHold(keys):
    if(app.state == 'running'):
        if(app.currKeybinds[2][0] in keys or app.currKeybinds[2][1] in keys):
            if(not Player.touchLeft):
                Player.state = 'running'
                if(Player.touchGround):
                    if(Player.dX > -Player.maxRun):
                        Player.dX += -0.5 * app.blockSize
                else:
                    if(Player.dX > -Player.maxRun/2):
                        Player.dX += -0.25 * app.blockSize
        elif(app.currKeybinds[3][0] in keys or app.currKeybinds[3][1] in keys):
            if(not Player.touchRight):
                Player.state = 'running'
                if(Player.touchGround):
                    if(Player.dX < Player.maxRun):
                        Player.dX += 0.5 * app.blockSize
                else:
                    if(Player.dX < Player.maxRun/2):
                        Player.dX += 0.25 * app.blockSize
        if((app.currKeybinds[0][0] in keys or app.currKeybinds[0][1] in keys or app.currKeybinds[0][2] in keys) and Player.touchGround):
            if(not Player.touchCeiling):
                Player.state = 'jumping'
                Player.dY = -Player.maxJump * 2
        if((app.currKeybinds[6][0] in keys or app.currKeybinds[6][1] in keys) and len(keys) == 1):
            app.levelOffsetOn = True
            if(abs(app.levelOffsetX) < app.levelOffsetMax):
                app.levelOffsetX += (app.mouseX - 200) / 4
            else:
                app.levelOffsetX = abs(app.levelOffsetX)/app.levelOffsetX * app.levelOffsetMax
            if(abs(app.levelOffsetY) < app.levelOffsetMax):
                app.levelOffsetY += (app.mouseY - 200) / 4
            else:
                app.levelOffsetY = abs(app.levelOffsetY)/app.levelOffsetY * app.levelOffsetMax
        else:
            app.levelOffsetOn = False
            
def onKeyRelease(key):
    if(app.state == 'running'):
        if(key in [app.currKeybinds[2][0], app.currKeybinds[3][0], app.currKeybinds[2][1], app.currKeybinds[3][1]]):
            Player.state = 'standing'
        if(key in [app.currKeybinds[0][0], app.currKeybinds[0][1], app.currKeybinds[0][2]]):
            if(Player.dY < 0): Player.dY /= 1.5
        if(key in [app.currKeybinds[6][0], app.currKeybinds[6][1]]):
            app.levelOffsetOn = False
        if(key in [app.currKeybinds[6][0], app.currKeybinds[6][1]]):
            Player.relX = Player.relXOld
            Player.relY = Player.relYOld
            currentLevelBlocks.centerX += 200 - Player.centerX
            currentLevelBlocks.centerY += 200 - Player.centerY
            
            if(currentLevelBlocks.left > 0): currentLevelBlocks.left = 0
            if(currentLevelBlocks.right < 400): currentLevelBlocks.right = 400
            if(currentLevelBlocks.top > 0): currentLevelBlocks.top = 0
            if(currentLevelBlocks.bottom < 400): currentLevelBlocks.bottom = 400
            
            Player.centerX = currentLevelBlocks.centerX + Player.relX
            Player.centerY = currentLevelBlocks.centerY + Player.relY
        
def onKeyPress(key):
    app.key = key
    if(app.state == 'running'):
        if(key in [app.currKeybinds[4][0], app.currKeybinds[4][1]]):
            if(app.PGun.setting.fill == rgb(0, 120, 255)): #Blue
                app.PGun.setting.fill = rgb(250, 100, 0)
            else:
                app.PGun.setting.fill = rgb(0, 120, 255)
        if(key in [app.currKeybinds[5][0], app.currKeybinds[5][1]]):
            app.PGun.blueShot.visible = app.PGun.orangeShot.visible = False
            app.PGun.blueShot.dX = app.PGun.orangeShot.dX = app.PGun.blueShot.dY = app.PGun.orangeShot.dY = 0
            app.bluePortal.visible = app.orangePortal.visible = False
        if(key == app.currKeybinds[7][0]):
            app.escapeMenu.visible = True
            app.escapeMenu.toFront()
            app.stepsPerSecond = 30
            app.state = 'escape'
        if(key in [app.currKeybinds[6][0], app.currKeybinds[6][1]]):
            Player.relXOld = Player.relX
            Player.relYOld = Player.relY
        
    elif(app.state == 'start'):
        app.group.remove(app.pressAnyKeyToStart)
        app.state = 'info'
        app.stepsPerSecond = 20
        app.info.visible = True
        app.info.toFront()

    elif(app.state == 'info'):
        if(app.msgLabels[11].value != app.message[11]):
            for i in range(len(app.message)):
                app.msgLabels[i].value = app.message[i]
                app.stepsPerSecond = 0
        elif(key == app.currKeybinds[7][0]):
            app.info.visible = False
            app.stepsPerSecond = 60
            app.state = 'running'
            drawLevel(Level01)
            app.points.visible = True
            drawPlayer()
            playerRespawn()
            onStep()
            onKeyPress(app.currKeybinds[5][0])
            onKeyPress(app.currKeybinds[7][0])
            
    elif(app.state == 'escape'):
        if(key == app.currKeybinds[7][0]):
            app.escapeMenu.visible = False
            app.escapeMenu.toBack()
            app.stepsPerSecond = 60
            app.state = 'running'
        if(key in [app.currKeybinds[0][0], app.currKeybinds[0][1]]):
            if(app.menuSelect > 0):
                app.menuSelect -= 1
            else:
                app.menuSelect = 2
        if(key in [app.currKeybinds[1][0], app.currKeybinds[1][1]]):
            if(app.menuSelect < 2):
                app.menuSelect += 1
            else:
                app.menuSelect = 0
        if(key in ['space', 'enter']):
            if(app.menuSelect == 0):
                onKeyPress(app.currKeybinds[7][0])
            elif(app.menuSelect == 1):
                app.escapeMenu.visible = False
                app.keybinding.visible = True
                app.keybinding.toFront()
                app.state = 'keybind'
            elif(app.menuSelect == 2):
                levelSelect()
    elif(app.state == 'keybind'):
        if(key == app.currKeybinds[7][0]):
            app.keybinding.visible = False
            app.keybinding.toBack()
            app.state = 'escape'
            app.escapeMenu.visible = True
            app.escapeMenu.toFront()
    elif(app.state == 'win'):
        app.group.remove(app.win)
        app.stepsPerSecond = 60
        app.state = 'running'
        drawLevel(Level01)
        app.points.value = 0
        drawPlayer()
        playerRespawn()
        onStep()
        onKeyPress(app.currKeybinds[5][0])
        
def onMouseMove(x, y):
    app.mouseX = x
    app.mouseY = y
    if(app.state == 'escape'):
        if(112 <= x <= 288):
            if(112 <= y <= 168):
                app.menuSelect = 0
            elif(170 <= y <= 226):
                app.menuSelect = 1
            elif(228 <= y <= 284):
                app.menuSelect = 2

def onMousePress(x, y):
    if(app.state == 'running'):
        if(app.PGun.setting.fill == rgb(0, 120, 255)): #Blue
            app.PGun.blueShot.centerX = app.PGun.centerX
            app.PGun.blueShot.centerY = app.PGun.centerY
            app.PGun.blueShot.relX = app.PGun.blueShot.centerX - currentLevelBlocks.centerX
            app.PGun.blueShot.relY = app.PGun.blueShot.centerY - currentLevelBlocks.centerY
    
            app.PGun.blueShot.visible = True
            app.PGun.blueShot.dX, app.PGun.blueShot.dY = getPointInDir(app.PGun.centerX, app.PGun.centerY, Player.lookAngle, 10)
            app.PGun.blueShot.dX = app.PGun.blueShot.centerX - app.PGun.blueShot.dX
            app.PGun.blueShot.dY = app.PGun.blueShot.centerY - app.PGun.blueShot.dY
    
        if(app.PGun.setting.fill == rgb(250, 100, 0)): #Orange
            app.PGun.orangeShot.centerX = app.PGun.centerX
            app.PGun.orangeShot.centerY = app.PGun.centerY
            app.PGun.orangeShot.relX = app.PGun.orangeShot.centerX - currentLevelBlocks.centerX
            app.PGun.orangeShot.relY = app.PGun.orangeShot.centerY - currentLevelBlocks.centerY

            app.PGun.orangeShot.visible = True
            app.PGun.orangeShot.dX, app.PGun.orangeShot.dY = getPointInDir(app.PGun.centerX, app.PGun.centerY, Player.lookAngle, 10)
            app.PGun.orangeShot.dX = app.PGun.orangeShot.centerX - app.PGun.orangeShot.dX
            app.PGun.orangeShot.dY = app.PGun.orangeShot.centerY - app.PGun.orangeShot.dY
    elif(app.state == 'escape'):
        if(112 <= x <= 288):
            if(112 <= y <= 168):
                onKeyPress(app.currKeybinds[7][0])
            elif(170 <= y <= 226):
                app.escapeMenu.visible = False
                app.keybinding.visible = True
                app.keybinding.toFront()
                app.state = 'keybind'
            elif(228 <= y <= 284):
                levelSelect()
    elif(app.state == 'keybind'):
        selX = (x // 100) - 1
        selY = (y // 40) - 2
        if([selY, selX] in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [2, 0], [2, 1], [3, 0], [3, 1], [4, 0], [4, 1], [5, 0], [5, 1], [6, 0], [6, 1], [7, 0]]):
            sel = app.getTextInput("Select the key you want. If it is not a letter, number, or character, type it's name, e.g. space, enter")
            if(sel != '' and sel != None):
                app.currKeybinds[selY][selX] = sel
                app.currKeybindsDisplay[selY][selX].value = sel
            
def onStep():
    if(app.state == 'running'):
        Player.relX = Player.centerX - currentLevelBlocks.centerX
        Player.relY = Player.centerY - currentLevelBlocks.centerY
    
        #Position Level
        currentLevelBlocks.centerX -= (Player.centerX - 200 + app.levelOffsetX) / 10
        currentLevelBlocks.centerY -= (Player.centerY - 200 + app.levelOffsetY) / 10
        
        if(currentLevelBlocks.left > app.canvasLeft): 
            currentLevelBlocks.left = app.canvasLeft
            app.levelScrollX = False
        if(currentLevelBlocks.right < 400 - app.canvasLeft): 
            currentLevelBlocks.right = 400 - app.canvasLeft
            app.levelScrollX = False
        if(currentLevelBlocks.top > app.canvasTop): 
            currentLevelBlocks.top = app.canvasTop
            app.levelScrollY = False
        if(currentLevelBlocks.bottom < 400 - app.canvasTop): 
            currentLevelBlocks.bottom = 400 - app.canvasTop
            app.levelScrollY = False
        if((currentLevelBlocks.left == app.canvasLeft and currentLevelBlocks.right > 400 - app.canvasLeft and Player.centerX >= 200) or (currentLevelBlocks.right == 400 - app.canvasLeft and currentLevelBlocks.left < app.canvasLeft and Player.centerX <= 200) or (currentLevelBlocks.left < app.canvasLeft and currentLevelBlocks.right > 400 - app.canvasLeft)):
            app.levelScrollX = True
        if((currentLevelBlocks.bottom == 400 - app.canvasTop and currentLevelBlocks.top < app.canvasTop and Player.centerY <= 200) or (currentLevelBlocks.top == app.canvasTop and currentLevelBlocks.bottom > 400 - app.canvasTop and Player.centerY >= 200)):
            app.levelScrollY = True
        
        if(Player.rotateAngle != 0):
            if(Player.rotateAngle <= 180):
                Player.rotateAngle -= 1000 / app.stepsPerSecond
            else:
                Player.rotateAngle += 1000 / app.stepsPerSecond
            
            if(Player.rotateAngle < 5 or Player.rotateAngle > 355):
                Player.rotateAngle = 0
                
        if(app.levelOffsetOn == False and app.levelOffsetX != 0 and app.levelOffsetY != 0):
            if(abs(app.levelOffsetX) > 10):
                app.levelOffsetX = 0
            else:
                app.levelOffsetX = 0
            if(abs(app.levelOffsetY) > 10):
                app.levelOffsetY = 0
            else:
                app.levelOffsetY = 0
            
        if(Player.hp <= 0):
            Player.hp = 1
            playerRespawn() 
            app.points.value -= 100
        app.hp.width = 4 * app.blockSize * Player.hp / 50 + 1
        app.hp.visible = True
        app.hp.right = 400
        app.hp.toFront()
        
        for i in coinList.keys():
            coin = coinList[i]
            if(coin.offset >= 0.0625 or coin.offset <= -0.0625):
                coin.dir *= -1
            coin.offset += 0.01 * coin.dir
            coin.centerY = currentLevelBlocks.centerY + coin.startY + coin.offset * app.blockSize
            
        deletelist = []
        for i in dangerList.keys():
            danger = dangerList[i]
            danger.XOld = danger.centerX
            danger.YOld = danger.centerY
            if(danger.visible == True):
                danger.centerX += danger.dX * danger.dir / app.stepsPerSecond
                danger.centerY += danger.dY * danger.dir / app.stepsPerSecond
                collision(danger)
            elif(danger.visible == False and danger.cooldown > 0):
                danger.dX = danger.dY = 0
                danger.cooldown -= 4/app.stepsPerSecond
            elif(danger.visible == False and danger.cooldown == -100):
                dangerList[i] = None
                deletelist.append(i)
            else:
                danger.centerX = currentLevelBlocks.centerX + danger.spawnX
                danger.centerY = currentLevelBlocks.centerY + danger.spawnY
                if(danger.spawnAxis == 'x'):
                    danger.dY = 0
                    danger.dX = randrange(int(app.blockSize * 5), int(app.blockSize * 15))
                elif(danger.spawnAxis == 'y'):
                    danger.dX = 0
                    danger.dY = randrange(int(app.blockSize * 5), int(app.blockSize * 15))
                danger.dir = randrange(-1, 2, 2)
                danger.visible = True
        for i in deletelist:
            del dangerList[i]
       
        #Apply Gravity
        if(not Player.touchGround):
            Player.dY += 0.5 * app.blockSize
            
        if(Player.state == 'standing'):
            if(abs(Player.dX) > 0):
                if(abs(Player.dX) <= app.blockSize * 0.2):
                    Player.dX = 0
                else:
                    if(Player.touchGround):
                        Player.dX -= Player.dX / 2
                    else:
                        Player.dX -= Player.dX / 5
        
        #Drag
        if(Player.dX != 0 and not Player.touchGround):
            Player.dX -= Player.dX * 0.005 / app.stepsPerSecond
        if(Player.dY != 0 and not Player.touchGround):
            Player.dY -= Player.dY * 0.02 / app.stepsPerSecond
        
        #Limit Maximum Speed
        if(Player.dX > Player.maxSpeed): Player.dX = Player.maxSpeed
        elif(Player.dX < -Player.maxSpeed): Player.dX = -Player.maxSpeed
        if(Player.dY > Player.maxSpeed): Player.dY = Player.maxSpeed
        elif(Player.dY < -Player.maxSpeed): Player.dY = -Player.maxSpeed
        
        if(app.PGun.blueShot.visible == True):
            collision(app.PGun.blueShot)
            app.PGun.blueShot.XOld = app.PGun.blueShot.centerX
            app.PGun.blueShot.YOld = app.PGun.blueShot.centerY
            app.PGun.blueShot.relX -= app.PGun.blueShot.dX
            app.PGun.blueShot.relY -= app.PGun.blueShot.dY
            app.PGun.blueShot.centerX = currentLevelBlocks.centerX + app.PGun.blueShot.relX
            app.PGun.blueShot.centerY = currentLevelBlocks.centerY + app.PGun.blueShot.relY
            
        if(app.PGun.orangeShot.visible):
            collision(app.PGun.orangeShot)
            app.PGun.orangeShot.XOld = app.PGun.orangeShot.centerX
            app.PGun.orangeShot.YOld = app.PGun.orangeShot.centerY
            app.PGun.orangeShot.relX -= app.PGun.orangeShot.dX
            app.PGun.orangeShot.relY -= app.PGun.orangeShot.dY
            app.PGun.orangeShot.centerX = currentLevelBlocks.centerX + app.PGun.orangeShot.relX
            app.PGun.orangeShot.centerY = currentLevelBlocks.centerY + app.PGun.orangeShot.relY
    
        collision(Player)
        
        Player.XOld = Player.centerX
        Player.YOld = Player.centerY
        
        Player.relX += Player.dX / app.stepsPerSecond
        Player.relY += Player.dY / app.stepsPerSecond
        Player.centerX = currentLevelBlocks.centerX + Player.relX
        Player.centerY = currentLevelBlocks.centerY + Player.relY
        
        Player.rotateAngleOld = Player.rotateAngle
        
        Player.toBack()
        Player.lookAngle = angleTo(Player.centerX, Player.centerY, app.mouseX, app.mouseY)
        app.PGun.rotateAngle = Player.lookAngle - 90
        app.PGun.centerX, app.PGun.centerY = getPointInDir(Player.centerX, Player.centerY, Player.lookAngle, app.blockSize * 0.2)
        
        Player.dXOld = Player.dX
        Player.dYOld = Player.dY
    
        Player.touchGroundOld = Player.touchGround
        Player.touchCeilingOld = Player.touchCeiling

        Player.touchLeftOld = Player.touchLeft
        Player.touchRightOld = Player.touchRight
        app.points.toFront()
        
        if((Player.left > currentLevelBlocks.right or Player.right < currentLevelBlocks.left or Player.bottom < currentLevelBlocks.top or Player.top > currentLevelBlocks.bottom) and app.levelOffsetX == app.levelOffsetY == 0):
            if(app.level == Level01):
                drawLevel(Level02)
                drawPlayer()
                playerRespawn()
                onStep()
                onKeyPress(app.currKeybinds[5][0])
            else:
                app.state = 'win'
                app.stepsPerSecond = 0
                app.win = Group(
                    Rect(0, 0, 400, 400, opacity = 90),
                    Label("The End", 200, 200, size = 50, font = 'monospace', fill='white'),
                    Label("Score: " + str(app.points.value), 200, 300, size = 20, font = 'monospace', fill='white'),
                    Label("Press any key to retry", 200, 375, size = 15, font = 'monospace', fill='white'))
                
            
    elif(app.state == 'start'):
        app.counterMenu += 1
        if(app.counterMenu % 3 == 0):
            if(app.pressAnyKeyToStart.visible): app.pressAnyKeyToStart.visible = False
            else: app.pressAnyKeyToStart.visible = True
            app.pressAnyKeyToStart.toFront()
        if(app.counterMenu >= 20):
            if(currentLevelBlocks.right > 400):
                currentLevelBlocks.centerX -= app.blockSize
            elif(currentLevelBlocks.right <= 400):
                currentLevelBlocks.left = 0
                app.counterMenu = 0
    
    elif(app.state == 'info'):  
        app.msgLabels[app.counterMsgs].value += app.message[app.counterMsgs][app.counterMsgLen]
         
        if(app.counterMsgLen < len(app.message[app.counterMsgs]) - 1):
            app.counterMsgLen += 1
        elif(app.counterMsgs < len(app.message) - 1):
            app.counterMsgLen = 0
            app.counterMsgs += 1
        else:
            app.stepsPerSecond = 0
        
    elif(app.state == 'escape'):
        if(app.menuSelect == 0):
            app.escapeMenu.select.visible = True
            app.escapeMenu.select.top = 112
        elif(app.menuSelect == 1):
            app.escapeMenu.select.visible = True
            app.escapeMenu.select.top = 170
        elif(app.menuSelect == 2):
            app.escapeMenu.select.visible = True
            app.escapeMenu.select.top = 228
        else:
            app.escapeMenu.select.visible = False

drawLevel(Menu)
app.stepsPerSecond = 4
