from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
import pygame as pg
import time
from math import *
from numpy import *

global xrot
global theta


def main():
    global xrot
    global theta
    pg.init()

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GL_DEPTH_BUFFER_BIT)
    glutInitWindowSize(1100, 900)
    glutInitWindowPosition(450, 5)
    glutCreateWindow("Light")
    glutSpecialFunc(specialkeys)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-0.1, 0.1, -0.1, 0.1, 0.2, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    theta = 0
    xrot = -14
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        glClearColor(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        z = cos(xrot)
        glPushMatrix()
        glRotatef(-60, 1, 0, 0)
        glRotatef(33, 0, 0, 1)
        glTranslatef(2, 3, -2)
        glPushMatrix()
        glRotatef(theta, 0, 1, 0)
        glTranslatef(z, 0, z)

        position = [0, 0, 1, 1]
        glLightfv(GL_LIGHT0, GL_POSITION, position)

        glTranslatef(0, 0, 1)
        glScalef(0.2, 0.2, 0.2)
        glColor3f(1, 1, 1)
        glutSolidSphere(0.275, 250, 250)
        glPopMatrix()

        glColor3f(0, 1, 0)
        glutSolidTorus(0.275, 0.85, 250, 250)

        glPopMatrix()

        glutSwapBuffers()

    return


def specialkeys(key, x, y):
    global xrot
    global theta
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:
        if xrot <= 14:  # Клавиша вверх
            xrot += 0.5  # Уменьшаем угол вращения по оси Х
            theta += 15
        else:
            xrot = -14
            theta += 15
    glutPostRedisplay()  # Вызываем процедуру перерисовки


main()
