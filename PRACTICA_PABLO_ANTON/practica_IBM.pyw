import numpy as np
from tkinter import *
from tkinter import messagebox

def generar_matriz(num_filas, num_columnas):

    matriz = np.random.randint(0, 9, size=(num_filas, num_columnas))

    if num_filas > 25 or num_columnas > 40:
        raise ZeroDivisionError
    return matriz
    


def mostrar_matriz(matriz, frame):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            label = Label(frame, text=str(matriz[i][j]), font=("IBM Plex Sans Seminegrita", 12), fg="snow", padx=1, pady=1, border=3)
            label.grid(row=i, column=j, padx=2, pady=2)
            label.config(background="#4589ff", justify="center")

def mostrar_resultados(row_sum, column_sum, total_sum, frame):
    row_result = Label(frame, text='SUMA DE FILAS: ' +  str(len(row_sum)) + '\n \n'  +  str(row_sum), font=("IBM Plex Sans Seminegrita", 12), background="#012749", fg="#ffb784",pady=4, wraplength=350)
    row_result.pack()
    column_result = Label(frame, text='SUMA DE COLUMNAS: ' + str(len(column_sum)) + '\n \n'  + str(column_sum), font=("IBM Plex Sans Seminegrita", 12), background="#012749", fg="#ffb784", pady=100, wraplength=350)
    column_result.pack()
    total_result = Label(frame, text="SUMA TOTAL: " + str(total_sum), font=("IBM Plex Sans Seminegrita", 12), background="#012749", fg="#ffb784", wraplength=150)
    total_result.pack()

def obtener_datos():
    try:
        num1 = int(fila_entry.get())
        num2 = int(colu_entry.get())

        matriz = generar_matriz(num1, num2)

        # LIMPIAR CONTENIDO EN miFrame_2
        for widget in miFrame_2.winfo_children():
            widget.destroy()

        # LIMPIAR CONTENIDO EN miFrame_3
        for widget in miFrame_3.winfo_children():
            widget.destroy()

        mostrar_matriz(matriz, miFrame_2)

        column_sum = np.sum(matriz, axis=0)
        row_sum = np.sum(matriz, axis=1)
        total_sum = np.sum(matriz)

        mostrar_resultados(row_sum, column_sum, total_sum, miFrame_3)

    except ZeroDivisionError as e:
        messagebox.showinfo(message="Valores introducidos muy elevados para ser representados en la matriz.\nPor favor, introduce valores inferiores de '25' para las filas \ny de '40' para las columnas", title="ERROR DE ENTRADA")
    except ValueError as e:
        messagebox.showinfo(message="Debes introducir números enteros, o alguna casilla está vacía", title="ERROR TIPO DE DATOS")




root = Tk()
root.title("Práctica curso IBM Python")
root.geometry("1200x1080")
root.iconbitmap("ibm-logo-6.ico")
root.config(background="#343a3f")
root.resizable(True, False)

miFrame_0 = Frame(root)
miFrame_0.config(background="#d9fbfb", height=150, width= 700, padx=10, pady=10)
miFrame_0.pack(side="top", fill="x")
logo_ibm = PhotoImage("ibm-logo-6.png")

label_titulo = Label(miFrame_0, text="Programa del curso de IBM para Python", background="#d9fbfb", fg= "navy", font=("IBM Plex Sans Seminegrita", 16))
label_titulo.pack(anchor="center")

miFrame_1 = Frame(root)
miFrame_1.config(background="#012749", padx=2, relief="solid")
miFrame_1.pack(side="left", fill="y", anchor="center")

label_fila = Label(miFrame_1, text="Nº de Filas: ", font=("IBMPlexSans-Light", 10),background="#012749", fg= "snow")
label_fila.grid(row=0, column=0, sticky=W, padx=3)

fila_entry = Entry(miFrame_1)
fila_entry.grid(row=0, column=1, sticky=W, pady=3, padx=3)

label_colu = Label(miFrame_1, text="Nº de Columnas: ", font=("IBMPlexSans-Light", 10),background="#012749", fg= "snow")
label_colu.grid(row=1, column=0, sticky=W, padx=2)

colu_entry = Entry(miFrame_1)
colu_entry.grid(row=1, column=1, sticky=W, pady=3, padx=3)

button_1 = Button(miFrame_1, text="Generar matriz", command=obtener_datos)
button_1.config(justify="center", background="#009d9a", fg="snow", font=("IBMPlexSans-Bold", 11), padx=10, pady=3)
button_1.grid(row=2, column=1, sticky="ew", pady=10)

button_2 = Button(miFrame_1, text="Cerrar programa", command=exit)
button_2.config(justify="center", background="#009d9a", fg="snow", font=("IBMPlexSans-Bold", 11), padx=10, pady=3)
button_2.grid(row=4, column=1, sticky="ew", pady=30)

miFrame_2 = Frame(root)
miFrame_2.config(background="#4589ff", padx=5, pady=5)
miFrame_2.pack(side="left", fill="both", expand=True)

miFrame_3 = Frame(root)
miFrame_3.config(background="#012749", padx=2, relief="solid")
miFrame_3.pack(side="right", fill="y", anchor="center")

root.mainloop()
