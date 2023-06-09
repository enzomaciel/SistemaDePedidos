from tkinter import * 
from screen import ScadastroCliente as cc
from screen import ScadastroProduto as cp
from screen import ScadastroPedido as cpp
from screen import SverPedidos as vp



def telaInicial():
    #iniciando tela

    home  = Tk()
    #Evento de button 
    def btn_cadastrarCliente_onclick():
        home.destroy()
        cc.telaCadastroCliente()

    def btn_cadastrarProduto_onclick():
        home.destroy()
        cp.telaCadastroProduto()

    def btn_cadastrarPedidos_onclick():
        home.destroy()
        cpp.telaCadastroPedidos()

    def btn_relatorioPedidos_onclick():
        home.destroy()
        vp.relatorioPedidos()
        print("verificar Produtos")

   
    #colocando o botão para fechar o programa
    btn_fecharprograma = Button(home, width=5, border=0,padx=2, text="X", command=home.destroy)
    btn_fecharprograma.place(x=550, y= 10)

    h1 = Label(home, font=("Microsoft YaHei UI Light",25,"bold") ,text="SISTEMA GEVE", foreground='#F8F8F8', background='#4A00FF' )
    h1.place(x=175,y=50)

    btn_cadastrarCliente = Button(home,width=20,pady=5, bg="#F8F8F8",fg="#4A00FF", border=0, text="Cadastrar Cliente",command=btn_cadastrarCliente_onclick, relief="solid")
    btn_cadastrarCliente.place(x=220,y=140)

    btn_cadastrarProduto = Button(home,width=20,pady=5, bg="#F8F8F8",fg="#4A00FF", border=0, text="Cadastro de Produto", command=btn_cadastrarProduto_onclick)
    btn_cadastrarProduto.place(x=220,y=180)

    btn_cadastrarPedidos = Button(home,width=20,pady=5, bg="#F8F8F8",fg="#4A00FF", border=0, text="Cadastrar Pedido", command=btn_cadastrarPedidos_onclick)
    btn_cadastrarPedidos.place(x=220,y=220)

    btn_atualizarProdutos = Button(home,width=20,pady=5, bg="#F8F8F8",fg="#4A00FF", border=0, text="Relatorio de Pedidos", command=btn_relatorioPedidos_onclick)
    btn_atualizarProdutos.place(x=220,y=260)



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
    home.configure(background='#4A00FF')
    home.mainloop()
