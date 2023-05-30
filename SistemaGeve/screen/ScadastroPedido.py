from tkinter import * 
from tkinter import messagebox
from screen import Shome as hm
from scriptDB import crubPedidos as cp
from scriptDB import crubProdutos as cpp
from scriptDB import crubPedidosProdutos as ci
import datetime 


def telaCadastroPedidos():
    

    #iniciando tela

    home  = Tk()

    def btn_irparahome_onclick():
        home.destroy()
        hm.telaInicial()

    #Evento de button 
    def btn_cadastrarPedido_onclick():
        data_emissao = datetime.date.today()
        cp.cadastrarPedido(nome.get(),prazo.get(),data_emissao,subtotal.cget('text'))
        num_pedido = cp.selecionarUltimoPedido()
        for i in range(lbxProdutos.size()): 
             ci.cadastrarProdutoPedido(num_pedido[0],lbxProdutos.get(i),data_emissao,lbxQuantidade.get(i),lbxPreco.get(i),lbxTotal.get(i))
        home.destroy()
        hm.telaInicial()

        
    def subTotal(sub):
        total = float(subtotal.cget('text'))
        sub = sub + total
        subtotal.config(text=sub)
    
    def btn_inserirProdutos():
        cont = 0
        if(lbxProdutos.size() == 0):  
            lbxProdutos.insert(END,nome_product.get())
            lbxQuantidade.insert(END,quantidade.get())
            lbxPreco.insert(END,valor.get())
            aux = float(lbxPreco.get(0))* float(lbxQuantidade.get(0))
            aux_format = f"{aux:.2f}"
            subtotal.config(text=aux_format)
            lbxTotal.insert(END,aux_format)
           
        else:
            for i in range(lbxProdutos.size()):
                if nome_product.get() == lbxProdutos.get(i):
                    cont = cont + 1           
            if(cont == 0):
                lbxProdutos.insert(END,nome_product.get())
                lbxQuantidade.insert(END,quantidade.get())
                lbxPreco.insert(END,valor.get())
                aux = float(lbxPreco.get(END))* float(lbxQuantidade.get(END))
                aux_format = f"{aux:.2f}"
                subTotal(aux)
                lbxTotal.insert(END,aux_format)
            else:
                messagebox.showinfo("Erro", "Produto Cadastrado")
            

    def on_focus_nome(event,nome_product):
        if(cpp.ver_nome_produtos(nome_product.get())):
            return
        else:
            messagebox.showinfo("Alerta, Produto não encontrado")
    
    def validarFloat(evento,value):
        entry_value = value.get()
        try:
            float(entry_value)
        except ValueError:
            messagebox.showinfo("EXCEPTION","Numeros incorretos")

    #Topo da Página
    fmTop = Frame(home, bg="#F8F8F8", width=600, height=200)
    fmTop.place(x=0,y=0)

    #Botao de cadastro de produto
    btn_cadastrarProduto = Button(fmTop, width=14,pady=5, bg="#4A00FF",fg="#F8F8F8", text="Cadastrar", border=0,command=btn_cadastrarPedido_onclick)
    btn_cadastrarProduto.place(x=490,y=5)
    #Botao de cancelar o cadastro
    btn_cancelar = Button(fmTop, width=14,pady=5, bg="#4A00FF",fg="#F8F8F8", text="Cancelar", border=0,command=btn_irparahome_onclick)
    btn_cancelar.place(x=380,y=5)
    #Botal para inserir produto

    btnInserirProdutos = Button(fmTop,width=14,pady=5, bg="#4A00FF",fg="#F8F8F8", text="Inserir Produtos", border=0,command=btn_inserirProdutos)
    btnInserirProdutos.place(x=270,y=5)

    #Header Text
    h1 = Label(fmTop, font=("Microsoft YaHei UI Light",14) ,text="CADASTRO DE PEDIDO", foreground='#4A00FF', background='#F8F8F8')
    h1.place(x=10,y=40)

    
    ##DIV PRODUTOS
    ##
    fmProduto = Frame(fmTop, bg="#F8F8F8", width=400, height=400)
    fmProduto.place(x=280,y=35)
    #Pegando o nome do Produto
    nomeLabel = Label(fmProduto, font=("Microsoft YaHei UI Light",10),bg='#F8F8F8',fg='#4A00FF', text="Digite o nome do produto")
    nomeLabel.place(x=0,y=0)
    nome_product = Entry(fmProduto, width=40)
    nome_product.place(x=0,y=25)
    nome_product.bind("<FocusOut>", lambda event: on_focus_nome(event,nome_product))

    #Pegando a quantidade
    quantidadeLabel = Label(fmProduto, font=("Microsoft YaHei UI Light",10),bg='#F8F8F8',fg='#4A00FF', text="Digite a quantidade")
    quantidadeLabel.place(x=0,y=50)
    quantidade = Entry(fmProduto, width=40)
    quantidade.bind("<FocusOut>", lambda event: validarFloat(event,quantidade))
    quantidade.place(x=0,y=75)

    #Pegando o valor
    valorLabel = Label(fmProduto, font=("Microsoft YaHei UI Light",10),bg='#F8F8F8',fg='#4A00FF', text="Digite o valor")
    valorLabel.place(x=0,y=100)
    valor = Entry(fmProduto, width=40)
    valor.bind("<FocusOut>", lambda event: validarFloat(event,valor))
    valor.place(x=0,y=125)
    ##FIM DA DIV PRODUTOS

    #Pegando o nome do Cliente
    nomeLabel = Label(fmTop, font=("Microsoft YaHei UI Light",10),bg='#F8F8F8',fg='#4A00FF', text="Digite o nome do cliente")
    nomeLabel.place(x=10,y=70)
    nome = Entry(fmTop, width=40)
    nome.place(x=10,y=100)

    #Pegando o prazo
    prazoLabel = Label(fmTop, font=("Microsoft YaHei UI Light",10),bg='#F8F8F8',fg='#4A00FF', text="Digite o prazo")
    prazoLabel.place(x=10,y=130)
    prazo = Entry(fmTop, width=40)
    prazo.place(x=10,y=160)

#Rodape da pagina ____________________________________________________________________________________________________________________________________________
    fmDown = Frame(home, bg="#4A00FF", width=600, height=200)
    fmDown.place(x=0,y=200)

    #Inserir os produtos
    lbProdutos = Label(fmDown, bg="#4A00FF",fg="#F8F8F8", text="Produtos:", border=0,font=("Microsoft YaHei UI Light",12))
    lbProdutos.place(x=5,y=10)
    lbxProdutos = Listbox(fmDown, width=18, height=7, bg="#4A00FF",fg="#F8F8F8",border=1,font=("Microsoft YaHei UI Light",10))
    lbxProdutos.place(x=5, y=50)

    lbQuantidade = Label(fmDown, bg="#4A00FF",fg="#F8F8F8", text="Quantidade:", border=0,font=("Microsoft YaHei UI Light",12))
    lbQuantidade.place(x=150,y=10)
    lbxQuantidade = Listbox(fmDown, width=18, height=7, bg="#4A00FF",fg="#F8F8F8",border=1,font=("Microsoft YaHei UI Light",10))
    lbxQuantidade.place(x=150, y=50)

    lbPreco = Label(fmDown, bg="#4A00FF",fg="#F8F8F8", text="Preço:", border=0,font=("Microsoft YaHei UI Light",12))
    lbPreco.place(x=295,y=10)
    lbxPreco = Listbox(fmDown, width=18, height=7, bg="#4A00FF",fg="#F8F8F8",border=1,font=("Microsoft YaHei UI Light",10))
    lbxPreco.place(x=295, y=50)

    lbTotal = Label(fmDown, bg="#4A00FF",fg="#F8F8F8", text="Total:", border=0,font=("Microsoft YaHei UI Light",12))
    lbTotal.place(x=440,y=10)
    subtotal = Label(fmDown, bg="#4A00FF",fg="#F8F8F8",  border=0,font=("Microsoft YaHei UI Light",12))
    subtotal.place(x=490,y=10)

    lbxTotal = Listbox(fmDown, width=18, height=7, bg="#4A00FF",fg="#F8F8F8",border=1,font=("Microsoft YaHei UI Light",10))
    lbxTotal.place(x=440, y=50)
    

    
    
    
  


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
