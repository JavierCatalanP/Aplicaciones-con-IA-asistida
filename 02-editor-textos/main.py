import tkinter as tk
from tkinter import filedialog

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de Texto")
        self.master.geometry("800x600")

        # Crear el cuadro de texto
        self.text = tk.Text(self.master, font=("Arial", 12))
        self.text.pack(expand=True, fill="both")
        # Habilitar la opción de copiar y pegar texto usando el botón derecho del ratón
        self.text.bind("<Button-3>", self.show_menu)
        self.text.bind("<Control-c>", self.copy_text)
        self.text.bind("<Control-v>", self.paste_text)

        # Crear el menú de opciones
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo", command=self.new_file)
        filemenu.add_command(label="Abrir", command=self.open_file)
        filemenu.add_command(label="Guardar", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.master.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        self.master.config(menu=menubar)

        # Variables de instancia para el archivo abierto y su contenido
        self.filename = None
        self.filecontent = None

    def show_menu(self, event):
        # Mostrar el menú de opciones de copiar y pegar
        menu = tk.Menu(self.master, tearoff=0)
        menu.add_command(label="Copiar", command=self.copy_text)
        menu.add_command(label="Pegar", command=self.paste_text)
        menu.tk.call("tk_popup", menu, event.x_root, event.y_root)

    def copy_text(self, event=None):
        # Copiar el texto seleccionado al portapapeles
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    def paste_text(self, event=None):
        # Pegar el texto del portapapeles
        self.text.insert("insert", self.text.clipboard_get())

    def new_file(self):
        # Crear un nuevo archivo vacío
        self.filename = None
        self.text.delete("1.0", tk.END)

    def open_file(self):
        # Abrir un diálogo para seleccionar el archivo
        self.filename = filedialog.askopenfilename(initialdir=".", title="Seleccionar archivo",
                                                   filetypes=(
                                                   ("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")))
        # Leer el contenido del archivo seleccionado y mostrarlo en el cuadro de texto
        if self.filename:
            with open(self.filename, "r") as f:
                self.filecontent = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, self.filecontent)

    def save_file(self):
        # Si no hay archivo abierto, mostrar un diálogo de guardar archivo para crear uno nuevo
        if self.filename is None:
            self.filename = filedialog.asksaveasfilename(initialdir=".", title="Guardar archivo como",
                                                         defaultextension=".txt", filetypes=(
                    ("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")))
            if not self.filename:
                return

        # Guardar el contenido actual del cuadro de texto en el archivo seleccionado
        self.filecontent = self.text.get("1.0", tk.END)
        with open(self.filename, "w") as f:
            f.write(self.filecontent)


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
