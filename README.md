# Clean Code
Practica de limpieza de codigo hecho por 
- Fabricio Daniel Lara Valencia
- Diego Alonso Gomez Martin del Campo

## Objetivo
- Practicar el flujo de trabajo de Git: crear ramas, hacer commits, Pull Requests y Code
Review.
- Aplicar principios de Clean Code para mejorar legibilidad y estructura del código.
- Colaborar en equipo revisando y mejorando el código de otros compañeros.

## Codigo base
```bash
import random

def startGame():
    number = random.randint(1, 20)
    guess = 0
    attempts = 0

    print("Adivina el número entre 1 y 20")
    while guess != number:
        guess = int(input("Ingresa tu intento: "))
    attempts += 1

    if guess < number:
        print("Muy bajo")
    elif guess > number:
        print("Muy alto")
    elif guess == number:
        print("¡Correcto!")
    else:
        print("Error")

    print("Número de intentos:", attempts)

startGame()
```
## Cambios hechos
Se implemento una refactorizacion basa en la programacion orientada objetos, abstrayendo los atributos pertinente y encapsulando los metodos en un clase para mantenerlo mas ordenado y escalable.

## Como correr el proyecto
Primeramente se tiene que copiar el repositorio a la computadora usando:
```bash
git clone https://github.com/Fabricio1210/Clean_Code.git
```
luego se tiene que situar en la carpeta base del proyecto:
```bash
cd C://...
```
Por ultimo se corre el comando para comenzar el programa.
```bash
python .\GuessTheNumberGame.py
```
