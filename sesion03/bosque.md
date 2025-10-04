En la simulación de un bosque los arboles pueden crecer
tienen una especie y pueden ser frutales o no.
Nacen desde una semilla, y crecen con el tiempo
Cuando llegan a 10 metros de altura pueden dar frutos
Todos los arboles cuando tiene más de 15 metros mueren

# Análisis

Requisitos:
- Crear un árbol
- Los árboles tienen una especie
- Los árboles pueden ser frutales o no
- Los árboles nacen desde una semilla
- Los árboles crecen con el tiempo
- Los árboles dan frutos cuando tienen 10 metros de altura
- Los árboles mueren cuando tienen más de 15 metros

Objetos:
- Árbol

Características:
- Árbol: especie, frutal, altura, vivo

Acciones:
- Árbol: nacer, crecer, dar_frutos, morir

```mermaid
classDiagram
    class Arbol {
        Strign especie
        Bool frutal
        float altura
        Bool vivo
        germinar(especie)
        crecer(metros)
        dar_frutos()
        puede_morir(arbol)
    }
```