"""
# Project: AGENDA
"""

""" Biblioteca """
from agenda_dict import AGENDA

""""""""""""""""""""""""
""" Metodos: Suporte """
""""""""""""""""""""""""

def entrada_contato():
    return input("\033[01;32m# Contato: \033[01;00m")


def entrada_tel_ema_end():
    telefone = input("\033[01;33m# Telefone: \033[01;00m")
    email = input("\033[01;33m# Email: \033[01;00m")
    endereco = input("\033[01;33m# Endereco: \033[01;00m")

    return telefone, email, endereco


# Funcao: Verificacao de existencia de contato dentro da Agenda
def contato_verificar(contato):
    return contato in AGENDA


# Funcao: Nomear arquivo
def entrada_nome_arquivo_csv():
    return input("# Nome do arquivo: ")


# Metodo: Salva agenda no banco de dados
def save():
    exportar_contatos("database")


# Metodo: Carregar agenda do banco de dados
def load():
    importar_contatos("database")

def contatos_contador():
    try:
        with open("database.csv", "r") as file:
            print(f"\n\033[01;31m# Contatos: {len(file.readlines())}\033[01;00m")

    except FileNotFoundError:
        print("\033[01;31m# Arquivo nao encontrado !\033[01;00m")
        return

""""""""""""""""""""""""
""" Metodos: Contatos """
""""""""""""""""""""""""

# Menu: Opcao 1
def mostrar_contatos():

    # Agenda com contatos
    if len(AGENDA) > 0:
        print(f"\033[01;33m{'=-=' * 15}\033[01;00m")

        for i in AGENDA.keys():
            buscar_contato(i)
            print(f"\033[01;33m{'=-=' * 15}\033[01;00m")
    else:
        print("\033[01;31m# Agenda sem contatos !\033[01;00m")


# Menu: Opcao 2
def buscar_contato(contato):

    if contato_verificar(contato):
        print(f"# Contato: {contato}\n"
              f"# Telefone: {AGENDA[contato]["telefone"]}\n"
              f"# E-mail: {AGENDA[contato]["email"]}\n"
              f"# Endereco: {AGENDA[contato]["endereco"]}")
    else:
        print("\033[01;31m# Contato inexistente !\033[01;00m")

# Menu: Opcao 3 | Opcao 4
def incluir_editar_contato(contato, telefone, email, endereco):

    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }

    print(f"\n\033[01;32m# Contato atualizado com sucesso \033[01;00m")

    # Salvando dados
    save()

# Menu: Opcao 5
def excluir_contato(contato):

    if contato_verificar(contato):
        AGENDA.pop(contato)
        print(f"\n\033[01;32m# Contato excluido com sucesso \033[01;00m")

        # Salvando dados
        save()

    else:
        print("\033[01;31m# Contato inexistente !\033[01;00m")

""""""""""""""""""""""""""""""""""""""""""""
""" Metodos: Banco de dados de contatos """
""""""""""""""""""""""""""""""""""""""""""""

# Menu: Opcao 6
def exportar_contatos(arquivo):

    try:
        # Nome do arquivo
        arquivo += ".csv"

        with open(arquivo, "w") as file:

            # Cabecalho do arquivo (.csv)
            # file.write("contato,email,telefone,endereco\n")

            # Conteudos da AGENDA
            for i in AGENDA.keys():
                file.write(f"{i},{AGENDA[i]["email"]},{AGENDA[i]["telefone"]},{AGENDA[i]["endereco"]}\n")

            # print(f"\033[01;32m# Agenda exportada com sucesso \033[01;00m")
        return True

    except Exception as e:
        print(e)


# Menu: Opcao 7
def importar_contatos(arquivo):

    # Nome do arquivo
    arquivo += ".csv"

    # Leitura dos contatos na AGENDA
    try:
        with open(arquivo, "r") as file:

            linhas = file.readlines()

            for i in linhas:
                contato = i.strip().split(",")[0]
                telefone = i.strip().split(",")[1]
                email = i.strip().split(",")[2]
                endereco = i.strip().split(",")[3]

                AGENDA[contato] = {
                    "telefone": telefone,
                    "email": email,
                    "endereco": endereco
                }

    except FileNotFoundError:
        print(f"\n\033[01;31m# Arquivo nao encontrado !\033[01;00m")

""""""""""""""""""""""""""""""""""""""""""
""" Metodos: Procedimentos principais """
""""""""""""""""""""""""""""""""""""""""""
def menu():

    while True:
        try:
            print(f"\n\033[01;36m{'=-=' * 10} MENU {'=-=' * 10}\033[01;00m")
            print("# [1] - Mostrar contatos")
            print("# [2] - Buscar contato")
            print("# [3] - Incluir contato")
            print("# [4] - Editar contato")
            print("# [5] - Excluir contato")
            print("# [6] - Exportar contatos (.csv)")
            print("# [7] - Importar contatos (.csv)")
            print("# [0] - Saida")
            print(f"\033[01;36m{'=-=' * 22}\033[01;00m")
            opc = int(input("# Opc.: ").strip())
            print("")

            if opc == 0:
                print("\033[01;31m# Programa Encerrado !\033[01;00m")
                return

            elif opc == 1:
                mostrar_contatos()

            elif opc == 2:

                if len(AGENDA) == 0:
                    print("\033[01;31m# Agenda sem contatos !\033[01;00m")

                else:
                    buscar_contato(contato=entrada_contato())

            elif opc == 3:
                con = entrada_contato()

                if contato_verificar(contato=con):
                    print("\033[01;31m# Contato existente !\033[01;00m")

                else:
                    tel, ema, end = entrada_tel_ema_end()
                    incluir_editar_contato(contato=con, telefone=tel, email=ema, endereco=end)

            elif opc == 4:
                con = entrada_contato()

                if contato_verificar(contato=con):
                    tel, ema, end = entrada_tel_ema_end()
                    incluir_editar_contato(contato=con, telefone=tel, email=ema, endereco=end)

                else:
                    resp = input(f"\033[01;35m# Contato '{con}' inexistente, deseja incluir:\n"
                                 f"# [s] Sim \n"
                                 f"# [n] Nao \n"
                                 f"# Opc: \033[01;00m")[0].lower().strip()

                    if resp == 's':
                        tel, ema, end = entrada_tel_ema_end()
                        incluir_editar_contato(contato=con, telefone=tel, email=ema, endereco=end)

                    else:
                        print(f"\033[01;31m# Contato '{con}' nao adicionado! \033[01;00m")

            elif opc == 5:
                excluir_contato(contato=entrada_contato())

            elif opc == 6:
                if exportar_contatos(entrada_nome_arquivo_csv()):
                    print(f"\033[01;32m# Agenda exportada com sucesso \033[01;00m")

            elif opc == 7:
                importar_contatos(entrada_nome_arquivo_csv())

        except ValueError:
            print("\033[01;31m# Opcao invalida !\033[01;00m")

        except NameError:
            print("erro")

        except KeyboardInterrupt:
            print("\n\033[01;31m# Programa Encerrado !\033[01;00m")
            exit(0)


# Metodo: Procedimentos funcionais
def main():
    contatos_contador()
    load()
    menu()

# Metodo: Execucao
if __name__ == '__main__':
    main()