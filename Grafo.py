from tkinter import messagebox
import tkinter
import math


class Grafo:
    def __init__(self, master):
        self.areaDesenho = master.ObterAreaDesenho()
        self.master = master

        self.nos = []
        self.matrizAdjascencia = []
        self.fatiasX = 6
        self.fatiasY = 6
        self.raio = 30

    def Inicializa(self):
        self.nos = []
        self.matrizAdjascencia = []

    def EstaVazio(self):
        if not self.nos:
            return True
        else:
            return False

    def LerGrafo(self, nomeArquivo):
        f = open(nomeArquivo, 'r')
        graf = f.readlines()
        f.close()

        self.Inicializa()

        valor = graf[0].split()
        numVertice = int(valor[0])


        for i in range(1, numVertice+1):
            valor = graf[i].split()
            dic = {'nome': valor[1], 'x': int(valor[2]), 'y': int(valor[3])}
            self.nos.append(dic)

        for i in range(0, numVertice):
            aux = []
            for j in range(0, numVertice):
                aux.append({})

            self.matrizAdjascencia.append(aux)

        valor = graf[numVertice+1].split()
        numAresta = int(valor[0])

        ini = numVertice+2
        for i in range(ini, ini+numAresta):
            valor = graf[i].split()
            a = int(valor[0])-1
            b = int(valor[1])-1
            self.matrizAdjascencia[a][b]['custo'] = valor[2]

            if len(valor) == 3:
                anchor = "n"
            else:
                anchor = valor[3]

            self.matrizAdjascencia[a][b]['ancora'] = anchor

        self.ImprimirVisual()

    def ImprimirVisual(self):
        width = self.areaDesenho.winfo_width()
        height = self.areaDesenho.winfo_height()

        self.areaDesenho.delete('all')
        self.DesenharGrafo(width, height)

    def DesenharGrafo(self, width, height):

        #Ajustando as coordenadas
        for i in range(0, len(self.nos)):
            self.nos[i]['coordX'] = self.nos[i]['x'] * (width/self.fatiasX)
            self.nos[i]['coordY'] = self.nos[i]['y'] * (height / self.fatiasY)

        #Desenhando os círculos
        for i in range(0, len(self.nos)):
            self.CreateCircle(self.nos[i]['coordX'], self.nos[i]['coordY'], self.raio, fill='white', outline='white')
            self.areaDesenho.create_text((self.nos[i]['coordX'], self.nos[i]['coordY']), text=self.nos[i]['nome'],
                                     font=("Purisa", 16), fill='black')

        for i in range(0, len(self.nos)):
            for j in range(0, len(self.nos)):
                if self.matrizAdjascencia[i][j]:
                    self.CriarAresta(self.nos[i]['coordX'], self.nos[i]['coordY'], self.nos[j]['coordX'],
                                     self.nos[j]['coordY'], self.raio, self.nos[j]['nome'] > self.nos[i]['nome'],
                                     self.matrizAdjascencia[i][j]['custo'], self.matrizAdjascencia[i][j]['ancora'])


    def CreateCircle(self, x, y, r, **kwargs):
        self.areaDesenho.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    def EhIgual(self, a, b):
        if -1 < a-b < 1:
            return True
        else:
            return False

    def DefinirVerticesAresta(self, x1, y1, x2, y2, raio, pos, var):

        distText = 15
        anchor = 'w'

        fator = 1
        if not pos:
            fator *= -1
            anchor = 'e'

        if self.EhIgual(x1, x2):
            if y1 > y2:
                retX1 = x1 - var
                retY1 = y1 - raio
                retX2 = x2 - var
                retY2 = y2 + raio
                retxt = x1 - distText
                retyt = int((y1+y2)/2)
                anchor = 'e'
            else:
                retX1 = x1 + var
                retY1 = y1 + raio
                retX2 = x2 + var
                retY2 = y2 - raio
                retxt = x1 + distText
                retyt = int((y1 + y2) / 2)
                anchor = 'w'
        elif self.EhIgual(y1, y2):
            if x1 > x2:
                retX1 = x1 - raio
                retY1 = y1 - var
                retX2 = x2 + raio
                retY2 = y2 - var
                retxt = int((x1+x2)/2)
                retyt = y1 - distText
                anchor = 's'
            else:
                retX1 = x1 + raio
                retY1 = y1 + var
                retX2 = x2 - raio
                retY2 = y2 + var
                retxt = int((x1 + x2) / 2)
                retyt = y1 + distText
                anchor = 'n'
        else:

            #Calculando os pontos de partida próximos aos vértices
            ma = (y2-y1)/(x2-x1)
            mb = -1/ma

            delta = pow((2*-1*x1)-(2*x1*pow(mb, 2)), 2) - (4*(pow(mb, 2)+1)*((pow(x1, 2)*pow(mb, 2))+pow(x1, 2) -
                                                                          pow(var, 2)))

            auxX1 = ((2*x1*pow(mb, 2)) + (2*x1) + (fator*math.sqrt(delta))) / (2*(pow(mb, 2)+1))
            auxY1 = ((auxX1-x1)*mb) + y1

            delta = pow((2 * -1 * x2) - (2 * x2 * pow(mb, 2)), 2) - (
                        4 * (pow(mb, 2) + 1) * ((pow(x2, 2) * pow(mb, 2)) + pow(x2, 2) -
                                                pow(var, 2)))

            auxX2 = ((2 * x2 * pow(mb, 2)) + (2 * x2) + (fator*math.sqrt(delta))) / (2 * (pow(mb, 2) + 1))
            auxY2 = ((auxX2 - x2) * mb) + y2


            #Calcular o recuo
            dist = math.sqrt(pow(y1-y2, 2) + pow(x1-x2, 2))

            retX1 = ((raio*(auxX2-auxX1))/dist) + auxX1
            retY1 = ((raio*(auxY2-auxY1))/dist) + auxY1
            retX2 = auxX2 - (((auxX2-auxX1)*raio)/dist)
            retY2 = auxY2 - (((auxY2 - auxY1) * raio) / dist)

            #Cálculo do pontos próximos aos vértices (texto)

            delta = pow((2 * -1 * x1) - (2 * x1 * pow(mb, 2)), 2) - (
                        4 * (pow(mb, 2) + 1) * ((pow(x1, 2) * pow(mb, 2)) + pow(x1, 2) -
                                                pow(distText+3, 2)))

            auxX1 = ((2 * x1 * pow(mb, 2)) + (2 * x1) + (fator * math.sqrt(delta))) / (2 * (pow(mb, 2) + 1))
            auxY1 = ((auxX1 - x1) * mb) + y1

            delta = pow((2 * -1 * x2) - (2 * x2 * pow(mb, 2)), 2) - (
                    4 * (pow(mb, 2) + 1) * ((pow(x2, 2) * pow(mb, 2)) + pow(x2, 2) -
                                            pow(distText+3, 2)))

            auxX2 = ((2 * x2 * pow(mb, 2)) + (2 * x2) + (fator * math.sqrt(delta))) / (2 * (pow(mb, 2) + 1))
            auxY2 = ((auxX2 - x2) * mb) + y2

            retxt = int((auxX1+auxX2)/2)
            retyt = int((auxY1+auxY2)/2)

        return retX1, retY1, retX2, retY2, retxt, retyt, anchor





    def CriarAresta(self, x1, y1, x2, y2, raio, pos, texto, ancora):

        # Verificar se é auto relacionamento;
        if (x1 == x2) and (y1 == y2):
            variacao = 30
            meiaVariacao = int(variacao/2)
            if ancora == 'n':
                self.areaDesenho.create_line(x1 - meiaVariacao, y1 - raio, x1 - meiaVariacao, y1 - raio - variacao,
                                             fill='white', width=2)
                self.areaDesenho.create_line(x1 - meiaVariacao, y1 - raio - variacao, x1 + meiaVariacao,
                                             y1 - raio - variacao, fill='white', width=2)
                self.areaDesenho.create_line(x1 + meiaVariacao, y1 - raio - variacao, x1 + meiaVariacao,
                                             y1 - raio, fill='white', width=2, arrow=tkinter.LAST)
                self.areaDesenho.create_text((x1, y1-raio-variacao-2), text=texto, anchor='s', font=("Purisa", 14),
                                             fill='white')
            elif ancora == 's':
                self.areaDesenho.create_line(x1 - meiaVariacao, y1 + raio, x1 - meiaVariacao, y1 + raio + variacao,
                                             fill='white', width=2)
                self.areaDesenho.create_line(x1 - meiaVariacao, y1 + raio + variacao, x1 + meiaVariacao,
                                             y1 + raio + variacao, fill='white', width=2)
                self.areaDesenho.create_line(x1 + meiaVariacao, y1 + raio + variacao, x1 + meiaVariacao,
                                             y1 + raio, fill='white', width=2, arrow=tkinter.LAST)
                self.areaDesenho.create_text((x1, y1 + raio + variacao + 2), text=texto, anchor='n',
                                             font=("Purisa", 14), fill='white')

            elif ancora == 'e':
                self.areaDesenho.create_line(x1 + raio, y1 - meiaVariacao, x1 + raio + variacao, y1 - meiaVariacao,
                                             fill='white', width=2)
                self.areaDesenho.create_line(x1 + raio + variacao, y1 - meiaVariacao, x1 + raio + variacao,
                                             y1 + meiaVariacao, fill='white', width=2)
                self.areaDesenho.create_line(x1 + raio + variacao, y1 + meiaVariacao, x1 + raio,
                                             y1 + meiaVariacao, fill='white', width=2, arrow=tkinter.LAST)
                self.areaDesenho.create_text((x1 + raio + variacao + 3, y1), text=texto, anchor='w',
                                             font=("Purisa", 14), fill='white')
            else:
                self.areaDesenho.create_line(x1 - raio, y1 - meiaVariacao, x1 - raio - variacao, y1 - meiaVariacao,
                                             fill='white', width=2)
                self.areaDesenho.create_line(x1 - raio - variacao, y1 - meiaVariacao, x1 - raio - variacao,
                                             y1 + meiaVariacao, fill='white', width=2)
                self.areaDesenho.create_line(x1 - raio - variacao, y1 + meiaVariacao, x1 - raio,
                                             y1 + meiaVariacao, fill='white', width=2, arrow=tkinter.LAST)
                self.areaDesenho.create_text((x1 - raio - variacao - 3, y1), text=texto, anchor='e',
                                             font=("Purisa", 14), fill='white')
        else:
            variacao = 10

            rx1, ry1, rx2, ry2, rxt, ryt, ranchor = self.DefinirVerticesAresta(x1, y1, x2, y2, raio, pos, variacao)

            self.areaDesenho.create_line(rx1, ry1, rx2, ry2, fill='white', arrow=tkinter.LAST, width=2)

            self.areaDesenho.create_text((rxt, ryt), text=texto, anchor=ranchor, font=("Purisa", 14), fill='white')
