from conexao import *

def xx():
    from os import system
    import platform
    a = platform.system()

    if a == 'Windows':
        system('cls')

    elif a == 'Linux':
        system('clear')


def exitt():
    import sys
    sys.exit()


def linha(tam = 80):
    return '-' * tam


def linhanotebook(tam = 177):
    return '-' * tam


def cabecalhonotebook(txt):
    print(linhanotebook())
    print(f'{txt:^177}')
    print(linhanotebook())



def cabecalho(txt):
    print(linha())
    print(f'{txt:^80}')
    print(linha())



def leiaint(txt):
    while True:
        try:
            a = int(input(txt))

        except:
            print('\033[31mPOR FAVOR, DIGITE UM NÚMERO VÁLIDO\033[m')

        else:
            if a < 0:
                print('Digite um valor correto.')

            else:
                return a
            




def menu(titulo, lst):

    cabecalho(titulo)
    for item in range (0, len(lst)):
        print(f'{item + 1} ---- {lst[item]}')

    while True:
        opcao = leiaint('Sua opção: ')

        if opcao > len(lst):
            print('\033[31mOPÇÃO INVÁLIDA\033[m')

        else:
            return lst[opcao - 1]



def data_atual():
    from datetime import datetime

    # Obtém a data atual
    data_atual = datetime.today().date()

    return data_atual



def hora_atual():
    from datetime import datetime

    # Obtém a hora e o minuto atuais
    hora_atual = datetime.now().hour
    minuto_atual = datetime.now().minute

    if hora_atual < 10:
        if minuto_atual < 10:
            return f'0{hora_atual}:0{minuto_atual}'
        
        else:
            return f'0{hora_atual}:{minuto_atual:2d}'
    
    else:
        if minuto_atual < 10:
            return f'{hora_atual:2d}:0{minuto_atual}'
        
        else:
            return f'{hora_atual:2d}:{minuto_atual:2d}'



def fail(ja, txt, wi, he):
    import tkinter as tk
    from tkinter import ttk

    fail_label = ttk.Label(ja, text=f'{txt}', font=('Arial', 20))
    fail_label.place(x=wi, y=he)



def fechar(jan):
    jan.destroy()




def ret_ano():
    import datetime

    ano_atual = datetime.datetime.now().year

    anos = []

    for year in range(ano_atual , 1970, -1):
        anos.append(str(year))

    return anos



def dia_mes_ano(escolha):
    import datetime

    now = datetime.datetime.now()

    if escolha == 'dia':
        year = now.day
    
    elif escolha == 'mes':
        year = now.month
    
    elif escolha == 'ano':
        year = now.year


    return year

def lista_datas(year, mouth):
    import calendar
    from datetime import datetime, timedelta

    ano = year
    mes = mouth

    # Obtem o primeiro dia da semana e o número total de dias no mês
    primeiro_dia_semana, num_dias_mes = calendar.monthrange(ano, mes)

    # Cria uma lista de datas para o mês fornecido
    datas = [datetime(ano, mes, dia).date() for dia in range(1, num_dias_mes + 1)]

    # Retorna a lista de datas
    return datas



def grafico_geral_atividade(year, month, ja):
    import pandas as pd
    import matplotlib.pyplot as plt


    if year == '' or month == '':
        fail(ja, 'PREENCHA OS CAMPOS CORRETAMENTE', 500, 100)
    
    else:
    
        datas = lista_datas(int(year), int(month))

        con = conex()

        if con:
            pen = con.cursor()

            usar_computador = []

            mesa_estudos = []

            for date in datas:

                dataa = (str(date),)

                comando2 = "select count(pk_computador) from usar_computador where data_computador = %s;"

                pen.execute(comando2, dataa)

                frequencia = pen.fetchone()

                usar_computador.append(frequencia[0])

                comando3 = "select count(pk_estudos) from mesa_estudos where data_estudos = %s;"

                pen.execute(comando3, dataa)

                frequencia2 = pen.fetchone()

                mesa_estudos.append(frequencia2[0])

            

            # Crie um DataFrame de exemplo com datas como índice
            data = {'Mesa de estudos': mesa_estudos, 'Usar o computador': usar_computador}
            dates = datas
            df = pd.DataFrame(data, index=dates)

            # Plot as duas colunas em um gráfico de linhas
            ax = df.plot(kind='line', y=['Mesa de estudos', 'Usar o computador'])

            # Define os nomes dos eixos x e y
            ax.set_xlabel('Datas')
            ax.set_ylabel('Frequência')

            
            # Mostra o gráfico
            plt.show()


