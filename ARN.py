import AVL

class ARN(AVL.AVL):
    def __init__(self, master):
        super().__init__(master)

    def LerArvore(self, nomeArquivo):
        super().LerArvore(nomeArquivo)

    def InserirElemento(self, pos, x, pai=-1):
        #NULL
        if self.arvore[pos]['info'] == -1:
            dice = {'info': -1, 'esq': -1, 'dir': -1, 'max': -1, 'min': -1, 'coordX': -1, 'coordY': -1,
                    'pai': pos, 'cor': 'P'}
            dicd = {'info': -1, 'esq': -1, 'dir': -1, 'max': -1, 'min': -1, 'coordX': -1, 'coordY': -1,
                    'pai': pos, 'cor': 'P'}
            self.arvore[pos]['info'] = x
            self.arvore[pos]['esq'] = self.InserirProximaPosicao(dice)
            self.arvore[pos]['dir'] = self.InserirProximaPosicao(dicd)
            self.arvore[pos]['cor'] = 'V'

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

    def DesenharNo(self, coordX, coordY, pos):

        valor = self.arvore[pos]['info']
        if self.arvore[pos]['cor'] == 'P':
            corCentro = 'black'
            corTexto = 'white'
        else:
            corCentro = 'red'
            corTexto = 'white'


        if valor == -1:
            self.areaDesenho.create_rectangle(coordX - int(self.tamCaixaTextoX / 2),
                                              coordY - int(self.tamCaixaY / 2),
                                              coordX + int(self.tamCaixaTextoX / 2),
                                              coordY + int(self.tamCaixaY / 2),
                                              outline='white', fill=corCentro, width=2)
            self.areaDesenho.create_text((coordX, coordY + 5), text="N",
                                         font=(self.fontLetra, self.fontLetraZize), fill=corTexto)
        else:
            self.areaDesenho.create_rectangle(coordX - int(self.tamCaixaX / 2), coordY - int(self.tamCaixaY / 2),
                                              coordX + int(self.tamCaixaX / 2), coordY + int(self.tamCaixaY / 2),
                                              outline='white', width=2)
            self.areaDesenho.create_rectangle(coordX - int(self.tamCaixaX / 2), coordY - int(self.tamCaixaY / 2),
                                              coordX - int(self.tamCaixaTextoX / 2), coordY + int(self.tamCaixaY / 2),
                                              outline='white')
            self.areaDesenho.create_rectangle(coordX + int(self.tamCaixaTextoX / 2), coordY - int(self.tamCaixaY / 2),
                                              coordX + int(self.tamCaixaX / 2), coordY + int(self.tamCaixaY / 2),
                                              outline='white')
            self.areaDesenho.create_rectangle(coordX - int(self.tamCaixaTextoX / 2) + 1,
                                              coordY - int(self.tamCaixaY / 2) + 1,
                                              coordX + int(self.tamCaixaTextoX / 2),
                                              coordY + int(self.tamCaixaY / 2) - 1,
                                              outline=corCentro, fill=corCentro, width=0)
            self.areaDesenho.create_text((coordX, coordY + 5), text=str(valor),
                                         font=(self.fontLetra, self.fontLetraZize), fill=corTexto)


    def CopiarDic(self, pos, dic):
        self.arvore[pos]['info'] = dic['info']
        self.arvore[pos]['esq'] = dic['esq']
        self.arvore[pos]['dir'] = dic['dir']
        self.arvore[pos]['max'] = dic['max']
        self.arvore[pos]['min'] = dic['min']
        self.arvore[pos]['coordX'] = dic['coordX']
        self.arvore[pos]['coordY'] = dic['coordY']
        self.arvore[pos]['pai'] = dic['pai']
        self.arvore[pos]['cor'] = dic['cor']
