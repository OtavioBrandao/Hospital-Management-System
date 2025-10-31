from abc import ABC, abstractmethod
from datetime import datetime

# Utilizando o padrão Observer para notificar funcionários sobre emergências
class Observer:
    def update(self, mensagem):
        pass

class FuncionarioObserver:
    def __init__(self, funcionario, email=None, whatsapp=None):
        self.nome = funcionario if isinstance(funcionario, str) else funcionario.nome
        self.email = email  
        self.whatsapp = whatsapp  

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
        # Utilizando o adapter para notificar por outros meios além do console
        self.email_notificador = EmailAdapter()
        self.whatsapp_notificador = WhatsAppAdapter()

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
            if hasattr(observer, 'email'):
                self.email_notificador.enviar(observer.email, mensagem)
            
            if hasattr(observer, 'whatsapp'):
                self.whatsapp_notificador.enviar(observer.whatsapp, mensagem)
    
    def registrar_emergencia(self, nome, prioridade):
        try:
            # Validação de prioridade
            if not prioridade or prioridade.strip() == "":
                raise ValueError("Prioridade é obrigatória para registrar uma emergência. Use: alta, media ou baixa.")
            
            prioridades_validas = ["alta", "media", "baixa"]
            if prioridade.lower() not in prioridades_validas:
                raise ValueError(f"Prioridade inválida. Use uma das opções: {', '.join(prioridades_validas)}")
            
            self.emergencias.append((nome, prioridade.lower()))
            mensagem = f"🚨 EMERGÊNCIA: {nome} - Prioridade: {prioridade.upper()}"
            self.notificar_turno_atual(mensagem)
            return True
        except ValueError as ve:
            print(f"❌ Erro ao registrar emergência: {ve}")
            return False

    def ver_emergencias(self):
        if not self.emergencias:
            print("Nenhuma emergência.")
            return
        prioridades = {"alta": 1, "media": 2, "baixa": 3}
        ordenadas = sorted(self.emergencias, key=lambda x: prioridades.get(x[1], 4)) 
        for nome, prioridade in ordenadas:
            print(f"🚑 {nome} - Prioridade: {prioridade}")


# Simulando o uso de algum serviço externo de notificação
# Neste caso estamos notificando apenas emergências, mas poderia ser expandido para outros tipos de notificação
class ServicoEmailExterno:
    def send_email(self, to, subject, body):
        print(f"📧 [EMAIL ENVIADO]")
        print(f"   De: sistema@hospital.com")
        print(f"   Para: {to}")
        print(f"   Assunto: {subject}")
        print(f"   Corpo: {body}\n")


class ServicoWhatsAppExterno:
    def enviar_mensagem_whatsapp(self, numero, texto):
        print(f"💚 [WHATSAPP ENVIADO]")
        print(f"   Para: {numero}")
        print(f"   Texto: {texto}\n")

# Implementação do Adapter
class AdapterInterface(ABC):
    @abstractmethod
    def enviar_mensagem(self, destinatario, mensagem):
        pass

class EmailAdapter(AdapterInterface):
    def enviar_mensagem(self, destinatario, mensagem):
        servico_email = ServicoEmailExterno()
        assunto = "🚨 Notificação de Emergência"
        corpo = f"Prezado funcionário,\n\n{mensagem}\n\n---\nMensagem automática do Sistema Hospitalar\nData: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        servico_email.send_email(destinatario, assunto, corpo)
    
    def enviar(self, email, mensagem):
        self.enviar_mensagem(email, mensagem)

class WhatsAppAdapter(AdapterInterface):
    def enviar_mensagem(self, destinatario, mensagem):
        servico_whatsapp = ServicoWhatsAppExterno()
        texto_formatado = f"*HOSPITAL - EMERGÊNCIA*\n\n{mensagem}\n\n_{datetime.now().strftime('%H:%M')}_"
        servico_whatsapp.enviar_mensagem_whatsapp(destinatario, texto_formatado)
    
    def enviar(self, numero, mensagem):
        self.enviar_mensagem(numero, mensagem)
