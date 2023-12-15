
#----------- Conversando com o Sistema Operacional ----------#

import platform # biblioteca que consulta a confirguração da maquina

from datetime import datetime # biblioteca que consulta o horario

import getpass
#
# print("Nome da maquina:.....", platform.node())
# print("Arquitetura:.....",platform.architecture())
# print("Sistema Operacional:.....", platform.system())
# print("Versão do SO:.....",platform.release())
# print("Processador:.....",platform.processor())
# print("Versão do Python:.....",platform.python_version())
#
# print(datetime.now()) # retorna a data e o horario

# print(getpass.getuser()) # retorna o usuario que ta logado na maquina
# print(getpass.getpass("Digite sua senha:...")) # requisita uma entrada de dados do usuario

print("\n##### Tela de Login #####\n")
usuario = getpass.getuser()
senha = getpass.getpass("Digite a senha...:")

if usuario == 'andre' and  senha == '123':
    print("\nBem vindo andre")
else :
    print("\nVoce não tema acesso!")
