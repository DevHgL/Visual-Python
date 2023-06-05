

import ViewPrincipal
import Grafo
from tkinter import messagebox
from ViewPrincipal import isInt

class ViewGrafo(ViewPrincipal.ViewPrincipal):
    def __init__(self, master=None):
        super().__init__(master)

        self.dirEntrada = "Grafo\\"
        self.dirAlgoritmos = self.dirEntrada + 'Algoritmos\\'

    def LimpaTelaCanvas(self):
        self.areaDesenho.delete('all')
        '''if self.arvore.ObterRaiz() != -1:
            self.arvore.ImprimirVisual()'''


    def ThreadExecutarMenu(self):
        textoPadrao = ''
        if not self.menuDefinido:
            textoPadrao = '\nMenu de opções:\n\n1- Ler grafo\n2- Imprimir'
            self.areaTexto['text'] = textoPadrao
            self.menuDefinido = True

            self.grafo = Grafo.Grafo(self)

        while True:
            strValor = self.LerValor('Opção:')
            if not isInt(strValor):
                valor = 0
            else:
                valor = int(strValor)

            if valor == 1:
                arquivoAlgoritmo = self.dirAlgoritmos + 'LerGrafo.txt'
                self.DefinirPrograma(arquivoAlgoritmo)
                arquivo = self.LerValor('Arquivo:')
                self.grafo.LerGrafo(self.dirEntrada + arquivo)
            elif valor == 2:
                arquivoAlgoritmo = self.dirAlgoritmos + 'LerArvoreBinaria.txt'

            else:
                messagebox.showinfo("Aviso", "Índice de menu não definido!")

