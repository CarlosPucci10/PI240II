import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import sqlite3
from tkinter import messagebox
import time



imagem_logo = None
entrylogin = None
entrynome = None
entrycpf = None
entrydatanasc = None
entryrua = None
entrynumero = None
entryvila = None

def criar_tabela():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT,
        datanasc TEXT,
        rua TEXT,
        numero TEXT,
        vila TEXT
    )
    ''')

    conn.commit()
    conn.close()

criar_tabela()
#_________________________________________________________________________________________________________________________________________
def ajuda():
    janelaajuda = tk.Toplevel()
    janelaajuda.title("Projeto Pedala Sarapuí")
    janelaajuda.geometry("340x480")
    janelaajuda.configure(bg="white")
    
    imagem_logo1 = PhotoImage(file="logo01.png")
    label_imagem = tk.Label(janelaajuda, image=imagem_logo1, bg="white")
    label_imagem.pack()

    textotitulo = tk.Label(janelaajuda, text="Projeto Pedala Sarapuí", bg="white", font="Arial 15")
    textotitulo.pack()
    textotitulo = tk.Label(janelaajuda, text="", bg="white", font="Arial 15")
    textotitulo.pack()
    textotitulo = tk.Label(janelaajuda, text="Contatos:", bg="white", font="Arial 14")
    textotitulo.pack()

    textocontato = tk.Label(janelaajuda, text="André - (15) 99622-1111", bg="white", font="Arial 12", compound="left")
    # Load the image and set it as the icon
    imagem_tel1 = PhotoImage(file="tel.png")
    textocontato.config(image=imagem_tel1)
    textocontato.pack()
    
    textocontato = tk.Label(janelaajuda, text="Carlos - (15) 99622-2222", bg="white", font="Arial 12", compound="left")
    # Load the image and set it as the icon
    imagem_tel2 = PhotoImage(file="tel.png")
    textocontato.config(image=imagem_tel2)
    textocontato.pack()

    textocontato = tk.Label(janelaajuda, text="Jéssica - (15) 99622-3333", bg="white", font="Arial 12", compound="left")
    # Load the image and set it as the icon
    imagem_tel3 = PhotoImage(file="tel.png")
    textocontato.config(image=imagem_tel3)
    textocontato.pack()

    textocontato = tk.Label(janelaajuda, text="João Paulo - (15) 99622-4444", bg="white", font="Arial 12", compound="left")
    # Load the image and set it as the icon
    imagem_tel4 = PhotoImage(file="tel.png")
    textocontato.config(image=imagem_tel4)
    textocontato.pack()

    textocontato = tk.Label(janelaajuda, text="Talita - (15) 99622-5555", bg="white", font="Arial 12", compound="left")
    # Load the image and set it as the icon
    imagem_tel5 = PhotoImage(file="tel.png")
    textocontato.config(image=imagem_tel5)
    textocontato.pack()

    textocontato = tk.Label(janelaajuda, text="vanderlei - (15) 99622-6666", bg="white", font="Arial 12", compound="left")
    # Load the image and set it as the icon
    imagem_tel6 = PhotoImage(file="tel.png")
    textocontato.config(image=imagem_tel6)
    textocontato.pack()


    frame_bottom = ttk.Frame(janelaajuda)
    frame_bottom.pack(side="bottom", fill="both")

    toolbar = tk.Label(frame_bottom, text="Projeto Integrador 240", foreground="#1F9FDA", font=("Arial", 10))
    toolbar.pack(side="top")

    janelaajuda.mainloop()

#_________________________________________________________________________________________________________________________________________

bike_plate_numbers = ["1031", "5245", "2121", "4685", "2514", "2145", "5698", "4878", "6896", "7854"]

def usuario(user):
    def validate_plate_number(plate_number):
        bike_plate_numbers = ["1031", "5245", "2121", "4685", "2514", "2145", "5698", "4878", "6896", "7854"]
        return plate_number in bike_plate_numbers

    def start_countdown():
        plate_number = entryplaca.get()
        if validate_plate_number(plate_number):
            countdown_time = 10  # 150 minutes
            update_countdown(countdown_time, countdown_label)
        else:
            messagebox.showerror("Error", "Invalid plate number")

    def format_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def update_countdown(time_remaining, label):
        if time_remaining > 0:
            label.config(text=f"Tempo Restante: {format_time(time_remaining)}")
            janelausuario.after(1000, update_countdown, time_remaining - 1, label)
        else:
            label.config(text="DEVOLVA A BICICLETA \n NO PONTO MAIS PRÓXIMO")

    janelausuario = tk.Toplevel()
    janelausuario.title("Projeto Pedala Sarapuí")
    janelausuario.geometry("340x480")
    janelausuario.configure(bg="white")
    imagem_logo1 = PhotoImage(file="logo01.png")
    label_imagem = tk.Label(janelausuario, image=imagem_logo1, bg="white")
    label_imagem.pack()
    
    # Create a label to display the current time
    current_time_label = tk.Label(janelausuario, text="", bg="white", font="Arial 12")
    current_time_label.pack()

    def update_current_time():
        current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
        current_time_label.config(text=f"Hora Atual: {current_time}")
        janelausuario.after(1000, update_current_time)  # Update the time every 1000ms (1 second)

    update_current_time()  # Start updating the current time

    textotitulo = tk.Label(janelausuario, text="Projeto Pedala Sarapuí", bg="white", font="Arial 15")
    textotitulo.pack()

    user_label = tk.Label(janelausuario, text=f"Nome: {user['name']}", bg="white", font="Arial 12")
    user_label.pack()

    entryplaca = tk.Entry(janelausuario)
    entryplaca.pack()

    countdown_label = tk.Label(janelausuario, text="", bg="white", font="Arial 12")
    countdown_label.pack()

    botaoiniciar = tk.Button(janelausuario, text="Iniciar", bg="#4EB7B0", width=10, fg="white", font="Arial 10 bold", command=start_countdown)
    botaoiniciar.pack(padx=8, pady=8)

    janelausuario.mainloop()







    botaoiniciar = tk.Button(janelausuario, text="Iniciar", bg="#4EB7B0", width=10, fg="white", font= "Arial 10 bold")
    botaoiniciar.pack(padx=8, pady=8)

    janelausuario.mainloop()




#_________________________________________________________________________________________________________________________________________
    
def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg="black")

def inserir_cliente():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()

    nome = entrynome.get()
    cpf = entrycpf.get()
    datanasc = entrydatanasc.get()
    rua = entryrua.get()
    numero = entrynumero.get()
    vila = entryvila.get()

    cursor.execute("INSERT INTO clientes (nome, cpf, datanasc, rua, numero, vila) VALUES (?, ?, ?, ?, ?, ?)",
                   (nome, cpf, datanasc, rua, numero, vila))

    conn.commit()
    conn.close()
#_________________________________________________________________________________________________________________________________________


def cadastrar():
    global imagem_logo, entrynome, entrycpf, entrydatanasc, entryrua, entrynumero, entryvila
    janelacadastro = tk.Toplevel()
    janelacadastro.title("Projeto Pedala Sarapuí")
    janelacadastro.geometry("340x480")
    janelacadastro.configure(bg="white")

    imagem_logo1 = PhotoImage(file="logo01.png")
    label_imagem = tk.Label(janelacadastro, image=imagem_logo1, bg="white")
    label_imagem.pack()

    textotitulo = tk.Label(janelacadastro, text="Projeto Pedala Sarapuí", bg="white", font="Arial 15")
    textotitulo.pack()

    entrynome = tk.Entry(janelacadastro, width=30, fg="gray")
    entrynome.insert(0, "Nome")
    entrynome.bind("<FocusIn>", lambda event: on_entry_click(event, entrynome, "Nome"))
    entrynome.pack()

    entrycpf = tk.Entry(janelacadastro, width=30, fg="gray")
    entrycpf.insert(0, "CPF")
    entrycpf.bind("<FocusIn>", lambda event: on_entry_click(event, entrycpf, "CPF"))
    entrycpf.pack()

    entrydatanasc = tk.Entry(janelacadastro, width=30, fg="gray")
    entrydatanasc.insert(0, "Data de Nascimento")
    entrydatanasc.bind("<FocusIn>", lambda event: on_entry_click(event, entrydatanasc, "Data de Nascimento"))
    entrydatanasc.pack()

    entryrua = tk.Entry(janelacadastro, width=30, fg="gray")
    entryrua.insert(0, "Rua")
    entryrua.bind("<FocusIn>", lambda event: on_entry_click(event, entryrua, "Rua"))
    entryrua.pack()

    entrynumero = tk.Entry(janelacadastro, width=30, fg="gray")
    entrynumero.insert(0, "Número")
    entrynumero.bind("<FocusIn>", lambda event: on_entry_click(event, entrynumero, "Número"))
    entrynumero.pack()

    entryvila = tk.Entry(janelacadastro, width=30, fg="gray")
    entryvila.insert(0, "Vila")
    entryvila.bind("<FocusIn>", lambda event: on_entry_click(event, entryvila, "Vila"))
    entryvila.pack()

    botaoajuda = tk.Button(janelacadastro, text="Salvar", bg="#4EB7B0", width=10, fg="white", font="Arial 10 bold", command=inserir_cliente)
    botaoajuda.pack(padx=8, pady=8)

    janelacadastro.mainloop()

#_________________________________________________________________________________________________________________________________________
def on_login_entry_click(event):
    global entrylogin  # Use a variável global entrylogin
    if entrylogin.get() == "Login":
        entrylogin.delete(0, "end")
        entrylogin.config(fg="black")

def on_senha_entry_click(event):
    global entrysenha  # Use a variável global entrysenha
    if entrysenha.get() == "Senha":
        entrysenha.delete(0, "end")
        entrysenha.config(fg="black")

def login():
    global imagem_logo, entrylogin, entrysenha  # Use as variáveis globais
    janelalogin = tk.Toplevel()
    janelalogin.title("Projeto Pedala Sarapuí")
    janelalogin.geometry("340x480")
    janelalogin.configure(bg="white")

    try:
        imagem_logo1 = PhotoImage(file="logo01.png")
    except Exception as e:
        print(f"Error loading image: {e}")

    imagem_logo1 = PhotoImage(file="logo01.png")

    label_imagem = tk.Label(janelalogin, image=imagem_logo1, bg="white")
    label_imagem.pack()

    textotitulo = tk.Label(janelalogin, text="Projeto Pedala Sarapuí", bg="white", font="Arial 15")
    textotitulo.pack()

    textotitulo1 = tk.Label(janelalogin, text="", bg="white", font="Arial 40")
    textotitulo1.pack()

    imagem_logo2 = PhotoImage(file="user.png")

    label_imagem2 = tk.Label(janelalogin, image=imagem_logo2, bg="white")
    label_imagem2.pack()

   # Campos de entrada para login e senha com dicas (placeholders)
    entrylogin = tk.Entry(janelalogin, width=30, fg="gray")
    entrylogin.insert(0, "Login")
    entrylogin.bind("<FocusIn>", on_login_entry_click)
    entrylogin.pack()

    entrysenha = tk.Entry(janelalogin, width=30, fg="gray", show="*")
    entrysenha.insert(0, "Senha")
    entrysenha.bind("<FocusIn>", on_senha_entry_click)
    entrysenha.pack()


    def verificar_login():
        # Get the entered CPF (login) and the first 3 digits of the CPF
        entered_cpf = entrylogin.get()
        cpf_prefix = entered_cpf[:3]

        # Check if the user with the entered CPF is registered in the database
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome, cpf FROM clientes WHERE cpf=?", (entered_cpf,))
        result = cursor.fetchone()
        conn.close()

        if result:
            # The user exists, and the CPF matches
            user_name, user_cpf = result  # Extract the user's name and CPF from the database
            janelalogin.destroy()  # Close the login window

            # Create a user dictionary with information to pass to 'usuario'
            user_info = {
                "name": user_name,
                "cpf": user_cpf  # Include the 'cpf' in the dictionary
                # Add other user information here
            }

            usuario(user_info)  # Call the "usuario" function with user information
        else:
            # User not found
            messagebox.showerror("Login Error", "User not found")

    botaoentrar = tk.Button(janelalogin, text="Entrar", bg="#EF3070", width=10, fg="white", font= "Arial 10 bold", command=verificar_login)
    botaoentrar.pack(padx=8, pady=8)

    janelalogin.mainloop()
#_________________________________________________________________________________________________________________________________________
janelaprincipal = tk.Tk()
janelaprincipal.title("Projeto Pedala Sarapuí")
janelaprincipal.geometry("340x480")
janelaprincipal.configure(bg="white")


imagem_logo1 = PhotoImage(file="logo01.png")

label_imagem1 = tk.Label(janelaprincipal, image=imagem_logo1, bg="white")
label_imagem1.place(x=212, y=-22)

imagem_logo = PhotoImage(file="logo05.png")

label_imagem = tk.Label(janelaprincipal, image=imagem_logo, bg="white")
label_imagem.place(x=1, y=1)

textotitulo = tk.Label(janelaprincipal, text="Prefeitura Municipal de \n Sarapuí", bg="white", font="Arial 12")
textotitulo.pack(pady=10)

textotitulo = tk.Label(janelaprincipal, text="Projeto Pedala Sarapuí", bg="white", font="Arial 12")
textotitulo.pack(pady=10)

textotitulo = tk.Label(janelaprincipal, text="", bg="white", font="Arial 25")
textotitulo.pack(pady=10)

framejanelaprincipal = ttk.Frame(janelaprincipal, width=300, height=100)
framejanelaprincipal.pack(padx=1, pady=1)
framejanelaprincipal['borderwidth'] = 2
framejanelaprincipal['relief'] = 'solid'

texto = "Sarapuí agora oferece um inovador sistema de compartilhamento de bicicletas públicas, que é mais contemporâneo e, o melhor de tudo, gratuito para todos os cidadãos. Este sistema está perfeitamente integrado à rede de transporte coletivo da cidade. Não perca a chance de  aproveitar essa novidade."
textolabel = ttk.Label(framejanelaprincipal, text=texto, wraplength=janelaprincipal.winfo_width(), justify='center')
textolabel.pack()

textotitulo1 = tk.Label(janelaprincipal, text="", bg="white", font="Arial 40")
textotitulo1.pack()
estilo = ttk.Style()
estilo.configure("MeuEstilo.TButton", font=("Arial", 12), foreground="blue")



# Cria um frame para os botões e alinha-os horizontalmente
frame_botoes = tk.Frame(janelaprincipal, bg="white")
frame_botoes.place(y=400)

botaoentrar = tk.Button(frame_botoes, text="Entrar", bg="#EF3070", width=10, fg="white", font= "Arial 10 bold", command=login)
botaoentrar.pack(side="left", padx=8, pady=8)

botaocadastrar = tk.Button(frame_botoes, text="Cadastrar", bg="#FA971F", width=10, fg="white", font= "Arial 10 bold", command=cadastrar)
botaocadastrar.pack(side="left", padx=8, pady=8)

botaoajuda = tk.Button(frame_botoes, text="Ajuda", bg="#4EB7B0", width=10, fg="white", font= "Arial 10 bold", command=ajuda)
botaoajuda.pack(side="left", padx=8, pady=8)


frame_bottom = ttk.Frame(janelaprincipal)
frame_bottom.pack(side="bottom", fill="both")

toolbar = tk.Label(frame_bottom, text="Projeto Integrador 240", foreground="#1F9FDA", font=("Arial", 10))
toolbar.pack(side="top")

def atualizar_wraplength(event):
    textolabel['wraplength'] = janelaprincipal.winfo_width()

janelaprincipal.bind("<Configure>", atualizar_wraplength)

janelaprincipal.mainloop()