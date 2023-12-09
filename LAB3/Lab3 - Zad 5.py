import sys
import math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


viewer = [0.0, 0.0, 10.0]

theta = 90.0
phi = 0.0
pix2angle = 1.0

left_mouse_button_pressed = 0
right_mouse_button_pressed = 0
mouse_x_pos_old = 0
mouse_y_pos_old = 0
delta_x = 0
delta_y = 0
R = 10.0

xeye_val = 0
yeye_val = 0
zeye_val = 10

x_center_pos = 0
y_center_pos = 0
z_center_pos = 0

upButton = 0
downButton = 0
leftButton = 0
rightButton = 0

wButton = 0
sButton = 0
aButton = 0
dButton = 0

plusButton = 0
minusButton = 0

ctrlButton = 0
shiftButton = 0

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

def xeye(R, theta, phi):
    return R * math.cos(theta) * math.cos(phi)

def yeye(R, theta, phi):
    return R * math.sin(phi)

def zeye(R, theta, phi):
    return R * math.sin(theta) * math.cos(phi)


def render(time,deep):
    global theta
    global phi
    global R
    global xeye_val
    global yeye_val
    global zeye_val
    global x_center_pos
    global y_center_pos
    global z_center_pos


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    theta_pi = theta * (math.pi / 180)
    phi_pi = phi * (math.pi / 180)

    theta_pi = (theta * (math.pi / 180)) % (2 * math.pi)
    phi_pi = (phi * (math.pi / 180)) % (2 * math.pi)

    xeye_val = xeye(R, theta_pi, phi_pi)
    yeye_val = yeye(R, theta_pi, phi_pi)
    zeye_val = zeye(R, theta_pi, phi_pi)

    gluLookAt(xeye_val, yeye_val, zeye_val, x_center_pos, y_center_pos, z_center_pos, 0.0, 1.0, 0.0)


    if upButton:
        y_center_pos += 0.2

    if downButton:
        y_center_pos -= 0.2

    if rightButton:
        x_center_pos += 0.2

    if leftButton:
        x_center_pos -= 0.2


    if wButton:
        phi += 1

    if sButton:
        phi -= 1

    if aButton:
        theta += 1

    if dButton:
        theta -= 1


    if plusButton:
        R -= 0.1

    if minusButton:
        R += 0.1

    if ctrlButton:
        z_center_pos += 0.2

    if shiftButton:
        z_center_pos -= 0.2

    #axes()

    if deep == 0:
        printPiramid(-5, -5, -5, 10, 10)
    else:
        calculatePiramideLocation(-5,-5,-5,10,10,deep,1)

    draw_sphere(0.3,x_center_pos, y_center_pos, z_center_pos)

    glFlush()

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

def draw_sphere(radius, x, y, z, slices=32, stacks=16):
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)

    for i in range(stacks):
        lat0 = math.pi * (-0.5 + (i / stacks))
        lat1 = math.pi * (-0.5 + ((i + 1) / stacks))

        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)

        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)

        for j in range(slices + 1):
            lng = 2 * math.pi * (j / slices)
            x0 = x + zr0 * math.cos(lng)
            y0 = y + zr0 * math.sin(lng)

            x1 = x + zr1 * math.cos(lng)
            y1 = y + zr1 * math.sin(lng)

            glNormal3f(x0 - x, y0 - y, z0)
            glVertex3f(x0, y0, z + z0)

            glNormal3f(x1 - x, y1 - y, z1)
            glVertex3f(x1, y1, z + z1)

    glEnd()


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
    global wButton
    global sButton
    global aButton
    global dButton
    global plusButton
    global minusButton
    global ctrlButton
    global shiftButton

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

    if key == GLFW_KEY_W and action == GLFW_PRESS:
        wButton = 1
    elif key == GLFW_KEY_W and action == GLFW_RELEASE:
        wButton = 0

    if key == GLFW_KEY_S and action == GLFW_PRESS:
        sButton = 1
    elif key == GLFW_KEY_S and action == GLFW_RELEASE:
        sButton = 0

    if key == GLFW_KEY_A and action == GLFW_PRESS:
        aButton = 1
    elif key == GLFW_KEY_A and action == GLFW_RELEASE:
        aButton = 0

    if key == GLFW_KEY_D and action == GLFW_PRESS:
        dButton = 1
    elif key == GLFW_KEY_D and action == GLFW_RELEASE:
        dButton = 0

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

    if key == GLFW_KEY_LEFT_CONTROL and action == GLFW_PRESS:
        ctrlButton = 1
    else:
        ctrlButton = 0

    if key == GLFW_KEY_LEFT_SHIFT and action == GLFW_PRESS:
        shiftButton = 1
    else:
        shiftButton = 0

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


def main(deep):
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
        render(glfwGetTime(),deep)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    deep = int(input("Poziom iteracji:"))
    main(deep)