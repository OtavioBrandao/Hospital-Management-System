# Utilizando o Strategy design pattern para os diferentes tipos de faturamento
from entidades.exame import VALORES_EXAMES

class FaturamentoStrategy:
    def calcular_faturamento(self, paciente):
        raise NotImplementedError("Subclasses devem implementar este método.")
    
class FaturamentoParticular(FaturamentoStrategy):
    def calcular_faturamento(self, paciente):
        total_consultas = len(paciente.consultas) * 25
        total_exames = sum(VALORES_EXAMES.get(exame.codigo, 0) for exame in paciente.exames)
        fatura = total_consultas + total_exames
        return round(fatura, 2)
    
class FaturamentoSUS(FaturamentoStrategy):
    def calcular_faturamento(self, paciente):
        fatura = 0.0
        return fatura

class FaturamentoConvenioUnimed(FaturamentoStrategy):
    def calcular_faturamento(self, paciente):
        quant_consultas = len(paciente.consultas)

        if quant_consultas > 5:
            quant_consultas = 5  # Unimed cobra até 5 consultas, depois é grátis

        total_consultas = quant_consultas * 7.50
        total_exames = sum(VALORES_EXAMES.get(exame.codigo, 0) * 0.3 for exame in paciente.exames)
        fatura = total_consultas + total_exames
        return round(fatura, 2)

class FaturamentoConvenioAmil(FaturamentoStrategy): 
    def calcular_faturamento(self, paciente):
        quant_consultas = len(paciente.consultas)

        total_consultas = quant_consultas * 3.50
        total_exames = sum(VALORES_EXAMES.get(exame.codigo, 0) * 0.2 for exame in paciente.exames)
        fatura = (total_consultas + total_exames)*0.9  # Desconto de 10%
        return round(fatura, 2)

class FaturamentoConvenioHapvida(FaturamentoStrategy):
    def calcular_faturamento(self, paciente):
        quant_consultas = min(len(paciente.consultas), 4)
        total_consultas = quant_consultas * 6.00

        total_exames = sum(VALORES_EXAMES.get(exame.codigo, 0.0) * 0.25 for exame in paciente.exames)
        total_exames = min(total_exames, 120.00)  
        return round(total_consultas + total_exames, 2)

class FaturamentoConvenioBradesco(FaturamentoStrategy):
    def calcular_faturamento(self, paciente):
        total_consultas = len(paciente.consultas) * 9.00
        total_exames = 0.0

        for exame in paciente.exames:
            base = VALORES_EXAMES.get(exame.codigo, 0.0)
            repasse = max(base * 0.35, 25.00)
            total_exames += repasse

        fatura = total_consultas + total_exames
        return round(fatura, 2)

class FaturamentoConvenioSulAmerica(FaturamentoStrategy):
    def calcular_faturamento(self, paciente):
        total_consultas = len(paciente.consultas) * 8.00

        total_exames = 0.0
        for exame in paciente.exames:
            base = VALORES_EXAMES.get(exame.codigo, 0.0)
            if base <= 100:
                repasse = base * 0.30
            elif base <= 250:
                repasse = base * 0.27
            else:
                repasse = base * 0.24
            total_exames += repasse

        total_exames = min(total_exames, 220.00)
        fatura = total_consultas + total_exames
        return round(fatura, 2)

def estrategia_para_faturar(paciente): 
    if not paciente.tipo_plano:
        return FaturamentoParticular()
    
    tipo_plano_str = str(paciente.tipo_plano.value) if paciente.tipo_plano else ""
    tipo_convenio_str = str(paciente.tipo_convenio.value) if paciente.tipo_convenio else ""
    
    if "SUS" in tipo_plano_str:
        return FaturamentoSUS()
    
    if "Particular" in tipo_plano_str:
        return FaturamentoParticular()
    
    if "Convênio" in tipo_plano_str:
        if "Unimed" in tipo_convenio_str:
            return FaturamentoConvenioUnimed()
        elif "Amil" in tipo_convenio_str:
            return FaturamentoConvenioAmil()
        elif "Hapvida" in tipo_convenio_str:
            return FaturamentoConvenioHapvida()
        elif "Bradesco" in tipo_convenio_str:
            return FaturamentoConvenioBradesco()
        elif "SulAmérica" in tipo_convenio_str:
            return FaturamentoConvenioSulAmerica()
    
    return FaturamentoParticular() 