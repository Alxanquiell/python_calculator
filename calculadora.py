
from tkinter import  Tk,Button,Entry,StringVar,Menu,messagebox as mb
from math import sqrt
from ast import literal_eval


class Calculator:
    def __init__(self):
        """"self.datos_resultados" datos que se procesaran con "eval".
        "self.paso" hace que no se pueda introducir numeros despues de a ver hecho los calculos,
        Ya que esto haria que se agregara otro numero al resultado.
        "self.varible_pantalla es la variable de pantalla, temporal el verdadero variable es "self.varp"
        se llama a la funcion "self.structura" que es la base de la calculadora.""" 
        self.datos_resultados=""
        self.paso="no"
        self.variable_pantalla=""
        self.digitos=0
        self.no_borrar=0
        self.a_digit=0
        self.valor_a_borrar=-1
        self.valor_parentesis=2

        self.structura()

    """Aqui los digitos se agregan a "self.variable_pantalla" y a "self.datos_resultados".
    Se valida si ha dividido entre "0" y se verifica si intenta agregar
    un numero despues de los calculos, para hacer esto se utiliza una variable
    llamada "type" que dice que tipo de dato recibe, sin antes a ver elegido un digito matematico,
    despues de que lo introduce se puede poner numeros de nuevo,"for" reformatea el texto para cambiar el
    % por MDL """
    def poner(self,valor,typee):
        if "ZeroDivisionError" in self.varp.get():
            self.varp.set("")
            self.datos_resultados=""

        if self.paso=="no" and typee =="numeros" or typee=="Digito":
            self.paso="no"
            self.datos_resultados+=valor
            self.variable_pantalla+=valor
            self.valor_a_borrar=-1

            if typee=="Digito":
                self.a_digit+=1

            elif typee=="numeros":
                self.a_digit=0

            if valor=="%":
                self.valor_a_borrar=-3
                self.variable_pantalla=self.variable_pantalla.replace("%","MDL")

                """self.variable_pantalla=""
                for i in self.datos_resultados:
                    if i == "%":
                        i=(" MDL ")
                    self.variable_pantalla+=i"""

            elif valor=="**":
                self.variable_pantalla=self.variable_pantalla.replace("**","^")

            elif valor=="/100":
                self.variable_pantalla=self.variable_pantalla.replace("/100","%")

            elif valor=="(" or valor == ")":
                self.valor_parentesis=3

            if self.a_digit==self.valor_parentesis:
                self.valor_parentesis=2
                self.a_digit=1

                self.variable_pantalla=self.variable_pantalla[:self.valor_a_borrar]

                if self.valor_a_borrar==-3:
                    self.valor_a_borrar=-1

                if valor=="**":
                    self.valor_a_borrar=-2

                self.datos_resultados=self.datos_resultados[:self.valor_a_borrar]
            self.varp.set(self.variable_pantalla)
            self.no_borrar=0

    #Aqui hacemos los calculalos utilizando el entring de la variable self.datos_resultados con el metodo eval
    
    def operacion(self):
        if self.datos_resultados!="" and self.varp!="":
            try:
                self.e=eval(self.datos_resultados)
                self.varp.set(self.e)
                self.ccz=str(self.e)
                self.paso="si"
                self.variable_pantalla=self.ccz
                self.no_borrar=1

            except ZeroDivisionError:
                self.varp.set("     ZeroDivisionError")

            except SyntaxError:
                self.varp.set("     SyntaxError")

            except TypeError:
                self.varp.set("     Introduce digito antes de (") 
    """Utilizamos el metodo "sqrt" de la libreria "math" para sacar la raiz cuadrada, a este
    lo agregamos al principio de los datos para que pueda ser procesado, y lo agregamos a la pantalla"""
    def raiz(self):
        self.datos_resultados=f"sqrt({self.datos_resultados})"
        self.varp.set(self.varp.get()+" raiz^2 ")

    """Borramos el ultimo digito de la pantalla y la variable que utiliza el eval"""
    def borrar(self):
        if self.no_borrar==0:
            self.datos_resultados=self.datos_resultados[:-1]
            self.variable_pantalla=self.variable_pantalla[:-1]
            self.varp.set(self.variable_pantalla)
            self.a_digit=0
            



    """Borramos los campos de pantalla y los datos de "self.datos_resultados" """
    def limpiar(self):
        self.datos_resultados=""
        self.variable_pantalla=""
        self.varp.set("")
        self.paso="no"


    def active_button(self):
        #self.b["background"]="red"
        self.bb["bg"]="red"
        print("d")

    def disable_button(self):
        #self.b["background"]="black"
        self.bb["bg"]="#1EF775"
        print("ddd")

    """Se configuran los botones y se les agrega la funcion "lambda" pasandole los parametros typee
    y el tipo de operacion"""
    def structura(self):
        self.root=Tk()
        self.root.title("Calculadora")
        self.varp=StringVar()  #readonly
        self.pantalla=Entry(self.root,justify="center",bd=15,state="readonly",textvariable=self.varp,fg="red",font=("calibri")).grid(row=0,columnspan=10,column=0,ipadx=40,ipady=10)
        self.root.resizable(0,0)
        self.root.config(bg="#062C5E")


        #menu
        self.menu=Menu(self.root)
        self.root.config(menu=self.menu)
        self.acerca_de=Menu(self.menu,tearoff=0)
        self.acerca_de.add_command(label="Acerca de..",command=lambda:mb.showinfo("Datos","Version= 1.1\nFecha de creacion= 31/08/2021\nCreado en= Python 3.9"))
        self.menu.add_cascade(label="Acerca de..",menu=self.acerca_de)

        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="MDL", width=5,height=3,font=("arial,11"),command=lambda:self.poner("%","Digito")).grid(row=1,column=4,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="%",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("/100","Digito")).grid(row=4,column=4,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text=")",   width=5,height=3,font=("arial,11"),command=lambda:self.poner(")","Digito")).grid(row=2,column=4,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="(",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("(","Digito")).grid(row=3,column=4,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="/",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("/","Digito")).grid(row=1,column=3,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="*",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("*","Digito")).grid(row=2,column=3,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="^x",  width=5,height=3,font=("arial,11"),command=lambda:self.poner("**","Digito")).grid(row=5,column=3,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="+",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("+","Digito")).grid(row=3,column=3,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="-",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("-","Digito")).grid(row=4,column=3,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text=".",   width=5,height=3,font=("arial,11"),command=lambda:self.poner(".","Digito")).grid(row=4,column=2,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="C",   width=5,height=3,font=("arial,11"),command=lambda:self.limpiar()).grid(row=4,column=0,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="Del", width=5,height=3,font=("arial,11"),command=lambda:self.borrar()).grid(row=5,column=0,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="green",  text="=",   width=5,height=3,font=("arial,11"),command=lambda:self.operacion()).grid(row=5,column=1,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#98E4DE",text="Raiz",width=5,height=3,font=("arial,11"),command=lambda:self.raiz()).grid(row=5,column=2,padx=2)
        self.b=Button(self.root,text=":D",width=5,height=3,font=("arial,11")).grid(row=5,column=4)


        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="0",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("0","numeros")).grid(row=4,column=1,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="9",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("9","numeros")).grid(row=1,column=2,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="8",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("8","numeros")).grid(row=1,column=1,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="7",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("7","numeros")).grid(row=1,column=0,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="6",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("6","numeros")).grid(row=2,column=2,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="5",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("5","numeros")).grid(row=2,column=1,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="4",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("4","numeros")).grid(row=2,column=0,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="3",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("3","numeros")).grid(row=3,column=2,padx=2)
        self.b=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="2",   width=5,height=3,font=("arial,11"),command=lambda:self.poner("2","numeros")).grid(row=3,column=1,padx=2)
        self.bb=Button(self.root,activebackground="#C4D3E3",bg="#1EF775",text="1",  width=5,height=3,font=("arial,11"),command=lambda:self.poner("1","numeros"))
        self.bb.grid(row=3,column=0,padx=2)

        self.bb.bind("<Enter>", self.active_button())
        self.bb.bind("<Leave>", self.disable_button())

        self.root.mainloop() 
Calculator()        
