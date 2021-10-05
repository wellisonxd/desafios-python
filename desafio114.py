import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLerror:
    print('O site PUDIM não está acessível.')
else:
    print('Consegui acessar o site PUDIM com sucesso')