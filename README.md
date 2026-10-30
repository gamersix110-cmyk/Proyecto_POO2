# 📚 Gestor de Libros

## Descripción del proyecto

**Gestor de Libros** es una aplicación de escritorio desarrollada en Python que permite administrar una colección de libros mediante una interfaz gráfica. Su propósito es facilitar el registro, consulta, modificación y lectura de libros de manera sencilla.

El programa utiliza la biblioteca Tkinter para crear la interfaz gráfica y archivos JSON para almacenar la información, permitiendo conservar los registros aunque se cierre la aplicación.

## Tecnologías utilizadas

* **Python:** lenguaje de programación principal.
* **Tkinter:** biblioteca utilizada para desarrollar la interfaz gráfica.
* **JSON:** formato utilizado para almacenar y recuperar la información de los libros.
* **OS:** módulo utilizado para administrar las rutas y carpetas donde se guardan los datos.

## Funcionalidades principales

El programa cuenta con las siguientes opciones:

### 1. Crear libro

Permite registrar un nuevo libro ingresando los siguientes datos:

* Título.
* Autor.
* Número de páginas.
* ISBN.

El programa valida que los campos estén completos y que el número de páginas sea un valor numérico válido.

### 2. Mostrar libros

Permite consultar todos los libros registrados y visualizar su información.

Además, clasifica automáticamente los libros de acuerdo con su cantidad de páginas:

* **Libro corto:** tiene 200 páginas o menos.
* **Libro largo:** tiene más de 200 páginas.

### 3. Modificar libro

Permite buscar un libro mediante su título y actualizar su información.

Actualmente se pueden modificar:

* Autor.
* Número de páginas.

### 4. Leer página

Permite simular la lectura de un libro página por página.

Cada vez que se utiliza esta opción, el programa muestra la página actual y avanza automáticamente a la siguiente. Cuando se alcanza el límite de páginas, informa que el libro ya terminó de leerse.

### 5. Salir

Cierra la aplicación.

## Estructura del proyecto

El proyecto está organizado mediante archivos Python y archivos JSON.

```text
Proyecto/
│
├── main.py
│
├── Clases/
│   └── classLibro.py
│
└── src/
    └── config/
        └── libros.json
```

### Descripción de los archivos

| Archivo         | Descripción                                                                               |
| --------------- | ----------------------------------------------------------------------------------------- |
| `main.py`       | Contiene la interfaz gráfica, las funciones principales y el funcionamiento del programa. |
| `classLibro.py` | Define la clase Libro y sus atributos y métodos.                                          |
| `libros.json`   | Almacena la información de los libros registrados.                                        |

## Programación orientada a objetos

El programa utiliza programación orientada a objetos mediante la clase `Libro`.

Cada objeto representa un libro y contiene los siguientes atributos:

* `titulo`: nombre del libro.
* `autor`: nombre del autor.
* `numero_de_paginas`: cantidad total de páginas.
* `isbn`: identificador del libro.
* `pagina_actual`: página en la que se encuentra la lectura.

La clase también contiene métodos para leer una página, consultar la información del libro, obtener su título y modificar algunos de sus datos.

## Almacenamiento de información

La información se guarda en un archivo JSON ubicado en:

```text
src/config/libros.json
```

El programa comprueba si existe la carpeta necesaria y, si no existe, la crea automáticamente.

Cuando se registra o modifica un libro, los datos se guardan en el archivo JSON. Al iniciar la aplicación, los registros se cargan automáticamente.

**Nota:** La posición de lectura (`pagina_actual`) se mantiene durante la ejecución, pero no se guarda en el archivo JSON. Por lo tanto, al reiniciar el programa, la lectura comienza nuevamente desde la primera página.

## Instalación y ejecución

### Requisitos

* Tener Python instalado.
* Contar con los archivos del proyecto.
* Mantener la estructura de carpetas indicada anteriormente.

No es necesario instalar bibliotecas externas, ya que el programa utiliza módulos incluidos en Python.

### Pasos para ejecutar

1. Descargar o copiar la carpeta del proyecto.
2. Verificar que los archivos estén organizados correctamente.
3. Abrir una terminal dentro de la carpeta principal.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

5. Se abrirá la ventana principal del Gestor de Libros.

## Interfaz gráfica

La interfaz fue desarrollada con Tkinter y cuenta con:

* Campos de texto para ingresar los datos del libro.
* Botones para ejecutar las diferentes funciones.
* Ventana de mensajes para mostrar información, confirmaciones y errores.
* Diseño visual con fondo turquesa y botones de color azul claro.

## Objetivo del proyecto

Desarrollar una aplicación que permita aplicar conceptos de programación en Python, programación orientada a objetos, manejo de archivos JSON y creación de interfaces gráficas.

El proyecto busca ofrecer una herramienta sencilla para administrar una colección de libros y practicar el desarrollo de aplicaciones mediante la separación de clases, funciones y almacenamiento de datos.

---

**Proyecto:** Gestor de Libros
**Lenguaje:** Python
**Interfaz gráfica:** Tkinter
**Almacenamiento:** JSON
