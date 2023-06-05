
import ViewPrincipal
import GrafoAF
from tkinter import messagebox
from ViewPrincipal import isInt


class ViewGrafoAF(ViewPrincipal.ViewPrincipal):
    def __init__(self, master=None):
        super().__init__(master)

        self.dirEntrada = "GrafoAF\\"
        self.dirAlgoritmos = self.dirEntrada + 'Algoritmos\\'

    def LimpaTelaCanvas(self):
        self.areaDesenho.delete('all')


    def ThreadExecutarMenu(self):
        textoPadrao = ''
        if not self.menuDefinido:
            textoPadrao = '\nMenu de opções:\n\n1- Ler grafo'
            self.areaTexto['text'] = textoPadrao
            self.menuDefinido = True

            self.grafo = GrafoAF.GrafoAF(self)

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

            else:
                messagebox.showinfo("Aviso", "Índice de menu não definido!")
