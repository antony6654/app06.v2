import flet as ft
import random
from flet_core.textfield import TextField
from flet_core.elevated_button import ElevatedButton

#Función principal
#funcion para adivinar el numero
def verificar_adivinanza(e,page):
    adivinanza_usuario=int(entrada_numero.value)
    
    if adivinanza_usuario == numero_Secreto:
        texto_resultado.value="¡felicidades¡ adivinante el numero secreto"
        boton_adivinar.disabled=True
        img2=ft.Image(src="correcto.png")
        page.add(ft.Audio(src="victoria.mp3",autoplay=True),img2)
        
    elif adivinanza_usuario < numero_Secreto:
        texto_resultado.value="¡fallaste¡ el numero es secreto es maypr"
        boton_adivinar.disabled=True
        img2=ft.Image(src="mal.png")
        page.add(ft.Audio(src="boing.mp3",autoplay=True),img2)
        
    else:
        texto_resultado.value="¡fallastes¡ el numero secreto es menor"
        boton_adivinar.disabled=True
        img2=ft.Image(src="mal.png")
        page.add(ft.Audio(src="boing.mp3",autoplay=True),img2)


def main(page: ft.Page):
    #Variables globales
    global numero_Secreto,entrada_numero,texto_resultado,boton_adivinar
    
    page.title = "Adivina el número"
    
    #Generar un número aleatorio
    numero_Secreto = random.randint(1,100)
    
    #Crear los elementos de la interfaz
    titulo=ft.Text("Adivina el número",size= 20,color="white")
    entrada_numero=ft.TextField(label="Tu Adivinanza entrre el 1 y 100",width=330)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    texto_resultado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=300
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="red",
        width=page.window.width,    
        height=page.window.height,
        padding=20
            
        
    )
    page.add(contenedor_principal)



ft.app(main)
