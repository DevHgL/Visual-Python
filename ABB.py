import ArvoreBinaria


class ABB(ArvoreBinaria.ArvoreBinaria):
    def __init__(self, master):
        super().__init__(master)

        self.listaRemovidos = []
        self.Inicializa()

    def Inicializa(self):
        super().Inicializa()
        self.listaRemovidos = []

    def ObterProximaPosicao(self):
        if len(self.listaRemovidos) > 0:
            indice = self.listaRemovidos[0]
            self.listaRemovidos.pop(0)
            return indice
        else:
            self.posArvore += 1
            return self.posArvore - 1

    def CopiarDic(self, pos, dic):
        self.arvore[pos]['info'] = dic['info']
        self.arvore[pos]['esq'] = dic['esq']
        self.arvore[pos]['dir'] = dic['dir']
        self.arvore[pos]['max'] = dic['max']
        self.arvore[pos]['min'] = dic['min']
        self.arvore[pos]['coordX'] = dic['coordX']
        self.arvore[pos]['coordY'] = dic['coordY']
        self.arvore[pos]['pai'] = dic['pai']

    def InserirProximaPosicao(self, dic):
        if len(self.listaRemovidos) > 0:
            indice = self.listaRemovidos[0]
            self.listaRemovidos.pop(0)
            self.CopiarDic(indice, dic)
            # self.arvore.insert(indice, dic)
            return indice
        else:
            self.posArvore += 1
            self.arvore.append(dic)
            return self.posArvore - 1

    def InserirElemento(self, pos, x):
        # NULL
        if self.arvore[pos]['info'] == -1:
            dice = {'info': -1, 'esq': -1, 'dir': -1, 'max': -1, 'min': -1, 'coordX': -1, 'coordY': -1}
            dicd = {'info': -1, 'esq': -1, 'dir': -1, 'max': -1, 'min': -1, 'coordX': -1, 'coordY': -1}
            self.arvore[pos]['info'] = x
            self.arvore[pos]['esq'] = self.InserirProximaPosicao(dice)
            self.arvore[pos]['dir'] = self.InserirProximaPosicao(dicd)
        else:
            if x <= self.arvore[pos]['info']:
                self.InserirElemento(self.arvore[pos]['esq'], x)
            else:
                self.InserirElemento(self.arvore[pos]['dir'], x)

    def MarcarNoComX(self, pos, corX='red'):

        valor = self.arvore[pos]['info']
        if valor == -1:
            self.areaDesenho.create_line(self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2) - 10,
                                         self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) - 10,
                                         self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) + 10,
                                         self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2) + 10,
                                         fill=corX, width=3)

            self.areaDesenho.create_line(self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2) - 10,
                                         self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2) + 10,
                                         self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) + 10,
                                         self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) - 10,
                                         fill=corX, width=3)
        else:
            self.areaDesenho.create_line(self.arvore[pos]['coordX'] - int(self.tamCaixaX / 2) - 10,
                                         self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) - 10,
                                         self.arvore[pos]['coordX'] + int(self.tamCaixaX / 2) + 10,
                                         self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2) + 10,
                                         fill=corX, width=3)

            self.areaDesenho.create_line(self.arvore[pos]['coordX'] - int(self.tamCaixaX / 2) - 10,
                                         self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2) + 10,
                                         self.arvore[pos]['coordX'] + int(self.tamCaixaX / 2) + 10,
                                         self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) - 10,
                                         fill=corX, width=3)

    def AjustarInfoNo(self, pos, valor):

        coordX = self.arvore[pos]['coordX']
        coordY = self.arvore[pos]['coordY']

        self.areaDesenho.create_rectangle(coordX - int(self.tamCaixaTextoX / 2) + 2,
                                          coordY - int(self.tamCaixaY / 2) + 6,
                                          coordX + int(self.tamCaixaTextoX / 2) - 2,
                                          coordY + int(self.tamCaixaY / 2) - 2,
                                          outline='blue', fill='blue', width=0)

        self.areaDesenho.create_text((coordX, coordY + 5), text=str(valor),
                                     font=(self.fontLetra, self.fontLetraZize), fill='white')

    def RemoverElemento(self, pos, valor, pai=-1, filho=''):
        # Encontrando o elemento
        if self.arvore[pos]['info'] == valor:
            # É folha?
            if self.arvore[self.arvore[pos]['esq']]['info'] == -1 and \
                    self.arvore[self.arvore[pos]['dir']]['info'] == -1:
                self.listaRemovidos.append(pos)
                self.listaRemovidos.append(self.arvore[pos]['dir'])

                # Raiz
                if pai == -1:
                    self.raiz = self.arvore[pos]['esq']
                else:
                    self.arvore[pai][filho] = self.arvore[pos]['esq']

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

            else:
                aux = self.arvore[pos]['esq']
                while self.arvore[self.arvore[aux]['dir']]['info'] != -1:
                    aux = self.arvore[aux]['dir']

                y = self.arvore[aux]['info']
                self.arvore[aux]['info'] = self.arvore[pos]['info']
                self.arvore[pos]['info'] = y

                self.RemoverElemento(self.arvore[pos]['esq'], valor, pos, 'esq')

        elif valor <= self.arvore[pos]['info']:
            self.RemoverElemento(self.arvore[pos]['esq'], valor, pos, 'esq')
        else:
            self.RemoverElemento(self.arvore[pos]['dir'], valor, pos, 'dir')
