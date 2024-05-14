
import tkinter as tk
global x1
global x2
global y2
global y1
# Coordenadas do retangulo
x1 = -260
y1 = 200
x2 = 260
y2 = 600

# Funcao para mover o retangulo para cima
def move_2(event):
    global x1
    global x2
    global y2
    global y1
    if(y1>50):
        y1=y1-8
        y2=y2+8
        #x1=x1-8
        #x2=x2+8


    canvas.coords(l1,x1,y1,x2,y2)
    canvas.coords(l2,x1,y1+60,x2-60,y2-60)

   
    



# Funcao para mover o retangulo para baixo
def move_1(event):
    global x1
    global x2
    global y2
    global y1
    if(y1<200):
        y1=y1+8
        y2=y2-8
        #x1=x1+8
        #x2=x2-8
    
    canvas.coords(l1,x1,y1,x2,y2)
    
    canvas.coords(l2,x1,y1+60,x2-60,y2-60)



# Criar uma janela
window = tk.Tk()
window.title("horizante")

# Definir o tamanho da janela
window.geometry("400x400")

# Criar um canvas (area para desenho)
canvas = tk.Canvas(window, bg="yellow", width=400, height=400)
canvas.pack()


# Desenhar o retangulo no centro do canvas

cords=-260,200,260,600
cords2=-260,260,200,660
rectangle = canvas.create_rectangle(0, 200, 400, 400, fill="gold")
l1=canvas.create_arc(cords,start=0,extent=90,fill="yellow")
l2=canvas.create_arc(cords2,start=0,extent=90,fill="gold")
rectangle = canvas.create_rectangle(0, 0, 400, 200, fill="yellow")
#l2=canvas.create_arc(0,45,100,fill="yellow")
# Associar as teclas de seta para cima e para baixo as funcoes de movimento
window.bind("<Left>", move_2)
window.bind("<Right>", move_1)



# Executar o loop da janela
window.mainloop()