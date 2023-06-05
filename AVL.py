
import ABB
import math

class AVL(ABB.ABB):
    def __init__(self, master):
        super().__init__(master)

    def LerArvore(self, nomeArquivo):
        super().LerArvore(nomeArquivo)
        self.AjustarArvore(self.raiz)

    def AjustarArvore(self, pos, pai=-1):
        self.arvore[pos]['pai'] = pai
        if self.arvore[pos]['info'] != -1:
            he = self.CalcularAltura(self.arvore[pos]['esq'])
            hd = self.CalcularAltura(self.arvore[pos]['dir'])

            self.arvore[pos]['he'] = he
            self.arvore[pos]['hd'] = hd

            self.AjustarArvore(self.arvore[pos]['esq'], pos)
            self.AjustarArvore(self.arvore[pos]['dir'], pos)

    def InserirElemento(self, pos, x, pai=-1):
        #NULL
        if self.arvore[pos]['info'] == -1:
            dice = {'info': -1, 'esq': -1, 'dir': -1, 'max': -1, 'min': -1, 'coordX': -1, 'coordY': -1, 'pai': pos}
            dicd = {'info': -1, 'esq': -1, 'dir': -1, 'max': -1, 'min': -1, 'coordX': -1, 'coordY': -1, 'pai': pos}
            self.arvore[pos]['info'] = x
            self.arvore[pos]['esq'] = self.InserirProximaPosicao(dice)
            self.arvore[pos]['dir'] = self.InserirProximaPosicao(dicd)

            if pai == -1:
                self.raiz = pos

            return pos
        else:
            if x <= self.arvore[pos]['info']:
                return self.InserirElemento(self.arvore[pos]['esq'], x, pos)
            else:
                return self.InserirElemento(self.arvore[pos]['dir'], x, pos)

    def RemoverElemento(self, pos, valor, pai=-1, filho=''):
        #Encontrando o elemento
        if self.arvore[pos]['info'] == valor:
            #É folha?
            if self.arvore[self.arvore[pos]['esq']]['info'] == -1 and \
                    self.arvore[self.arvore[pos]['dir']]['info'] == -1:
                self.listaRemovidos.append(pos)
                self.listaRemovidos.append(self.arvore[pos]['dir'])

                #Raiz
                if pai == -1:
                    self.raiz = self.arvore[pos]['esq']
                else:
                    self.arvore[pai][filho] = self.arvore[pos]['esq']

                self.arvore[self.arvore[pos]['esq']]['pai'] = pai

                return pai

            elif self.arvore[self.arvore[pos]['esq']]['info'] == -1 or \
                    self.arvore[self.arvore[pos]['dir']]['info'] == -1:

                if self.arvore[self.arvore[pos]['esq']]['info'] == -1:
                    noValido = self.arvore[pos]['dir']
                    noInvalido = self.arvore[pos]['esq']
                else:
                    noValido = self.arvore[pos]['esq']
                    noInvalido = self.arvore[pos]['dir']

                self.listaRemovidos.append(pos)
                self.listaRemovidos.append(noInvalido)

                # Raiz
                if pai == -1:
                    self.raiz = noValido
                else:
                    self.arvore[pai][filho] = noValido

                self.arvore[noValido]['pai'] = pai

                return pai

            else:

                aux = self.arvore[pos]['esq']
                while self.arvore[self.arvore[aux]['dir']]['info'] != -1:
                    aux = self.arvore[aux]['dir']

                y = self.arvore[aux]['info']
                self.arvore[aux]['info'] = self.arvore[pos]['info']
                self.arvore[pos]['info'] = y

                return self.RemoverElemento(self.arvore[pos]['esq'], valor, pos, 'esq')

        elif valor <= self.arvore[pos]['info']:
            return self.RemoverElemento(self.arvore[pos]['esq'], valor, pos, 'esq')
        else:
            return self.RemoverElemento(self.arvore[pos]['dir'], valor, pos, 'dir')


    def RotacaoEsquerdaSimples(self, pos):
        pai = self.arvore[pos]['pai']

        novaRaiz = self.arvore[pos]['esq']
        aux = self.arvore[novaRaiz]['dir']
        self.arvore[novaRaiz]['dir'] = pos
        self.arvore[pos]['pai'] = novaRaiz
        self.arvore[pos]['esq'] = aux
        self.arvore[aux]['pai'] = pos

        self.arvore[novaRaiz]['pai'] = pai

        if pai == -1:
            self.raiz = novaRaiz
        else:
            if self.arvore[pai]['esq'] == pos:
                self.arvore[pai]['esq'] = novaRaiz
            else:
                self.arvore[pai]['dir'] = novaRaiz

        return novaRaiz

    def RotacaoDireitaSimples(self, pos):
        pai = self.arvore[pos]['pai']

        novaRaiz = self.arvore[pos]['dir']
        aux = self.arvore[novaRaiz]['esq']
        self.arvore[novaRaiz]['esq'] = pos
        self.arvore[pos]['pai'] = novaRaiz
        self.arvore[pos]['dir'] = aux
        self.arvore[aux]['pai'] = pos

        self.arvore[novaRaiz]['pai'] = pai

        if pai == -1:
            self.raiz = novaRaiz
        else:
            if self.arvore[pai]['esq'] == pos:
                self.arvore[pai]['esq'] = novaRaiz
            else:
                self.arvore[pai]['dir'] = novaRaiz

        return novaRaiz

    def RotacaoEsquerdaDupla(self, pos):
        self.RotacaoDireitaSimples(self.arvore[pos]['esq'])
        return self.RotacaoEsquerdaSimples(pos)

    def RotacaoDireitaDupla(self, pos):
        self.RotacaoEsquerdaSimples(self.arvore[pos]['dir'])
        return self.RotacaoDireitaSimples(pos)

    def DesenhaSeta(self, pos, sentido, corLinha='yellow', larguraLinha=3):
        raio = 15
        deslY = 50
        a = self.arvore[pos]['coordX']
        b = self.arvore[pos]['coordY'] + deslY

        x = self.arvore[pos]['coordX'] - raio
        y = self.arvore[pos]['coordY'] + deslY

        while x < self.arvore[pos]['coordX'] + raio:
            x2 = x + 1
            y2 = b - math.sqrt(math.pow(raio, 2) - pow(x2-a, 2))

            self.areaDesenho.create_line(x, y, x2, y2, fill=corLinha, width=larguraLinha)

            x = x2
            y = y2

        if sentido == 'esq':
            x = self.arvore[pos]['coordX'] + raio
        else:
            x = self.arvore[pos]['coordX'] - raio

        y = self.arvore[pos]['coordY'] + deslY + 5
        x2 = x - 5
        y2 = y - 10
        self.areaDesenho.create_line(x, y, x2, y2, fill=corLinha, width=larguraLinha)

        x2 = x + 5
        y2 = y - 10
        self.areaDesenho.create_line(x, y, x2, y2, fill=corLinha, width=larguraLinha)
