import tkinter as tk
import pygame
import os

class ReproductorMusical(tk.Frame):
    def __init__(self, container):
        
        # Definición de contenedor
        super().__init__(container)
        self.container = container
        container.configure(background = 'dark slate gray')
        self.title = container.title('BIT Music')
        self.geometry = container.geometry('300x300')

        canciones = os.listdir('Canciones')
        self.listaCanciones = tk.Listbox(container, selectmode = 'SINGLE')
        
        k = 1
        for j in canciones:
            self.listaCanciones.insert(k, j)
            k += 1
        
        var = tk.StringVar()
        self.cancion = tk.Label(container, textvariable=var)
        
        self.reproducir = tk.Button(container, width=5, height=1, text='PLAY', command=self.ReproducirCancion)
        self.pausar = tk.Button(container, width=5, height=1, text='PAUSE', command=self.PausarCancion)
        self.detener = tk.Button(container, width=5, height=1, text='STOP', command=self.DetenerCancion)
        
        self.cancion.pack()
        self.reproducir.pack(fill='x')
        self.pausar.pack(fill='x')
        self.detener.pack(fill='x')
        
        self.listaCanciones.pack(fill='both', expand='yes')

    pygame.init()
    pygame.mixer.init()
    def ReproducirCancion(self):
        pygame.mixer.music.load(self.listaCanciones.get(tk.ACTIVE))
        var.set(self.listaCanciones.get(tk.ACTIVE))
        pygame.mixer.music.play()
    
    def DetenerCancion(self):
        pygame.mixer.music.stop()
    
    def PausarCancion(self):
        pygame.mixer.music.pause()
    
root = tk.Tk()
app = ReproductorMusical(root)
app.mainloop()