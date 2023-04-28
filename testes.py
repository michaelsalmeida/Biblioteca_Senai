from conexao import *
from funcoes_insersoes import *
from funcoes_internas import *
from funcoes_consultas import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt


# 2023-03-01 até 2023-06-10


# con = conex()

# if con:
#     pen = con.cursor()

#     dataA = input('Primeira data: ')
#     dataB = input('Segunda data: ')

#     # comando1 = 'select data_computador from usar_computador order by data_computador asc;'
#     comando1 = 'select data_computador from usar_computador where data_computador between %s and %s;'

#     valores = (dataA, dataB)
#     pen.execute(comando1, valores)
#     ppp = pen.fetchall() #retorna uma lista assim [(datetime.date(2023, 3, 10),), (datetime.date(2023, 3, 14),), ].
#     #utiliza o [0][0] para pegar só a data específica.
    

#     datass = [] # As datas que estão no banco de dados serão armazenadas aqui.


#     for a in ppp:
#         if str(a[0]) not in datass:
#             datass.append(str(a[0]))

    # frequencias = []

    # for data in datass:

    #     s = (str(data),)

    #     comando2 = "select count(id_computador) from usar_computador where data_computador = %s;"

    #     pen.execute(comando2, s)

    #     aaa = pen.fetchone()

    #     frequencias.append(aaa[0])

    # freque_mesaestudos = []

    # for data in datass:

    #     s = (str(data),)

    #     comando2 = "select count(pk_estudos) from mesa_estudos where data_estudo = %s;"

    #     pen.execute(comando2, s)

    #     aaa = pen.fetchone()

    #     freque_mesaestudos.append(aaa[0])


#     meus_dados = {}

#     for dd in range (0, len(datass)):
#         meus_dados[datass[dd]] = frequencias[dd]




con = conex()

if con:
    pen = con.cursor()

    dataA = '2023-03-14'
    dataB = '2023-03-16'

    # # comando1 = 'select data_computador from usar_computador order by data_computador asc;'
    # comando1 = 'select data_computador from usar_computador where data_computador between %s and %s;'

    # valores = (dataA, dataB)
    # pen.execute(comando1, valores)
    # ppp = pen.fetchall() #retorna uma lista assim [(datetime.date(2023, 3, 10),), (datetime.date(2023, 3, 14),), ].
    # #utiliza o [0][0] para pegar só a data específica.
    

    # datass = [] # As datas que estão no banco de dados serão armazenadas aqui.


    # for a in ppp:
    #     if str(a[0]) not in datass:
    #         datass.append(str(a[0]))

    # usarcomputador = []

    # for data in datass:

    #     s = (str(data),)

    #     comando2 = "select count(id_computador) from usar_computador where data_computador = %s;"

    #     pen.execute(comando2, s)

    #     aaa = pen.fetchone()

    #     usarcomputador.append(aaa[0])

    # mesaestudos = []

    # for data in datass:

    #     s = (str(data),)

    #     comando2 = "select count(id_estudos) from mesa_estudos where data_livro = %s;"

    #     pen.execute(comando2, s)

    #     aaa = pen.fetchone()

    #     mesaestudos.append(aaa[0])

# def lista_datas(year, mouth):
#     import calendar
#     from datetime import datetime, timedelta

#     ano = year
#     mes = mouth

#     # Obtem o primeiro dia da semana e o número total de dias no mês
#     primeiro_dia_semana, num_dias_mes = calendar.monthrange(ano, mes)

#     # Cria uma lista de datas para o mês fornecido
#     datas = [datetime(ano, mes, dia).date() for dia in range(1, num_dias_mes + 1)]

#     # Retorna a lista de datas
#     return datas

# print(lista_datas(2023, 2))

# import pandas as pd
# import matplotlib.pyplot as plt

# # Crie um DataFrame de exemplo com datas como índice
# data = {'Mesa de estudos': mesaestudos, 'Usar o computador': usarcomputador}
# dates = datass
# df = pd.DataFrame(data, index=dates)

# # Plot as duas colunas em um gráfico de linhas
# ax = df.plot(kind='line', y=['Mesa de estudos', 'Usar o computador'])

# # Define os nomes dos eixos x e y
# ax.set_xlabel('Datas')
# ax.set_ylabel('Frequência')

# # Mostra o gráfico
# plt.show()
