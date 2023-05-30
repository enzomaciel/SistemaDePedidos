from tkinter import * 
from screen import ScadastroCliente as cc
from screen import ScadastroProduto as cp
from screen import ScadastroPedido as cpp
from scriptDB import crubPedidos
from scriptDB import crubPedidosProdutos



def relatorioPedidos():
    #iniciando tela

    home  = Tk()
    #Evento de button 
    

   
    #colocando o botão para fechar o programa
    btn_fecharprograma = Button(home, width=5, border=0,padx=2, text="X", command=home.destroy)
    btn_fecharprograma.place(x=550, y= 10)

    h1 = Label(home, font=("Microsoft YaHei UI Light",25,"bold") ,text="Relatorio de pedidos", foreground='#F8F8F8', background='#4A00FF' )
    h1.place(x=175,y=50)
    aux = crubPedidos.selecionarUltimoPedido()[0]
    
    for i in range(aux):
        lbNumPedido = Label(home, font=("Microsoft YaHei UI Light",10,"bold"), foreground='#F8F8F8', background='#4A00FF')
        aux2 = crubPedidos.ver_num_pedidos(i)
        num_pedido = aux2[0]
        nome_cliente = aux2[1]
        relatorioPedido = "N.Pedido= "+str(num_pedido)+ "   "+ "Cliente: "+nome_cliente
        lbNumPedido.config(text=relatorioPedido)
        aux4 = crubPedidosProdutos.selecionarUltimoProduto()[0]
        for j in range(aux4):
            lbNumPedido2 = Label(home, font=("Microsoft YaHei UI Light",10,"bold"), foreground='#F8F8F8', background='#4A00FF')
            aux3 = crubPedidosProdutos.ver_num_prodPedido(j,i)
            num_pedido2 = aux3[1]
            produto = aux3[2]
            quantidade = aux3[4]
            valor = aux3[5]
            total = aux3[6]
            relatorioPedido2 = "N.Pedido= "+num_pedido2+ "   "+ "Produto= "+produto +"   "+ "Quantidade= "+quantidade+ "   "+ "valor= "+valor+"   "+"Total= "+total
            lbNumPedido2.config(text=relatorioPedido2)
            nrow = (120+i*20)
            lbNumPedido.place(x=40, y=nrow)


        nrow = (100+i*40)
        lbNumPedido.place(x=10, y=nrow)

    



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
