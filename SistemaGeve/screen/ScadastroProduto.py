from tkinter import * 
from screen import Shome as hm
from scriptDB import crubProdutos as c
def telaCadastroProduto():

    #iniciando tela
    home  = Tk()

    def btn_irparahome_onclick():
        home.destroy()
        hm.telaInicial()

    #Evento de button 
    def btn_cadastrarProduto_onclick():
        c.cadastrarProduto(nome.get(),unidade.get(),valor.get(),comissao.get())

    h1 = Label(home, font=("Microsoft YaHei UI Light",20) ,text="CADASTRO DE PRODUTO", foreground='#F8F8F8', background='#4A00FF')
    h1.place(x=150,y=40)

    #Pegando o nome do Produto
    nomeLabel = Label(home, font=("Microsoft YaHei UI Light",10),bg='#4A00FF',fg='#F8F8F8', text="Digite o nome do produto")
    nomeLabel.place(x=188,y=100)
    nome = Entry(home, width=40)
    nome.place(x=188,y=125)

    #Pegando o unidade do produto
    unidadeLabel = Label(home,font=("Microsoft YaHei UI Light",10),bg='#4A00FF',fg='#F8F8F8', text="Digite a unidade do produto")
    unidadeLabel.place(x=188,y=150)
    unidade = Entry(home, width=40)
    unidade.place(x=188,y=175)

    #pegando o valor unitario do produto

    valorLabel = Label(home, font=("Microsoft YaHei UI Light",10), bg='#4A00FF', fg='#F8F8F8', text="Digite o valor unitario do produto")
    valorLabel.place(x=188, y=200)
    valor = Entry(home, width=40)
    valor.place(x=188,y=225)

    #pegando o valor da comissao do produto

    comissaoLabel = Label(home, font=("Microsoft YaHei UI Light",10), bg='#4A00FF', fg='#F8F8F8', text="Digite o comissao do produto")
    comissaoLabel.place(x=188, y=250)
    comissao = Entry(home, width=40)
    comissao.place(x=188,y=275)


    btn_cadastrarProduto = Button(home, width=10, font=("Microsoft YaHei UI Light",10), bg='#F8F8F8', fg='#4A00FF', text="Cadastrar",command=btn_cadastrarProduto_onclick)
    btn_cadastrarProduto.place(x=340,y=300)

    btn_cancelar = Button(home, width=10,font=("Microsoft YaHei UI Light",10), bg='#4A00FF', fg='#F8F8F8', text="Cancelar",command=btn_irparahome_onclick)
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
    home.configure(background='#4A00FF')
    home.mainloop()
