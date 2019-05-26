# -*- coding: utf-8 -*-
from enum import Enum
from typing import List

class Direcoes(Enum):
    LESTE = 1
    SUDESTE = 2
    SUL = 3
    SUDOESTE = 4
    OESTE = 5
    NOROESTE = 6
    NORTE = 7
    NORDESTE = 8

class Posicao:
    int i = 0// linha
    int j = 0// coluna

class Matriz(list):
    m = 0
    n = 0

    def imprime_matriz(matriz):
        for i in range(0, len(matriz)/len(matriz[0])):
            for j in range(0, len(matriz[0])):
                print(matriz[i][j], end='')
            print('\n')

def main():
    #Leitura da matriz de entrada
    global matriz_entrada = Matriz()
    tamanho_lista = -1
    while tamanho_lista < 0:
        l = input()
        if str(l).isdigit():
            tamanho_lista = int(l)
        else:
            l = str(l).split(" ")
            matriz_entrada.append(l)

    #Pega as dimensões da matriz de entrada
    global qntd_linhas = len(matriz_entrada)/len(matriz_entrada[0])
    global qntd_colunas = len(matriz_entrada[0])

    #Cria lista de saídas
    matriz_saida = []
    for i in range (0, qntd_linhas):
        for j in range (0, qntd_colunas):
            matriz_saida[i][j] = "."

    #Leitura da lista de palavras da entrada
    lista_palavras = []
    for i in range(0, n):
        elemento = input()
        lista_palavras.append(elemento)

    #Função que verifica se a posicao é válida
    def posicao_valida(i,j):
        if (0 <= i < qntd_linhas) and (0 <= j < qntd_colunas):
            return True
        else:
            return False

    #Percorre a lista de palavras
    for palavra in lista_palavras:
        achou = False

        #Percorre a matriz
        for j in range(0, qntd_colunas):
            for i in range(0, qntd_linhas):

                #Procura primeira letra da palavra
                if matriz_entrada[i][j] == palavra[0] and not achou:
                    achou = True
                    for direcao in direcoes:
                        cont = 1
                        while posicao_valida(direcao) and len(palavra) > cont and achou:
                            cont += 1
                            if matriz_entrada[direcao] == palavra[cont-1]:
                                pass
                            else:
                                achou = False
                        if


if _name_ == '_main_':
    main()
