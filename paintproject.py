#Rick and Morty Paint
#Faisal Ahmed 
    #Indivdual features
    #Eye dropper tool
    #Polygon tool (fill and unfilled)
    #Fill canvas tool
    #Highlight each selected tool 
    #show x and y position for mouse pos
    #Show tool selected 
    #Change size of tools and stamps using scroll wheel
    #Text tool
    #Cut tool
    #undo/redo tool (sort of)
    #new canvas tool 

    #Attention to detail 
    #Corners of rectangles and lines are curved 
    #User cant enter an empty name when saving, ('it would be called unnamed.png')
    #when you enter a filename which doesnt exit for the load tool, you have to reenter the name so it doesnt crash
    #you can only make one copy of the selected item you have for the cut tool which you can drag around (same for text tool, and also load tool). No multiple copies
    #When you select polygon/cut or eyedropper tool, it highlights the text at the bottom

from glob import *
from tkinter import *                
from pygame import*
from random import *
from math import *
import os



drawColor=(0,0,0)#sets initial color value to black
drawcanvascolor=(255,255,255) #sets color of the canvas
res=(1200,800)#sets resolution of screen 

thickness=1#radius of the pencil/whatever
tool='Pencil'#tells you which tool youre on
toool=''#tool variable specifically for undo and redo so you can use it, while using another tool 
cutbool=False #checks to make sure an item was selected for the cut tool

font.init()# initializes font 
init()
pencil_strings = (            #sized 24x24
  "XX                      ",
  "XXX                     ",
  "XXXX                    ",
  "XX.XX                   ",
  "XX..XX                  ",
  "XX...XX                 ",
  "XX....XX                ",
  "XX.....XX               ",
  "XX......XX              ",
  "XX.......XX             ",
  "XX........XX            ",
  "XX........XXX           ",
  "XX......XXXXX           ",
  "XX.XXX..XX              ",
  "XXXX XX..XX             ",
  "XX   XX..XX             ",
  "     XX..XX             ",
  "      XX..XX            ",
  "      XX..XX            ",
  "       XXXX             ",
  "                        ",
  "                        ",
  "                        ",
  "                        ")


#.wav SOUND EFFECTS
rickSound = mixer.Sound("sounds/rick.wav")
mortySound = mixer.Sound("sounds/morty.wav")
mrmSound = mixer.Sound("sounds/mrm.wav")
prSound = mixer.Sound("sounds/picklerick.wav") 
mrpSound = mixer.Sound("sounds/mrp.wav")
ysSound = mixer.Sound("sounds/ys.wav")
drSound=mixer.Sound("sounds/dr.wav")
bpSound=mixer.Sound("sounds/bp.wav")
emSound=mixer.Sound("sounds/em.wav")
jSound=mixer.Sound("sounds/jerry.wav")

screen=display.set_mode(res)
display.set_caption("Rick and Morty Paint Project")#sets the title for pyc file
picklerick=image.load("Rick stamps/picklerick.png")
picklerick=transform.scale(picklerick,(100,100))
display.set_icon(picklerick)#sets icon for pyc file
running= True

######CURSOR##########

#datatuple, masktuple = cursors.compile( thickarrow_strings,black='.', white='X', xor='o' )
datatuple, masktuple = cursors.compile( pencil_strings,black='.', white='X', xor='o' )
mouse.set_cursor( (24,24), (0,0), datatuple, masktuple )

#background music
mixer.music.load("sounds/rmts.mp3")   
mixer.music.play(-1)

bg = image.load("Icons and Other Pictures/bg.png")#background image
bg = transform.scale(bg, (1200, 800))#transforms it to size
screen.blit(bg,(0,0))

#canvas
draw.rect(screen,(drawcanvascolor),(355,10,840,580))# draws the canvas rect
canvas=Rect(355,10,840,580)
draw.rect(screen,(drawColor),(350,5,850,590),5)
pos=(355,10)#position of canvas
size=(840,580) #size of canvas
Rcanvas=Surface((840, 580))#makes surface for canvas

#color spectrum initial area 

color=image.load("Icons and Other Pictures/color.png")
color=transform.scale(color,(320,150))
screen.blit(color,(7,640))
colorrect=Rect(7,640,320,150)#creates area for where it will be placed
draw.rect(screen,(0,200,255),colorrect,5)#draws rectangle around image 

#stamp tool box
draw.rect(screen,(150,0,255),(360,640,830,150))#box for all stamps
draw.rect(screen,(255,0,255),(360,640,830,150),7)#outlined box for all stamps

#drawing tools
draw.rect(screen,(100,100,100),(10,135,320,150))#box for all drawing tools
draw.rect(screen,(0,255,255),(10,135,320,150),5)#outlined box for all drawing tools

pencilRect=Rect(25,145,50,60) #area made for the pencil tool
pencil=image.load("Icons and Other Pictures/pencil.png")# loads the image 
pencil = transform.scale(pencil,(50,60))# changes the size of image
screen.blit(pencil,(25,145))
draw.rect(screen,(255,0,255),(25,145,50,60),5) #draws rect for pencil tool

## REST OF TOOLS USE THE SAME FORMAT AS THE PENCIL TOOL^^##
eraserRect=Rect(95,145,50,60) 
eraser=image.load("Icons and Other Pictures/eraser.png")
eraser=transform.scale(eraser,(50,60))
screen.blit(eraser,(95,145))
draw.rect(screen,(0,255,255),eraserRect,5)

fb=image.load("Icons and Other Pictures/fillbucket.png")
fb=transform.scale(fb,(50,50))
fbRect=Rect(165,145,50,60)
screen.blit(fb,(165,145))
draw.rect(screen,(0,255,255),fbRect,5)

ab=image.load("Icons and Other Pictures/airbrush.png")
ab=transform.scale(ab,(50,60))
abRect=Rect(235,145,50,60)
screen.blit(ab,(235,145))
draw.rect(screen,(0,255,255),abRect,5) 

spRect=Rect(25,215,50,60)
spraypaint=image.load("Icons and Other Pictures/spraypaint.png")
spraypaint=transform.scale(spraypaint,(50,60)) 
screen.blit(spraypaint,(25,215))
draw.rect(screen,(0,255,255),spRect,5)

brush=image.load("Icons and Other Pictures/font.png")
brush=transform.scale(brush,(50,60))
brushRect=Rect(95,215,50,60)
screen.blit(brush,(95,215))
draw.rect(screen,(0,255,255),brushRect,5)

fontt=image.load("Icons and Other Pictures/fonticon.png")
fontt=transform.scale(fontt,(50,60))
fontRect=Rect(165,215,50,60)
screen.blit(fontt,(165,215))
draw.rect(screen,(0,255,255),fontRect,5) 

ed=image.load("Icons and Other Pictures/eyedropper.png")
ed=transform.scale(ed,(50,60))
edRect=Rect(235,215,50,60)
screen.blit(ed,(235,215))
draw.rect(screen,(0,255,255),edRect,5) 

#shapes
draw.rect(screen,(100,100,100),(10,480,320,150))#box for shapes
draw.rect(screen,(0,255,255),(10,480,320,150),5)#outline box for shapes 
#line
draw.line(screen,(255,0,255),(235,515),(285,515),5)
lineRect=Rect(235,490,50,60) 
draw.rect(screen,(0,255,255),lineRect,5)
#Rect
draw.rect(screen,(255,0,255),(175,500,30,40),1)
rectRect=Rect(165,490,50,60)
draw.rect(screen,(0,255,255),rectRect,5)

draw.rect(screen,(255,0,255),(175,570,30,40))
fillrectRect=Rect(165,560,50,60)
draw.rect(screen,(0,255,255),fillrectRect,5)
#Quad
poly=image.load("Icons and Other Pictures/poly.png")
poly=transform.scale(poly,(50,60))
screen.blit(poly,(95,490)) 
polyRect=Rect(95,490,50,60)
draw.rect(screen,(0,255,255),polyRect,5)

fillpolyRect=Rect(95,560,50,60)
fillpoly=image.load("Icons and Other Pictures/fillpoly.png")
fillpoly=transform.scale(fillpoly,(50,65))
screen.blit(fillpoly,(95,560)) 
draw.rect(screen,(0,255,255),fillpolyRect,5)

cutRect=Rect(235,560,50,60)
cut=image.load("Icons and Other Pictures/cut.png")
cut=transform.scale(cut,(50,60))
screen.blit(cut,(235,560))
draw.rect(screen,(0,255,255),cutRect,5)
#ellipse
draw.circle(screen,(255,0,255),(50,520),20,1)
circleRect=Rect(25,490,50,60)
draw.rect(screen,(0,255,255),circleRect,5)

draw.circle(screen,(255,0,255),(50,590),20)
fillcircleRect=Rect(25,560,50,60)
draw.rect(screen,(0,255,255),fillcircleRect,5)

#file toolbox stuff
draw.rect(screen,(100,100,100),(10,335,325,70))#box for all file toolbar tools 
draw.rect(screen,(150,0,255),(10,335,325,70),4)#outlined box for file toolbar tools 

openn=image.load("Icons and Other Pictures/load.png")
openn=transform.scale(openn,(50,60))
opennRect=Rect(272,342,50,60)
screen.blit(openn,(272,342))

undob=image.load("Icons and Other Pictures/undo.png")
undob=transform.scale(undob,(40,50))
undoRect=Rect(190,345,40,50)
screen.blit(undob,(190,345)) 
    
redob=image.load("Icons and Other Pictures/redo.png")
redob=transform.scale(redob,(40,50))
redRect=Rect(230,345,40,50)
screen.blit(redob,(230,345))

save=image.load("Icons and Other Pictures/save.png")
save=transform.scale(save,(50,50))
saveRect=Rect(140,345,50,50)
screen.blit(save,(140,345))

load=image.load("Icons and Other Pictures/open.png")
load=transform.scale(load,(70,60))
loadRect=Rect(70,340,70,60)
screen.blit(load,(70,340))

new=image.load("Icons and Other Pictures/portal.gif")
new=transform.scale(new,(50,70))
newRect=Rect(15,335,50,70)
screen.blit(new,(15,335))
newd=image.load("Icons and Other Pictures/portald.png")
newd=transform.scale(newd,(50,70))
newdRect=Rect(15,335,50,70)

#title image
title = image.load("Icons and Other Pictures/rickandmory.png")
title=transform.scale(title,(375,145)) 
screen.blit(title,(-10,0))

                    ##stamps##

yellowstamp=image.load("Rick stamps/showmewhatyougot.png")
yellowstamp = transform.scale(yellowstamp, (50, 70))
ysRect=Rect(450,650,70,70)
screen.blit(yellowstamp,(460,650))
draw.rect(screen,(255,255,255),ysRect,6) 

rick=image.load("Rick stamps/rick1.png")
rick=transform.scale(rick,(70,70))
rRect=Rect(770,650,70,70)
screen.blit(rick,(770,650))
draw.rect(screen,(255,255,255),rRect,6) 

morty=image.load("Rick stamps/morty1.png")
morty=transform.scale(morty,(70,70))
mRect=Rect(690,650,70,70)
screen.blit(morty,(690,650))
draw.rect(screen,(255,255,255),mRect,6) 

picklerick=image.load("Rick stamps/picklerick.png")
picklerick=transform.scale(picklerick,(70,70))
prRect=Rect(610,650,70,70)
screen.blit(picklerick,(610,650))
draw.rect(screen,(255,255,255),prRect,6) 

mrpRect=Rect(530,650,70,70)
mrp=image.load("Rick stamps/stamp5.png")
mrp=transform.scale(mrp,(100,100))
screen.blit(mrp,(520,635))
draw.rect(screen,(255,255,255),mrpRect,6) 

mrmRect=Rect(370,650,73,100)
mrm=image.load("Rick stamps/mrm.png")
mrm=transform.scale(mrm,(73,100))
screen.blit(mrm,(370,650))
draw.rect(screen,(255,255,255),mrmRect,6) 

drRect=Rect(850,650,70,70)
dr=image.load("Rick stamps/dumbrick.png")
dr=transform.scale(dr,(70,70))
screen.blit(dr,(850,650))
draw.rect(screen,(255,255,255),drRect,6)

emRect=Rect(930,650,70,70)
em=image.load("Rick stamps/evilmor.png")
em=transform.scale(em,(70,70))
screen.blit(em,(930,650))
draw.rect(screen,(255,255,255),emRect,6)

jRect=Rect(1010,650,70,70)
jerry=image.load("Rick stamps/jerry.png")
jerry=transform.scale(jerry,(70,70))
screen.blit(jerry,(1010,650))
draw.rect(screen,(255,255,255),jRect,6)

bpRect=Rect(1090,650,70,70)
bp=image.load("Rick stamps/bp.png")
bp=transform.scale(bp,(100,100))
screen.blit(bp,(1075,640))
draw.rect(screen,(255,255,255),bpRect,6)


undo=[]#empty undo list
redo=[]#empty redo list
undo.append(Rcanvas)#appends blank canvas to undo list
polypts=[]#empty polygon point list
fl=[]
comicFont = font.SysFont("Comic Sans MS", 20)#gets the font format
y = 20


while running:
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    click = False
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            pic=screen.copy()
            Rcanvas.blit(screen,(0,0),(pos,size))  # Blits canvas on to Rcanvas (surface for canvas)
            if e.button == 1:
               startx=e.pos[0]  #gets start position of x
               starty=e.pos[1]#gets start position of y 
               click=True
            if e.button==4 and tool!='cut':# if scroll wheel is moved upwards
                if tool=='Pencil': 
                    if 10>thickness>=0:# makes sure that the thickness of the pencil is between 0-10
                        thickness+=1 
                if tool=='brush': # makes sure thickness of the brush is between 0-25 
                    if 25>thickness>=0:
                        thickness+=1
                elif thickness>=0: 
                    thickness+=1 
            if e.button==5 and tool!='cut': 
                if thickness>0:
                    thickness-=1
        if e.type == MOUSEBUTTONUP:
            if canvas.collidepoint(mx,my) and mb[0]==1 and tool!='' and tool!='eyedropper':
                undo.append(Rcanvas.copy())#adds copiees of the screen to undo list
                print(len(undo))
            if toool=='undo': #undo tool - if the length of the undo list is >=1 and it is clicked, then the last item in the list is removed and added to the redo list
                if len(undo)>1:
                    redo.append(undo.pop())
                    screen.blit(redo[-1],pos)
            if toool=='redo':#redo tool - if length of the redo list is >1 and is clicked, the last item in the list is removed and added back to the undo list 
                if len(redo)>=1:
                    undo.append(redo.pop())
                    screen.blit(undo[-1],pos)
                    
    if mb[0]==1 and canvas.collidepoint((mx,my)):
        screen.set_clip(canvas)#makes sure no drawings go outside of the canvas 
 
 ####font stuff###
    
    #for the thickness, xval,and yval, you are currently on          
    myfont = font.SysFont('Courrier New', 15)
    textsize = myfont.render('Thickness:', False, (0, 0,0))#renders font setting
    numbersize=myfont.render(str(thickness), False,(0,0,0))
    draw.rect(screen,(255,255,255),(1100,545,85,45))#draws rects for where text will be placed
    draw.rect(screen,(0),(1100,545,85,45),1) 
    screen.blit(numbersize,(1160,547))
    screen.blit(textsize,(1100,547))

    xvaltext=myfont.render('x pos:', False,(0,0,0)) 
    xval=myfont.render(str(mx), False,(0,0,0))
    screen.blit(xvaltext,(1102,558))
    screen.blit(xval,(1160,558))

    yvaltext=myfont.render('y pos:',False,(0,0,0)) 
    yval=myfont.render(str(my),False,(0,0,0))
    screen.blit(yvaltext,(1102,570))
    screen.blit(yval,(1160,570))

    #for Stamps box
    myfont = font.SysFont('Comic Sans MS', 48)
    stamptext=myfont.render('STAMPS',True,(255,0,255))
    screen.blit(stamptext,(630,725))

    #for shapes
    myfont = font.SysFont('Comic Sans MS', 24)
    shapetext=myfont.render('SHAPES',False,(255,0,255))
    screen.blit(shapetext,(10,440))

    #for drawing tools
    myfont = font.SysFont('Comic Sans MS', 24)
    shapetext=myfont.render('DRAWING TOOLS',False,(255,0,255))
    screen.blit(shapetext,(10,290))

    myfont=font.SysFont('Comic Sans MS',12)
    draw.rect(screen,(255,255,255),(355,565,200,25))
    draw.rect(screen,(0,0,0),(355,565,200,25),1)
    selectext=myfont.render("Tool Selected:",True,(0,0,0))
    tooltext=myfont.render(tool.upper(),True,(0,0,0))
    screen.blit(tooltext,(450,570))
    screen.blit(selectext,(360,570))

    #tip box
    draw.rect(screen,(111,111,111),(350,600,850,33))
    draw.rect(screen,(drawColor),(350,600,850,33),5)
    myfont=font.SysFont('Comic Sans MS',16)
    tiptext=myfont.render("THICKNESS-MOUSEWHEEL || POLYGON & CUT EXIT-RIGHT CLICK",True,(255,255,255))
    screen.blit(tiptext,(560,605))

    #functions
    

    def getName(screen,showFiles):

        ans = ""                    # final answer will be built one letter at a time.
        arialFont = font.SysFont("Times New Roman", 16)
        back = screen.copy()        # copy screen so we can replace it when done
        textArea = Rect(355,10,200,25) # make changes here.

        if showFiles:
            pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
            n = len(pics)
            choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
            draw.rect(screen,(220,220,220),choiceArea)        # draw the text window and the text.
            draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
            for i in range(n):
                 txtPic = arialFont.render(pics[i], True, (0,111,0))   #
                 screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))

        cursorShow = 0
        myclock = time.Clock()
        typing = True
        while typing:
            cursorShow += 1
            for e in event.get():
                if e.type == QUIT:
                    event.post(e)   # puts QUIT back in event list so main quits
                    return ""
                if e.type == KEYDOWN:
                    if e.key == K_BACKSPACE:    # remove last letter
                        if len(ans)>0:
                            ans = ans[:-1]
                    elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                        typing = False
                    elif e.key < 256:
                        ans += e.unicode       # add character to ans
                        
            txtPic = arialFont.render(ans, True, (0,0,0))   #
            draw.rect(screen,(255,255,255),textArea)        # draw the text window and the text.
            draw.rect(screen,(0,0,0),textArea,2)            
            screen.blit(txtPic,(textArea.x+3,textArea.y+2))
            if cursorShow // 50 % 2 == 1:
                cx = textArea.x+txtPic.get_width()+3
                cy = textArea.y+3
                draw.rect(screen,(255,0,0),(cx,cy,2,textArea.height-6))
            myclock.tick(100)
            display.flip()
            
        screen.blit(back,(0,0))
        return ans


    #picks color # 

    if colorrect.collidepoint(mx,my) and mb[0]==1:
        drawColor=screen.get_at((mx,my))
        draw.rect(screen,(drawColor),(350,5,850,590),5)
    #checks which tools you're using currently#


            ## If you click on a certain object, it indicates you are using that tool by highlighting the box with a color, while resetting the rest 
            ## of the tools to the default color of the box given. 

    if  pencilRect.collidepoint(mx,my) and mb[0]==1: 
        draw.rect(screen,(255,0,255),pencilRect,5)

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)

        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        tool='Pencil'
    if eraserRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),eraserRect,5)

        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)

        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),edRect,5)

        tool='Eraser'

    if spRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),spRect,5)

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)

        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        tool='spraypaint'      
    if brushRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),brushRect,5) 

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)

        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(0,255,255),cutRect,5)       
        tool='brush'
    if abRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),abRect,5) 

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),edRect,5)

        tool='airbrush'
    if fontRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),fontRect,5) 

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),edRect,5)

        
        tool='text'
    if fbRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),fbRect,5) 

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        tool='fillbucket'

    if edRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),edRect,5)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(255,255,255),ysRect,6) 
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)

        tool='eyedropper'

    if ysRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)

        draw.rect(screen,(0,255,255),ysRect,6) 

        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        ysSound.play() 
        tool='yellowstamp'

    if rRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),rRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        rickSound.play() 
        tool='rick'

    if mRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),mRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 

        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        mortySound.play() 
        tool='morty'

    if prRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),prRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)

        prSound.play() 
        tool='picklerick'

    if mrpRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),mrpRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)

        mrpSound.play() 
        tool='mrp'
    if mrmRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),mrmRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)

        mrmSound.play() 
        tool='mrm'
    if bpRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),bpRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        bpSound.play() 
        tool='bp'
    if jRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),jRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)

        jSound.play() 
        tool='jerry'
    if emRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),emRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)

        emSound.play() 
        tool='em'
    if drRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(0,255,255),drRect,6)

        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)

        drSound.play() 
        tool='dr'
    if lineRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),lineRect,5) 

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        tool='line'
    if rectRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),rectRect,5) 

        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)
        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        tool='rect'
    if polyRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),polyRect,5) 

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),cutRect,5)
        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)

        tool='randshape'
    if circleRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),circleRect,5) 

        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),cutRect,5)
        tool='circle'
    if fillcircleRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),fillcircleRect,5)

        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5) 
        draw.rect(screen,(0,255,255),cutRect,5)
        tool='fillcircle'
    if fillrectRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),fillrectRect,5)

        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),lineRect,5) 
        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),cutRect,5)
        tool='fillrect'
    if fillpolyRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),fillpolyRect,5) 

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        draw.rect(screen,(0,255,255),cutRect,5)        

        tool='fillpoly'
    if cutRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,(255,0,255),cutRect,5) 

        draw.rect(screen,(0,255,255),eraserRect,5)
        draw.rect(screen,(0,255,255),pencilRect,5)
        draw.rect(screen,(0,255,255),spRect,5)
        draw.rect(screen,(0,255,255),fbRect,5)
        draw.rect(screen,(0,255,255),rectRect,5)
        draw.rect(screen,(0,255,255),lineRect,5)
        draw.rect(screen,(0,255,255),circleRect,5)
        draw.rect(screen,(0,255,255),fillcircleRect,5)
        draw.rect(screen,(0,255,255),fillrectRect,5)
        draw.rect(screen,(0,255,255),polyRect,5)
        draw.rect(screen,(0,255,255),fillpolyRect,5)
        draw.rect(screen,(0,255,255),edRect,5)
        draw.rect(screen,(255,255,255),mrpRect,6)
        draw.rect(screen,(255,255,255),prRect,6)
        draw.rect(screen,(255,255,255),ysRect,6)
        draw.rect(screen,(255,255,255),mRect,6)
        draw.rect(screen,(255,255,255),rRect,6)
        draw.rect(screen,(255,255,255),mrmRect,6)
        draw.rect(screen,(255,255,255),bpRect,6)
        draw.rect(screen,(255,255,255),jRect,6)
        draw.rect(screen,(255,255,255),emRect,6)
        draw.rect(screen,(255,255,255),drRect,6)

        draw.rect(screen,(0,255,255),fontRect,5)
        draw.rect(screen,(0,255,255),abRect,5)
        draw.rect(screen,(0,255,255),brushRect,5)
        tool='cut'
    if undoRect.collidepoint(mx,my) and mb[0]==1:
        toool='undo'
    if redRect.collidepoint(mx,my) and mb[0]==1:
        toool='redo'
    if saveRect.collidepoint(mx,my) and mb[0]==1:
        tool='save'
    if opennRect.collidepoint(mx,my) and mb[0]==1:
        tool='open'
    if loadRect.collidepoint(mx,my) and mb[0]==1: 
        toool='load'
    if newRect.collidepoint(mx,my):
        screen.blit(newd,(15,335))
        if mb[0]==1:
            draw.rect(screen,(0,255,255),circleRect,5) 

            draw.rect(screen,(0,255,255),polyRect,5)
            draw.rect(screen,(0,255,255),lineRect,5) 
            draw.rect(screen,(0,255,255),eraserRect,5)
            draw.rect(screen,(0,255,255),pencilRect,5)
            draw.rect(screen,(0,255,255),spRect,5)
            draw.rect(screen,(0,255,255),fbRect,5)
            draw.rect(screen,(0,255,255),rectRect,5)
            draw.rect(screen,(0,255,255),fillcircleRect,5)
            draw.rect(screen,(0,255,255),fillrectRect,5)
            draw.rect(screen,(0,255,255),fillpolyRect,5)
            draw.rect(screen,(0,255,255),cutRect,5)
            draw.rect(screen,(0,255,255),edRect,5)
            draw.rect(screen,(255,255,255),mrpRect,6)
            draw.rect(screen,(255,255,255),prRect,6)
            draw.rect(screen,(255,255,255),ysRect,6)
            draw.rect(screen,(255,255,255),mRect,6)
            draw.rect(screen,(255,255,255),rRect,6)
            draw.rect(screen,(255,255,255),mrmRect,6)
            draw.rect(screen,(255,255,255),bpRect,6)
            draw.rect(screen,(255,255,255),jRect,6)
            draw.rect(screen,(255,255,255),emRect,6)
            draw.rect(screen,(255,255,255),drRect,6)

            draw.rect(screen,(0,255,255),fontRect,5)
            draw.rect(screen,(0,255,255),abRect,5)
            draw.rect(screen,(0,255,255),brushRect,5)
            tool='new'
    else: 
        screen.blit(new,(15,335))


    ###USING ACTUAL TOOLS###

                #DRAWING TOOLS#

    if  tool=='Pencil': 
        if thickness>10:#makes it so the max limit of the pencil thickness is 10
            thickness=1
        if canvas.collidepoint(mx,my) and mb[0]==1:
            draw.line(screen,(drawColor),(omx,omy),(mx,my),thickness)
    if  tool=='Eraser':
        if canvas.collidepoint(mx,my) and mb[0]==1:
            draw.circle(screen,(drawcanvascolor),(mx,my),thickness)
    if tool=='spraypaint':
        if  canvas.collidepoint(mx,my) and mb[0]==1:
            for i in range (20):
                x2=randint(-(thickness+30),thickness+30) #gets random spot to place lines 
                y2=randint(-(thickness+30),thickness+30)
                if (((x2)**2 + (y2)**2)**0.5) <=thickness+30: # determines if the x and y value are less than the hypotneuse, using pythagorean theorem
                    draw.line(screen,drawColor,(mx+x2,my+y2),(mx+x2,my+y2),1) #places line at that spot if so^
    if  tool=='fillbucket':
        if mb[0]==1:
            cpos=[(mx,my)]#makes the color position list 
            c=screen.get_at((mx,my))#gets the color for the current area 
            if c!=drawColor:#if the color on the mouse pos isnt the same as the color selected 
                while len(cpos)>0:#while length of the pixel position list is greater than one, loop runs
                    if canvas.collidepoint(cpos[0]) and screen.get_at(cpos[0]) == c:
                        screen.set_at(cpos[0],drawColor)#changes the first item in the list to the drawColor variable 
                        cpos.append((cpos[0][0],cpos[0][1]+1))#adds on points in the surrounding area to the list until the color is all the same
                        cpos.append((cpos[0][0],cpos[0][1]-1))
                        cpos.append((cpos[0][0]+1,cpos[0][1]))
                        cpos.append((cpos[0][0]-1,cpos[0][1]))
                    del(cpos[0])# deletes first point after changed, so next point can be changed 
       
    if tool=='airbrush':
        cover = Surface((50,50)).convert()                  # make blank Surface
        cover.set_alpha(thickness+5) #sets the transparency value
        cover.fill((255,0,255)) 
        cover.set_colorkey((255,0,255))
        draw.circle(cover,drawColor,(25,25),25) #draws circle over the cover
        if mb[0]==1 and canvas.collidepoint(mx,my):
            screen.blit(cover,(mx-25,my-25))

    if tool=='text':
        txt = getName(screen,False)                     # this is how you would call my getName function
        comicFont = font.SysFont("Comic Sans MS",20+thickness)               # your main loop will stop looping until user hits enter
        txtPic = comicFont.render(txt, True, (drawColor))
        pic2=screen.copy()
        tool='Text'
    if canvas.collidepoint(mx,my) and tool=='Text' and mb[0]==1:
        screen.blit(pic,(0,0))
        screen.blit(pic2,(0,0))
        comicFont = font.SysFont("Comic Sans MS",20+thickness)               # your main loop will stop looping until user hits enter
        txtPic = comicFont.render(txt, True, (drawColor))
        screen.blit(txtPic,(mx,my))

    if tool=='brush':
        if thickness>25:
            thickness=3
        if canvas.collidepoint(mx,my) and mb[0]==1:
           x=mx-omx #gets the distance for the x and y values by subtracting old mx from current
           y=my-omy
           dist=hypot(x,y)#using the hypot function, gets the hypot using pythagorean theorem 
           if dist==0:
               dist=1
           for i in range(int(dist)):# for loop used to draw a circle for every pixel on the screen on the the hypot of the triangle
                dx=int(omx+i/dist*x)
                dy=int(omy+i/dist*y)  
                draw.circle(screen,drawColor,(dx,dy),thickness)
    if tool=='eyedropper':
        pic2=screen.copy()
        tool='Eyedropper'
    if tool=='Eyedropper':#proceeds to second part of the eyedropper tool 
        if mb[0]==1 and canvas.collidepoint(mx,my):
            screen.blit(pic,(0,0))
            screen.blit(pic2,(0,0))

            draw.circle(screen,(0),(mx,my),10,1)#draws the eyedropper circle which selects the colour
            drawColor=screen.get_at((mx,my))#gets color 
        if mb[0]==0:
            screen.blit(pic2,(0,0))
            draw.rect(screen,(drawColor),(350,5,850,590),5)#shows color which is selected
            draw.rect(screen,(drawColor),(350,600,850,33),5)# "    "     "     "    "  

                          ###STAMPS###

    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='yellowstamp':
        screen.blit(pic,(0,0))
        yellowstamp=image.load("Rick stamps/showmewhatyougot.png")#loads picture again so it wont be blurry when transforming
        yellowstamp=transform.scale(yellowstamp,(50+thickness,70+thickness))# transforms pictures based on what u make it (scroll the mouse wheel)
        screen.blit(yellowstamp,(mx-30,my-30))#blits the picture where ever the mouse pos is
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='rick':
        screen.blit(pic,(0,0)) 
        rick=image.load("Rick stamps/rick1.png")
        rick=transform.scale(rick,(70+thickness,70+thickness))
        screen.blit(rick,(mx-40,my-40))
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='morty':
        screen.blit(pic,(0,0))
        morty=image.load("Rick stamps/morty1.png")
        morty=transform.scale(morty,(70+thickness,70+thickness))
        screen.blit(morty,(mx-30,my-40))
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='picklerick':
        screen.blit(pic,(0,0))
        picklerick=image.load("Rick stamps/picklerick.png") 
        picklerick=transform.scale(picklerick,(70+thickness,70+thickness))
        screen.blit(picklerick,(mx-40,my-30))
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='mrp':
        screen.blit(pic,(0,0))
        mrp=image.load("Rick stamps/stamp5.png") 
        mrp=transform.scale(mrp,(100+thickness,100+thickness))
        screen.blit(mrp,(mx-45,my-50)) 
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='mrm':
        screen.blit(pic,(0,0))
        mrm=image.load("Rick stamps/mrm.png") 
        mrm=transform.scale(mrm,(100+thickness,100+thickness))
        screen.blit(mrm,(mx-40,my-40)) 
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='bp':
        screen.blit(pic,(0,0))
        bp=image.load("Rick stamps/bp.png") 
        bp=transform.scale(bp,(150+thickness,150+thickness))
        screen.blit(bp,(mx-65,my-60))
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='em':
        screen.blit(pic,(0,0))
        em=image.load("Rick stamps/evilmor.png") 
        em=transform.scale(em,(100+thickness,100+thickness))
        screen.blit(em,(mx-60,my-60))
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='dr':
        screen.blit(pic,(0,0))
        dr=image.load("Rick stamps/dumbrick.png") 
        dr=transform.scale(dr,(73+thickness,100+thickness))
        screen.blit(dr,(mx-40,my-50))
    if  canvas.collidepoint(mx,my) and mb[0]==1 and tool=='jerry':
        screen.blit(pic,(0,0))
        jerry=image.load("Rick stamps/jerry.png") 
        jerry=transform.scale(jerry,(100+thickness,100+thickness))
        screen.blit(jerry,(mx-50,my-55))
                        #SHAPES#

    if  tool=='line':
        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.blit(pic,(0,0)) 
            draw.line(screen,(drawColor),(startx,starty),(mx,my),int(thickness)) 
            draw.circle(screen,drawColor,(startx,starty),thickness//2)
            draw.circle(screen,drawColor,(mx,my),thickness//2)
    if  tool=='rect':
        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.blit(pic,(0,0)) 
            draw.rect(screen, (drawColor),(startx,starty,mx-startx,my-starty),thickness)#height and width for rectangle determined by getting distance from mouse pos to start point
            draw.circle(screen,drawColor,(mx,my),thickness//2)
            draw.circle(screen,drawColor,(startx,starty),thickness//2)
            draw.circle(screen,drawColor,(mx,starty),thickness//2)
            draw.circle(screen,drawColor,(startx,my),thickness//2)
    if  tool=='randshape':
        tiptext=myfont.render("POLYGON & CUT EXIT-RIGHT CLICK",True,(0,255,255))
        screen.blit(tiptext,(802,605))
        if canvas.collidepoint(mx,my):
            if mb[0]==1:
                polypts.append((startx,starty))#adds the initial point of the line where you clicked to the list
                if len(polypts)>1:
                    draw.line(screen,drawColor,(polypts[-2]),(polypts[-1]),thickness)#draws line from end point of last line to mouse pos.
            if mb[2]==1 and len(polypts)>1:
                draw.polygon(screen,drawColor,polypts,thickness)#once you right click, it takes all the points and makes a polygon
                polypts=[]#empties list
    if tool=='circle':
        if canvas.collidepoint(mx,my)  and mb[0]==1:
            screen.blit(pic,(0,0)) 
            elRect = Rect(startx,starty,mx-startx,my-starty)
            elRect.normalize()
            if elRect.height<thickness*2 or elRect.width<thickness*2:#if the height and width is less than the radius, it just creates an ellipse with a solid fill
                draw.ellipse(screen,drawColor,(elRect))
            else:
                draw.ellipse(screen,drawColor,(elRect), thickness)
    if tool=='fillcircle':
        if canvas.collidepoint(mx,my)  and mb[0]==1:
            screen.blit(pic,(0,0)) 
            elRect= Rect(startx,starty,mx-startx,my-starty)#Rect function used, the height and width used are the distance between the start point and current pos
            elRect.normalize()#normalizes the Rect
            draw.ellipse(screen,drawColor,(elRect))
    if  tool=='fillrect':
        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.blit(pic,(0,0)) 
            draw.rect(screen, (drawColor),(startx,starty,mx-startx,my-starty))#same thing as the normal rect with no fill, except no thickness here
    if  tool=='fillpoly':
        tiptext=myfont.render("POLYGON & CUT EXIT-RIGHT CLICK",True,(0,255,255))
        screen.blit(tiptext,(802,605))
        if canvas.collidepoint(mx,my):
            if mb[0]==1:
                polypts.append((startx,starty))
                if len(polypts)>1:
                    draw.line(screen,drawColor,(polypts[-2]),(polypts[-1]),thickness)
            if mb[2]==1 and len(polypts)>1:
                draw.polygon(screen,drawColor,polypts)#draws a fill polygon with the polygon points
                polypts=[]#empties list for new polygon 
    if tool=='cut':
        if canvas.collidepoint(mx,my) and mb[0]==1:
            screen.blit(pic,(0,0)) 
            if drawcanvascolor==(0,0,0):
                draw.rect(screen,(255,255,255),(startx,starty,mx-startx,my-starty),1)#used as the item selector (if background of canvas is black, outline is changed to white)
            else: 
                draw.rect(screen,(0),(startx,starty,mx-startx,my-starty),1)#used as the item selector 
            RectCanvas=Rect(startx,starty,mx-startx,my-starty)#items position and size
            RectCanvas.normalize()#normalizes rect
            x=RectCanvas.width#x is set as the width
            y=RectCanvas.height#y is set as the height
            RC=Surface((x,y))#turns it into a surface
            cutbool=True#since something was selected, it is now true
        if canvas.collidepoint(mx,my) and cutbool==True and mb[0]==0:
            startpoint=(startx,starty)
            area=(x,y)
            RC.blit(screen,(0,0),(startpoint,area)) #blits selection onto surface
            draw.rect(screen,(255,255,255),RectCanvas)#cuts item selected - draws white surface over
            pic2=screen.copy() #copies screen for when you want to change location of surface 
            tool='Cut'
            cutbool=False#set back to false
        tiptext=myfont.render("POLYGON & CUT EXIT-RIGHT CLICK",True,(0,255,255))
        screen.blit(tiptext,(802,605))
    if tool=='Cut':
        tiptext=myfont.render("POLYGON & CUT EXIT-RIGHT CLICK",True,(0,255,255))
        screen.blit(tiptext,(802,605))
        if mb[0]==1 and canvas.collidepoint(mx,my):
            screen.blit(pic,(0,0))
            screen.blit(pic2,(0,0))
            screen.blit(RC,(mx,my))#blits new image anywhere
            draw.rect(screen,(drawcanvascolor),(mx,my,x,y),1)#prevents the outline of initial selection area to appear as well
    if tool =='Cut' and mb[2]==1:
        tool='cut' #permanently places the selected item when right clicked, and just goes back to selecting a new item to cut 

                                    #FILE TOOLBAR#

    if  tool=='new':
            #redraws a blank white canvas as well as the box with the thickness and coordinates
            draw.rect(screen,(255,255,255),canvas)
            draw.rect(screen,(0),(350,5,850,590),5)
            drawcanvascolor =(255,255,255)

            draw.rect(screen,(255,255,255),(1100,545,85,45))
            draw.rect(screen,(0),(1100,545,85,45),1) 
            screen.blit(numbersize,(1170,547))
            screen.blit(textsize,(1100,547))

            screen.blit(xvaltext,(1102,558))
            screen.blit(xval,(1160,558))

            screen.blit(yvaltext,(1102,570))
            screen.blit(yval,(1160,570))

            draw.rect(screen,(255,255,255),(355,565,200,25))
            draw.rect(screen,(0,0,0),(355,565,200,25),1)
            screen.blit(tooltext,(450,570))
            screen.blit(selectext,(360,570))

            tool='Pencil'
            drawColor=(0,0,0)

    if tool=='save':
        result = getName(screen,False)        
        if result=="":
           result="unnamed.png"             # calls getName function
        if result[-4:]!=".png" and result[-4:]!=".jpg" and result[-4:]!=".bmp":
            result=result+".png"
        Rcanvas.blit(screen,(0,0),(pos,size))  # Blits canvas to surface (Rcanvas)
        image.save(Rcanvas ,result)  # Save the image to computer
        print(result)
        tool=''
    if tool=='open':#this open tool just makes a movable sticker of a previously saved image 
        result = getName(screen,False)   
        if result=="" or not os.path.isfile(result): #checks if the filename entered exists
            tool=''
            print("Enter a valid filename")#if it doesnt, tells you to retry
            result= getName(screen,False)
        else:
            pic2=screen.copy() #takes another copy of screen in order for there to only be one version of the image when clicked 
            tool='Open'
    if tool=='Open' and canvas.collidepoint(mx,my) and mb[0]==1:
        screen.blit(pic,(0,0))
        screen.blit(pic2,(0,0))
        picc=image.load(result)
        picc=transform.scale(picc,(100+thickness,100+thickness))
        screen.blit(picc,(mx,my))
    if toool=='load': #loads and blit image saved before covering whole canvas 
        result=getName(screen,False)
        if result=="" or not os.path.isfile(result): #checks if the filename entered exists
            tool=''
            print("Enter a valid filename")#if it doesnt, tells you to retry
            result= getName(screen,False)
        else: 
            loadedimg=image.load(result)
            loadedimg=transform.scale(loadedimg,(size))#transforms image so it fits the canvas perfectly 
            screen.blit(loadedimg,(pos))
            toool=''
    omx=mx
    omy=my
    screen.set_clip(None)# stops clipping the canvas 
    display.flip()
font.quit()
del comicFont
quit()
#The endddddddddddddd