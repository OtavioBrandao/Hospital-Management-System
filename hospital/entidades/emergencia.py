
from datetime import datetime

# Utilizando o padrão Observer para notificar funcionários sobre emergências
class Observer:
    def update(self, mensagem):
        pass

class FuncionarioObserver(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, mensagem):
        print(f"‼️ {self.nome} recebeu a notificação: {mensagem}")

class EmergenciaManager:
    def __init__(self):
        self.emergencias = []
        self.observers_por_turno = {
            "Manhã": [],
            "Tarde": [],
            "Noite": []
        }
        self.log = []  

    def adicionar_observer(self, observer, turno):
        if turno in self.observers_por_turno:
            self.observers_por_turno[turno].append(observer)
    
    def get_turno_atual(self):
        hora = datetime.now().hour
        if 6 <= hora < 12:
            return "Manhã"
        elif 12 <= hora < 18:
            return "Tarde"
        else:
            return "Noite"
    
    def notificar_turno_atual(self, mensagem):
        turno = self.get_turno_atual()
        observers = self.observers_por_turno.get(turno, [])
        
        if not observers:
            print(f"⚠️  Nenhum funcionário cadastrado no turno {turno}")
            return
        
        print(f"\n🔔 Notificando funcionários do turno: {turno}")
        for observer in observers:
            observer.update(mensagem)
            self.log.append((datetime.now(), observer, mensagem))
    
    def registrar_emergencia(self, nome, prioridade):
        self.emergencias.append((nome, prioridade))
        mensagem = f"🚨 EMERGÊNCIA: {nome} - Prioridade: {prioridade.upper()}"
        self.notificar_turno_atual(mensagem)


    def ver_emergencias(self):
        if not self.emergencias:
            print("Nenhuma emergência.")
            return
        prioridades = {"alta": 1, "media": 2, "baixa": 3}
        ordenadas = sorted(self.emergencias, key=lambda x: prioridades.get(x[1], 4)) 
        for nome, prioridade in ordenadas:
            print(f"🚑 {nome} - Prioridade: {prioridade}")

