from tkinter import * 
from screen import ScadastroCliente as cc
from screen import ScadastroProduto as cp


def telaInicial():
    #iniciando tela
    home  = Tk()

    #Evento de button 
    def btn_cadastrarCliente_onclick():
        home.destroy()
        cc.telaCadastroCliente()
        print("acessou o cadastro de cliente")

    def btn_cadastrarProduto_onclick():
        cp.telaCadastroProduto()
        print("acessou o cadastro do produto")

    def btn_cadastrarPedidos_onclick():
        print("Verificar Pedidos")

    def btn_atualizarProdutos_onclick():
        print("verificar Produtos")

   
    #colocando o botão para fechar o programa
    btn_fecharprograma = Button(home, width=5, text="X", command=home.destroy)
    btn_fecharprograma.place(x=550, y= 10)

    h1 = Label(home, font="arial, 20" ,text="SISTEMA GEVE", foreground='#FFFFFF', background='#880000' )
    h1.place(x=188,y=80)

    btn_cadastrarCliente = Button(home, width=20, text="Cadastrar Cliente",command=btn_cadastrarCliente_onclick)
    btn_cadastrarCliente.place(x=220,y=140)

    btn_cadastrarProduto = Button(home, width=20, text="Cadastro de Produto", command=btn_cadastrarProduto_onclick)
    btn_cadastrarProduto.place(x=220,y=180)

    btn_cadastrarPedidos = Button(home, width=20, text="Cadastrar Pedido", command=btn_cadastrarPedidos_onclick)
    btn_cadastrarPedidos.place(x=220,y=220)

    btn_atualizarProdutos = Button(home, width=20, text="Verificar Pedidos", command=btn_atualizarProdutos_onclick)
    btn_atualizarProdutos.place(x=220,y=260)

    btn_atualizarProdutos = Button(home, width=20, text="Atualizar Produto", command=btn_atualizarProdutos_onclick)
    btn_atualizarProdutos.place(x=220,y=300)

    btn_atualizarProdutos = Button(home, width=20, text="Ver relatorio", command=btn_atualizarProdutos_onclick)
    btn_atualizarProdutos.place(x=220,y=340)



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
