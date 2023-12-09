import sys
import numpy

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *



def startup():
    update_viewport(None, 1000, 1000)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def printPiramid(x,y,z,high,width):
    # Podstawa piramidy
    glColor3f(0.3, 0.5, 0.2)
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x + width, y, z)
    glVertex3f(x + width, y, z + width)
    glVertex3f(x, y, z + width)
    glEnd()

    # Ściany piramidy
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(x, y, z)
    glVertex3f(x + width, y, z)
    glVertex3f(x + width / 2, y + high, z + width / 2)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(x + width, y, z)
    glVertex3f(x + width, y, z + width)
    glVertex3f(x + width / 2, y + high, z + width / 2)

    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(x + width, y, z + width)
    glVertex3f(x, y, z + width)
    glVertex3f(x + width / 2, y + high, z + width / 2)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(x, y, z + width)
    glVertex3f(x, y, z)
    glVertex3f(x + width / 2, y + high, z + width / 2)
    glEnd()

def calculatePiramideLocation(x,y,z,high,width,deep,curddeep):
    if(curddeep == deep):
        printPiramid(x, y, z, high/2, width/2)
        printPiramid(x + width / 2, y, z, high / 2, width / 2)
        printPiramid(x , y , z + width / 2, high / 2, width / 2)
        printPiramid(x + width / 2, y , z + width / 2, high / 2, width / 2)
        printPiramid(x + width / 4, y + high / 2, z + width / 4, high / 2, width / 2)
    else:
        calculatePiramideLocation(x, y, z, high / 2, width / 2,deep,curddeep+1)
        calculatePiramideLocation(x + width / 2, y, z, high / 2, width / 2,deep,curddeep+1)
        calculatePiramideLocation(x, y, z + width / 2, high / 2, width / 2,deep,curddeep+1)
        calculatePiramideLocation(x + width / 2, y, z + width / 2, high / 2, width / 2,deep,curddeep+1)
        calculatePiramideLocation(x + width / 4, y + high / 2, z + width / 4, high / 2, width / 2,deep,curddeep+1)



def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def render(time,deep):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    spin(time*3.1415)
    #axes()
    if deep == 0:
        printPiramid(-5, -5, -5, 10, 10)
    else:
        calculatePiramideLocation(-5,-5,-5,10,10,deep,1)

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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main(deep):
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
        render(glfwGetTime(),deep)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    deep = int(input("Poziom iteracji:"))
    main(deep)