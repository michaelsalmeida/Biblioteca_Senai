from funcoes_consultas import *
from funcoes_insersoes import *
from funcoes_leitor import *
from telas import *
from testes import *


while True:

    matricula = obter_matricula()

    if matricula == None:
        
        tela_adm()

    else:

        veri = verificacao(matricula)

        if veri:

            tela_veio_para(matricula)

        else:
        
            tela_cadastro(matricula)
