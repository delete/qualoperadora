# -*- coding: utf-8 -*-
#!/usr/bin/env python2
#
# Created: Thu Jun 20 11:03:24 2013
#
# Site Oficial: http://www.qualoperadora.net/
# O site não é é de minha autoria!!
#
# Programador: Fellipe Pinheiro
# Contato: https://twitter.com/PinheiroFellipe
# Código: https://github.com/delete
#
# Versão 0.1 - beta

import mechanize
import cookielib
import os


class Operadora(object):

    def setNumero(self, numero):
        self.numero = numero

    def configura(self):
        ##cria um navegador, um browser de codigo...
        br = mechanize.Browser()
        url = 'http://www.qualoperadora.net/'

        ## Prepara para tratar cookies...
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)

        ## Ajusta algumas opções do navegador...
        br.set_handle_equiv(True)
        br.set_handle_gzip(False)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        ## Configura o user-agent.
        ## Do ponto de vista do servidor, o navegador agora o Firefox.
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11;\
         U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615\
        Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        ## Pronto! Agora é navegar, acessando a URL usando o método HTTP GET
        br.open(url)

        ## Se existirem formulários, você pode selecionar o primeiro (#0), por exemplo..
        br.select_form(nr=0)

        ## Preencher o formulário com os dados de login...
        br.form['telefone'] = str(self.numero)

        ## Enviar o formulário usando o método HTTP POST
        br.submit()

        ## E finalmente, busque o HTML retornado:
        html = br.response().read()

        ##Salva o codigo HTML em um arquivo
        arq = open('t.txt', 'w')
        arq.write(html)
        arq.close()

    def filtro(self):
        #Filtra os dados
        lista = []
        string = ''

        for line in open('t.txt'):
            if 'dados' in line:
                string = line[line.find('>')+1:]
                lista.append(string[:string.find('<')])

        os.remove('t.txt')
        return lista

if __name__ == '__main__':
    p = Operadora()
    num = input('Digite DDD+NUMERO: ')
    p.setNumero(num)
    p.configura()
    lista = p.filtro()

    print('Numero: ' + lista[0])
    print('Operadora: ' + lista[1])
    print('Estado: ' + lista[2])
