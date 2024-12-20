import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    imagem = cv2.imread('imagens/diversas/lena.jpg',0)
    limiar = histogramaImagemOriginal(imagem)
    imagembi = binarizacaoImagem(limiar,imagem)
    exibir(imagembi,imagem)

def histogramaImagemOriginal(imagem):
    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('niveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagem.ravel(), bins=256, range=[0, 255])
    plt.show()
    limiar = int(input("Digite o valor do limiar: "))

    return limiar

def binarizacaoImagem(limear,imagem):
    [altura,largura] = imagem.shape
    imagembi = np.copy(imagem)
    for i in range(altura):
        for j in range(largura):
            if(imagem[i][j] >= limear):
                imagembi[i][j] =  255
            else:
                imagembi[i][j] = 0

    return imagembi


def exibir(imagembi,imagem):
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem Binarizada', imagembi)

    plt.subplot(121)
    plt.title('Imagem Original')
    plt.xlabel('niveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagem.ravel(), bins=256, range=[0, 255])

    plt.subplot(122)
    plt.title('Imagem Binarizada')
    plt.xlabel('niveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagembi.ravel(), bins=256, range=[0, 255])

    plt.show()
    cv2.waitKey(0)

main()