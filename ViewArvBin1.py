import ViewPrincipal
import ArvoreBinaria
from tkinter import messagebox
from ViewPrincipal import isInt


class ViewArvBin1(ViewPrincipal.ViewPrincipal):
    def __init__(self, master=None):
        super().__init__(master)

        self.dirEntrada = "ArvBin1\\"
        self.dirAlgoritmos = self.dirEntrada + 'Algoritmos\\'

    def LimpaTelaCanvas(self):
        self.areaDesenho.delete('all')
        if self.arvore.ObterRaiz() != -1:
            self.arvore.ImprimirVisual()


    def ThreadExecutarMenu(self):
        textoPadrao = ''
        if not self.menuDefinido:
            textoPadrao = '\nMenu de opções:\n\n1- Ler árvore\n2- Imprimir\n3- Altura' + \
                          '\n4- Verificar se um elemento existe'
            self.areaTexto['text'] = textoPadrao
            self.menuDefinido = True

            self.arvore = ArvoreBinaria.ArvoreBinaria(self)

        while True:
            strValor = self.LerValor('Opção:')
            if not isInt(strValor):
                valor = 0
            else:
                valor = int(strValor)

            if valor == 1:
                arquivoAlgoritmo = self.dirAlgoritmos + 'LerArvoreBinaria.txt'
                self.DefinirPrograma(arquivoAlgoritmo)
                arquivo = self.LerValor('Arquivo:')
                self.arvore.LerArvore(self.dirEntrada + arquivo)
            elif valor == 2:
                textoMenuImprimir = '\nSubmenu - Imprimir:\n\n1- Pré-ordem\n2- Em ordem\n3- Pós-ordem\n4- Sair'
                self.areaTexto['text'] = textoMenuImprimir

                while True:
                    strValorSubmenu = self.LerValor('Opção:')
                    if not isInt(strValorSubmenu):
                        valorSubmenu = 0
                    else:
                        valorSubmenu = int(strValorSubmenu)

                    if valorSubmenu == 1:
                        arquivoAlgoritmo = self.dirAlgoritmos + 'ImprimirPreOrdem.txt'
                        self.DefinirPrograma(arquivoAlgoritmo)
                        self.ImprimirPreOrdem(self.arvore.ObterRaiz(), '')
                        self.Aguardar(5)
                        self.arvore.DesmarcarArvore(self.arvore.ObterRaiz())
                    elif valorSubmenu == 2:
                        arquivoAlgoritmo = self.dirAlgoritmos + 'ImprimirEmOrdem.txt'
                        self.DefinirPrograma(arquivoAlgoritmo)
                        self.ImprimirEmOrdem(self.arvore.ObterRaiz(), '')
                        self.Aguardar(5)
                        self.arvore.DesmarcarArvore(self.arvore.ObterRaiz())
                    elif valorSubmenu == 3:
                        arquivoAlgoritmo = self.dirAlgoritmos + 'ImprimirPosOrdem.txt'
                        self.DefinirPrograma(arquivoAlgoritmo)
                        self.ImprimirPosOrdem(self.arvore.ObterRaiz(), '')
                        self.Aguardar(5)
                        self.arvore.DesmarcarArvore(self.arvore.ObterRaiz())
                    elif valorSubmenu == 4:
                        texto = textoPadrao
                        self.areaTexto['text'] = texto
                        break
                    else:
                        messagebox.showinfo("Aviso", "Índice de menu não definido!")
            elif valor == 3:
                arquivoAlgoritmo = self.dirAlgoritmos + 'AlturaArvoreBinaria.txt'
                self.DefinirPrograma(arquivoAlgoritmo)
                valor = self.CalcularAltura(self.arvore.ObterRaiz())
                self.arvore.DestacarRaiz(valor)
                self.EscreverValor('Altura = ' + str(valor))
                self.Aguardar(5)
                self.arvore.ImprimirVisual()
            elif valor == 4:
                arquivoAlgoritmo = self.dirAlgoritmos + 'BuscaArvoreBinaria.txt'
                self.DefinirPrograma(arquivoAlgoritmo)
                strValor = self.LerValor('Valor de x:')
                if not isInt(strValor):
                    self.EscreverValor('Valor ' + strValor + ' não existente!')
                    self.Aguardar(5)
                else:
                    x = int(strValor)
                    valor = self.BucarElemento(self.arvore.ObterRaiz(), x)
                    self.arvore.DestacarRaiz(valor)
                    if valor == 1:
                        self.EscreverValor('Valor ' + str(x) + ' existente!')
                    else:
                        self.EscreverValor('Valor ' + str(x) + ' não existente!')
                    self.Aguardar(5)
                    self.arvore.ImprimirVisual()
            else:
                messagebox.showinfo("Aviso", "Índice de menu não definido!")

    def ImprimirPreOrdem(self, pos, texto):

        # Not NULL
        if self.arvore.RetornarObjeto(pos, 'info') != -1:
            texto += str(self.arvore.RetornarObjeto(pos, 'info')) + ' '
            self.EscreverValor(texto)
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, esquerda=1)
            texto = self.ImprimirPreOrdem(self.arvore.RetornarObjeto(pos, 'esq'), texto)

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, direita=1)
            texto = self.ImprimirPreOrdem(self.arvore.RetornarObjeto(pos, 'dir'), texto)

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
        else:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
        return texto

    def ImprimirEmOrdem(self, pos, texto):

        # Not NULL
        if self.arvore.RetornarObjeto(pos, 'info') != -1:
            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, esquerda=1)
            texto = self.ImprimirEmOrdem(self.arvore.RetornarObjeto(pos, 'esq'), texto)

            texto += str(self.arvore.RetornarObjeto(pos, 'info')) + ' '
            self.EscreverValor(texto)

            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, direita=1)
            texto = self.ImprimirEmOrdem(self.arvore.RetornarObjeto(pos, 'dir'), texto)

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
        else:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
        return texto

    def ImprimirPosOrdem(self, pos, texto):

        # Not NULL
        if self.arvore.RetornarObjeto(pos, 'info') != -1:

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, esquerda=1)
            texto = self.ImprimirPosOrdem(self.arvore.RetornarObjeto(pos, 'esq'), texto)

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, direita=1)
            texto = self.ImprimirPosOrdem(self.arvore.RetornarObjeto(pos, 'dir'), texto)

            texto += str(self.arvore.RetornarObjeto(pos, 'info')) + ' '
            self.EscreverValor(texto)

            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
        else:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
        return texto

    def CalcularAltura(self, pos):
        if self.arvore.RetornarObjeto(pos, 'info') == -1:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)

            return 0
        else:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, esquerda=1)
            he = self.CalcularAltura(self.arvore.RetornarObjeto(pos, 'esq'))

            self.arvore.DestacarRetorno(self.arvore.RetornarObjeto(pos, 'esq'), 'e', he)

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, direita=1)
            hd = self.CalcularAltura(self.arvore.RetornarObjeto(pos, 'dir'))

            self.arvore.DestacarRetorno(self.arvore.RetornarObjeto(pos, 'dir'), 'd', hd)

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)

            if he > hd:
                return he + 1
            else:
                return hd + 1

    def BucarElemento(self, pos, x):
        if self.arvore.RetornarObjeto(pos, 'info') == -1:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
            return 0
        else:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
            if self.arvore.RetornarObjeto(pos, 'info') == x:
                return 1
            else:
                self.arvore.MarcarNo(pos, caixa=0, esquerda=1)
                if self.BucarElemento(self.arvore.RetornarObjeto(pos, 'esq'), x) == 1:
                    self.arvore.DestacarRetorno(self.arvore.RetornarObjeto(pos, 'esq'), 'e', 1)
                    self.arvore.MarcarNo(pos, caixa=1)
                    self.Aguardar(1)
                    self.arvore.MarcarNo(pos, caixa=0)
                    return 1
                else:
                    self.arvore.DestacarRetorno(self.arvore.RetornarObjeto(pos, 'esq'), 'e', 0)
                    self.arvore.MarcarNo(pos, caixa=1)
                    self.Aguardar(1)
                    self.arvore.MarcarNo(pos, caixa=0, direita=1)
                    ret = self.BucarElemento(self.arvore.RetornarObjeto(pos, 'dir'), x)
                    self.arvore.DestacarRetorno(self.arvore.RetornarObjeto(pos, 'dir'), 'd', ret)
                    self.arvore.MarcarNo(pos, caixa=1)
                    self.Aguardar(1)
                    self.arvore.MarcarNo(pos, caixa=0)
                    return ret
