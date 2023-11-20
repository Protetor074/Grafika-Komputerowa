#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

#Część odpowiedzialna za rysownaie
def render(time,xlocation, ylocation, width, height,d):
    glClear(GL_COLOR_BUFFER_BIT)

    print(d)
    width = (width*d)%100
    height = (height*d)%100
    print(width)
    print(height)

    #Prostąkąt z 2 trujkątów

    glBegin(GL_TRIANGLES)
    glColor3f(d*0.1%1, d*0.2%1, d*0.3%1)
    glVertex2f(xlocation - (width / 2), ylocation + (height / 2))

    glColor3f(d*0.4%1, d*0.5%1, d*0.6%1)
    glVertex2f(xlocation + (width / 2), ylocation + (height / 2))

    glColor3f(d*0.7%1, d*0.8%1, d*0.9%1)
    glVertex2f(xlocation - (width / 2), ylocation - (height / 2))
    glEnd()


    glBegin(GL_TRIANGLES)
    glColor3f(0.1/d, 0.2/d, 0.3/d)
    glVertex2f(xlocation + (width / 2), ylocation - (height / 2))
    glColor3f(0.4/d, 0.5/d, 0.6/d)
    glVertex2f(xlocation + (width / 2), ylocation + (height / 2))
    glColor3f(0.7/d, 0.8/d, 0.9/d)
    glVertex2f(xlocation - (width / 2), ylocation - (height / 2))
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

    window = glfwCreateWindow(400, 400, __file__, None, None)
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
    random.seed()
    d = random.random()
    main(xlocation, ylocation, width, height, d )
