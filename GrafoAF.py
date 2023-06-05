
import Grafo
import tkinter

class GrafoAF (Grafo.Grafo):
    def __init__(self, master):
        super().__init__(master)

        self.inicial = {}
        self.final = []

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

            if valor[2] == 'e':
                self.matrizAdjascencia[a][b]['custo'] = 'ε'
            else:
                self.matrizAdjascencia[a][b]['custo'] = valor[2]

            if len(valor) == 3:
                anchor = "n"
            else:
                anchor = valor[3]

            self.matrizAdjascencia[a][b]['ancora'] = anchor

        ini = ini+numAresta

        valor = graf[ini].split()
        self.inicial = {'no': int(valor[0])-1, 'ancora': valor[1]}

        ini += 1
        valor = graf[ini].split()
        totFinal = int(valor[0])

        ini += 1

        self.final = []
        for i in range(ini, ini+totFinal):
            valor = graf[i].split()
            self.final.append(int(valor[0])-1)

        self.ImprimirVisual()

    def DesenharGrafo(self, width, height):

        super().DesenharGrafo(width, height)

        x1 = self.nos[self.inicial['no']]['coordX']
        y1 = self.nos[self.inicial['no']]['coordY']
        variacao = 30
        if self.inicial['ancora'] == 'n':
            self.areaDesenho.create_line(x1, y1 - self.raio - variacao, x1, y1 - self.raio, fill='white', width=2,
                                         arrow=tkinter.LAST)
        elif self.inicial['ancora'] == 's':
            self.areaDesenho.create_line(x1, y1 + self.raio + variacao, x1, y1 + self.raio, fill='white', width=2,
                                         arrow=tkinter.LAST)
        elif self.inicial['ancora'] == 'w':
            self.areaDesenho.create_line(x1 - self.raio - variacao, y1, x1 - self.raio, y1, fill='white', width=2,
                                         arrow=tkinter.LAST)
        else:
            self.areaDesenho.create_line(x1 + self.raio + variacao, y1, x1 + self.raio, y1, fill='white', width=2,
                                         arrow=tkinter.LAST)

        for i in range(0, len(self.final)):
            x1 = self.nos[self.final[i]]['coordX']
            y1 = self.nos[self.final[i]]['coordY']
            self.CreateCircle(x1, y1, self.raio - 5, outline='black', width=2)

