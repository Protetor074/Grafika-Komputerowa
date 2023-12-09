import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


viewer = [0.0, 0.0, 10.0]

theta = 0.0
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

buttonPlus = 0
buttonMinus = 0
buttonA = 0
buttonD = 0
buttonS = 0
button1 = 0
button2 = 0
button3 = 0
button4 = 0
buttonCTRL = 0


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    updateData()
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

def updateData():
    global buttonPlus
    global buttonMinus
    global buttonA
    global buttonD
    global buttonS
    global button1
    global button2
    global button3
    global button4
    global buttonCTRL
    dif = 0.01

    if buttonCTRL == 1:
        buttonA = 0
        buttonD = 0
        buttonS = 0
        button1 = 0
        button2 = 0
        button3 = 0
        button4 = 0

    #Ambient
    if buttonA == 1:
        if button1 == 1:
            if buttonPlus == 1:
                if(light_ambient[0] <= 1):
                    light_ambient[0] += dif
                    print(light_ambient)

            if buttonMinus == 1:
                if(light_ambient[0] >= 0):
                    light_ambient[0] -= dif
                    print(light_ambient)

        if button2 == 1:
            if buttonPlus == 1:
                if (light_ambient[1] <= 1):
                    light_ambient[1] += dif
                    print(light_ambient)

            if buttonMinus == 1:
                if (light_ambient[1] >= 0):
                    light_ambient[1] -= dif
                    print(light_ambient)

        if button3 == 1:
            if buttonPlus == 1:
                if (light_ambient[2] <= 1):
                    light_ambient[2] += dif
                    print(light_ambient)

            if buttonMinus == 1:
                if (light_ambient[2] >= 0):
                    light_ambient[2] -= dif
                    print(light_ambient)

        if button4 == 1:
            if buttonPlus == 1:
                if (light_ambient[3] <= 1):
                    light_ambient[3] += dif
                    print(light_ambient)

            if buttonMinus == 1:
                if (light_ambient[3] >= 0):
                    light_ambient[3] -= dif
                    print(light_ambient)
    #Diffuse
    if buttonD == 1:
        if button1 == 1:
            if buttonPlus == 1:
                if (light_diffuse[0] <= 1):
                    light_diffuse[0] += dif
                    print(light_diffuse)

            if buttonMinus == 1:
                if (light_diffuse[0] >= 0):
                    light_diffuse[0] -= dif
                    print(light_diffuse)

        if button2 == 1:
            if buttonPlus == 1:
                if (light_diffuse[1] <= 1):
                    light_diffuse[1] += dif
                    print(light_diffuse)

            if buttonMinus == 1:
                if (light_diffuse[1] >= 0):
                    light_diffuse[1] -= dif
                    print(light_diffuse)

        if button3 == 1:
            if buttonPlus == 1:
                if (light_diffuse[2] <= 1):
                    light_diffuse[2] += dif
                    print(light_diffuse)

            if buttonMinus == 1:
                if (light_diffuse[2] >= 0):
                    light_diffuse[2] -= dif
                    print(light_diffuse)

        if button4 == 1:
            if buttonPlus == 1:
                if (light_diffuse[3] <= 1):
                    light_diffuse[3] += dif
                    print(light_diffuse)

            if buttonMinus == 1:
                if (light_diffuse[3] >= 0):
                    light_diffuse[3] -= dif
                    print(light_diffuse)
    #Specular
    if buttonS == 1:
        if button1 == 1:
            if buttonPlus == 1:
                if (light_specular[0] <= 1):
                    light_specular[0] += dif
                    print(light_specular)

            if buttonMinus == 1:
                if (light_specular[0] >= 0):
                    light_specular[0] -= dif
                    print(light_specular)

        if button2 == 1:
            if buttonPlus == 1:
                if (light_specular[1] <= 1):
                    light_specular[1] += dif
                    print(light_specular)

            if buttonMinus == 1:
                if (light_specular[1] >= 0):
                    light_specular[1] -= dif
                    print(light_specular)

        if button3 == 1:
            if buttonPlus == 1:
                if (light_specular[2] <= 1):
                    light_specular[2] += dif
                    print(light_specular)

            if buttonMinus == 1:
                if (light_specular[2] >= 0):
                    light_specular[2] -= dif
                    print(light_specular)

        if button4 == 1:
            if buttonPlus == 1:
                if (light_specular[3] <= 1):
                    light_specular[3] += dif
                    print(light_specular)

            if buttonMinus == 1:
                if (light_specular[3] >= 0):
                    light_specular[3] -= dif
                    print(light_specular)

def shutdown():
    pass


def render(time):
    global theta

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    updateData()
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle

    glRotatef(theta, 0.0, 1.0, 0.0)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)

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
    global buttonPlus
    global buttonMinus
    global buttonA
    global buttonD
    global buttonS
    global button1
    global button2
    global button3
    global button4
    global buttonCTRL


    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

    if key == GLFW_KEY_KP_ADD and action == GLFW_PRESS:
        buttonPlus = 1
    else:
        buttonPlus = 0

    if key == GLFW_KEY_KP_SUBTRACT and action == GLFW_PRESS:
        buttonMinus = 1
    else:
        buttonMinus = 0

    if key == GLFW_KEY_A and action == GLFW_PRESS:
        buttonA = 1

    if key == GLFW_KEY_D and action == GLFW_PRESS:
        buttonD = 1

    if key == GLFW_KEY_S and action == GLFW_PRESS:
        buttonS = 1

    if key == GLFW_KEY_1 and action == GLFW_PRESS:
        button1 = 1

    if key == GLFW_KEY_2 and action == GLFW_PRESS:
        button2 = 1

    if key == GLFW_KEY_3 and action == GLFW_PRESS:
        button3 = 1

    if key == GLFW_KEY_4 and action == GLFW_PRESS:
        button4 = 1

    if key == GLFW_KEY_LEFT_CONTROL and action == GLFW_PRESS:
        buttonCTRL = 1
    else:
        buttonCTRL = 0

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