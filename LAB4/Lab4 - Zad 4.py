#!/usr/bin/env python3
import sys
import numpy

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *


mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001

def startup():
    update_viewport(None, 1000, 1000)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


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

def z1(tab,tabToNormal,n):
    #n=6 i-0-4 - 5var
    colmod = False
    for i in range(int(n/2)):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):
            # if(colmod):
            #     glColor3f(1, 0.6, 0.3)
            # else:
            #     glColor3f(0.3, 1, 0.6)
            glNormal(tabToNormal[i][j][0], tabToNormal[i][j][1], tabToNormal[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            # if (colmod):
            #     glColor3f(0.3, 1, 0.6)
            # else:
            #     glColor3f(1, 0.6, 0.3)
            glNormal(tabToNormal[i+1][j][0], tabToNormal[i+1][j][1], tabToNormal[i+1][j][2])
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
        i = int(n - i - 2)
        for j in range(n):
            # if (colmod):
            #     glColor3f(0.3, 1, 0.6)
            # else:
            #     glColor3f(1, 0.6, 0.3)
            glNormal(tabToNormal[i][j][0], tabToNormal[i][j][1], tabToNormal[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            # if (colmod):
            #     glColor3f(1, 0.6, 0.3)
            # else:
            #     glColor3f(0.3, 1, 0.6)
            glNormal(tabToNormal[i + 1][j][0], tabToNormal[i + 1][j][1], tabToNormal[i + 1][j][2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
        glEnd()
        colmod = not colmod

def calculate(n):
    tab = numpy.zeros((n, n, 3))

    for i in range(n):
        for j in range(n):
            u = i/(n-1)
            v = j/(n-1)
            tab[i][j][0] = (-90 * u**5 + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * cos(pi * v)
            tab[i][j][1] = 160 * u**4 - 320 * u**3 + 160 * u**2 - 5
            tab[i][j][2] = (-90 * u**5 + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * sin(pi * v)
    #print(tab)
    return tab

def calculateNormalVector(n):
    tabToNormal = numpy.zeros((n, n, 3))
    for i in range(0, n):
        for j in range(0, n):
            u = i / (n-1)
            v = j / (n-1)

            xu = (-450 * pow(u, 4) + 900 * pow(u, 3) - 810 * pow(u, 2) + 360 * u - 45) * cos(pi * v)
            xv = pi * (90 * pow(u, 5) - 225 * pow(u, 4) + 270 * pow(u, 3) - 180 * pow(u, 2) + 45 * u) * sin(pi * v)
            yu = 640 * pow(u, 3) - 960 * pow(u, 2) + 320 * u
            yv = 0
            zu = (-450 * pow(u, 4) + 900 * pow(u, 3) - 810 * pow(u, 2) + 360 * u - 45) * sin(pi * v)
            zv = (- pi) * (90 * pow(u, 5) - 225 * pow(u, 4) + 270 * pow(u, 3) - 180 * pow(u, 2) + 45 * u) * cos(pi * v)

            x = yu * zv - zu * yv
            y = zu * xv - xu * zv
            z = xu * yv - yu * xv

            sum = pow(x, 2) + pow(y, 2) + pow(z, 2)
            length = sqrt(sum)

            if length > 0:
                x = x / length
                y = y / length
                z = z / length

            tabToNormal[i][j][0] = x
            tabToNormal[i][j][1] = y
            tabToNormal[i][j][2] = z

    return tabToNormal

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def render(time,tab,tabToNormal,n):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    spin(time*3.1415*10)
    #axes()
    z1(tab,tabToNormal,n)

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


def main(tab,tabToNormal,n):
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
        render(glfwGetTime(),tab,tabToNormal,n)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    n = 50
    tab = calculate(n)
    tabToNormal = calculateNormalVector(n)
    main(tab,tabToNormal,n)