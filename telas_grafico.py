from funcoes_consultas import *
from funcoes_internas import *
from funcoes_insersoes import *
from conexao import *


def mensal():
    xx()
    import tkinter as tk
    from tkinter import ttk

    janela = tk.Tk()
    janela.attributes("-fullscreen", True)

    janela.title("Seleção de datas")

    titulo = ttk.Label(text='SELECIONE O PERÍODO', width=40, font=('Arial', 20))
    titulo.place(x=500, y=20)

    ano = ttk.Label(janela, text='ANO: ', font=('Arial', 20))
    ano.place(x=550, y=200)
    a_var = tk.StringVar()
    a_dropdown = ttk.Combobox(janela, textvariable=a_var, width=50, font=50)
    a_dropdown["values"] = ret_ano()
    a_dropdown.place(x=630, y=205)

    m = ttk.Label(janela, text='MÊS: ', font=('Arial', 20))
    m.place(x=550, y=270)
    m_var = tk.StringVar()
    m_dropdown = ttk.Combobox(janela, textvariable=m_var, width=50, font=50)
    m_dropdown['values'] = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    m_dropdown.place(x=630, y=275)

    
    gerar_button = ttk.Button(janela, text="GERAR GRÁFICO", command=lambda: grafico_geral_atividade(a_var.get(), m_var.get(), janela), padding=25)
    gerar_button.place(x=720, y=350)

    fechar_button = ttk.Button(janela, text="VOLTAR", command=lambda: fechar(janela), padding=25)
    fechar_button.place(x=720, y=450)

    janela.mainloop()

