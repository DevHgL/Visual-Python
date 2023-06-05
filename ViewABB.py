
import ViewPrincipal
import ABB
from tkinter import messagebox
from ViewPrincipal import isInt

class ViewABB(ViewPrincipal.ViewPrincipal):
    def __init__(self, master=None):
        super().__init__(master)

        self.dirEntrada = "ABB\\"
        self.dirAlgoritmos = self.dirEntrada + 'Algoritmos\\'

    def LimpaTelaCanvas(self):
        self.areaDesenho.delete('all')
        if self.arvore.ObterRaiz() != -1:
            self.arvore.ImprimirVisual()


    def ThreadExecutarMenu(self):
        textoPadrao = ''
        if not self.menuDefinido:
            textoPadrao = '\nMenu de opções:\n\n1- Ler árvore\n2- Imprimir\n3- Altura' + \
                          '\n4- Verificar existência (geral)\n5- Verificar existência (ABB)' + \
                          '\n6- Inserir elemento\n7- Remover elemento\n8- Imprimir valores maiores que X'
            self.areaTexto['text'] = textoPadrao
            self.menuDefinido = True

            self.arvore = ABB.ABB(self)

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
                textoMenuImprimir = '\nSubmenu - Imprimir:\n\n1- Pré-ordem\n2- Em ordem\n3- Pós-ordem' + \
                                    '\n4- Imprimir Notação\n5- Imprimir em largura\n6- Sair'
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
                        arquivoAlgoritmo = self.dirAlgoritmos + 'ImprimirNotacao.txt'
                        self.DefinirPrograma(arquivoAlgoritmo)
                        self.ImprimirNotacao(self.arvore.ObterRaiz(), '')
                        self.Aguardar(5)
                        self.arvore.DesmarcarArvore(self.arvore.ObterRaiz())
                    elif valorSubmenu == 5:
                        arquivoAlgoritmo = self.dirAlgoritmos + 'ImprimirLargura.txt'
                        self.DefinirPrograma(arquivoAlgoritmo)
                        h = self.CalcularAltura(self.arvore.ObterRaiz(), False)
                        self.ImprimirLargura(h, '')
                        self.Aguardar(5)
                        self.arvore.DesmarcarArvore(self.arvore.ObterRaiz())
                    elif valorSubmenu == 6:
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
            elif valor == 5:
                arquivoAlgoritmo = self.dirAlgoritmos + 'BuscaABB.txt'
                self.DefinirPrograma(arquivoAlgoritmo)
                strValor = self.LerValor('Valor de x:')
                if not isInt(strValor):
                    self.EscreverValor('Valor ' + strValor + ' não existente!')
                    self.Aguardar(5)
                else:
                    x = int(strValor)
                    valor = self.BucarElementoABB(self.arvore.ObterRaiz(), x)
                    self.arvore.DestacarRaiz(valor)
                    if valor == 1:
                        self.EscreverValor('Valor ' + str(x) + ' existente!')
                    else:
                        self.EscreverValor('Valor ' + str(x) + ' não existente!')
                    self.Aguardar(5)
                    self.arvore.ImprimirVisual()
            elif valor == 6:
                arquivoAlgoritmo = self.dirAlgoritmos + 'inserir.txt'
                self.DefinirPrograma(arquivoAlgoritmo)
                strValor = self.LerValor('Valor:')
                if not isInt(strValor):
                    messagebox.showinfo("Aviso", "Valor deve ser inteiro!")
                else:
                    x = int(strValor)
                    self.AcharEDestacarPosicaoABB(self.arvore.ObterRaiz(), x)
                    self.Aguardar(5)
                    self.arvore.InserirElemento(self.arvore.ObterRaiz(), x)
                    self.arvore.ImprimirVisual()
            elif valor == 7:
                arquivoAlgoritmo = self.dirAlgoritmos + 'remover.txt'
                self.DefinirPrograma(arquivoAlgoritmo)
                strValor = self.LerValor('Valor:')
                if not isInt(strValor):
                    messagebox.showinfo("Aviso", "Valor deve ser inteiro!")
                else:
                    x = int(strValor)
                    self.RemoverElemento(x)
            elif valor == 8:
                arquivoAlgoritmo = self.dirAlgoritmos + 'ImprimirMaioresX.txt'
                self.DefinirPrograma(arquivoAlgoritmo)
                strValor = self.LerValor('Valor:')
                if not isInt(strValor):
                    messagebox.showinfo("Aviso", "Valor deve ser inteiro!")
                else:
                    x = int(strValor)
                    self.ImprimirValoreMaiorexX(self.arvore.ObterRaiz(), '', x)
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

    def ImprimirNotacao(self, pos, texto):

        # Not NULL
        if self.arvore.RetornarObjeto(pos, 'info') != -1:
            texto += '(' + str(self.arvore.RetornarObjeto(pos, 'info'))
            self.EscreverValor(texto)
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, esquerda=1)
            texto = self.ImprimirNotacao(self.arvore.RetornarObjeto(pos, 'esq'), texto)

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)

            self.arvore.MarcarNo(pos, caixa=0, direita=1)
            texto = self.ImprimirNotacao(self.arvore.RetornarObjeto(pos, 'dir'), texto)

            texto += ')'
            self.EscreverValor(texto)
            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
        else:
            texto += '(-1)'
            self.EscreverValor(texto)
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)
        return texto

    def ImprimirNivel(self, pos, cont, n, texto):
        if self.arvore.RetornarObjeto(pos, 'info') != -1:
            if cont == n:
                self.arvore.MarcarNo(pos, caixa=1)
                texto += str(self.arvore.RetornarObjeto(pos, 'info')) + ' '
                self.EscreverValor(texto)
                self.Aguardar(1)
            else:
                texto = self.ImprimirNivel(self.arvore.RetornarObjeto(pos, 'esq'), cont+1, n, texto)
                texto = self.ImprimirNivel(self.arvore.RetornarObjeto(pos, 'dir'), cont+1, n, texto)

        return texto


    def ImprimirLargura(self, h, texto):
        for i in range(0, h):
            texto = self.ImprimirNivel(self.arvore.ObterRaiz(), 0, i, texto)
            texto += '\n'
            self.arvore.DesmarcarArvore(self.arvore.ObterRaiz())


    def CalcularAltura(self, pos, animacao=True):
        if self.arvore.RetornarObjeto(pos, 'info') == -1:

            if animacao:
                self.arvore.MarcarNo(pos, caixa=1, centro=1)
                self.Aguardar(1)
                self.arvore.MarcarNo(pos, caixa=0)

            return 0
        else:
            if animacao:
                self.arvore.MarcarNo(pos, caixa=1, centro=1)
                self.Aguardar(1)
                self.arvore.MarcarNo(pos, caixa=0, esquerda=1)

            he = self.CalcularAltura(self.arvore.RetornarObjeto(pos, 'esq'), animacao)

            if animacao:
                self.arvore.DestacarRetorno(self.arvore.RetornarObjeto(pos, 'esq'), 'e', he)
                self.arvore.MarcarNo(pos, caixa=1)
                self.Aguardar(1)
                self.arvore.MarcarNo(pos, caixa=0, direita=1)

            hd = self.CalcularAltura(self.arvore.RetornarObjeto(pos, 'dir'), animacao)

            if animacao:
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

    def BucarElementoABB(self, pos, x):
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
            elif x < self.arvore.RetornarObjeto(pos, 'info'):
                self.arvore.MarcarNo(pos, caixa=0, esquerda=1)
                ret = self.BucarElementoABB(self.arvore.RetornarObjeto(pos, 'esq'), x)
                self.arvore.DestacarRetorno(self.arvore.RetornarObjeto(pos, 'esq'), 'e', ret)
                self.arvore.MarcarNo(pos, caixa=1)
                self.Aguardar(1)
                self.arvore.MarcarNo(pos, caixa=0)
                return ret
            else:
                self.arvore.MarcarNo(pos, caixa=0, direita=1)
                ret = self.BucarElementoABB(self.arvore.RetornarObjeto(pos, 'dir'), x)
                self.arvore.DestacarRetorno(self.arvore.RetornarObjeto(pos, 'dir'), 'd', ret)
                self.arvore.MarcarNo(pos, caixa=1)
                self.Aguardar(1)
                self.arvore.MarcarNo(pos, caixa=0)
                return ret

    def AcharEDestacarPosicaoABB(self, pos, x):
        if self.arvore.RetornarObjeto(pos, 'info') == -1:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            return -1
        else:
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            if self.arvore.RetornarObjeto(pos, 'info') == x:
                return pos
            elif x < self.arvore.RetornarObjeto(pos, 'info'):
                self.arvore.MarcarNo(pos, caixa=0, esquerda=1)
                ret = self.AcharEDestacarPosicaoABB(self.arvore.RetornarObjeto(pos, 'esq'), x)
                return ret
            else:
                self.arvore.MarcarNo(pos, caixa=0, direita=1)
                ret = self.AcharEDestacarPosicaoABB(self.arvore.RetornarObjeto(pos, 'dir'), x)
                return ret

    def RemoverElemento(self, x):
        pos = self.AcharEDestacarPosicaoABB(self.arvore.ObterRaiz(), x)
        if pos == -1:
            messagebox.showinfo("Aviso", "Valor não existente!")
        else:
            if self.arvore.RetornarObjeto(self.arvore.RetornarObjeto(pos, 'esq'), 'info') != -1 and \
                    self.arvore.RetornarObjeto(self.arvore.RetornarObjeto(pos, 'dir'), 'info') != -1:

                #Encontrar o maior elemento da esquerda
                aux = self.arvore.RetornarObjeto(pos, 'esq')
                while self.arvore.RetornarObjeto(self.arvore.RetornarObjeto(aux, 'dir'), 'info') != -1:
                    aux = self.arvore.RetornarObjeto(aux, 'dir')

                self.arvore.MarcarNo(pos, esquerda=1)
                self.Aguardar(2)
                self.AcharEDestacarPosicaoABB(self.arvore.RetornarObjeto(pos, 'esq'),
                                              self.arvore.RetornarObjeto(aux, 'info'))

                self.arvore.AjustarInfoNo(pos, self.arvore.RetornarObjeto(aux, 'info'))
                self.arvore.AjustarInfoNo(aux, self.arvore.RetornarObjeto(pos, 'info'))

                self.Aguardar(2)

                self.arvore.MarcarNoComX(aux)
            else:
                self.arvore.MarcarNoComX(pos)

            self.arvore.RemoverElemento(self.arvore.ObterRaiz(), x)
            self.Aguardar(5)
            self.arvore.ImprimirVisual()


    def ImprimirValoreMaiorexX(self, pos, texto, x):

        # Not NULL
        if self.arvore.RetornarObjeto(pos, 'info') != -1:

            if self.arvore.RetornarObjeto(pos, 'info') > x:
                texto += str(self.arvore.RetornarObjeto(pos, 'info')) + ' '
                self.EscreverValor(texto)
            self.arvore.MarcarNo(pos, caixa=1, centro=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)

            if x < self.arvore.RetornarObjeto(pos, 'info'):
                self.arvore.MarcarNo(pos, esquerda=1)
                texto = self.ImprimirValoreMaiorexX(self.arvore.RetornarObjeto(pos, 'esq'), texto, x)

                self.arvore.MarcarNo(pos, caixa=1)
                self.Aguardar(1)

                self.arvore.MarcarNo(pos, caixa=0, direita=1)
                texto = self.ImprimirValoreMaiorexX(self.arvore.RetornarObjeto(pos, 'dir'), texto, x)

            else:
                self.arvore.MarcarNo(pos, direita=1)
                texto = self.ImprimirValoreMaiorexX(self.arvore.RetornarObjeto(pos, 'dir'), texto, x)

            self.arvore.MarcarNo(pos, caixa=1)
            self.Aguardar(1)
            self.arvore.MarcarNo(pos, caixa=0)

        return texto


