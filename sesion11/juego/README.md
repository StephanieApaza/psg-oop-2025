Juega "Piedra, Papel o Tijera" con un jugador y una computadora
Ingresa el nombre del jugador y elige piedra, papel o tijera
La computadora hará su elección al azar
y se determinará el ganador según las reglas del juego
Puede jugar varias rondas hasta que el jugador decida salir
El juego esta compuesto por ambos jugadores
Cuenta con un menú

1. jugar 
2. salir

Elimina la duplicidad del código en OPCIONES almacenando
en paquete que se llame `constantes` y crea un 
archivo `opciones.py` donde almacenes las opciones 
válidas del juego y reglas

El juego debe funcionar con emojis: 🧱, 📄 y ✂️
cambiando en las constantes y la lógica del juego

Crea las reglas del juego en un diccionario 
para determinar el ganador
 
# Analisis
Requisitos:
- El jugador debe ingresar su nombre
- El jugador debe elegir entre piedra, papel o tijera
- La computadora debe elegir al azar entre piedra, papel o tijera
- El juego debe determinar el ganador según las reglas del juego
- El juego debe mostrar el resultado de cada partida
- El juego debe permitir al jugador jugar varias partidas
- El juego debe tener un menú para jugar o salir
- El juego esta compuesto por ambos jugadores (Jugador y Computadora)

Objetos:
- Jugador
- Computadora
- Juego

Características:
- Jugador:
    - nombre
- Computadora:
    - nombre
- Juego: 
    - jugador
    - computadora

Acciones:
- Jugador:
    - elegir
    - validar eleccion
    - ingresar
- Computadora:
    - elegir
- Juego:
    - jugar
    - determinar ganador
    - mostrar elecciones

```mermaid
classDiagram
    class Jugador {
        +nombre: string
        +ingresar(mensaje)
        +validar_eleccion(eleccion)
        +elegir()
    }
    class Computadora {
        +nombre: string
        +elegir()
    }
    class Juego {
        +jugador: Jugador
        +computadora: Computadora
        +determinar_ganador(eleccion_jugador, eleccion_cpu)
        +mostrar_elecciones(jugador, eleccion)
        +jugar()
    }
    Juego *-- Jugador
    Juego *-- Computadora
```