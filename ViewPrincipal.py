# f


import tkinter
from abc import abstractmethod
import CMenuButton
import abc
import time
import threading
from tkinter import ttk


def isInt(valor):
    try:
        int(valor)
        return True
    except:
        return False

class ViewPrincipal(abc.ABC):
    def __init__(self, master=None):

        self.menuDefinido = False
        self.edValor = ""
        self.edLido = False
        self.canvasClicked = False
        self.dirAlgoritmos = ''
        self.dirEntrada = ''

        #self.penColor = '#BF13DB'
        self.penColor = 'cyan'
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0

        top = tkinter.Frame(master)
        top['bg'] = 'white'
        top.configure(relief="flat")
        top.pack(side="top", fill='both', expand=True)

        botton = tkinter.Frame(master, width=50)
        botton['bg'] = '#1e2b2b'
        botton.configure(relief="flat")
        botton.pack(side="top", fill='both')

        fDesenho = tkinter.Frame(top)
        fDesenho['bg'] = 'white'
        fDesenho.configure(relief="flat")
        fDesenho.pack(side="left", fill='both', expand=True)

        fDir = tkinter.Frame(top)
        fDir['bg'] = 'white'
        fDir.configure(relief="flat")
        fDir.pack(side="right", fill='both')

        fTexto = tkinter.Frame(fDir)
        fTexto['bg'] = 'white'
        fTexto.configure(relief="flat")
        fTexto.pack(side="top", fill='both', expand=True)

        self.areaDesenho = tkinter.Canvas(fDesenho)
        self.areaDesenho['bg'] = 'black'
        self.areaDesenho.configure(relief="flat", border=2)
        self.areaDesenho.pack(side="left", fill='both', expand=True)
        self.areaDesenho.bind("<Button-1>", self.onCanvasClick)
        self.areaDesenho.bind("<Motion>", self.tell_me_where_you_are)
        self.areaDesenho.bind("<B1-Motion>", self.draw_from_where_you_are)

        self.areaTexto = tkinter.Label(fTexto, text="", width=30, anchor='nw', justify='left')
        self.areaTexto['bg'] = 'white'
        self.areaTexto.configure(relief="flat", border=10, font="Times 20 bold")
        self.areaTexto.pack(side="top", fill='both', expand=True)



        ##########   Área de Leitura   ###########
        self.fLeitura = tkinter.Frame(fTexto)
        self.fLeitura['bg'] = 'white'
        self.fLeitura.configure(relief="flat")
        self.fLeitura.pack(side="top", fill='both')

        lSepara = tkinter.Label(self.fLeitura, text="   ")
        lSepara['bg'] = 'black'
        lSepara.configure(relief="flat", border=1, font="Times 1")
        lSepara.pack(side="top", fill='both')

        lSepara2 = tkinter.Label(self.fLeitura, text="   ")
        lSepara2['bg'] = 'white'
        lSepara2.configure(relief="flat", border=1, font="Times 20")
        lSepara2.pack(side="top", fill='both')

        fLeituraComandos = tkinter.Frame(self.fLeitura)
        fLeituraComandos['bg'] = 'white'
        fLeituraComandos.configure(relief="flat")
        fLeituraComandos.pack(side="top", fill='both')

        self.lEditBox = tkinter.Label(fLeituraComandos, text="Input:")
        self.lEditBox['bg'] = 'white'
        self.lEditBox.configure(relief="flat", border=1, font="Times 20 bold")
        self.lEditBox.pack(side="left", fill='both')

        self.editBox = tkinter.Entry(fLeituraComandos)
        self.editBox['bg'] = '#FFFFCA'
        self.editBox['fg'] = 'black'
        self.editBox.configure(relief="ridge", bd=1, border=4, font="Times 20 bold")
        self.editBox.pack(side="left", fill='both')

        btEditBox = CMenuButton.MenuButton(fLeituraComandos, '#FFFFCA', '#FFFF60', text="OK",
                                           command=self.onOKClick)
        btEditBox['bg'] = '#FFFFCA'
        btEditBox['fg'] = 'black'
        btEditBox.configure(relief="ridge", border=4, font="Times 20 bold")
        btEditBox.pack(side="left")

        lSepara3 = tkinter.Label(self.fLeitura, text="   ")
        lSepara3['bg'] = 'white'
        lSepara3.configure(relief="flat", border=1, font="Times 20")
        lSepara3.pack(side="top", fill='both')




        #########################   Área de escrita   #######################

        self.fEscrita = tkinter.Frame(fTexto)
        self.fEscrita['bg'] = 'white'
        self.fEscrita.configure(relief="flat")
        self.fEscrita.pack(side="top", fill='both')

        lSeparaEscrita = tkinter.Label(self.fEscrita, text="   ")
        lSeparaEscrita['bg'] = 'black'
        lSeparaEscrita.configure(relief="flat", border=1, font="Times 1")
        lSeparaEscrita.pack(side="top", fill='both')

        lSeparaEscrita2 = tkinter.Label(self.fEscrita, text="   ")
        lSeparaEscrita2['bg'] = 'white'
        lSeparaEscrita2.configure(relief="flat", border=1, font="Times 20")
        lSeparaEscrita2.pack(side="top", fill='both')


        self.areaTextoEscrita = tkinter.Label(self.fEscrita, text='   ', width=30, anchor='w', justify='left')
        self.areaTextoEscrita['bg'] = 'white'
        self.areaTextoEscrita['fg'] = 'black'
        self.areaTextoEscrita.configure(relief="flat", border=10, font="Times 20 bold")
        self.areaTextoEscrita.pack(side="top", fill='both', expand=True)

        lSeparaEscrita3 = tkinter.Label(self.fEscrita, text="   ")
        lSeparaEscrita3['bg'] = 'white'
        lSeparaEscrita3.configure(relief="flat", border=1, font="Times 20")
        lSeparaEscrita3.pack(side="top", fill='both')





        #################### Área do algoritmo #####################

        self.scrollAlgoritmo = tkinter.Scrollbar(fTexto)
        self.scrollAlgoritmo.pack(side='right', fill='y')
        self.areaTextoAlgoritmo = tkinter.Listbox(fTexto, width=33, yscrollcommand=self.scrollAlgoritmo.set)
        self.areaTextoAlgoritmo['bg'] = 'white'
        self.areaTextoAlgoritmo.configure(relief="flat", border=10, font="Times 20 bold")
        self.areaTextoAlgoritmo.pack(side="left", fill='both', expand=True)
        self.scrollAlgoritmo.config(command=self.areaTextoAlgoritmo.yview)


        fbottonEsq = tkinter.Frame(fDir)
        fbottonEsq['bg'] = '#1e2b2b'
        fbottonEsq.configure(relief="flat")
        fbottonEsq.pack(side="left", fill='both')
        comboButton = CMenuButton.MenuButton(fbottonEsq, 'white', '#FFFFCA', text="Console",
                                             command=self.onConsoleClick)
        comboButton['bg'] = 'white'
        comboButton['fg'] = '#1e2b2b'
        comboButton.configure(relief="flat", border=2, font="Times 16 bold")
        comboButton.pack(side="left")

        lSepara4 = tkinter.Label(fbottonEsq, text=" ")
        lSepara4['bg'] = '#1e2b2b'
        lSepara4.configure(relief="flat", border=0, font="Times 1")
        lSepara4.pack(side="left", fill='both')

        comboButton2 = CMenuButton.MenuButton(fbottonEsq, 'white', '#FFFFCA', text="Algoritmo",
                                              command=self.onAlgoritmoClick)
        comboButton2['bg'] = 'white'
        comboButton2['fg'] = '#1e2b2b'
        comboButton2.configure(relief="flat", border=2, font="Times 16 bold")
        comboButton2.pack(side="left")


        ################# Check Box ############################
        fbottonDir = tkinter.Frame(fDir)
        fbottonDir['bg'] = '#1e2b2b'
        fbottonDir.configure(relief="flat")
        fbottonDir.pack(side="right", fill='both', expand=True)

        self.chkValue = tkinter.BooleanVar()
        self.ckButtton = tkinter.Checkbutton(fbottonDir, text='Manual ', anchor='e', variable=self.chkValue,
                                             activebackground='#1e2b2b', activeforeground='white',
                                             relief='ridge', selectcolor='#1e2b2b')
        self.ckButtton['bg'] = '#1e2b2b'
        self.ckButtton['fg'] = 'white'
        self.ckButtton.configure(border=0, font="Times 16 bold")
        self.ckButtton.pack(side="right", fill='both')

        self.chkPenValue = tkinter.BooleanVar()
        self.ckPenButtton = tkinter.Checkbutton(fbottonDir, text='Pen ', anchor='e', variable=self.chkPenValue,
                                             activebackground='#1e2b2b', activeforeground='white',
                                             relief='ridge', selectcolor='#1e2b2b', command=self.onCkPenClick)
        self.ckPenButtton['bg'] = '#1e2b2b'
        self.ckPenButtton['fg'] = 'white'
        self.ckPenButtton.configure(border=0, font="Times 16 bold")
        self.ckPenButtton.pack(side="right", fill='both')




        ################## Setagem de parâmetros #########################

        self.dicAbas = {'menu': self.areaTexto.pack_info(), 'entrada': self.fLeitura.pack_info(),
                        'saida': self.fEscrita.pack_info(), 'algoritmo':  self.areaTextoAlgoritmo.pack_info(),
                        'scroll': self.scrollAlgoritmo.pack_info()}

        self.estaEscrevendo = False
        self.estaLendo = False

        self.abaAtiva = 1
        self.HabilitarAbaMenu()


    def __del__(self):
        self.threadMenu.join()


    def HabilitarAbaMenu(self):
        self.abaAtiva = 1

        self.dicAbas['algoritmo'] = self.areaTextoAlgoritmo.pack_info()
        self.areaTextoAlgoritmo.pack_forget()

        self.dicAbas['sensor'] = self.scrollAlgoritmo.pack_info()
        self.scrollAlgoritmo.pack_forget()

        self.areaTexto.pack(self.dicAbas['menu'])

        if self.estaEscrevendo:
            self.fEscrita.pack(self.dicAbas['saida'])

        if self.estaLendo:
            self.fLeitura.pack(self.dicAbas['entrada'])

        self.DefinirMenu()

    def onConsoleClick(event):
        event.HabilitarAbaMenu()

    def onAlgoritmoClick(event):
        event.abaAtiva = 2

        if event.areaTexto.winfo_ismapped():
            event.dicAbas['menu'] = event.areaTexto.pack_info()
            event.areaTexto.pack_forget()

        if event.fEscrita.winfo_ismapped():
            event.dicAbas['saida'] = event.fEscrita.pack_info()
            event.fEscrita.pack_forget()

        if event.fLeitura.winfo_ismapped():
            event.dicAbas['entrada'] = event.fLeitura.pack_info()
            event.fLeitura.pack_forget()

        if not event.areaTextoAlgoritmo.winfo_ismapped():
            event.areaTextoAlgoritmo.pack(event.dicAbas['algoritmo'])

        if not event.scrollAlgoritmo.winfo_ismapped():
            event.scrollAlgoritmo.pack(event.dicAbas['sensor'])

    def DefinirMenu(self):
        if not self.menuDefinido:
            self.threadMenu = threading.Thread(target=self.ThreadExecutarMenu, args=())
            self.threadMenu.start()

    @abstractmethod
    def ThreadExecutarMenu(self):
        pass

    def onOKClick(event):
        valor = str(event.editBox.get())
        if valor != '':
            event.edValor = valor
            event.edLido = True
            event.editBox.delete(0, 'end')

    def LerValor(self, texto):

        #Desabilitar área de escrita
        self.estaEscrevendo = False
        self.fEscrita.pack_forget()

        #Habilitar área de leitura
        self.estaLendo = True

        if self.abaAtiva == 1:
            self.fLeitura.pack(self.dicAbas['entrada'])
        self.lEditBox['text'] = texto

        self.edLido = False
        while not self.edLido:
            pass

        #Desabilitar área de leitura
        self.fLeitura.pack_forget()
        self.estaLendo = False

        return self.edValor

    def AjustarTamanhoTexto(self, texto, num):

        total = 0
        for i in range(0, len(texto)):
            if texto[i] == '\n':
                total = 0
            else:
                total += 1

        if total <= num:
            return texto
        else:
            i = 0
            strRet = ''
            while total > num:
                ini = num*i
                fim = num*(i+1)
                strRet += texto[ini:fim] + '\n'
                i += 1
                total -= num

            ini = num * i
            fim = num * (i + 1)
            strRet += texto[ini:fim]

        return strRet



    def EscreverValor(self, texto):

        #Desabilitar área de leitura
        self.fLeitura.pack_forget()

        #Habilitar área de escrita
        if not self.estaEscrevendo:
            self.fEscrita.pack(self.dicAbas['saida'])
            self.estaEscrevendo = True

        #Jogar as informações em área de texto 2
        texto = self.AjustarTamanhoTexto(texto, 40)
        self.areaTextoEscrita['text'] = texto



    def ObterAreaDesenho(self):
        return self.areaDesenho

    def RepeatUntilClick(self):
        self.canvasClicked = False
        while not self.canvasClicked:
            pass

    def Aguardar(self, total):
        if not self.chkValue.get():
            time.sleep(total)
        else:
            self.RepeatUntilClick()

    def DefinirPrograma(self, texto):
        if texto == '':
            self.areaTextoAlgoritmo.delete(0, 'end')
            #self.areaTextoAlgoritmo['text'] = texto
        else:
            self.areaTextoAlgoritmo.delete(0, 'end')
            arquivo = open(texto, 'r')
            for linha in arquivo:
                self.areaTextoAlgoritmo.insert('end', linha)
            arquivo.close()

    def onCanvasClick(self, coord):
        if not self.chkPenValue.get():
            self.canvasClicked = True

    def tell_me_where_you_are(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def draw_from_where_you_are(self, event):
        if self.chkPenValue.get():
            self.x = event.x
            self.y = event.y
            self.areaDesenho.create_line(self.previous_x, self.previous_y,
                                    self.x, self.y, fill=self.penColor, width=2)
            self.previous_x = self.x
            self.previous_y = self.y

    def onCkPenClick(event):
        if not event.chkPenValue.get():
            event.LimpaTelaCanvas()

    @abstractmethod
    def LimpaTelaCanvas(self):
        pass

