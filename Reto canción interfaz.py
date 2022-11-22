from tkinter import *
from tkinter import ttk
from pytube import YouTube


def descargarCancion():
    url= datos_Entrada.get()
    youTube= YouTube(url)
    cancion=youTube.streams.get_audio_only()
    cancion.download()

ventana = Tk()
ventana.title("·Descargar música·")
ventana.resizable(False,False)
ventana.geometry("500x200")
ventana.config(background="thistle")

datos_Entrada= ttk.Entry(ventana)
datos_Entrada.place(x=45, y=35)

boton_Descargar= ttk.Button(ventana,text="Descargar canción", command=descargarCancion)
boton_Descargar.place(x=45, y=65)

label_Titulo= ttk.Label(ventana, text="Introduce la URL del vídeo:")
label_Titulo.config(background="thistle", border=3, font=("Times New Roman",14))
label_Titulo.pack()




#https://www.cdmon.com/es/apps/tabla-colores














ventana.mainloop()