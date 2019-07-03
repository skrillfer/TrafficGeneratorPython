#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import moduleGeneratorTraffic as Traffic

from threading import Thread
import time

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from tkinter import ttk

entryText = ''
class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        global entryText
        entryText = StringVar(self.raiz)
        # Gets the requested values of the height and widht.
        windowWidth = self.raiz.winfo_reqwidth()
        windowHeight = self.raiz.winfo_reqheight()
        print("Width",windowWidth,"Height",windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.raiz.winfo_screenwidth()/3 - windowWidth/2)
        positionDown = int(self.raiz.winfo_screenheight()/3 - windowHeight/2)

        # Positions the window in the center of the page.
        self.raiz.geometry("+{}+{}".format(positionRight, positionDown))

        # Define la dimensión de la ventana
        self.raiz.geometry("750x400")
        self.raiz.resizable(0,0)
        self.raiz.title("Traffic Generator USAC")
        self.raiz.configure(bg="#12005e")

        
        #background_label = ttk.Label(self.raiz, "briot")
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)


        lbl1 = Label(self.raiz, text="Ingrese los parametros y opciones para enviar trafico",font=("Helvetica", 12))
        lbl1.place(x=10,y=10)

        #URL
        self.lblURL = Label(self.raiz, text = "URL:")
        self.lblURL.place(x=10,y=40)

        self.inputURL = Entry(self.raiz, bd = 2, width=50)
        self.inputURL.place(x=100,y=40)

        #Solicitudes
        self.lblRequest = Label(self.raiz, text = "Solicitudes:")
        self.lblRequest.place(x=10,y=70)

        self.inputRequest = Entry(self.raiz, bd = 2)
        self.inputRequest.place(x=100,y=70)

        #Concurrency
        OPTIONS = [
        "10",
        "100",
        "1000",
        "2000",
        "3000"
        ] #etc

        self.lblConcurrency = Label(self.raiz, text = "Concurrencia:")
        self.lblConcurrency.place(x=10,y=125)

        self.variable = StringVar(self.raiz)
        self.variable.set(OPTIONS[0]) # default value

        self.choiseConcurrency = OptionMenu(self.raiz, self.variable, *OPTIONS)
        self.choiseConcurrency.place(x=110,y=120)
        
        #Parametros
        self.lblParameters = Label(self.raiz, text = "Parametros:")
        self.lblParameters.place(x=10,y=175)


        self.inputFile = Entry(self.raiz,textvariable=entryText, state=DISABLED ,width=50 , bd = 5)
        self.inputFile.place(x=100,y=170)

        self.b1 = Button(self.raiz, text='Buscar', command=self.print_path)  
        self.b1.place(x=510,y=170)
        
        #TimeOut
        OPTIONS2 = [
        "1000",
        "2000",
        "3000"
        ] #etc

        self.lblTimeOut = Label(self.raiz, text = "TimeOut:")
        self.lblTimeOut.place(x=10,y=235)

        self.variable2 = StringVar(self.raiz)
        self.variable2.set(OPTIONS2[0]) # default value

        self.choiseTimeOut = OptionMenu(self.raiz, self.variable2, *OPTIONS2)
        self.choiseTimeOut.place(x=110,y=230)
        
        #ProgressBar
        self.lblTimeOut = Label(self.raiz, text = "Completado:")
        self.lblTimeOut.place(x=10,y=285)


        self.pbar_ind = ttk.Progressbar(self.raiz,length=300,maximum=100)
        #self.pbar_ind.grid(column = 0, row = 3, pady=10)
        self.pbar_ind.place(x=120,y=285)
        #self.pbar_ind.start(1000)

        self.b1 = Button(self.raiz, text='Ejecutar', command=self.execute)  
        self.b1.place(x=440,y=280)
        
        '''self.btn_datos = Button(self.raiz,text='Datos del Pez Leon', padx=5, pady=5,command=self.opcion1)
        self.btn_datos.pack(padx=5, pady=145)
        self.btn_datos.config(bg='#5f7f7a', fg='white')
        self.btn_datos.config(font=('helvetica', 20, 'bold'))'''

        self.raiz.mainloop()

    def opcion1(self):
        print('nada')

#https://recursospython.com/guias-y-manuales/barra-de-progreso-progressbar-tcltk-tkinter/
    def execute(self):
        
        #getting values input in the UI app
        url         = self.inputURL.get()
        request     = self.inputRequest.get()
        concurrency = self.variable.get()
        timeOut     = self.variable2.get()
        filePath    = self.inputFile.get()
        #verifing if all values are correct
        if checkAllValues(url,request,concurrency,timeOut,filePath):
            #Thread(target=self.progress).start()
            for i in range(int(concurrency)):
                Thread(target=self.startSendRequest(url,request,concurrency,timeOut,filePath,i)).start()
            print('Finalizado')

    def on_done(self,i):
        self.pbar_ind["value"]=(i+1)*100/int(self.variable.get())
        time.sleep(0.05)
        self.raiz.update_idletasks()
        #print('finish:'+str((i+1)*100/int(self.variable.get())))

    def startSendRequest(self,url,request,concurrency,timeOut,filePath,x):
        for i in range(int(request)):
            Traffic.sendDataToServer(url,int(timeOut))
        self.on_done(x)
        #Thread(target=self.on_done(x)).start()
        

    def progress(self):
        print('')
        '''for x in range(101):
            print(x)
            #self.pbar_ind.step(0)
            self.pbar_ind["value"]=x
            #time.sleep(1)'''

    def print_path(self):
        f = filedialog.askopenfilename(
            parent=self.raiz, initialdir='/home/fernando/Desktop',
            title='Choose file',
            filetypes=[('txt files', '.txt')]
            )
        global entryText
        entryText.set(f)

def checkAllValues(url,request,concurrency,timeOut,filePath):
    checkOk = True
    if filePath:
            if not os.path.exists(filePath):
                checkOk = False
                messagebox.showinfo("Alert!!",'Parameters source:'+filePath+' not exist')
    else:
        checkOk = False
        messagebox.showinfo("Alert!!",'Parameters source is null o empty')

    if not(url and request and concurrency and timeOut):
        checkOk = False
        messagebox.showinfo("Alert!!",'some value was not entered, please check it!!!')
    else:
        if not isNumber(request):
            checkOk = False
            messagebox.showinfo("Alert!!",'the value of request is invalid, It should be a number')
    return checkOk

def isNumber(val):
    return val.isdigit()


def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()