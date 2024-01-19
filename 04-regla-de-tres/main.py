import tkinter as tk
from tkinter import font


class ReglaDeTres:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Regla de Tres")
        self.root.geometry("400x300")
        self.root.config(bg="#f2f2f2")

        # Creación del formulario
        title_font = font.Font(family="Helvetica", size=20, weight="bold")
        title_label = tk.Label(self.root, text="Regla de Tres", font=title_font, bg="#f2f2f2")
        title_label.pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#f2f2f2")
        form_frame.pack(pady=10)

        form_font = font.Font(family="Helvetica", size=14)

        valor1_label = tk.Label(form_frame, text="Valor 1:", font=form_font, bg="#f2f2f2")
        valor1_label.grid(row=0, column=0, padx=5, pady=5)
        self.valor1 = tk.Entry(form_frame, font=form_font)
        self.valor1.grid(row=0, column=1, padx=5, pady=5)

        valor2_label = tk.Label(form_frame, text="Valor 2:", font=form_font, bg="#f2f2f2")
        valor2_label.grid(row=1, column=0, padx=5, pady=5)
        self.valor2 = tk.Entry(form_frame, font=form_font)
        self.valor2.grid(row=1, column=1, padx=5, pady=5)

        valor3_label = tk.Label(form_frame, text="Valor 3:", font=form_font, bg="#f2f2f2")
        valor3_label.grid(row=2, column=0, padx=5, pady=5)
        self.valor3 = tk.Entry(form_frame, font=form_font)
        self.valor3.grid(row=2, column=1, padx=5, pady=5)

        self.boton = tk.Button(self.root, text="Calcular", font=form_font, bg="#4CAF50", fg="white",
                               command=self.calcular_regla_de_tres)
        self.boton.pack(pady=10)

        self.resultado_label = tk.Label(self.root, text="", font=form_font, bg="#f2f2f2")
        self.resultado_label.pack(pady=10)

    def calcular_regla_de_tres(self):
        # Obtención de los valores ingresados
        valor1 = float(self.valor1.get())
        valor2 = float(self.valor2.get())
        valor3 = float(self.valor3.get())

        # Cálculo de la regla de tres
        resultado = (valor3 * valor2) / valor1

        # Mostrar resultado
        self.resultado_label.config(text=f"Resultado: {resultado}")


# Ejecución del programa
if __name__ == '__main__':
    root = tk.Tk()
    app = ReglaDeTres(root)
    root.mainloop()
