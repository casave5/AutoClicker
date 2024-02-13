import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyautogui as raton
import time
import random
coordenadas_x = []
coordenadas_y = []
contador = 1
# Definir las opciones disponibles para el combo
opciones = ["Si", "No"]


def validar_numero(valor):
    # Verificamos si el valor ingresado es un número
    if valor.isdigit():
        return True  # Aceptamos el valor
    else:
        return False  # Rechazamos el valor

# Función que se ejecuta cuando se modifica el contenido de cualquier Entry
def on_modificar(event):
    # Obtenemos el widget que generó el evento
    widget = event.widget
    
    # Obtenemos el contenido del Entry
    valor = widget.get()
    
    # Validamos el contenido del Entry
    if not validar_numero(valor):
        # Si el contenido no es válido, borramos el último carácter
        widget.delete(len(valor) - 1)

def activar_evento():
    # Asociar la función capturar_posicion al evento de tecla presionada
    messagebox.showinfo("Información", "Para determinar el Área a clicquear, Ubique el puntero del Raton Arriba a la Izquierda Y presione la tecla C Luego abajo a la derecha y presione la tecla C")
    ventana.bind("<KeyPress>", capturar_posicion)

def capturar_posicion(event):
    global contador
    #Verificar si se presionó la tecla deseada para activar la captura
    if event.char == 'c' and contador <= 2:
        #Obtener las coordenadas x , y del ratón fuera de la ventana
        x, y = raton.position()
        coordenadas_x.append(x)
        coordenadas_y.append(y)
        etiqueta.config(text=f"Posición {contador} del ratón: X={coordenadas_x}, Y={coordenadas_y}")
        etiqueta.grid(row=5, column=0, pady = 2, padx = 2, columnspan = 3)
        contador += 1 
    if contador > 2:
        etiqueta2.config(text="Ya se guardó el área a clickear")
        etiqueta2.grid(row=6, column=0, pady = 2, padx = 2, columnspan = 3)
        ventana.unbind("<KeyPress>")
        btn_activar.config(state="disabled")
        Boton.config(state="normal")

def Cuenta_Final(tiempo_inicio,pancake):
#Calculado el Tiempo de ejecución en segundos
    tiempo_fin = time.perf_counter()
    tiempo_Total = tiempo_fin - tiempo_inicio
    tiempo_Total = round(tiempo_Total)
#Formateando el resusltado en HH:MM:SS
    Horas = tiempo_Total//3600
    Sobra_H = tiempo_Total%3600
    Minutos = Sobra_H//60
    Segundos = Sobra_H%60
    label_resultado = tk.Label(ventana, text="")
    label_resultado.config(text=f"{pancake} Comidas Realizadas en: {Horas}H:{Minutos}M:{Segundos}S")
    label_resultado.grid(row=7, column=0, pady = 2, padx = 4, columnspan=2)
    
def Status_Bot():
    #Ubicando el Raton
    rango_x = (coordenadas_x)
    rango_y = (coordenadas_y)
    P1_x = (261,1830)
    P1_y = (166,960)
    posicion_Aleatoria_P1X, posicion_Aleatoria_P1Y = random.randrange(*P1_x), random.randrange(*P1_y)
    posicion_x, posicion_y = random.randrange(*rango_x), random.randrange(*rango_y)
    posicion_actual = raton.position()
    if seleccion == 'Si':
        raton.moveTo(posicion_x, posicion_y)
        raton.click()
        raton.moveTo(posicion_Aleatoria_P1X,posicion_Aleatoria_P1Y,)
        raton.click()
    else:
        raton.moveTo(posicion_x, posicion_y)
        raton.click()
        raton.moveTo(posicion_actual)
    
def iniciar_barra(tiempo):
    barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")
    barra_progreso.grid(row=6, column=0, padx=4, columnspan = 4, sticky="nsew")
    barra_progreso["value"] = 0  # Restablecer la barra de progreso
    ventana.update()
    segundos = tiempo
    for i in range(tiempo + 1):
            barra_progreso["value"] = (i / tiempo) * 100
            ventana.update()
            etiqueta2.config(text=f"{segundos}", justify="center")
            etiqueta2.grid(row=6, column=0, pady=2, padx=2, columnspan = 4)
            #etiqueta2.winfo_toplevel().attributes('-alpha', 0.5)
            etiqueta2.lift()
            time.sleep(1)  # Simular alguna tarea
            segundos-= 1
    barra_progreso["value"] = 0
    ventana.update()

def validar_dinamica():
    seleccion = combo.get()
    if combo.get() not in opciones:
        messagebox.showerror("Error", "Debes seleccionar una opción válida Si o No.")
        combo.focus_set()  # Establecer el foco en el combobox
    else:
        #tk.messagebox.showinfo("Selección válida", f"Has seleccionado: {seleccion}")
        iniciar_Colecta(cantidad,Tmp_C)
   
def realizar_click(entrada,tiempo_coccion):
    try:
        global cantidad , Tmp_C 
        cantidad = int(entrada.get())
        Tmp_C = int(tiempo_coccion.get())
        label_resultado = tk.Label(ventana, text="")
        label_resultado.grid(row=15, column=0, columnspan=3)
        validar_dinamica()
    except ValueError:
        tk.messagebox.showerror("Error", "Recuerda debes colocar la cantidad a realizar o el tiempo de cocción")
        entrada.focus_set()
    
def iniciar_Colecta(cantidad,Tmp_C):
    etiqueta = tk.Label(ventana, text="")
    #Declarando Variables
    pancake = 0
    tiempo_total = 0
    tiempo_inicio = time.perf_counter()
    while pancake < cantidad:
        ventana.update()
        tiempo_inicial = time.perf_counter()
        pancake += 1

    #CREAR PANCAKE  
        Status_Bot()
        aleatoreo = random.randint(3,6)
        tiempo = aleatoreo + Tmp_C
        texto = tk.Text(ventana, height=3, width=40)
        texto.grid(row=5, column=0, pady = 2, padx = 4, columnspan=3)
        texto.delete(1.0, tk.END)
        resultado = f"Haciendo Comida #{pancake} de {cantidad}"
        texto.insert(tk.END, resultado + "\n")
        resultado =f"Esperando {tiempo} Segundos"
        texto.insert(tk.END, resultado + "\n")
        iniciar_barra(tiempo)
                                
    #COLECTAR PANCAKE   
        Status_Bot()
        tiempo = random.randint(3,5)
        tiempo_final = time.perf_counter()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        texto.delete(1.0, tk.END)
        resultado = f"Colectó Comida #{pancake} de {cantidad} en {int(tiempo_ejecucion)} segundos"
        texto.insert(tk.END, resultado + "\n")
        if pancake < cantidad:
            resultado =f"Esperando {tiempo} Segundos"
            texto.insert(tk.END, resultado + "\n")
            iniciar_barra(tiempo)
        else:
            Cuenta_Final(tiempo_inicio,pancake)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Click Automatico")
ventana.geometry("400x250") #Configurar tamaño
#ventana.resizable(1,1)
ventana.resizable(False, False)
#Agregando la propiedades de fondo transparente
ventana.wm_attributes('-transparentcolor', '#ab23ff')
# Variable para almacenar la selección del usuario
seleccion = tk.StringVar()

# Crear etiquetas y entradas para ingresar las coordenadas

tk.Label(ventana, text="Ingrese la cantidad a realizar: ", justify="left").grid(row=1, column=0, pady = 4, padx = 2, sticky="w")
entrada = tk.Entry(ventana, width=5)
entrada.grid(row = 1, column = 1, pady = 2, sticky="w")
entrada.bind("<KeyRelease>", on_modificar)  # Asociar la función de validación al evento de modificación

tk.Label(ventana, text="Ingrese tiempo de Cocción:", justify="left").grid(row=2, column=0, pady = 4, padx = 2, sticky="w")
tiempo_coccion = tk.Entry(ventana, width=5)
tiempo_coccion.grid(row = 2, column = 1, pady = 2, sticky="w")
tiempo_coccion.bind("<KeyRelease>", on_modificar)  # Asociar la función de validación al evento de modificación

tk.Label(ventana, text="¿El bot está solo? ", justify="left").grid(row = 3, column = 0, pady = 4, padx = 2, sticky="w")
combo = ttk.Combobox(ventana, values=opciones, textvariable=seleccion, state="readonly", width=5)
combo.grid(row = 3, column = 1, pady = 2, sticky="w")
combo.set(opciones[1])

# Etiqueta para mostrar la posición del ratón
etiqueta = tk.Label(ventana, text="", justify="center")
etiqueta2 = tk.Label(ventana, text="", justify="center", bg=ventana['bg'])
 
# Botón para realizar el clic
Boton = tk.Button(ventana, text="Ejecutar", state="disabled", command=lambda: realizar_click(entrada,tiempo_coccion)) 
Boton.grid(row = 4, column = 0, pady = 3, padx = 4, sticky="nsew")

# Botón para activar y desactivar el evento de capatura del area para hcer click
btn_activar = tk.Button(ventana, text="Capturar Área", command=activar_evento)
btn_activar.grid(row = 4, column = 1, pady = 3, padx = 2, columnspan = 2, sticky="nsew")

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
