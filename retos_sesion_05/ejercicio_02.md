# Escenario
Debes desarrollar un videojuego tipo aventura, donde los personajes tiene distintas habilidades
Cada personaje pertenece a uno o más tipos que definen sus comportamientos:
Nadador: Puede ejecutar la acción nadar(), que representa la acción de desplazarse en el agua.
Volador: Puede ejecutar la acción volar(), que representa la acción de desplazarse por el aire.
En el juego existen tres personajes principales, cada uno con habilidades específicas:
Pez: tiene la habilidad de nadar.
Pájaro: tiene la habilidad de volar.
Pato: tiene ambas habilidades, puede nadar y volar.
Cada personaje debe contar con un método mostrar() que indique el tipo de personaje y su habilidad principal o combinada.

# Análisis
Requisitos:
- Desarrollar un videojuego tipo aventura con personajes que tienen distintas habilidades.
- El tipo nadador puede ejecutar la acción nadar.
- El tipo volador puede ejecutar la acción volar.
- El personaje pez tiene la habilidad de nadar.
- El personaje pájaro tiene la habilidad de volar.
- El personaje pato tiene la habilidad de nadar y volar.

Objetos:
- Nadador (clase padre)
- Volador (clase padre)
- Pez (clase hija)
- Pajaro (clase hija)
- Pato (hereda de Nadador y Volador)

Caracteristicas:
- Nadador:
  - (sin características)
- Volador:
  - (sin características)
- Pez:
  - (sin características)
- Pajaro:
  - (sin características)
- Pato:
  - (sin características)

Acciones:
- Nadador:
  - nadar()
- Volador:
  - volar()
- Pez:
  - mostrar()
- Pajaro:
  - mostrar()
- Pato:
  - mostrar()

```mermaid
classDiagram
    class Nadador {
      +nadar()
    }
    class Volador {
      +volar()
    }
    class Pez {
      +mostrar()
    }
    class Pajaro {
      +mostrar()
    }
    class Pato {
      +mostrar()
    }
    Nadador <|-- Pez
    Volador <|-- Pajaro
    Nadador <|-- Pato
    Volador <|-- Pato
```