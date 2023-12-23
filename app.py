import os

restaurantes = [{"Nome": "Banzai", "Categoria": "Japonesa", "Ativo": False}, {"Nome": "Panetone", "Categoria": "Natalina", "Ativo": True} ]

def exibir_nome_programa():
      """Função para exibir o nome da empresa"""      
      print("""      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def voltar_menu_principal():
      """Função para retornar ao menu principal"""
      input("\nDigite uma tecla para voltar para o menu principal ")
      main()
      
def exibir_subtitulo(texto):
      """Função de estilização do terminal"""
      os.system("cls")
      linha = "*" * len(texto)
      print(linha)
      print(texto)
      print(linha)

def opcao_invalida():
      """Função que retorna 'Opção inválida' para o usuário"""
      print("Opção inválida\n")
      voltar_menu_principal()
      
def exibir_opcoes():
      """Função responsável por oferecer o menu de opções para o usuário"""
      print("1. Cadastrar restaurante")
      print("2. Listar restaurantes")
      print("3. Altenar status do restaurante")
      print("4. Sair\n")
      
def cadastrar_restaurante():
      """Função responsável por cadastrar um novo restaurante"""
      exibir_subtitulo("Cadastro de novos restaurantes\n")      
      nome_do_restaurante = input("Digite nome do restaurante: ")
      categoria_do_restaurante = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
      dados_do_restaurante = {"Nome": nome_do_restaurante, "Categoria": categoria_do_restaurante, "Ativo": False}
      restaurantes.append(dados_do_restaurante)    
      print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")
      voltar_menu_principal()

def listar_restaurantes():
      """Função responsável por listar restaurantes"""
      exibir_subtitulo("Listando restaurantes\n") 
      print(f"{"Nome do restaurante".ljust(10)} | {"Categoria".ljust(10)} | Status")      
      for restaurante in restaurantes:
            nome_restaurante = restaurante["Nome"] 
            categoria_restaurante = restaurante["Categoria"]
            ativo_restaurante = "Ativado" if restaurante["Ativo"] else "Desativado"   
            print(f"- {nome_restaurante.ljust(17)} | {categoria_restaurante.ljust(10)} | {ativo_restaurante}")
      voltar_menu_principal()

def altenar_status_restaurante():
      """Função responsável por alterar status do restaurante"""
      exibir_subtitulo("Alternando status do restaurante")
      nome_restaurante = input("Digite nome do restaurante que deseja alterar o status: ")
      restaurante_encontrado = False
      
      for restaurante in restaurantes:
            if nome_restaurante == restaurante["Nome"]:
                  restaurante_encontrado = True
                  restaurante["Ativo"] = not restaurante["Ativo"]
                  mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["Ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
                  print(mensagem)
      if not restaurante_encontrado:
            print("O restaurante não foi encontrado")
      voltar_menu_principal()
      
            
def escolher_opcoes():
      """Função responsiva para a escolha do usuário"""          
      try:
           opcao_escolhida = int(input("Escolha uma opção:"))  
           if opcao_escolhida == 1:
                 cadastrar_restaurante()
           elif opcao_escolhida == 2:
                 listar_restaurantes()
           elif opcao_escolhida == 3:
                 altenar_status_restaurante()
           elif opcao_escolhida == 4:
                 finalizando_app()
           else:
                 opcao_invalida()
      except:
            opcao_invalida()  
            
def finalizando_app():
      """Função para finalizar o programa"""
      exibir_subtitulo("Encerrando o programa\n")         
                  
def main():
      """Função princial""" 
      os.system("cls")     
      exibir_nome_programa()
      exibir_opcoes()
      escolher_opcoes()      
      
if __name__ == "__main__":
      main()
          