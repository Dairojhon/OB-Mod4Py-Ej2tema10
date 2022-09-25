import tkinter

from tkinter import ttk

def mostrarSeleccion():
    seleccion=listado.get()
    texto='Usted ha seleccionado {}'.format(seleccion)
    lblSeleccion=tkinter.Label(window, text=texto)
    lblSeleccion.place(x=10,y=100)

window = tkinter.Tk()
window.config(widt=300, height=250)
lblpeticion=tkinter.Label(window,text='Por favor seleccione de la lista la opción que desea:',)
listado=ttk.Combobox(state='readonly',
                     values=['Verano','Invierno','Otoño','Primavera'])
btnSeleccion=ttk.Button(text='Seleccionar',command=mostrarSeleccion)
lblpeticion.place(x=10,y=10)
listado.place(x=10, y=40)
btnSeleccion.place(x=10,y=70)


window.mainloop()