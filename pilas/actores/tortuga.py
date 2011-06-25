# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

import pilas
from pilas.actores import Actor


class Tortuga(Actor):
    "Representa una tortuga que se mueve por la pantalla como la tortuga de Logo."

    def __init__(self, x=0, y=0, dibuja=True):
        self.pizarra = pilas.actores.Pizarra()

        imagen = pilas.imagenes.cargar('tortuga.png')
        Actor.__init__(self, imagen, x=x, y=y)

        self.rotacion = 0
        self.velocidad = 6

        #if dibuja:
        #    self.bajalapiz()
        #else:
        #    self.subelapiz()

    def avanzar(self, pasos):
        self.hacer_luego(pilas.comportamientos.Avanzar(pasos, self.velocidad))

    def giraderecha(self, delta):
        self.hacer_luego(pilas.comportamientos.Girar(abs(delta), self.velocidad))
    
    def giraizquierda(self, delta):
        self.hacer_luego(pilas.comportamientos.Girar(-abs(delta), self.velocidad))

    def actualizar(self):
        self.pizarra.mover_lapiz(self.x, self.y)

    def bajalapiz(self):
        self.hacer_luego(pilas.comportamientos.BajarLapiz())

    def subelapiz(self):
        self.hacer_luego(pilas.comportamientos.SubirLapiz())

    def pon_color(self, color):
        self.hacer_luego(pilas.comportamientos.CambiarColor(color))

    def crear_poligono(self, lados = 4, escala = 100, sentido = -1):
        "dibuja un poligono de n lados"
        for i in range(lados):
            rotacion = 360 / lados
            self.avanzar(escala)
            if sentido == 1:
                self.giraderecha(rotacion)
            else:
                self.giraizquierda(rotacion)
                
    def crear_circulo(self, radio = 30, sentido = -1):
        "dibuja un circulo"
        for i in range(36):
            self.avanzar(radio)
            if sentido == 1:
                self.giraderecha(10)
            else:
                self.giraizquierda(10)

    # Alias de metodos
    av = avanzar
    gd = giraderecha
    gi = giraizquierda
    bl = bajalapiz
    sl = subelapiz
    pc = pon_color


    def get_color(self):
        return self.pizarra.color

    def set_color(self, color):
        self.pizarra.definir_color(color)

    color = property(get_color, set_color)

    def limpiar(self):
        self.pizarra.limpiar()

    def pintar(self, color=None):
        self.pizarra.pintar(color)
