# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:21:18 2015

@author: lvrizzo
"""
import turtle
window= turtle.Screen()
window.bgcolor("Black")
window.title("Jogo da Forca")

linha=turtle.Turtle()
linha.speed(5)
linha.pencolor("White")

linha.penup()
linha.setpos(-300,0)
linha.pendown ()
linha.left(90)
linha.forward(50)
linha.left(270)
linha.forward(100)
linha.left(270)
linha.forward(50)
linha.left(270)
linha.forward(100)
linha.penup()
linha.setpos(-250,50)#poste
linha.pendown()
linha.right(90)
linha.fd(200)
linha.right(90)
linha.fd(100)
linha.right(90)
linha.fd(25)#fim do poste da forca
linha.penup() #position(-150,225)
linha.setpos(-165,210)#head
linha.pendown()
linha.circle(15)
linha.penup()
linha.setpos(-150,195)#pescoço
linha.pendown()
linha.down()
linha.forward(10)
linha.forward(20)
linha.penup()
linha.setpos(-150,185)#regiao do ombro
linha.left(45)#braco esquerdo
linha.pendown()
linha.fd(20)
linha.penup()
linha.setpos(-150,185)#regiao do ombro
linha.right(90)#braco direito
linha.pendown()
linha.forward(20)
linha.penup()
linha.setpos(-150,165)#umbigo
linha.pendown()
linha.fd(30)#perna esquerda
linha.penup()
linha.setpos(-150,165)#umbigo
linha.pendown()
linha.left(90)#perna direita 
linha.fd(30)
linha.penup()
linha.setpos(-165,195)
#linha.forward(35)
window.exitonclick()


