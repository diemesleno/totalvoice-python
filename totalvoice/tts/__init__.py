# coding=utf-8

from totalvoice.cliente import Cliente
from totalvoice.helper import utils
from totalvoice.helper.routes import Routes
from totalvoice.totalvoice import Totalvoice
import json, requests

class Tts(Totalvoice):
    cliente = None

    def __init__(self, cliente):
        self.cliente = cliente

    def enviar(self, numero_destino, mensagem, velocidade=None, resposta_usuario=None, tipo_voz=None, bina=None):
        """
        :Descrição:

        Função para enviar TTS (Text-to-speech)

        :Utilização:

        enviar(self, numero_destino, mensagem, velocidade, resposta_usuario, tipo_voz, bina)

        :Parâmetros:
        
        - numero_destino:
        Número do telefone que irá receber a mensagem, formato DDD + Número exemplo: 4832830151.

        - mensagem:
        Mensagem que será lida para o destinatário.

        - valocidade
        De -10 a 10. Onde -10=muito lento, 0=normal e 10=muito rápido.

        - resposta_usuario:
        Aguardar uma resposta do destinatário. true ou false.

        - tipo_voz:
        Informe a sigla do idioma concatenado ao nome do personagem que vai falar. Ex: br-Ricardo, br-Vitoria.

        - bina:
        Número e telefone que aparecerá no identificador de quem receber a chamada, formato DDD + Número exemplo: 4832830151.
        """
        host = self.buildHost(self.cliente.host, Routes.TTS)
        data = self.__buildTts(numero_destino, mensagem, velocidade, resposta_usuario, tipo_voz, bina)
        response = requests.post(host, headers=utils.buildHeader(self.cliente.access_token), data=data)
        return response.content

    def getById(self, id):
        """
        :Descrição:

        Função para buscar informações de TTS e respostas.

        :Utilização:

        getById(id)

        :Parâmetros:

        - id:
        ID do tts.
        """
        host = self.buildHost(self.cliente.host, Routes.TTS, [id])
        return self.getRequest(host)

    def getRelatorio(self, data_inicio, data_fim):
        """
        :Descrição:
        
        Função para pegar o relatório de tts.

        :Utilização:

        getRelatorio(data_inicio, data_fim)

        :Parâmetros:

        - data_inicio:
        Data início do relatório (2016-03-30T17:15:59-03:00)
        format UTC

        - data_fim:
        Data final do relatório (2016-03-30T17:15:59-03:00)
        format UTC    

        """
        host = self.buildHost(self.cliente.host, Routes.TTS, ["relatorio"])
        params = (('data_inicio', data_inicio),('data_fim', data_fim),)
        return self.getRequest(host, params)

    def __buildTts(self, numero_destino, mensagem, velocidade, resposta_usuario, tipo_voz, bina):
        data = {}
        data.update({"numero_destino" : numero_destino})
        data.update({"mensagem" : mensagem})
        data.update({"velocidade" : velocidade})
        data.update({"resposta_usuario" : resposta_usuario})
        data.update({"tipo_voz" : tipo_voz})
        data.update({"bina" : bina})
        return json.dumps(data)