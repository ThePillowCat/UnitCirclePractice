from pygame import *
from sympy import sin, cos, tan, pi, zoo
from random import *

options = [i for i in range(0, 2001, 30)] + [i for i in range(0, 2001, 45)] + [i for i in range(0, 2001, 60)]
functions = ["sin", "cos", "tan"]
dividers = [2, 2, 2, 2, 2, 4, 4, 4, 6, 6, 6, 6, 1]
questions = []
answers = []

pos = 0

def generateQuestions(deg, rad):
    global options
    global functions
    global questions
    global answers
    for i in range(deg):
        vals = [choice(functions), choice(options)]
        #choice(functions)+"("+str(choice(options))+")"
        questions.append(str(vals[0])+"("+str(vals[1])+"°)")
        answers.append(eval(str(vals[0])+"("+str(vals[1])+"%360*(pi/180)"+")"))
        if (answers[-1] == zoo):
            answers.pop()
            answers.append("undefined")
    for i in range(rad):
        vals = [choice(functions), randint(1,10), choice(dividers)]
        questions.append(str(vals[0])+"("+str(vals[1])+"pi"+"/"+str(vals[2])+")")
        answers.append(eval(str(vals[0])+"("+str(vals[1])+"*pi"+"/"+str(vals[2]) + ")"))
        if (answers[-1] == zoo):
            answers.pop()
            answers.append("undefined")

width,height=800,600
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)

running=True
font.init()

font1 = font.SysFont("Calibri", 50)
font2 = font.SysFont("Calibri", 75)

rad = 0
deg = 0
scr = "Start!"

while running:

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if Rect(0,0,266,100).collidepoint((mx, my)):
                if (rad == 10):
                    rad=0
                rad+=1
            if Rect(266,0,266,100).collidepoint((mx, my)):
                if (deg == 10):
                    deg=0
                deg+=1
            if Rect(266+266,0,266,100).collidepoint((mx, my)):
                if scr == "Start!":
                    questions = []
                    answers = []
                    generateQuestions(deg, rad)
                    scr = "Answers"
                elif scr == "Answers":
                    scr = "Back"
                else:
                    scr = "Start!"

    screen.fill((128, 128, 128))

    draw.line(screen, BLACK, (400, 100), (400, 590))
    draw.line(screen, BLACK, (0, 100), (800, 100))
    draw.line(screen, BLACK, (266, 0), (266, 100))
    draw.line(screen, BLACK, (534, 0), (534, 100))

    #render(text, antialias, color, background=None)
    screen.blit(font1.render("RAD:", True, (0,0,0)), (25,25))
    screen.blit(font1.render(str(rad), True, (0,0,0)), (25+110,25))
    screen.blit(font1.render("DEG:", True, (0,0,0)), (266+25,25))
    screen.blit(font1.render(str(deg), True, (0,0,0)), (266+25+110,25))
    screen.blit(font1.render(str(scr), True, (0,0,0)), (266*2+25,25))

    if (scr == "Answers"):
        for i in range(len(questions)):
            screen.blit(font2.render(str(questions[i]), True, (0,0,0)), (i//5*400+25,110+i%5*100))
    
    if (scr == "Back"):
        for i in range(len(questions)):
            screen.blit(font2.render(str(answers[i])[0:12], True, (0,0,0)), (i//5*400+25,110+i%5*100))

    display.flip()
            
quit()