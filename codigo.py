# Passo a passo do projeto
 
 # 1-> Abrir o sistema da empresa

 #abrir o navegador (chrome)
 # 2-> Fazer login
 # 3 -> Abrir/Importar a base de dados de produtos para cadastrar
 # 4-> Cadastrar um produto
 # 5-> Repetir isso tudo até acabar a lista de produtos

import pandas as pd 
import time 
import pyautogui as py
import numpy as np

#abrir o navegador

py.press('win')
time.sleep(1)
py.write('chrome')
py.press('enter')
time.sleep(1)
#Entrar no site do sistema
py.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
py.press('enter')

time.sleep(1)



# Fazer login -> como os campos de e-mail e senha nao estão selecionados, vamos pegar a posição do mouse.
# Criei um novo arquivo auxiliar, para pegar os valores dos eixos x e y

py.click(x=924, y=473)
time.sleep(0.3)
py.write('suzanarfontes@gmail.com')
time.sleep(0.3)
py.press('Tab')
py.write('Pokemon123')
py.press('enter')
time.sleep(0.2)





 # Importar a base de produtos 
try:
    tabela = pd.read_csv('produtos.csv')
except FileNotFoundError:
    print('Arquivo produtos.csv não encontrado')
   



# CADASTRANDO UM PRODUTO 

for linha in tabela.index:
    codigo_produto = str(tabela.loc[linha, "codigo"])
    py.click(x=742, y=326)
 
    py.write(codigo_produto)
    py.press('Tab') 
   
    py.write(str(tabela.loc[linha, "marca"]))
    py.press('Tab')
    py.write(str(tabela.loc[linha, "tipo"]))
    py.press('Tab')
    time.sleep(0.3)
    py.write(str(tabela.loc[linha, "categoria"]))
    py.press('Tab')
    time.sleep(0.3)
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    py.press('Tab')
    py.write(str(tabela.loc[linha, "custo"]))
    py.press('Tab')
   
    obs =str(tabela.loc[linha, "obs"])
    if obs != "nan":
        py.write(obs)
    py.press('Tab')
    time.sleep(0.5)
    py.press('Enter')

    py.scroll(3000)
# REPETIR ISSO TUDO ATÉ ACABAR A LISTA DE PRODUTOS 
