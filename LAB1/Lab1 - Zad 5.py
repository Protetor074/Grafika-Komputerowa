#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import math

def startup():
    update_viewport(None, 1000, 1000)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def obroc_wektor(ax, ay, bx, by, kat):
    kat_radiany = math.radians(kat)
    x_przesuniete = bx + (ax - bx) * math.cos(kat_radiany) - (ay - by) * math.sin(kat_radiany)
    y_przesuniete = by + (ax - bx) * math.sin(kat_radiany) + (ay - by) * math.cos(kat_radiany)
    return x_przesuniete, y_przesuniete

#Część odpowiedzialna za rysownaie
def render(time,xStartPoin):
    glClear(GL_COLOR_BUFFER_BIT)
    # xy = 0,90
    # xy1 = obroc_wektor(xy[0],xy[1],0,0,-60)
    # xy2 = obroc_wektor(xy1[0],xy1[1] , 2*xy1[0],xy1[1]-xy1[1], 60)
    # xy3 = obroc_wektor(xy2[0], xy2[1],xy2[0], xy2[1] - xy1[1]+xy2[1], 60)
    # xy4 = -xy2[0],xy2[1]
    # xy5 = -xy1[0],xy1[1]
    #
    #
    #
    # if d==0:
    #     printLine(xy[0], xy1[0], xy[1], xy1[1])
    #     printLine(xy1[0], xy2[0], xy1[1], xy2[1])
    #     printLine(xy2[0], xy3[0], xy2[1], xy3[1])
    #     printLine(xy3[0], xy4[0], xy3[1], xy4[1])
    #     printLine(xy4[0], xy5[0], xy4[1], xy5[1])
    #     printLine(xy5[0], xy[0], xy5[1], xy[1])
    # else:
    #     dp = 1
    #     printCrashedLine(xy[0], xy1[0], xy[1], xy1[1], d, dp)
    #     printCrashedLine(xy1[0], xy2[0], xy1[1], xy2[1], d, dp)
    #     printCrashedLine(xy2[0], xy3[0], xy2[1], xy3[1], d, dp)
    #     printCrashedLine(xy3[0], xy4[0], xy3[1], xy4[1], d, dp)
    #     printCrashedLine(xy4[0], xy5[0], xy4[1], xy5[1], d, dp)
    #     printCrashedLine(xy5[0], xy[0], xy5[1], xy[1], d, dp)

    xy = 0, 75
    xy1 = 72, -50
    xy2 = -72, -50

    if d==0:
        printLine(xy[0], xy1[0], xy[1], xy1[1])
        printLine(xy1[0], xy2[0], xy1[1], xy2[1])
        printLine(xy2[0], xy[0], xy2[1], xy[1])

    else:
        dp = 1
        printCrashedLine(xy[0], xy1[0], xy[1], xy1[1], d, dp)
        printCrashedLine(xy1[0], xy2[0], xy1[1], xy2[1], d, dp)
        printCrashedLine(xy2[0], xy[0], xy2[1], xy[1], d, dp)



def printCrashedLine(xStartPoint,xEndPoint,yStartPoint,yEndPoint,d,dp):
    xleng = xEndPoint - xStartPoint
    yleng = yEndPoint - yStartPoint

    line1 = xStartPoint, xStartPoint + xleng / 3, yStartPoint, yStartPoint + yleng / 3
    # line1_1 = xStartPoint, xStartPoint + xleng / 9, yStartPoint, yStartPoint + yleng / 9
    # line1_2 = xStartPoint + xleng * 2 / 3, xStartPoint + xleng / 3, yStartPoint + yleng * 2 / 3, yStartPoint + yleng / 3
    x, y = obroc_wektor(xStartPoint + xleng / 3, yStartPoint + yleng / 3, xStartPoint + xleng * 2 / 3,
                        yStartPoint + yleng * 2 / 3, -60)
    line2 = xStartPoint + xleng / 3, x, yStartPoint + yleng / 3, y
    line3 = x, xStartPoint + xleng * 2 / 3, y, yStartPoint + yleng * 2 / 3
    line4 = xStartPoint + xleng * 2 / 3, xEndPoint, yStartPoint + yleng * 2 / 3, yEndPoint
    # line4_1 = xStartPoint + xleng * 2 / 3, xStartPoint + xleng * 7 / 9, yStartPoint + yleng * 2 / 3, yStartPoint + yleng * 7/ 9
    # line4_2 = xStartPoint + xleng * 8 / 9, xEndPoint, yStartPoint + yleng * 8/ 9, yEndPoint

    if d!=dp:
        dp=dp+1
        printCrashedLine(line1[0], line1[1], line1[2], line1[3], d, dp)
        printCrashedLine(line2[0], line2[1], line2[2], line2[3], d, dp)
        printCrashedLine(line3[0], line3[1], line3[2], line3[3], d, dp)
        printCrashedLine(line4[0], line4[1], line4[2], line4[3], d, dp)
    if d==dp:
        # printLine(line1_1[0], line1_1[1], line1_1[2], line1_1[3])
        # printLine(line1_2[0], line1_2[1], line1_2[2], line1_2[3])
        printLine(line1[0], line1[1], line1[2], line1[3])
        printLine(line2[0], line2[1], line2[2], line2[3])
        # printLine(line2[0],line3[1],line2[2],line3[3])
        printLine(line3[0], line3[1], line3[2], line3[3])
        printLine(line4[0], line4[1], line4[2], line4[3])
        # printLine(line4_1[0], line4_1[1], line4_1[2], line4_1[3])
        # printLine(line4_2[0], line4_2[1], line4_2[2], line4_2[3])


def printLine(xLocationStart,xLocationEnd,yLocationStart,yLoacationEnd):

    glColor3f(0,0,0)
    glBegin(GL_LINES)
    glVertex2f(xLocationStart,yLocationStart)
    glVertex2f(xLocationEnd,yLoacationEnd)
    glEnd()
    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def getPrintingValue():
    xlocation = int(input("Podaj pozycje początkową x:"))
    ylocation = int(input("Podaj pozycję początkową y:"))
    width = int(input("Podaj szerokość prostoąta:"))
    height = int(input("Podaj wysokość prostokąta:"))
    return xlocation,ylocation,width,height



def main(d):
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(1000, 1000, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):

        render(glfwGetTime(),d)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    d = int(input("Poziom iteracji"))
    #d=5
    main(d)
