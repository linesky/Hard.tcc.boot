
import tkinter as tk
global x1
global x2
global y2
global y1
# Coordenadas do retangulo
x1 = 0
y1 = 200
x2 = 400
y2 = 400

# Funcao para mover o retangulo para cima
def move_up(event):
    global x1
    global x2
    global y2
    global y1
    y1=y1+5

    canvas.coords(l1,200,y1,0,y2)
    canvas.coords(l2,200,y1,400,y2)
    canvas.coords(rectangle,x1,y1,x2,y2)
    



# Funcao para mover o retangulo para baixo
def move_down(event):
    global x1
    global x2
    global y2
    global y1
    y1=y1-5

    canvas.coords(l1,200,y1,0,y2)
    canvas.coords(l2,200,y1,400,y2)
    canvas.coords(rectangle,x1,y1,x2,y2)



# Criar uma janela
window = tk.Tk()
window.title("horizante")

# Definir o tamanho da janela
window.geometry("400x400")

# Criar um canvas (area para desenho)
canvas = tk.Canvas(window, bg="yellow", width=400, height=400)
canvas.pack()


# Desenhar o retangulo no centro do canvas
rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="gold")
l1=canvas.create_line(200,y1,0,y2,fill="black")
l2=canvas.create_line(200,y1,400,y2,fill="black")
# Associar as teclas de seta para cima e para baixo as funcoes de movimento
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)



# Executar o loop da janela
window.mainloop()