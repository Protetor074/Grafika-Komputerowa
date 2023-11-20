#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random

def startup():
    update_viewport(None, 1000, 1000)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

#Część odpowiedzialna za rysownaie
def render(time,xlocation, ylocation, width, height,d):
    glClear(GL_COLOR_BUFFER_BIT)
    printRectangele(xlocation, ylocation, width, height, 1, 0, 0)
    printCarpet(xlocation,ylocation,width,height,d)


def printCarpet(xlocation, ylocation, width, height,d):
    if d!=0:
        printRectangele(xlocation, ylocation, width / 3, height / 3, 1, 1, 1)
        d=d-1
        printCarpet(xlocation - (width / 3), ylocation + (height / 3), width / 3, height / 3, d)
        printCarpet(xlocation, ylocation + (height / 3), width / 3, height / 3, d)
        printCarpet(xlocation + (width / 3), ylocation + (height / 3), width / 3, height / 3, d)

        printCarpet(xlocation - (width / 3), ylocation, width / 3, height / 3, d)
        printCarpet(xlocation + (width / 3), ylocation, width / 3, height / 3, d)

        printCarpet(xlocation - (width / 3), ylocation - (height / 3), width / 3, height / 3, d)
        printCarpet(xlocation, ylocation - (height / 3), width / 3, height / 3, d)
        printCarpet(xlocation + (width / 3), ylocation - (height / 3), width / 3, height / 3, d)

def printRectangele(xlocation,ylocation,width,height,colR,colG,colB):
    #print(width,hight)

    ur = xlocation - (width / 2), ylocation + (height / 2)
    ul = xlocation + (width / 2), ylocation + (height / 2)
    br = xlocation - (width / 2), ylocation - (height / 2)
    bl = xlocation + (width / 2), ylocation - (height / 2)


    glColor3f(colR,colG,colB)
    glBegin(GL_TRIANGLES)
    glVertex2f(ur[0],ur[1])
    glVertex2f(ul[0],ul[1])
    glVertex2f(br[0],br[1])
    glEnd()

    glColor3f(colR,colG,colB)
    glBegin(GL_TRIANGLES)
    glVertex2f(bl[0],bl[1])
    glVertex2f(ul[0],ul[1])
    glVertex2f(br[0],br[1])
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



def main(xlocation, ylocation, width, height, d):
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

        render(glfwGetTime(),xlocation, ylocation, width, height, d)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    xlocation, ylocation, width, height = getPrintingValue()

    d = int(input("Poziom iteracji"))
    main(xlocation, ylocation, width, height, d )
