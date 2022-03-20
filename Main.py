from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
from Formulario import Formularios
from Analizador import Analizador
from Reportes import Reportes
import webbrowser
import easygui
import os

class VentanaMain:
    def __init__(self, master):
        self.master = master
        self.master.title("Primer Proyecto")
        self.master.resizable(False,False)
        self.master.config(bg="green")
        self.master.iconbitmap(".\Imagenes\ico.ico")
        self.Data=""
        self.Reportes=Reportes()
        self.Gadgetts()
        
    def Gadgetts(self):
        self.miFrame=Frame()
        self.miFrame.pack()
        self.miFrame.config(bg="pale green")
        self.miFrame.config(width="900", height="700")
        label_CargarArchivo=Label(self.miFrame, text="Cargar archivo .form",bg="pale green",fg="black", font=("Arial",12)).place(x=20,y=10)
        
        Faux=Frame()
        Faux.place(x=20,y=80)
        
        scroll=Scrollbar(Faux)
        scroll.pack(side="right",fill="y")

        self.textCaja=Text(Faux, width="105", height="35.5", yscrollcommand=scroll.set)
        self.textCaja.pack(side="left")

        scroll.config(command=self.textCaja.yview)

        self.botonCargarArchivo = Button(self.miFrame,text="Cargar Archivo",bg="spring green",activebackground="lawn green",font=("Arial",12),command=self.CargarArchivo)
        self.botonCargarArchivo.place(x=20,y=40)

        self.botonAnalizar = Button(self.miFrame,text="Analizar",bg="spring green",activebackground="lawn green",font=("Arial",12),command=self.Analizar)
        self.botonAnalizar.place(x=20,y=660)

        self.combobox=Combobox(self.miFrame,values=["Reporte de tokens","Reporte de errores","Manual de Usuario","Manual Técnico"],font=("Arial",12),state="readonly")
        self.combobox.place(x=675,y=45)
        self.combobox.current(0)
        self.combobox.bind('<<ComboboxSelected>>', self.seleccion)

    def seleccion(self,event):
        valor=self.combobox.get()
        if valor=="Manual Técnico":
            webbrowser.open_new_tab("file:///"+os.getcwd()+"/Manuales/Manual Tecnico.pdf")
        elif valor=="Manual de Usuario":
            webbrowser.open_new_tab("file:///"+os.getcwd()+"/Manuales/Manual de Usuario.pdf")
        elif valor=="Reporte de errores":
            if os.path.exists("./Reportes/ReporteErrores.html"):
                webbrowser.open_new_tab("file:///"+os.getcwd()+"/Reportes/ReporteErrores.html")
            else:
                showinfo(title='ERROR',message="Aun no se a generado el reporte.")
        elif valor=="Reporte de tokens":
            if os.path.exists("./Reportes/ReporteTokens.html"):
                webbrowser.open_new_tab("file:///"+os.getcwd()+"/Reportes/ReporteTokens.html")
            else:
                showinfo(title='ERROR',message="Aun no se a generado el reporte.")

    def Analizar(self):
        Data=str(self.textCaja.get("1.0",END))
        if Data!="":
            self.Data=Data
            print("[ANALIZAR]: Analizando...")
            analizador=Analizador()
            analizador.analizar(self.Data)
            formulario=Formularios(self.Data)
            formulario.Crear(analizador.listaTokens)
            self.Reportes.ReporteTokens(analizador.listaTokens)
            self.Reportes.ReporteErrores(analizador.listaErrores)
        else:
            print("[ERROR-ANALIZAR]: El campo esta vacio")

    def CargarArchivo(self):
        while True:
            try:
                #ruta=easygui.fileopenbox(title="Abre el archivo tipo .form")
                ruta="prueba1.form"
                extension=os.path.splitext(ruta)
                if extension[1].upper()==".FORM":
                    print("[CARGAR ARCHIVO]: La extension es correcta")
                    try:
                        Archivo=open(ruta,"r",encoding='utf-8')
                        Contenido=Archivo.read()
                        Archivo.close()
                        try:
                            self.textCaja.delete("1.0",END)
                            self.textCaja.insert(END,Contenido)
                            print("[CARGAR ARCHIVO]: Carga completada")
                        except:
                            print("[ERROR-CARGAR ARCHIVO]: Ocurrio un error al llevar la informacion a self.textCaja")
                        break
                    except:
                        print("[ERROR-CARGAR ARCHIVO]: Ocurrio un error al leer el archivo")
                else:
                    print("[ERROR-CARGAR ARCHIVO]: Extencion incorrecta")
            except:
                print("[ERROR-CARGAR ARCHIVO]: Ocurrio un error al abrir el archivo")
        

root = Tk()
Ventana=VentanaMain(root)
root.mainloop()