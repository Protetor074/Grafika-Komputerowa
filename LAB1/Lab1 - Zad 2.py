#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

#Część odpowiedzialna za rysownaie
def render(time,xlocation, ylocation, width, height):
    glClear(GL_COLOR_BUFFER_BIT)

    #print("xCenter  =", xlocation)
    #print("yCenter  =", ylocation)

    #Prostokąt

    #glBegin(GL_QUADS)

    # glColor3f(0.0, 1.0, 0.0)
    # glVertex2f(xlocation - (width / 2), ylocation + (height / 2))
    # #print("V1  =" ,xlocation + (width / 2), ylocation + (height / 2))
    #
    # glColor3f(1.0, 0.0, 0.0)
    # glVertex2f(xlocation - (width/2), ylocation - (height/2))
    # #print("V2  =", xlocation - (width / 2), ylocation - (height / 2))
    #
    # glColor3f(0.0, 0.0, 1.0)
    # glVertex2f(xlocation + (width / 2), ylocation - (height / 2))
    # #print("V3  =", xlocation + (width / 2), ylocation - (height / 2))
    #
    # glColor3f(0.5, 0.5, 0.5)
    # glVertex2f(xlocation + (width/2), ylocation + (height/2))
    # #print("V4  =", xlocation + (width / 2), ylocation + (height / 2))
    # glEnd()

    #Prostąkąt z 2 trujkątów

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(xlocation - (width / 2), ylocation + (height / 2))

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(xlocation + (width / 2), ylocation + (height / 2))

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(xlocation - (width / 2), ylocation - (height / 2))
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(xlocation + (width / 2), ylocation - (height / 2))
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(xlocation + (width / 2), ylocation + (height / 2))
    glColor3f(0.0, 0.0, 1.0)
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



def main(xlocation, ylocation, width, height ):
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

        render(glfwGetTime(),xlocation, ylocation, width, height)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    xlocation, ylocation, width, height = getPrintingValue()
    main(xlocation, ylocation, width, height )
