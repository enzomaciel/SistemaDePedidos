from tkinter import * 
from scriptDB import crubLogin as cl
from screen import Shome as h
import re

def telaLogin():
    #iniciando tela
    home  = Tk()
    home
    
    frameLogin = Frame(home, bg="#F8F8F8", width=600, height=400)
    frameLogin.place(x=0,y=0)
    #lado esquerdo <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def registrar():
        nome = entryName.get() 
        username = entryUsername.get()
        password = entryPassword.get()
        email = entryMail.get()
        data = entryData.get()
        cpf = entryCPF.get()
        cl.cadastrarUsuario(nome,username,password,email,data,cpf)     
    def login():
        frameLeftInt.pack_forget()
        frameRightInt.pack()
    frameLeft = Frame(frameLogin, bg="#4A00FF",width=300, height=400)
    frameLeft.place(x=0,y=0)
    frameLeftInt = Frame(frameLeft, bg="#4A00FF", width=300,height=400)
    #Header Register
    registerHeader = Label(frameLeftInt, text="Register Account",bg="#4a00ff", fg="#F8F8F8",font=("Microsoft YaHei UI Light",20,"bold"))
    registerHeader.place(x=30, y=20)
    #Insert Full Name
    labelName = Label(frameLeftInt, width=10, bg="#4A00FF",fg="#F8F8F8", text="Full Name:", border=0,font=("Microsoft YaHei UI Light",12))
    labelName.place(x=21, y=90)
    entryName = Entry(frameLeftInt, width=18, bg="#4A00FF",fg="#F8F8F8", border=0,font=("Microsoft YaHei UI Light",11))
    entryName.place(x=110, y=90)
    Frame(frameLeftInt, width=150,height=2, bg="black").place(x=110,y=110)

    #Insert UserName
    def on_key_press(e):
        padrao = r'[a-z0-9\s]'
        name = entryUsername.get()
        name = name.lower()
        name_form = re.sub(padrao,'',name)
        entryUsername.delete(0, 'end')
        entryUsername.insert(0,name_form)

    labelUsername = Label(frameLeftInt, width=10, bg="#4A00FF",fg="#F8F8F8", text="Username:", border=0,font=("Microsoft YaHei UI Light",12))
    labelUsername.place(x=21, y=130)
    entryUsername = Entry(frameLeftInt, width=18, bg="#4A00FF",fg="#F8F8F8", border=0,font=("Microsoft YaHei UI Light",11))
    entryUsername.place(x=110, y=130)
    entryUsername.bind('<KeyPress>', on_key_press)
    Frame(frameLeftInt, width=150,height=2, bg="black").place(x=110,y=150)
    #Insert Password
    def on_key_press(e):
        name = entryPassword.get()

    labelPassword = Label(frameLeftInt, width=10, bg="#4A00FF",fg="#F8F8F8", text="Password:", border=0,font=("Microsoft YaHei UI Light",12))
    labelPassword.place(x=21, y=170)
    entryPassword = Entry(frameLeftInt, width=18, bg="#4A00FF",fg="#F8F8F8", border=0,font=("Microsoft YaHei UI Light",11),show="*")
    entryPassword.place(x=110, y=170)
    entryPassword.bind('<KeyPress>', on_key_press)
    Frame(frameLeftInt, width=150,height=2, bg="black").place(x=110,y=190)

    #Insert e-mail
    def on_key_press(e):
        name = entryMail.get()
        name = name.lower()

        entryMail.delete(0, 'end')
        entryMail.insert(0,name)

    labelMail = Label(frameLeftInt, width=10, bg="#4A00FF",fg="#F8F8F8", text="E-Mail:", border=0,font=("Microsoft YaHei UI Light",12))
    labelMail.place(x=34, y=210)
    entryMail = Entry(frameLeftInt, width=20, bg="#4A00FF",fg="#F8F8F8", border=0,font=("Microsoft YaHei UI Light",10))
    entryMail.place(x=110, y=210)
    entryMail.bind('<KeyPress>', on_key_press)
    Frame(frameLeftInt,width=150,height=2, bg="black").place(x=110,y=230)

    #Insert Data
    def on_key_press(e):
        name = entryData.get()
        name = name.lower()
        entryData.delete(0, 'end')
        entryData.insert(0,name)

    labelData = Label(frameLeftInt, width=8, bg="#4A00FF",fg="#F8F8F8", text="Birthday:", border=0,font=("Microsoft YaHei UI Light",12))
    labelData.place(x=35, y=250)
    entryData = Entry(frameLeftInt, width=20, bg="#4A00FF",fg="#F8F8F8", border=0,font=("Microsoft YaHei UI Light",10))
    entryData.place(x=110, y=250)
    entryData.bind('<KeyPress>', on_key_press)
    Frame(frameLeftInt, width=150,height=2, bg="black").place(x=110,y=270)

    #Insert CPF
    def on_key_press(e):
        padrao = r'[0-9\s]'
        name = entryCPF.get()
        name = name.lower()
        name_form = re.sub(padrao,'',name)
        entryCPF.delete(0, 'end')
        entryCPF.insert(0,name_form)

    labelCPF = Label(frameLeftInt, width=8, bg="#4A00FF",fg="#F8F8F8", text="CPF:", border=0,font=("Microsoft YaHei UI Light",12))
    labelCPF.place(x=50, y=290)
    entryCPF = Entry(frameLeftInt, width=20, bg="#4A00FF",fg="#F8F8F8", border=0,font=("Microsoft YaHei UI Light",10))
    entryCPF.place(x=110, y=290)
    entryCPF.bind('<KeyPress>', on_key_press)
    Frame(frameLeftInt, width=150,height=2, bg="black").place(x=110,y=310)

    #Button Registrar-se
    buttonRegistrar = Button(frameLeftInt, width=14,pady=5, bg="#F8F8F8",fg="#4A00FF", text="Registrar-se", border=0, command=registrar)
    buttonRegistrar.place(x=158, y=330)

    #Button Logar
    buttonRegistrar = Button(frameLeftInt, width=14,pady=5, bg="#F8F8F8",fg="#4A00FF", text="Login", border=0, command=login)
    buttonRegistrar.place(x=40, y=330)

    #lado direito >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    btn_fecharprograma = Button(home, width=5,border=0, bg="#4A00FF",fg="#F8F8F8", padx=2, pady=2, text="X", command=home.destroy)
    btn_fecharprograma.place(x=550, y= 10)

    def signin():
        username = entryLogin.get()
        password = entrySenha.get()
        aux = cl.verificarUsuario(username,password)
        if aux == 1:
            home.destroy()
            h.telaInicial()

        
    def signup():
        frameRightInt.pack_forget()
        frameLeftInt.pack()
    frameRight = Frame(frameLogin,bg="#F8F8F8", width=300, height=400)
    frameRight.place(x=300,y=0)
    frameRightInt = Frame(frameRight,bg="#F8F8F8", width=300, height=400)
    frameRightInt.pack()
    #Header Login
    loginHeader = Label(frameRightInt, text="Login Account",bg="#F8F8F8", fg="#0A0060",font=("Microsoft YaHei UI Light",20,"bold"))
    loginHeader.place(x=50, y=60)
    #Username 
    def on_enter(e):
        entryLogin.delete(0, 'end')
    def on_leave(e):
        name = entryLogin.get()
        if name=='':
           entryLogin.insert(0,'Username') 

    entryLogin = Entry(frameRightInt, width=27, bg="#F8F8F8",fg="#4A00FF", border=0,font=("Microsoft YaHei UI Light",11))
    entryLogin.place(x=40, y=130)
    entryLogin.insert(0,"Username")
    entryLogin.bind('<FocusIn>', on_enter)
    entryLogin.bind('<FocusOut>', on_leave)
    Frame(frameRightInt, width=217,height=2, bg="black").place(x=40,y=150)
    #password 
    def on_enter(e):
        entrySenha.delete(0, 'end')
    def on_leave(e):
        password = entrySenha.get()
        if password=='':
           entrySenha.insert(0,'Password') 

    entrySenha = Entry(frameRightInt, width=27, bg="#F8F8F8", fg="#4A00FF",border=0,font=("Microsoft YaHei UI Light",11),show="*")
    entrySenha.place(x=40, y=170)
    entrySenha.insert(0,"Password")
    entrySenha.bind('<FocusIn>', on_enter)
    entrySenha.bind('<FocusOut>', on_leave)
    Frame(frameRightInt, width=217,height=2, bg="black").place(x=40,y=190)
    #Login button 
    buttonLogin = Button(frameRightInt, width=30,pady=7, bg="#0A0060",fg="#E6DEFF", text="Login", border=0, command=signin)
    buttonLogin.place(x=40, y=230)
    #Sign button 
    labelSign = Label(frameRightInt, text="Não possui uma conta?", fg="black", bg="#F8F8F8",font=("Microsoft YaHei UI Light",9))
    labelSign.place(x=40, y=290)
    signButton = Button(frameRightInt, width=8,text="Registrar-se" , border=0, bg="#f8f8f8", cursor="hand2", fg="#4A00FF" ,command=signup)
    signButton.place(x=180,y=290)








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
