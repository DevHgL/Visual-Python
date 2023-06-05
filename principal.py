
import tkinter
import ViewArvBin1
import ViewArvBin2
import ViewABB
import ViewAVL
import ViewARN
import ViewGrafo
import ViewGrafoAF

aula = "AVL"

root = tkinter.Tk()
root.title('Estruturas de Dados - Aulas Online')
root.iconbitmap('app.ico')

if aula == "ArvBin1":
    ViewArvBin1.ViewArvBin1(root)
elif aula == 'ArvBin2':
    ViewArvBin2.ViewArvBin2(root)
elif aula == 'ABB':
    ViewABB.ViewABB(root)
elif aula == 'AVL':
    ViewAVL.ViewAVL(root)
elif aula == 'ARN':
    ViewARN.ViewARN(root)
elif aula == 'Grafo':
    ViewGrafo.ViewGrafo(root)
elif aula == 'GrafoAF':
    ViewGrafoAF.ViewGrafoAF(root)

root.mainloop()
