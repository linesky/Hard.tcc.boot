
import tkinter as tk
global x1
global x2
global y2
global y1
# Coordenadas do retângulo
x1 = 190
y1 = 190
x2 = 210
y2 = 210
# Função para mover o retângulo para lado
def move_left(event):
    global x1
    global x2
    global y2
    global y1
    x1=x1-5
    x2=x2-5
    canvas.move(rectangle,  -5,0)
    canvas.coords(l1,0,0,x1,y1)
    canvas.coords(l2,400,0,x2,y1)
    canvas.coords(l3,0,400,x1,y2)
    canvas.coords(l4,400,400,x2,y2)
# Função para mover o retângulo para lado
def move_rigth(event):
    global x1
    global x2
    global y2
    global y1
    x1=x1+5
    x2=x2+5
    canvas.move(rectangle, 5,0)
    canvas.coords(l1,0,0,x1,y1)
    canvas.coords(l2,400,0,x2,y1)
    canvas.coords(l3,0,400,x1,y2)
    canvas.coords(l4,400,400,x2,y2)



# Função para mover o retângulo para cima
def move_up(event):
    global x1
    global x2
    global y2
    global y1
    y1=y1-5
    y2=y2-5
    canvas.move(rectangle, 0, -5)
    canvas.coords(l1,0,0,x1,y1)
    canvas.coords(l2,400,0,x2,y1)
    canvas.coords(l3,0,400,x1,y2)
    canvas.coords(l4,400,400,x2,y2)




# Função para mover o retângulo para baixo
def move_down(event):
    global x1
    global x2
    global y2
    global y1
    y1=y1+5
    y2=y2+5
    canvas.move(rectangle, 0, 5)
    canvas.coords(l1,0,0,x1,y1)
    canvas.coords(l2,400,0,x2,y1)
    canvas.coords(l3,0,400,x1,y2)
    canvas.coords(l4,400,400,x2,y2)



# Criar uma janela
window = tk.Tk()
window.title("Túnel Amarelo")

# Definir o tamanho da janela
window.geometry("400x400")

# Criar um canvas (área para desenho)
canvas = tk.Canvas(window, bg="yellow", width=400, height=400)
canvas.pack()


# Desenhar o retângulo no centro do canvas
rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
l1=canvas.create_line(0,0,x1,y1)
l2=canvas.create_line(400,0,x2,y1)
l3=canvas.create_line(0,400,x1,y2)
l4=canvas.create_line(400,400,x2,y2)
# Associar as teclas de seta para cima e para baixo às funções de movimento
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_rigth)



# Executar o loop da janela
window.mainloop()