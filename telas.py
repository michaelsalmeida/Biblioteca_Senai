from funcoes_consultas import *
from funcoes_internas import *
from funcoes_insersoes import *
from telas_grafico import *
from conexao import *


def fechar(jane):
    jane.destroy()

def adm(log, sen, ja):
    import tkinter as tk
    from tkinter import ttk
    con = conex()

    if con:
        cursor = con.cursor()

        comando1 = 'select * from masterkey where id_senha = 1;'
        cursor.execute(comando1)
        a = cursor.fetchone()
        login = a[1]
        senha = a[2]

        
        if log == login and sen == senha:
            cursor.close()
            con.close()
            ja.destroy()
            adm_data()

        else:
            fail_label = ttk.Label(ja, text='LOGIN OU SENHA INVÁLIDO. TENTE DE NOVO.', font=('Arial', 20))
            fail_label.place(x=430, y=450)


def tela_adm():
    import tkinter as tk
    from tkinter import ttk
    # Cria a janela principal
    janela = tk.Tk()
    # Define o título da janela
    janela.title("TELA DE LOGIN DE ADMINISTRADOR")

    janela.attributes("-fullscreen", True)

    lab = ttk.Label(janela, text="TELA LOGIN ADMINISTRADO", width=30, font=('Arial', 20))
    lab.place(x=550, y=20)


    login_label = ttk.Label(janela, text='LOGIN: ', font=('Arial', 20))
    login_label.place(x=460, y=200)
    login_entry = ttk.Entry(janela, width=70)
    login_entry.place(x=570, y=208)


    senha_label = ttk.Label(janela, text='SENHA: ', font=('Arial', 20))
    senha_label.place(x=460, y=300)
    senha_entry = ttk.Entry(janela, width=70)
    senha_entry.place(x=570, y=308)


    teste = ttk.Button(janela, text="ENTRAR", command=lambda: adm(login_entry.get(), senha_entry.get(), janela), padding=25)
    teste.place(x=700, y=550)
    enviar_button = ttk.Button(janela, text="SAIR", command=lambda : fechar(janela), padding=25)
    enviar_button.place(x=700, y=650)

    janela.mainloop()


def da():
    import tkinter as tk
    from tkinter import ttk

    con = conex()

    if con:
        cursor = con.cursor()

        comando1 = 'select SUM(mesa_estudos) from utilizacao;'
        cursor.execute(comando1)
        livro = cursor.fetchone()[0]
        if livro == None:
            livro = 0
        
        comando2 = 'select SUM(usou_computador) from utilizacao;'
        cursor.execute(comando2)
        computador = cursor.fetchone()[0]
        if computador == None:
            computador = 0

        cursor.close()
        con.close()

        # Cria a janela principal
        janela2 = tk.Tk()
        # Define o título da janela
        janela2.title("TELA DE LOGIN DE ADMINISTRADOR")

        janela2.attributes("-fullscreen", True)

        lab = ttk.Label(janela2, text="QUANTIDADE DE ALUNOS QUE: ", width=30, font=('Arial', 20))
        lab.place(x=550, y=20)


        livro_label = ttk.Label(janela2, text=f'MESA DE ESTUDOS/LEITURA:  {livro}', font=('Arial', 20))
        livro_label.place(x=550, y=300)

        comp_label = ttk.Label(janela2, text=f'USARAM O COMPUTADOR:  {computador}', font=('Arial', 20))
        comp_label.place(x=550, y=400)


        inicio_button = ttk.Button(janela2, text="INÍCIO", command=lambda : fechar(janela2), padding=25)
        inicio_button.place(x=700, y=650)

        janela2.mainloop()


def tela_veio_para(matricula):
    con = conex()

    if con:
        import tkinter as tk
        from tkinter import ttk

        cursor = con.cursor()

        comando1 = f'select * from cadastro where pk_matricula = {matricula};'
        cursor.execute(comando1)
        dados = cursor.fetchall()
        nome = dados[0][1]
        curso = dados[0][2]
        turma = dados[0][3]


        # Cria a janela principal
        janela = tk.Tk()
        # Define o título da janela
        janela.title("TELA DE FREQUENCIA")

        janela.attributes("-fullscreen", True)

        matricula_label = ttk.Label(janela, text="MATRÍCULA: ", font=('Arial', 20))
        matricula_label.place(x=450, y=100)
        matricula_label2 = ttk.Label(janela, text=f"{matricula}", font=('Arial', 20))
        matricula_label2.place(x=650, y=100)


        nome_label = ttk.Label(janela, text="NOME:", font=('Arial', 20))
        nome_label.place(x=450, y=150)
        nome_label2 = ttk.Label(janela, text=f"{nome}", font=('Arial', 20))
        nome_label2.place(x=650, y=150)


        curso_label = ttk.Label(janela, text="CURSO: ", font=('Arial', 20))
        curso_label.place(x=450, y=200)
        curso_label = ttk.Label(janela, text=f"{curso}", font=('Arial', 20))
        curso_label.place(x=650, y=200)


        turma_label = ttk.Label(janela, text="TURMA: ", font=('Arial', 20))
        turma_label.place(x=450, y=250)
        turma_label2 = ttk.Label(janela, text=f"{turma}", font=('Arial', 20))
        turma_label2.place(x=650, y=250)


        numero_label = ttk.Label(janela, text="VEIO PARA: ", font=('Arial', 20))
        numero_label.place(x=450, y=300)
        numero_var = tk.StringVar()
        numero_dropdown = ttk.Combobox(janela, textvariable=numero_var, width=50)
        numero_dropdown["values"] = ["MESA DE ESTUDOS/LEITURA", "USAR O COMPUTADOR"]
        numero_dropdown.place(x=650, y=310)


        enviar_button = ttk.Button(janela, text="ENVIAR", command=lambda: modificar(matricula, numero_var.get().strip(), janela), padding=25)
        enviar_button.place(x=700, y=500)


        janela.mainloop()


def tela_cadastro(matricula):
    xx()
    import tkinter as tk
    from tkinter import ttk

    # Cria a janela principal
    janela = tk.Tk()
    janela.attributes("-fullscreen", True)


    # Define o título da janela
    janela.title("Formulário de Inscrição")

    lab = ttk.Label(janela, text="TELA DE CADASTRO", width=30, font=('Arial', 20))
    lab.place(x=650, y=20)

    # Cria o campo de entrada para o nome
    nome_label = ttk.Label(janela, text="NOME:", font=('Arial', 20))
    nome_label.place(x=450, y=150)
    nome_entry = ttk.Entry(janela, width=100)
    nome_entry.place(x=680, y=157)

    # Cria o campo dropdown para escolha do curso
    curso_label = ttk.Label(janela, text="CURSO:", font=('Arial', 20))
    curso_label.place(x=450, y=250)
    curso_var = tk.StringVar()
    curso_dropdown = ttk.Combobox(janela, textvariable=curso_var, width=50)
    curso_dropdown["values"] = ["Técnico em Desenvolvimento de Sistema", "Técnico em Qualidade", "Técnico em Mecânica de Precisão", "Técnico em Redes de Computadores", "Tecnólogo em Mecânica de Precisão" , "Assistente Técnico de Vendas"]
    curso_dropdown.place(x=680, y=257)

    # Cria o campo dropdown para escolha do número
    numero_label = ttk.Label(janela, text="TURMA:", font=('Arial', 20))
    numero_label.place(x=450, y=350)
    numero_var = tk.StringVar()
    numero_dropdown = ttk.Combobox(janela, textvariable=numero_var)
    numero_dropdown["values"] = ['3DM', '1DT', '2DT', '3DN','2QC', '1QE', '3QE','1MA', '2MA', '3MA', '4MA', '1MC', '3MC', '2ME', '4ME', '2RM', '3TE', '5TE', 'ATV M1', 'ATV MA', 'ATV T2']
    numero_dropdown.place(x=680, y=357)

    fazer_label = ttk.Label(janela, text='VEIO PARA: ', font=('Arial', 20))
    fazer_label.place(x=450, y=450)
    fazer_var = tk.StringVar()
    fazer_dropdown = ttk.Combobox(janela, textvariable=fazer_var, width=50)
    fazer_dropdown["values"] = ["MESA DE ESTUDOS/LEITURA", "USAR O COMPUTADOR"]
    fazer_dropdown.place(x=680, y=457)

    enviar_button = ttk.Button(janela, text="ENVIAR", command= lambda: cadastrar(matricula, nome_entry.get().strip(), curso_var.get(), numero_var.get(), fazer_var.get(), janela), padding=25)
    enviar_button.place(x=700, y=650)

    enviar_button = ttk.Button(janela, text="VOLTAR", command=lambda: fechar(janela), padding=25)
    enviar_button.place(x=700, y=750)

    # Inicia o loop principal da janela
    janela.mainloop()


def adm_data():
    xx()
    import tkinter as tk
    from tkinter import ttk

    janela = tk.Tk()
    janela.attributes("-fullscreen", True)

    janela.title("Seleção de gráfico")

    titulo = ttk.Label(text='SELECIONE O GRÁFICO DESEJADO', width=40, font=('Arial', 20))
    titulo.place(x=500, y=20)
    
    geral = ttk.Button(text='Geral por atividades', command=lambda: chama_telas_grafico('geral por atividade', janela), padding=25)
    geral.place(x=300, y=150)

    fechar_button = ttk.Button(janela, text="VOLTAR", command=lambda: fechar(janela), padding=25)
    fechar_button.place(x=720, y=450)

    janela.mainloop()


def chama_telas_grafico(funcao, janel):
    funcoes = {'geral por atividade' : mensal}
    janel.destroy()
    funcoes[funcao]()


# adm_data()