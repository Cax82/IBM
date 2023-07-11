import unittest
import numpy as np
from tkinter import *
from tkinter import messagebox
from practica_3_IBM import generar_matriz
from practica_3_IBM import mostrar_matriz


class TestApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.root.geometry("200x200")
        print("----TEST COMPORTAMIENTO INTERFAZ----")

        global fila_entry, colu_entry, miFrame_2, miFrame_3
        miFrame_1 = Frame(self.root)
        miFrame_1.grid()

        fila_entry = Entry(miFrame_1)
        fila_entry.grid(row=0, column=1)

        colu_entry = Entry(miFrame_1)
        colu_entry.grid(row=1, column=1)

        miFrame_2 = Frame(self.root)
        miFrame_2.grid()

        miFrame_3 = Frame(self.root)
        miFrame_3.grid()

    def tearDown(self):
        self.root.destroy()

    def test_generar_matriz(self):
        print("----TEST DE ERROR EN VALORES INTRODUCIDOS----")
        matriz = generar_matriz(3, 4)
        self.assertEqual(matriz.shape, (3, 4))
        self.assertTrue((matriz >= 0).all())
        self.assertTrue((matriz <= 9).all())

        with self.assertRaises(ZeroDivisionError):
            generar_matriz(30, 40)



    def test_mostrar_matriz(self):
        print("----TEST MOSTRAR MATRIZ----")
        matriz = np.array([[1, 2, 3], [4, 5, 6]])
        mostrar_matriz(matriz, miFrame_2)
        labels = miFrame_2.winfo_children()
        self.assertEqual(len(labels), 6)


if __name__ == "__main__":
    unittest.main()
