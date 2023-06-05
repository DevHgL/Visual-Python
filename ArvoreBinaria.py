from tkinter import messagebox


class ArvoreBinaria:
    def __init__(self, master):
        self.areaDesenho = master.ObterAreaDesenho()
        self.master = master

        # NULL
        self.raiz = -1
        # Inicialmente vazia
        self.arvore = []
        self.posArvore = 0

        self.Inicializa()

        self.fontLetraZize = 20
        self.fontLetraZizeRetorno = 16
        self.fontLetra = "Purisa"
        self.tamCaixaX = 70
        self.tamCaixaY = 40
        self.tamCaixaTextoX = 50
        self.distX = 15
        self.distY = 50

    def Inicializa(self):
        # NULL
        self.raiz = -1
        # Inicialmente vazia
        self.arvore = []
        self.posArvore = 0

    def ObterRaiz(self):
        return self.raiz

    def InserirProximaPosicao(self, dic):
        self.posArvore += 1
        self.arvore.append(dic)
        return self.posArvore - 1

    def LerArvore(self, nomeArquivo):
        try:
            f = open(nomeArquivo, 'r')
            arv = f.readline()
            f.close()

            self.Inicializa()

            valor, pos = self.ConstruirArvore(arv, 0)

            if valor == -2:
                self.Inicializa()
            else:
                self.raiz = valor
                self.ImprimirVisual()
        except:
            messagebox.showinfo("Erro", "Erro ao ler a árvore!")

    def ConstruirArvore(self, arv, pos):
        if arv[pos] != '(':
            messagebox.showinfo("Aviso", "Árvore com erro de sintáxe!")
            return -2, pos

        pos += 1
        strNum = ''

        if arv[pos] == '-':
            strNum += '-'
            pos += 1

        while '0' <= arv[pos] <= '9':
            strNum += arv[pos]
            pos += 1

        num = int(strNum)
        dic = {'info': num}
        if num == -1:
            dic['esq'] = -1
            dic['dir'] = -1
            dic['max'] = -1
            dic['min'] = -1
            dic['coordX'] = -1
            dic['coordY'] = -1
            dic['cor'] = 'P'
            if arv[pos] != ')':
                messagebox.showinfo("Aviso", "Árvore com erro de sintáxe!")
                return -2, pos
            pos += 1
            posicao = self.InserirProximaPosicao(dic)
            return posicao, pos

        valorEsq, pos = self.ConstruirArvore(arv, pos)
        if valorEsq == -2:
            return -2, pos

        valorDir, pos = self.ConstruirArvore(arv, pos)
        if valorDir == -2:
            return -2, pos

        dic['esq'] = valorEsq
        dic['dir'] = valorDir
        dic['max'] = -1
        dic['min'] = -1
        dic['coordX'] = -1
        dic['coordY'] = -1

        if arv[pos] != ')':
            messagebox.showinfo("Aviso", "Árvore com erro de sintáxe!")
            return -2, pos

        pos += 1
        posicao = self.InserirProximaPosicao(dic)

        return posicao, pos

    def MontarMaxMinArvore(self, pos):
        # Testar se for Nulo
        if self.arvore[pos]['info'] == -1:
            self.arvore[pos]['min'] = 0
            self.arvore[pos]['max'] = self.tamCaixaTextoX
        else:
            self.MontarMaxMinArvore(self.arvore[pos]['esq'])
            self.MontarMaxMinArvore(self.arvore[pos]['dir'])

            maxDir = self.arvore[self.arvore[pos]['dir']]['max']
            minDir = self.arvore[self.arvore[pos]['dir']]['min']
            maxEsq = self.arvore[self.arvore[pos]['esq']]['max']
            minEsq = self.arvore[self.arvore[pos]['esq']]['min']

            self.arvore[pos]['min'] = 0
            if (maxEsq - minEsq) + self.distX + (maxDir - minDir) <= self.tamCaixaX:
                self.arvore[pos]['max'] = self.tamCaixaX
            else:
                self.arvore[pos]['max'] = (maxEsq - minEsq) + self.distX + (maxDir - minDir)

    def AjustarCoordenadas(self, pos, posXPai, posYPai, indice):

        # Se não for a raiz
        if posXPai != -1:
            # NULL
            if self.arvore[pos]['info'] == -1:
                meio = int((self.arvore[pos]['max'] - self.arvore[pos]['min']) / 2)
                self.arvore[pos]['coordX'] = posXPai + (int(self.distX / 2) + meio) * indice
                self.arvore[pos]['coordY'] = posYPai + self.distY + self.tamCaixaY
            else:
                maxEsq = self.arvore[self.arvore[pos]['esq']]['max']

                width = self.arvore[pos]['max']

                meio = maxEsq + int(self.distX / 2)

                if indice == 1:
                    self.arvore[pos]['coordX'] = posXPai + meio + int(self.distX / 2)
                    self.arvore[pos]['coordY'] = posYPai + self.distY + self.tamCaixaY
                else:
                    self.arvore[pos]['coordX'] = posXPai - (width - meio) - int(self.distX / 2)
                    self.arvore[pos]['coordY'] = posYPai + self.distY + self.tamCaixaY

        # Se não for NULL
        if self.arvore[pos]['info'] != -1:
            self.AjustarCoordenadas(self.arvore[pos]['esq'], self.arvore[pos]['coordX'],
                                    self.arvore[pos]['coordY'], -1)

            self.AjustarCoordenadas(self.arvore[pos]['dir'], self.arvore[pos]['coordX'],
                                    self.arvore[pos]['coordY'], 1)

    def DefinirCoordenadas(self, raiz, width):

        self.MontarMaxMinArvore(raiz)

        maximo = self.arvore[raiz]['max']
        minimo = self.arvore[raiz]['min']

        if maximo - minimo > width:
            messagebox.showinfo("Aviso", "Árvore larga demais para ser visualizada")
            return

        maxDir = 0
        minDir = 0
        maxEsq = 0
        minEsq = 0

        # NULL
        if self.arvore[raiz]['info'] == -1:
            meio = int(width / 2)
        else:
            maxDir = self.arvore[self.arvore[raiz]['dir']]['max']
            minDir = self.arvore[self.arvore[raiz]['dir']]['min']
            maxEsq = self.arvore[self.arvore[raiz]['esq']]['max']
            minEsq = self.arvore[self.arvore[raiz]['esq']]['min']

            dif = (maxDir - minDir) - (maxEsq - minEsq)

            # meio = int(width/2) - int(dif/2) + int(self.distX/2)
            meio = int((width - dif) / 2)

        # Se não teve as coordenadas setadas ainda
        if self.arvore[raiz]['coordX'] == -1:
            self.arvore[raiz]['coordX'] = meio
            self.arvore[raiz]['coordY'] = self.distY + int(self.tamCaixaY / 2)
        else:
            # Verificar se precisa mudar as coordenadas da raiz
            if self.arvore[raiz]['coordX'] - (maxEsq - minEsq) < 0 or self.arvore[raiz]['coordX'] + \
                    (maxDir - minDir) > width:
                self.arvore[raiz]['coordX'] = meio
                self.arvore[raiz]['coordY'] = self.distY + int(self.tamCaixaY / 2)
            else:
                self.arvore[raiz]['coordY'] = self.distY + int(self.tamCaixaY / 2)

        self.AjustarCoordenadas(raiz, -1, -1, 1)

    def DesenharNo(self, coordX, coordY, pos):

        valor = self.arvore[pos]['info']

        if valor == -1:
            self.areaDesenho.create_rectangle(coordX - int(self.tamCaixaTextoX / 2),
                                              coordY - int(self.tamCaixaY / 2),
                                              coordX + int(self.tamCaixaTextoX / 2),
                                              coordY + int(self.tamCaixaY / 2),
                                              outline='white', fill='white', width=2)
            self.areaDesenho.create_text((coordX, coordY + 5), text="N",
                                         font=(self.fontLetra, self.fontLetraZize), fill='black')
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
            self.areaDesenho.create_text((coordX, coordY + 5), text=str(valor),
                                         font=(self.fontLetra, self.fontLetraZize), fill='white')

    def DesenharArvore(self, pos):

        self.DesenharNo(self.arvore[pos]['coordX'], self.arvore[pos]['coordY'], pos)

        if self.arvore[pos]['info'] != -1:
            self.areaDesenho.create_line(self.arvore[pos]['coordX'] - int((self.tamCaixaX + self.tamCaixaTextoX) / 4),
                                         self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2),
                                         self.arvore[self.arvore[pos]['esq']]['coordX'],
                                         self.arvore[self.arvore[pos]['esq']]['coordY'] - int(self.tamCaixaY / 2),
                                         fill='white')

            self.areaDesenho.create_line(self.arvore[pos]['coordX'] + int((self.tamCaixaX + self.tamCaixaTextoX) / 4),
                                         self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2),
                                         self.arvore[self.arvore[pos]['dir']]['coordX'],
                                         self.arvore[self.arvore[pos]['dir']]['coordY'] - int(self.tamCaixaY / 2),
                                         fill='white')

            self.DesenharArvore(self.arvore[pos]['esq'])
            self.DesenharArvore(self.arvore[pos]['dir'])

    def TempImprimirInfo(self, pos):
        if self.arvore[pos]['info'] != -1:
            if pos == self.raiz:
                print('Arvore:')
            print(self.arvore[pos]['info'], self.arvore[self.arvore[pos]['pai']]['info'])

            self.TempImprimirInfo(self.arvore[pos]['esq'])
            self.TempImprimirInfo(self.arvore[pos]['dir'])

    def ImprimirVisual(self):
        width = self.areaDesenho.winfo_width()

        self.DefinirCoordenadas(self.raiz, width)
        self.areaDesenho.delete('all')
        self.DesenharArvore(self.raiz)

        #self.TempImprimirInfo(self.raiz)

    def RetornarObjeto(self, pos, obj):
        return self.arvore[pos][obj]

    def AlterarObjeto(self, pos, obj, x):
        self.arvore[pos][obj] = x

    def MarcarNo(self, pos, corCaixa='red', corLateral='yellow', caixa=2, esquerda=2, direita=2, centro=2):
        if pos != -1:
            valor = self.arvore[pos]['info']
            if caixa == 1:
                if valor == -1:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2),
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2),
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2),
                                                      self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2),
                                                      outline=corCaixa, width=3)
                else:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaX / 2),
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2),
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaX / 2),
                                                      self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2),
                                                      outline=corCaixa, width=3)
            elif caixa == 0:
                if valor == -1:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2),
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2),
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2),
                                                      self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2),
                                                      outline='white', width=3)
                else:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaX / 2),
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2),
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaX / 2),
                                                      self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2),
                                                      outline='white', width=3)

            if centro == 1:
                if valor == -1:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2) + 2,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 2,
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) - 2,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 5,
                                                      outline=corLateral, fill=corLateral)
                else:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2) + 1,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 2,
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) - 1,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 5,
                                                      outline=corLateral, fill=corLateral)
            elif centro == 0:
                if valor == -1:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2) + 2,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 2,
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) - 2,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 5,
                                                      outline='white', fill='white')
                else:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2) + 1,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 2,
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) - 1,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 5,
                                                      outline='black', fill='black')

            if valor != -1:
                if esquerda == 1:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaX / 2) + 2,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 2,
                                                      self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2) - 1,
                                                      self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2) - 2,
                                                      outline=corLateral, fill=corLateral)
                elif esquerda == 0:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] - int(self.tamCaixaX / 2) + 2,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 2,
                                                      self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX / 2) - 1,
                                                      self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2) - 2,
                                                      outline='black', fill='black')

                if direita == 1:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) + 1,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 2,
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaX / 2) - 2,
                                                      self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2) - 2,
                                                      outline=corLateral, fill=corLateral)
                elif direita == 0:
                    self.areaDesenho.create_rectangle(self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) + 1,
                                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) + 2,
                                                      self.arvore[pos]['coordX'] + int(self.tamCaixaX / 2) - 2,
                                                      self.arvore[pos]['coordY'] + int(self.tamCaixaY / 2) - 2,
                                                      outline='black', fill='black')

    def DestacarRetorno(self, pos, filho, valor):

        #NULL
        if self.arvore[pos]['info'] == -1:
            #Filho esquerdo
            if filho == 'e':
                self.areaDesenho.create_text((self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX/2) + 8,
                                              self.arvore[pos]['coordY'] - int(self.tamCaixaY/2) - 15),
                                             text=str(valor),
                                             font=(self.fontLetra, self.fontLetraZizeRetorno), fill='#BEE7F1')
            else:
                self.areaDesenho.create_text((self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) - 8,
                                              self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) - 15),
                                             text=str(valor),
                                             font=(self.fontLetra, self.fontLetraZizeRetorno), fill='#BEE7F1')

        else:
            #Filho esquerdo
            if filho == 'e':
                self.areaDesenho.create_text((self.arvore[pos]['coordX'] - int(self.tamCaixaTextoX/2) + 8,
                                              self.arvore[pos]['coordY'] - int(self.tamCaixaY/2) - 15),
                                             text=str(valor),
                                             font=(self.fontLetra, self.fontLetraZizeRetorno), fill='#BEE7F1')
            else:
                self.areaDesenho.create_text((self.arvore[pos]['coordX'] + int(self.tamCaixaTextoX / 2) - 8,
                                              self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) - 15),
                                             text=str(valor),
                                             font=(self.fontLetra, self.fontLetraZizeRetorno), fill='#BEE7F1')



    def DesmarcarArvore(self, pos):
        if self.arvore[pos]['info'] == -1:
            self.MarcarNo(pos, caixa=0, centro=0)
        else:
            self.MarcarNo(pos, caixa=0, centro=0, esquerda=0, direita=0)
            self.DesmarcarArvore(self.arvore[pos]['esq'])
            self.DesmarcarArvore(self.arvore[pos]['dir'])


    def DestacarRaiz(self, valor):
        pos = self.raiz
        self.areaDesenho.create_text((self.arvore[pos]['coordX'],
                                      self.arvore[pos]['coordY'] - int(self.tamCaixaY / 2) - 15),
                                     text=str(valor),
                                     font=(self.fontLetra, self.fontLetraZizeRetorno), fill='#BEE7F1')

    def CalcularAltura(self, pos):
        if self.arvore[pos]['info'] == -1:
            return 0
        else:
            he = self.CalcularAltura(self.arvore[pos]['esq'])
            hd = self.CalcularAltura(self.arvore[pos]['dir'])

            if he > hd:
                return he+1
            else:
                return hd+1
