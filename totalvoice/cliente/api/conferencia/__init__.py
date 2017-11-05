# coding=utf-8

from totalvoice.cliente.api.helper import utils
from totalvoice.cliente.api.helper.routes import Routes
from totalvoice.cliente.api.totalvoice import Totalvoice
import json, requests

class Conferencia(Totalvoice):

    def __init__(self, cliente):
        super(Conferencia, self).__init__(cliente)

    def criaConferencia(self):
        """
        :Descrição:

        Essa é uma função para postar uma conferência

        :Utilização:

        criaConferencia()

        """
        host = self.build_host(self.cliente.host, Routes.CONFERENCIA)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token))
        return response.content
    
    def getById(self, id):
        """
        :Descrição:

        Função para buscar as informações de uma conferência ativa.

        :Utilização:

        getById(id)

        :Parâmetros:

        - id:
        ID da conferência ativa.
        """
        host = self.cliente.host + Routes.CONFERENCIA + "/" + id
        return self.get_request(host)

    def addNumeroConferencia(self, idConferencia, numero, bina=None, gravar_audio=None):
        """
        :Descrição:

        Função para adicionar números de telefone na conferência ativa.

        :Utilização:

        addNumeroConferencia(idConferencia, numero, bina, gravar_audio)

        :Parâmetros:

        - idConferencia:
        ID da conferência ativa.

        - numero:
        Número do telefone que irá receber a chamada da conferência, formato DDD + Número exemplo: 4832830151

        - bina:
        Número e telefone que aparecerá no identificador de quem receber a chamada, formato DDD + Número exemplo: 4832830151

        - gravar_audio:
        Flag que indica se o áudio deve ser gravado
        """
        host = self.cliente.host + Routes.CONFERENCIA + "/" + idConferencia
        data = self.__buildConferencia(idConferencia, numero, bina, gravar_audio)
        response = requests.post(host, headers=utils.build_header(self.cliente.access_token), data=data)
        return response.content

    def __buildConferencia(self, numero, bina, gravar_audio):
        """
        :Descrição:

        Função privada para realizar o build dos dados.
        """
        data = {}
        data.update({"numero" : numero})
        data.update({"bina" : bina})
        data.update({"gravar_audio" : gravar_audio})
        return json.dumps(data)
            

    
    