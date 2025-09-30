from hospital import Hospital
#import gerarPdf
import funcoesAuxiliares
#import apresentacao
hospital = Hospital()

# Definir a instância global do hospital para funcoesAuxiliares
funcoesAuxiliares.hospital = hospital


# --- Execução principal ---
if __name__ == "__main__":
    funcoesAuxiliares.clear_screen()
    while True:
        
        funcoesAuxiliares.menu()
        op = input("Escolha uma opção: ")

        if op == '0':
            print("Encerrando o sistema.")
            break

        elif op == '1':
            funcoesAuxiliares.cadastro()

        elif op == '2':
            funcoesAuxiliares.menu_agendamento()

        elif op == '3':
            funcoesAuxiliares.prontuarioMedico()

        elif op == '4':
            nome = input("Nome do paciente: ")
            hospital.faturar_paciente(nome)
            input("Paciente faturado. Pressione Enter para continuar...")
            funcoesAuxiliares.clear_screen()

        elif op == '5':
            funcoesAuxiliares.estoque_menu(hospital)

        elif op == '6':
            funcoesAuxiliares.emergencias_menu(hospital)
        elif op == '7':
            funcoesAuxiliares.solicitarExame()
            input("Exame solicitado. Pressione Enter para continuar...")
            funcoesAuxiliares.clear_screen()

        elif op == '8':
            nome = input("Nome do paciente: ")
            hospital.alocar_leito(nome)
            input("Leito alocado. Pressione Enter para continuar...")
            funcoesAuxiliares.clear_screen()
        elif op == '9':
            funcoesAuxiliares.funcionarios(hospital)
        elif op == '10':
            funcoesAuxiliares.receituario_menu(hospital)
            pass
        elif op == '11':
            funcoesAuxiliares.relatorios_menu(hospital)
        else:
            print("Opção inválida.")
           
