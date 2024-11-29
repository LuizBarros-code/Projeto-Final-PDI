import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    imagem = cv2.imread('imagens/diversas/tools.jpg', 0)
    limiar = histogramaImagemOriginal(imagem)
    imagemdetec = dectecImagem(limiar, imagem)
    exibir(imagem, imagemdetec)

def histogramaImagemOriginal(imagem):
    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('níveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagem.ravel(), bins=256, range=[0, 255])
    plt.show()
    limiar = int(input("Digite o valor do limiar: "))
    return limiar

def dectecImagem(limear, imagem):
    [altura, largura] = imagem.shape
    imagemdetec = np.copy(imagem)
    laplaciano = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            regiao = imagem[i-1:i+2, j-1:j+2]
            laplaciano_resultado = np.sum(regiao * laplaciano)

            if laplaciano_resultado < 0:
                laplaciano_resultado = 0
            elif laplaciano_resultado > 255:
                laplaciano_resultado = 255

            imagemdetec[i, j] = laplaciano_resultado

    for i in range(altura):
        for j in range(largura):
            if imagemdetec[i][j] >= limear:
                imagemdetec[i][j] = 255
            else:
                imagemdetec[i][j] = 0

    return imagemdetec

def exibir(imagem, imagemdetec):
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem com Deteccao de Bordas', imagemdetec)

    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('níveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagem.ravel(), bins=256, range=[0, 255])

    plt.subplot(122)
    plt.title('Histograma Detecção de Bordas')
    plt.xlabel('níveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagemdetec.ravel(), bins=256, range=[0, 255])

    plt.show()
    cv2.waitKey(0)

main()