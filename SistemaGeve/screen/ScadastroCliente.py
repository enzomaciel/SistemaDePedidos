from tkinter import * 
from screen import Shome as hm
from scriptDB import crubClientes as c



def telaCadastroCliente():
    #iniciando tela
    home  = Tk()

    #Evento de button 
    def btn_irparahome_onclick():
        home.destroy()
        hm.telaInicial()

    def btn_cadastrarCliente_onclick():
        print(nome + telefone + endereco)
        print("Cadastro de cliente")

    

    
    h1 = Label(home, font="arial, 20" ,text="CADASTRO DE CLIENTE", foreground='#FFFFFF', background='#880000')
    h1.place(x=150,y=40)

    #Pegando o nome do Cliente
    nomeLabel = Label(home, font="arial, 10",bg='#880000',fg='#FFFFFF', text="Digite o nome do Cliente")
    nomeLabel.place(x=188,y=100)
    nome = Entry(home, width=40, text="Digite o nome do Cliente")
    nome.place(x=188,y=125)

    #Pegando o telefone do Cliente
    telefoneLabel = Label(home, font="arial, 10",bg='#880000',fg='#FFFFFF', text="Digite o telefone do cliente")
    telefoneLabel.place(x=188,y=150)
    telefone = Entry(home, width=40, text="Digite o numero do cliente")
    telefone.place(x=188,y=175)

    #pegando o endereço do Cliente

    enderecoLabel = Label(home, font="arial, 10", bg='#880000', fg='#FFFFFF', text="Digite o endereço do cliente")
    enderecoLabel.place(x=188, y=200)
    endereco = Entry(home, width=40, text="Digite o endereço do cliente")
    endereco.place(x=188,y=225)


    btn_cadastrarCliente = Button(home, width=10, font="arial, 10", bg='#FFFFFF', fg='#990000', text="Cadastrar",command=btn_cadastrarCliente_onclick)
    btn_cadastrarCliente.place(x=340,y=265)

    btn_cancelar = Button(home, width=10, font="arial, 10", bg='#990000', fg='#FFFFFF', text="cancelar",command=btn_irparahome_onclick)
    btn_cancelar.place(x=188,y=265)
    


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
