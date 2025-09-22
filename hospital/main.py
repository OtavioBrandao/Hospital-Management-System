from hospital import Hospital
#import gerarPdf
import funcoesAuxiliares
#import apresentacao
hospital = Hospital()


# --- Execução principal ---
if __name__ == "__main__":
    while True:
        
        funcoesAuxiliares.menu()
        op = input("Escolha uma opção: ")

        if op == '0':
            print("Encerrando o sistema.")
            break

        elif op == '1':
            funcoesAuxiliares.cadastro()

        elif op == '2':
            funcoesAuxiliares.agendarConsulta()

        elif op == '3':
            funcoesAuxiliares.prontuarioMedico()

        elif op == '4':
            nome = input("Nome do paciente: ")
            funcoesAuxiliares.hospital.faturar_paciente(nome)

        elif op == '5':
            funcoesAuxiliares.estoque_menu(hospital)

        elif op == '6':
            funcoesAuxiliares.emergencias_menu(hospital)
        elif op == '7':
            funcoesAuxiliares.solicitarExame()

        elif op == '8':
            nome = input("Nome do paciente: ")
            funcoesAuxiliares.hospital.alocar_leito(nome)

        elif op == '9':
            funcoesAuxiliares.funcionarios(hospital)
        elif op == '10':
            funcoesAuxiliares.receituario_menu(hospital)
            pass
        elif op == '11':
            #funcoesAuxiliares.relatorios_menu(hospital)
            pass
        else:
            print("Opção inválida.")
           
