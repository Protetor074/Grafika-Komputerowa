#!/usr/bin/env python3
import sys
import numpy

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

from PIL import Image


viewer = [0.0, 0.0, 10.0]

theta = 0.0
phi = 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
mouse_x_pos_old = 0
delta_x = 0

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

buttonNum8 = 0
buttonNum2 = 0
buttonNum4 = 0
buttonNum6 = 0
buttonZ = 0
buttonX = 0
image1 = Image
image2 = Image
start = 0

def startup():
    global image1
    global image2
    update_viewport(None, 400, 400)
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

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_CULL_FACE)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    image1 = Image.open("M4_t.tga")
    image2 = Image.open("zloto.tga")

    glTexImage2D(
        GL_TEXTURE_2D, 0, 3, image1.size[0], image1.size[1], 0,
        GL_RGB, GL_UNSIGNED_BYTE, image1.tobytes("raw", "RGB", 0, -1)
    )


def shutdown():
    pass


def render(time,tab,tab_graph,n):
    global theta
    global phi
    global buttonNum8
    global buttonNum2
    global buttonNum4
    global buttonNum6
    global buttonZ
    global buttonX

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle

    if buttonNum6 == 1:
        theta += 1.0

    if buttonNum4 == 1:
        theta -= 1.0

    if buttonNum8 == 1:
        phi += 1.0

    if buttonNum2 == 1:
        phi -= 1.0

    glRotatef(theta, 0.0, 1.0, 0.0)
    glRotatef(phi, 1.0, 0.0, 0.0)

    z1(tab,tab_graph, n)

    glFlush()

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

def calculate_texture(tab,n):
    tab_graph = numpy.zeros((n, n,2))

    for i in range(n):
        for j in range(n):
            if(tab[i][j][0] == 0):
                tab_graph[i][j][0] = (0 + (tab[i][j][2] / 5)) / 2
            elif(tab[i][j][2] == 0):
                tab_graph[i][j][0] = ((tab[i][j][0] / 5) + 0) / 2
            else:
                tab_graph[i][j][0] = ((tab[i][j][0] / 5) + (tab[i][j][2] / 5)) / 2

            if(tab[i][j][1] == 0):
                tab_graph[i][j][1] = 0
            else:
                tab_graph[i][j][1] = tab[i][j][1]/5
            #print(tab_graph[i][j][1])
    return tab_graph

def z1(tab,tab_graph,n):
    #n=6 i-0-4 - 5var
    colmod = False
    for i in range(int(n/2)):
        glBegin(GL_TRIANGLE_STRIP)
        #Zmiana kolejności wierzchołków 1 połówka
        for j in range(n):
            glTexCoord2f(tab_graph[i][j][0], tab_graph[i][j][1])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])

            glTexCoord2f(tab_graph[i + 1][j][0], tab_graph[i + 1][j][1])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
        i = int(n - i - 2)
        for j in range(n):
            glTexCoord2f(tab_graph[i + 1][j][0], tab_graph[i + 1][j][1])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])

            glTexCoord2f(tab_graph[i][j][0], tab_graph[i][j][1])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
        glEnd()
        colmod = not colmod



def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    global buttonNum8
    global buttonNum2
    global buttonNum4
    global buttonNum6
    global buttonZ
    global buttonX

    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

    if key == GLFW_KEY_KP_8 and action == GLFW_PRESS:
        buttonNum8 = 1
    else:
        buttonNum8 = 0

    if key == GLFW_KEY_KP_2 and action == GLFW_PRESS:
        buttonNum2 = 1
    else:
        buttonNum2 = 0

    if key == GLFW_KEY_KP_4 and action == GLFW_PRESS:
        buttonNum4 = 1
    else:
        buttonNum4 = 0

    if key == GLFW_KEY_KP_6 and action == GLFW_PRESS:
        buttonNum6 = 1
    else:
        buttonNum6 = 0

    if key == GLFW_KEY_Z and action == GLFW_PRESS:
        buttonZ = 1
    else:
        buttonZ = 0

    if key == GLFW_KEY_X and action == GLFW_PRESS:
        buttonX = 1
    else:
        buttonX = 0

def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0


def main(tab,tab_graph,n):
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(),tab,tab_graph,n)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    n = 50
    # Ymin = 0
    # Ymax = 0
    # Xmin = 0
    # Xmax = 0
    # Zmin = 0
    # Zmax = 0
    tab = calculate(n)
    # for i in range(n):
    #     if Xmin >  numpy.min(tab[i][0]):
    #         Xmin = numpy.min(tab[i][0])
    #     if Xmax <  numpy.max(tab[i][0]):
    #         Xmax = numpy.max(tab[i][0])
    #
    #     if Ymin >  numpy.min(tab[i][1]):
    #         Ymin = numpy.min(tab[i][1])
    #     if Ymax <  numpy.max(tab[i][1]):
    #         Ymax = numpy.max(tab[i][1])
    #
    #     if Zmin >  numpy.min(tab[i][2]):
    #         Zmin = numpy.min(tab[i][2])
    #     if Zmax <  numpy.max(tab[i][2]):
    #         Zmax = numpy.max(tab[i][2])

    # print(Xmin)
    # print(Xmax)
    # print(Ymin)
    # print(Ymax)
    # print(Zmin)
    # print(Zmax)
    tab_graph = calculate_texture(tab,n)
    #print(tab_graph)
    #print(tab)
    main(tab,tab_graph,n)