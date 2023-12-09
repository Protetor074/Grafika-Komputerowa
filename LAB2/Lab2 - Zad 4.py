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

def z1(tab,n):
    #n=6 i-0-4 - 5var
    colmod = False
    for i in range(int(n/2)):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):
            if(colmod):
                glColor3f(1, 0.6, 0.3)
            else:
                glColor3f(0.3, 1, 0.6)
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if (colmod):
                glColor3f(0.3, 1, 0.6)
            else:
                glColor3f(1, 0.6, 0.3)
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
        i = int(n - i - 2)
        for j in range(n):
            if (colmod):
                glColor3f(0.3, 1, 0.6)
            else:
                glColor3f(1, 0.6, 0.3)
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            if (colmod):
                glColor3f(1, 0.6, 0.3)
            else:
                glColor3f(0.3, 1, 0.6)
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
        glEnd()
        colmod = not colmod


    # for i in range(int(n/2)):
    #     for j in range(n):
    #         if j + 1 < n:
    #             glColor3f(1, 0.6, 0.3)
    #             glVertex3f(tab[i][j+1][0], tab[i][j+1][1], tab[i][j+1][2])
    #             glColor3f(0.3, 1, 0.6)
    #             glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
    #             glColor3f(0.6, 0.3, 1)
    #             glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
    #
    #             glColor3f(0.3, 0.6, 1)
    #             glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1], tab[i][j + 1][2])
    #             glColor3f(1, 0.3, 0.6)
    #             glVertex3f(tab[i+1][j+1][0], tab[i+1][j+1][1], tab[i+1][j+1][2])
    #             glColor3f(0.6, 1, 0.3)
    #             glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
    #
    #         i = int(n - i-2)
    #         for j in range(n):
    #             if j + 1 < n:
    #                 glColor3f(1, 0.6, 0.3)
    #                 glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1], tab[i][j + 1][2])
    #                 glColor3f(0.3, 1, 0.6)
    #                 glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
    #                 glColor3f(0.6, 0.3, 1)
    #                 glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
    #
    #                 glColor3f(0.3, 0.6, 1)
    #                 glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1], tab[i][j + 1][2])
    #                 glColor3f(1, 0.3, 0.6)
    #                 glVertex3f(tab[i + 1][j + 1][0], tab[i + 1][j + 1][1], tab[i + 1][j + 1][2])
    #                 glColor3f(0.6, 1, 0.3)
    #                 glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])


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


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def render(time,tab,n):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    spin(time*3.1415*10)
    axes()
    z1(tab,n)

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


def main(tab,n):
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
        render(glfwGetTime(),tab,n)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    n = 50
    tab = calculate(n)
    main(tab,n)