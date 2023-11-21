#!/usr/bin/env python3
import sys
import math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


viewer = [0.0, 0.0, 10.0]

theta = 90.0
phi = 0.0
pix2angle = 1.0

theta_o = 0.0
phi_o = 0.0
scale_o = 1

left_mouse_button_pressed = 0
right_mouse_button_pressed = 0
mouse_x_pos_old = 0
mouse_y_pos_old = 0
delta_x = 0
delta_y = 0
scale = 10.0

xeye_val = 0
yeye_val = 0
zeye_val = 10

upButton = 0
downButton = 0
leftButton = 0
rightButton = 0
plusButton = 0
minusButton = 0

def startup():
    update_viewport(None, 400, 400)
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


def example_object():
    glColor3f(1.0, 1.0, 1.0)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(-90, 0.0, 1.0, 0.0)

    gluSphere(quadric, 1.5, 10, 10)

    glTranslatef(0.0, 0.0, 1.1)
    gluCylinder(quadric, 1.0, 1.5, 1.5, 10, 5)
    glTranslatef(0.0, 0.0, -1.1)

    glTranslatef(0.0, 0.0, -2.6)
    gluCylinder(quadric, 0.0, 1.0, 1.5, 10, 5)
    glTranslatef(0.0, 0.0, 2.6)

    glRotatef(90, 1.0, 0.0, 1.0)
    glTranslatef(0.0, 0.0, 1.5)
    gluCylinder(quadric, 0.1, 0.0, 1.0, 5, 5)
    glTranslatef(0.0, 0.0, -1.5)
    glRotatef(-90, 1.0, 0.0, 1.0)

    glRotatef(-90, 1.0, 0.0, 1.0)
    glTranslatef(0.0, 0.0, 1.5)
    gluCylinder(quadric, 0.1, 0.0, 1.0, 5, 5)
    glTranslatef(0.0, 0.0, -1.5)
    glRotatef(90, 1.0, 0.0, 1.0)

    glRotatef(90, 0.0, 1.0, 0.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    gluDeleteQuadric(quadric)

def xeye(R, theta, phi):
    return R * math.cos(theta) * math.cos(phi)

def yeye(R, theta, phi):
    return R * math.sin(phi)

def zeye(R, theta, phi):
    return R * math.sin(theta) * math.cos(phi)


def render(time):
    global theta
    global phi
    global scale
    global xeye_val
    global yeye_val
    global zeye_val
    global theta_o
    global phi_o
    global scale_o


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    #gluLookAt(viewer[0], viewer[1], viewer[2], 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    theta_pi = theta * (math.pi / 180)
    phi_pi = phi * (math.pi / 180)

    gluLookAt(xeye_val, yeye_val, zeye_val, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)



    if left_mouse_button_pressed:
        theta += delta_x*2 * pix2angle
        phi += -delta_y*2 * pix2angle

        theta_pi = (theta * (math.pi / 180)) % (2*math.pi)
        phi_pi = (phi * (math.pi / 180)) % (2*math.pi)




        xeye_val = xeye(scale, theta_pi, phi_pi)
        yeye_val = yeye(scale, theta_pi, phi_pi)
        zeye_val = zeye(scale, theta_pi, phi_pi)

        # print("x = " + str(xeye_val))
        # print("y = " + str(yeye_val))
        # print("z = " + str(zeye_val))
        # print("t = " + str(theta_pi))
        # print("p = " + str(phi_pi))
        # print("p = " + str(scale))

    if right_mouse_button_pressed:
        scale += delta_x/10 * pix2angle

        if scale > 15:
            scale = 15
        if scale < 5:
            scale = 5

        theta_pi = theta * (math.pi / 180)
        phi_pi = phi * (math.pi / 180)

        xeye_val = xeye(scale, theta_pi, phi_pi)
        yeye_val = yeye(scale, theta_pi, phi_pi)
        zeye_val = zeye(scale, theta_pi, phi_pi)

        # print("x = " + str(xeye_val))
        # print("y = " + str(yeye_val))
        # print("z = " + str(zeye_val))

    if upButton:
        theta_o += 1

    if downButton:
        theta_o -= 1

    if rightButton:
        phi_o += 1

    if leftButton:
        phi_o -= 1

    if plusButton:
        scale_o += 0.1
        if scale_o > 5:
            scale_o = 5

    if minusButton:
        scale_o -= 0.1
        if scale_o < 0.5:
            scale_o = 0.5

    glRotatef(theta_o, 0.0, 1.0, 0.0)
    glRotatef(phi_o,0.0,0.0,1.0)

    glScalef(scale_o,scale_o,scale_o)

    axes()
    example_object()

    glFlush()


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
    global upButton
    global downButton
    global leftButton
    global rightButton
    global plusButton
    global minusButton

    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

        # Obsługa strzałki w górę
    if key == GLFW_KEY_UP and action == GLFW_PRESS:
        upButton = 1
    else:
        upButton = 0

        # Obsługa strzałki w dół
    if key == GLFW_KEY_DOWN and action == GLFW_PRESS:
        downButton = 1
    else:
        downButton = 0

        # Obsługa strzałki w lewo
    if key == GLFW_KEY_LEFT and action == GLFW_PRESS:
        leftButton = 1
    else:
        leftButton = 0

        # Obsługa strzałki w prawo
    if key == GLFW_KEY_RIGHT and action == GLFW_PRESS:
        rightButton = 1
    else:
        rightButton = 0

        # Obsługa klawisza numerycznego '+'
    if key == GLFW_KEY_KP_ADD and action == GLFW_PRESS:
        plusButton = 1
    else:
        plusButton = 0

        # Obsługa klawisza numerycznego '-'
    if key == GLFW_KEY_KP_SUBTRACT and action == GLFW_PRESS:
        minusButton = 1
    else:
        minusButton = 0

def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old
    global delta_y
    global mouse_y_pos_old


    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos

    delta_y = y_pos - mouse_y_pos_old
    mouse_y_pos_old = y_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed
    global right_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0

    if button == GLFW_MOUSE_BUTTON_RIGHT and action == GLFW_PRESS:
        right_mouse_button_pressed = 1
    else:
        right_mouse_button_pressed = 0

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def main():
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
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()