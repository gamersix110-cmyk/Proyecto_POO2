import tkinter as tk
from tkinter import messagebox
from Clases.classLibro import Libro
import os
import json

libros = []

#Ruta del archivo
RUTA = os.path.join("src", "config", "libros.json")

#Funciones
def asegurar_directorio():
    carpeta = os.path.dirname(RUTA)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

def guardar_libros():
    asegurar_directorio()
    try:
        data = [
            {
                "titulo": l.titulo,
                "autor": l.autor,
                "numero_de_paginas": l.numero_de_paginas,
                "isbn": l.isbn
            }
            for l in libros
        ]
        with open(RUTA, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

def cargar_libros():
    asegurar_directorio()
    if not os.path.exists(RUTA):
        with open(RUTA, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
        return

    try:
        with open(RUTA, "r", encoding="utf-8") as f:
            data = json.load(f)
        libros.clear()
        for item in data:
            try:
                nuevo_libro = Libro(
                    item["titulo"],
                    item["autor"],
                    int(item["numero_de_paginas"]),
                    item["isbn"]
                )
                libros.append(nuevo_libro)
            except:
                pass
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

def crear_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    numero_de_paginas = entry_paginas.get()
    isbn = entry_isbn.get()

    if not titulo or not autor or not numero_de_paginas.isdigit() or not isbn:
        messagebox.showerror("Error", "Por favor ingresa datos válidos.")
        return

    nuevo_libro = Libro(titulo, autor, int(numero_de_paginas), isbn)
    libros.append(nuevo_libro)
    guardar_libros()
    messagebox.showinfo("Éxito", f"Se ha creado el libro '{titulo}' y guardado en el registro.")
    limpiar_campos()

def mostrar_libros():
    if not libros:
        messagebox.showinfo("Sin libros", "No hay libros registrados.")
        return
    
    info = ""
    for l in libros:
        tipo_libro = "Libro largo" if l.numero_de_paginas > 200 else "Libro corto"
        info += (
            f"Título: {l.titulo}\n"
            f"Autor: {l.autor}\n"
            f"Número de páginas: {l.numero_de_paginas}\n"
            f"ISBN: {l.isbn}\n"
            f"{tipo_libro}\n"
            f"{'-'*40}\n"
        )

    messagebox.showinfo("Lista de libros", info)

def modificar_libro():
    titulo = entry_titulo.get()
    for l in libros:
        if l.get_titulo() == titulo:
            nuevo_autor = entry_autor.get()
            nuevas_paginas = entry_paginas.get()

            if nuevo_autor:
                l.set_autor(nuevo_autor)
            if nuevas_paginas.isdigit():
                l.set_paginas(int(nuevas_paginas))

            guardar_libros()
            messagebox.showinfo("Modificado", f"Datos de '{titulo}' actualizados y guardados.")
            limpiar_campos()
            return
    messagebox.showwarning("No encontrado", f"No se encontró un libro titulado '{titulo}'.")

def leer_libro():
    titulo = entry_titulo.get()
    for l in libros:
        if l.get_titulo() == titulo:
            messagebox.showinfo("Leyendo", l.leer_página())
            return
    messagebox.showwarning("No encontrado", f"No se encontró un libro titulado '{titulo}'.")

def limpiar_campos():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_paginas.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)

#Crear ventana
ventana = tk.Tk()
ventana.title("Gestor de Libros")
ventana.geometry("470x470")
ventana.config(bg="#8EDEE0")

# Etiquetas y Cajas de Texto
tk.Label(ventana, text="Título:", bg="#E8F0F2", font=("Arial", 11)).pack(pady=3)
entry_titulo = tk.Entry(ventana, bg="white", font=("Arial", 10))
entry_titulo.pack()

tk.Label(ventana, text="Autor:", bg="#E8F0F2", font=("Arial", 11)).pack(pady=3)
entry_autor = tk.Entry(ventana, bg="white", font=("Arial", 10))
entry_autor.pack()

tk.Label(ventana, text="Número de Páginas:", bg="#E8F0F2", font=("Arial", 11)).pack(pady=3)
entry_paginas = tk.Entry(ventana, bg="white", font=("Arial", 10))
entry_paginas.pack()

tk.Label(ventana, text="ISBN:", bg="#E8F0F2", font=("Arial", 11)).pack(pady=3)
entry_isbn = tk.Entry(ventana, bg="white", font=("Arial", 10))
entry_isbn.pack()

# Botones
tk.Button(ventana, text="Crear Libro", command=crear_libro, bg="#A1C6EA", width=20).pack(pady=5)
tk.Button(ventana, text="Mostrar Libros", command=mostrar_libros, bg="#A1C6EA", width=20).pack(pady=5)
tk.Button(ventana, text="Modificar Libro", command=modificar_libro, bg="#A1C6EA", width=20).pack(pady=5)
tk.Button(ventana, text="Leer Página", command=leer_libro, bg="#A1C6EA", width=20).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.destroy, bg="#E03939", width=20).pack(pady=10)

# Cargar libros al iniciar
cargar_libros()

ventana.mainloop()