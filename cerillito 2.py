import tkinter as GUI
import serial
import time

ventana = GUI.Tk()

PUERTO = "COM7"
arduino = serial.Serial(port=PUERTO, baudrate=115200, timeout=1)  

def CONECTAR():
    global PUERTO
    print("funcion conectar")
    PUERTO = EntryCOM.get()

def SEND():
    global PUERTO
    print("funcion ENVIO DE DATOS")
    x = SpinDATA.get()  
    arduino.write(bytes(x + '\n', 'utf-8')) 
    time.sleep(0.1)  
    data = arduino.read_until().decode('utf-8').strip()  
    LabelRECIVE.config(text=f"dato recibido = {data}")  

def CERRAR():
    print("cerrar")
    arduino.close()
    ventana.destroy()

# Instancia de los objetos
LabelCOM_NAME = GUI.Label(ventana, text="Escribe el nombre del puerto; ejem: COM2")
EntryCOM = GUI.Entry(ventana)
BotonCONECT = GUI.Button(ventana, text="CONECTAR", command=CONECTAR)
SpinDATA = GUI.Spinbox(ventana, from_=0, to=500)
BotonSEND = GUI.Button(ventana, text="ENVIAR", command=SEND)
LabelRECIVE = GUI.Label(ventana, text="dato recibido =")
BotonCerrar = GUI.Button(ventana, text="SALIR", command=CERRAR)

# Incrustacion en VENTANA
LabelCOM_NAME.pack(padx=1, pady=2)
EntryCOM.pack(padx=1, pady=2)
BotonCONECT.pack(padx=1, pady=2)
SpinDATA.pack(padx=1, pady=2)
BotonSEND.pack(padx=1, pady=2)
LabelRECIVE.pack(padx=1, pady=2)
BotonCerrar.pack(padx=1, pady=2)

ventana.mainloop()
