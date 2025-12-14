# Análisis
Requisitos:
- Registrar la información general de un edificio, nombre, dirección y composición por pisos
- Asociar pisos al edificio
- Registrar el número identificador de cada piso
- Asociar departamentos y oficinas a un piso
- Registrar el número identificador de cada departamento, un número que comienza con el número de piso seguido de un número de unidad
- Registrar el número identificador de cada oficina, un número que comienza con el número de piso seguido de una letra
- Registrar los inquilinos de un departamento
- Registrar el teléfono de una oficina
- Mostrar la información del edificio de forma jerárquica

Objetos:
- Edificio
- Piso
- Departamento
- Oficina

Características:
- Edificio:
    - nombre
    - direccion
- Piso:
    - numero
- Departamento:
    - numero
    - inquilinos
- Oficina:
    - numero
    - telefono
  
Acciones:
- Edificio:
    - agregar_piso()
    - mostrar_info()
- Piso:
    - agregar_departamento()
    - agregar_oficina()
- Departamento:
    - (sin acciones)
- Oficina:
    - (sin acciones)

# Diseño
Clases:
- Edificio:
  - Nombre: Edificio
  - Atributos:
      - nombre: String
      - direccion: String
  - Métodos:
      - agregar_piso()
      - mostrar_info()
- Piso:
  - Nombre: Piso
  - Atributos:
      - numero: Int
  - Métodos:
      - agregar_departamento()
      - agregar_oficina()
- Departamento:
  - Nombre: Departamento
  - Atributos:
      - numero: Int
      - inquilinos: List[String]
  - Métodos:
      - (sin metodos)
- Oficina:
  - Nombre: Oficina
  - Atributos:
      - numero: String
      - telefono: Int
  - Métodos:
      - (sin metodos)

```mermaid
classDiagram
    class Edificio {
        +nombre: String
        +direccion: String
        +agregar_piso()
        +mostrar_info()
    }
    class Piso {
        +numero: Int
        +agregar_departamento()
        +agregar_oficina()
    }
    class Departamento {
        +numero: Int
        +inquilinos: List[String]
    }
    class Oficina {
        +numero: String
        +telefono: Int
    }
    Edificio *-- Piso
    Piso *-- Departamento
    Piso *-- Oficina
```