from conexao import *
from funcoes_internas import *
from telas import *

def verificacao(matricula):
    con = conex()

    if con:
        xx()

        cursor = con.cursor() #crio o cursor para executar as querys no banco.

        comando1 = 'select pk_matricula from cadastro;'
        cursor.execute(comando1)
        lista = cursor.fetchall() # armazena uma lista com todas as matriculas que estão no banco de dados.

        esta = False

        for usu in range(len(lista)): # loop para verificar se a matricula lida está no banco ou não.
            if lista[usu][0] == matricula:
                esta = True
            
        cursor.close()
        con.close()
        return esta


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
            da()

        else:
            fail_label = ttk.Label(ja, text='LOGIN OU SENHA INVÁLIDO. TENTE DE NOVO.', font=('Arial', 20))
            fail_label.place(x=430, y=450)

