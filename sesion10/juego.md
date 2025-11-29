En un juego de rol, los jugadores pueden elegir diferentes
tipos de armas.
Cuando un jugador solicita un arma, el armero utiliza
la herramienta adecuada para crearla
Cada herramienta crea un solo tipo de arma:
- El martillo crea espadas
- La Sierra crea arcos
Todas las armas pueden usarse para atacar
Si el jugador escribe "salir" en lugar de un tipo de arma,
el programa finaliza.

# Análisis
Requisitos:
- En el juego de rol un jugador pueden elegir dos tipos de armas: Espada y Arco.
- El jugador solo debe pedir el tipo de arma que desea.
- Se usa la herramienta adecuada para fabricar cada arma.
- Cada herramienta fabrica un tipo de arma.
- Todas las armas pueden usarse para atacar.
- Si se ingresa "salir" se termina la ejecución.

Objetos:
- Arma (Espada, Arco)
- Herramienta (Martillo, Sierra)
- Armero

Características:
- Arma: (sin características)
- Espada: (Arma)
- Arco: (Arma)
- Herramienta: (sin características)
- Martillo: (Herramienta)
- Sierra: (Herramienta)
- Armero: (sin características)

Acciones:
- Arma: atacar()
- Espada: atacar()
- Arco: atacar()
- Herramienta: fabricar()
- Martillo: fabricar()
- Sierra: fabricar()
- Armero: fabricar arma

```mermaid
classDiagram
    class Arma {
        +atacar()
    }
    class Espada {
        +atacar()
    }
    class Arco {
        +atacar()
    }
    class Herramienta {
        +fabricar()
    }
    class Martillo {
        +fabricar()
    }
    class Sierra {
        +fabricar()
    }
    class Armero {
        +fabricar_arma()
    }
    Arma <|-- Espada
    Arma <|-- Arco
    Herramienta <|-- Martillo
    Herramienta <|-- Sierra
    Herramienta --> Arma
    Armero --> Herramienta
```
