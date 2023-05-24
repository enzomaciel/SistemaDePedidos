from tkinter import * 
from screen import Shome as hm
from scriptDB import crubPedidos as c
def telaCadastroPedidos():

    #iniciando tela
    home  = Tk()

    def btn_irparahome_onclick():
        home.destroy()
        hm.telaInicial()

    #Evento de button 
    def btn_cadastrarPedido_onclick():
        c.cadastrarProduto(nome.get())

    h1 = Label(home, font="arial, 20" ,text="CADASTRO DE PEDIDO", foreground='#FFFFFF', background='#880000')
    h1.place(x=150,y=40)

    #Pegando o nome do Cliente
    nomeLabel = Label(home, font="arial, 10",bg='#880000',fg='#FFFFFF', text="Digite o nome do cliente")
    nomeLabel.place(x=188,y=100)
    nome = Entry(home, width=40)
    nome.place(x=188,y=125)


    btn_cadastrarProduto = Button(home, width=10, font="arial, 10", bg='#FFFFFF', fg='#990000', text="Cadastrar",command=btn_cadastrarPedido_onclick)
    btn_cadastrarProduto.place(x=340,y=300)

    btn_cancelar = Button(home, width=10, font="arial, 10", bg='#990000', fg='#FFFFFF', text="Cancelar",command=btn_irparahome_onclick)
    btn_cancelar.place(x=188,y=300)


    #dimensoes da janela
    largura = 600
    altura = 400
    # resolução do nosso sistema
    largura_screen = home.winfo_screenwidth()
    altura_screen = home.winfo_screenheight()

    #posicao da janela
    posx =  largura_screen/2 - largura/2 
    posy = altura_screen/2 - altura/2 - 50

    #remover o titulo do tkinter
    home.overrideredirect(True)

    # definir a geometry
    home.geometry("%dx%d+%d+%d"% (largura,altura,posx,posy))
    home.title("Sistema Geve")
    home.configure(background='#880000')
    home.mainloop()
