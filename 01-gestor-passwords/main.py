import tkinter as tk
import string
import random


# Función para generar la contraseña aleatoria
def generate_password(length):
    # Definir los caracteres permitidos en la contraseña
    allowed_chars = string.ascii_letters + string.digits + string.punctuation

    # Generar la contraseña aleatoria
    password = ''.join(random.choice(allowed_chars) for i in range(length))

    # Mostrar la contraseña en el campo de texto
    password_text.delete('1.0', tk.END)
    password_text.insert('1.0', password)


# Función para copiar la contraseña al portapapeles
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_text.get('1.0', tk.END))


# Función para mostrar el menú contextual
def show_context_menu(event):
    menu.post(event.x_root, event.y_root)


# Crear la ventana principal
root = tk.Tk()
root.title('Generador de contraseñas')

# Crear un marco para la entrada de la longitud de la contraseña
length_frame = tk.Frame(root)
length_frame.pack(padx=10, pady=10)

length_label = tk.Label(length_frame, text='Longitud:')
length_label.pack(side=tk.LEFT)

length_entry = tk.Entry(length_frame)
length_entry.pack(side=tk.LEFT)

# Crear un botón para generar la contraseña
generate_button = tk.Button(root, text='Generar', command=lambda: generate_password(int(length_entry.get())))
generate_button.pack(padx=10, pady=10)

# Crear un campo de texto para mostrar la contraseña generada
password_text = tk.Text(root, font=('Arial', 16), height=1, width=30)
password_text.pack(padx=10, pady=10)

# Crear un menú contextual personalizado
menu = tk.Menu(password_text, tearoff=0)
menu.add_command(label='Copiar', command=copy_password)

# Asociar el menú contextual personalizado con el evento <Button-3>
password_text.bind('<Button-3>', show_context_menu)

# Ejecutar la aplicación
root.mainloop()
