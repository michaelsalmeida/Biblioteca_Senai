from funcoes_internas import *
from conexao import *


def cadastrar(matricula, nome, curso, turma, veio, janel):
    con = conex()
    a = ["Técnico em Desenvolvimento de Sistema", "Técnico em Qualidade", 
    "Técnico em Mecânica de Precisão", "Técnico em Redes de Computadores", 
    "Tecnólogo em Mecânica de Precisão" , "Assistente Técnico de Vendas"]

    b = ['MESA DE ESTUDOS/LEITURA', 'USAR O COMPUTADOR'] 

    c = {"Técnico em Desenvolvimento de Sistema" : ['3DM', '1DT', '2DT', '3DN'],
    "Técnico em Qualidade" : ['2QC', '1QE', '3QE'],
    "Técnico em Mecânica de Precisão" : ['1MA', '2MA', '3MA', '4MA', '1MC', '3MC', '2ME', '4ME'],
    "Técnico em Redes de Computadores" : ['2RM'],
    "Tecnólogo em Mecânica de Precisão" : ['3TE', '5TE'],
    "Assistente Técnico de Vendas" : ['ATV M1', 'ATV MA', 'ATV T2']}

    if con:
        if nome == '' or curso not in a or turma not in c[curso] or veio not in b:
            fail(janel, 'PREENCHA OS CAMPOS CORRETAMENTE.', 450, 550)

        else:
            cursor = con.cursor()

            comando1 = 'insert into cadastro values (%s, %s, %s, %s, %s, %s);'
            valores1 = (matricula, nome, curso, turma, data_atual(), hora_atual())

            comando11 = 'insert into utilizacao values (%s, %s, %s, %s);'
            valores11 = ('default', matricula, 0, 0)

            cursor.execute(comando1, valores1)
            con.commit()

            cursor.execute(comando11, valores11)
            con.commit()

            if veio == 'MESA DE ESTUDOS/LEITURA':
                xx()
                datual = data_atual()
                hatual = hora_atual()

                cursor = con.cursor()
                comando2 = f'select mesa_estudos from utilizacao where fk_matricula = {matricula}'
                cursor.execute(comando2)
                pegou = cursor.fetchone()
                
                comando3 = f'update utilizacao set mesa_estudos = {pegou[0] + 1} where fk_matricula = {matricula}'
                cursor.execute(comando3)
                con.commit()

                comando4 = 'insert into mesa_estudos values (%s, %s, %s, %s)'
                valores1 = ('default', matricula, datual, hatual)
                cursor.execute(comando4, valores1)
                con.commit()

                cursor.close()
                con.close()
                janel.destroy()

            elif veio == 'USAR O COMPUTADOR':
                xx()
                datual = data_atual()
                hatual = hora_atual()

                cursor = con.cursor()
                comando2 = f'select usou_computador from utilizacao where fk_matricula = {matricula};'
                cursor.execute(comando2)
                pegou = cursor.fetchone()
                
                comando3 = f'update utilizacao set usou_computador = {pegou[0] + 1} where fk_matricula = {matricula};'
                cursor.execute(comando3)
                con.commit()

                comando4 = 'insert into usar_computador values (%s, %s, %s, %s)'
                valores1 = ('default', matricula, datual, hatual)
                cursor.execute(comando4, valores1)
                con.commit()

                cursor.close()
                con.close()
                janel.destroy()




def modificar(matricula, acao, janela):
    con = conex()

    if con:
        
        if acao == 'MESA DE ESTUDOS/LEITURA':
            xx()
            datual = data_atual()
            hatual = hora_atual()

            cursor = con.cursor()
            comando2 = f'select mesa_estudos from utilizacao where fk_matricula = {matricula}'
            cursor.execute(comando2)
            pegou = cursor.fetchone()
            
            comando3 = f'update utilizacao set mesa_estudos = {pegou[0] + 1} where fk_matricula = {matricula}'
            cursor.execute(comando3)
            con.commit()

            comando4 = 'insert into mesa_estudos values (%s, %s, %s, %s)'
            valores1 = ('default', matricula, datual, hatual)
            cursor.execute(comando4, valores1)
            con.commit()

            cursor.close()
            con.close()
            janela.destroy()

        elif acao == 'USAR O COMPUTADOR':
            xx()
            datual = data_atual()
            hatual = hora_atual()

            cursor = con.cursor()
            comando2 = f'select usou_computador from utilizacao where fk_matricula = {matricula};'
            cursor.execute(comando2)
            pegou = cursor.fetchone()
            
            comando3 = f'update utilizacao set usou_computador = {pegou[0] + 1} where fk_matricula = {matricula};'
            cursor.execute(comando3)
            con.commit()

            comando4 = 'insert into usar_computador values (%s, %s, %s, %s)'
            valores1 = ('default', matricula, datual, hatual)
            cursor.execute(comando4, valores1)
            con.commit()

            cursor.close()
            con.close()
            janela.destroy()

        else:
            fail(janela, 'PREEENCHA OS CAMPOS CORRETAMENTE.', 450, 400)

