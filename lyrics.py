#!/usr/bin/env python3
import time
import sys
import os

VERDE = "\033[95m"

MORADO_CLARO = "\033[38,129m"

ROSADO = "\033[38,5,205m"

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else `clear`)

===subtitulos = [
    ("My mind says, no you're not good for me" , 1.6),
    ("You're not good,", 0.5),
    ("but my heart's made up on you", 1.5),
    ("My body can't take what you give to me", 1.6)
    ("what you get,", 0.5),
    ("got my heart made up on you", 1.6),
    ("wo oh, wo oh, wo oh", 4.5),
    ("got my heart made up on you", 1.6)
,===

===subtitulos = [
    ("Here we go...", 1.6),
    ("Come with me ...", 1.6),
    ("There's a world out there that we should see...", 2.5),
    ("Take my hand...", 1.6),
    ("Close your eyes... ", 1.6),
    ("With you right here, I'm a rocketeer", 3,2),
    ("Let's fly (fly, fly, fly, fly,)", 4.5),
    ("Up, up, here we go, go", 1.3),
    ("Up, up, here we go, go", 1.3),
    ("Let's fly (fly, fly, fly, fly,)", 4,5),
    ("Up, up, here we gp, go", 1.3),
    ("Where we stop? Nobody knows (knows)", 2,5)
]===

subtitulos = [
    ("Sometimes, you'd ask me fot something different", 1.8),
    ("Hated when you did it,", 1.5),
    ("I wish that you didn't , 2.8),
    ("I would do things and you'd get annoyed", 2.5),
    ("Should've never done them,", 1.6),
    ("I whish I was different", 3.0),
    ("Why do we have to step away now?", 1.3),
    ("It's been a year, been a couple days now", 0.4),
    ("Since you called me", 1.6),
    ("Sayin' you're worried", 2.0),				
    ("Been hard for me dealin' with this space now", 1.2),
    ("No company, wishin' we could sit down", 0.4),
    ("Cause I'm sorry...,", 1.1),
    ("but you don't want me...", 1.1)
]


def escribir_letra_por_letra(texto, velocidad=0.05):
    sys.stdout.write(ROSADO)
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

limpiar_consola()

for texto, delay in subtitulos:
    escribir_letra_por_letra(texto)
    time.sleep(delay)


