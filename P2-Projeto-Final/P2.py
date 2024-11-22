import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    imagem = cv2.imread('imagens/diversas/lena.jpg', 0)
    [altura, largura] = imagem.shape
    print(altura, largura)
    limear = histogramaImagemOriginal(imagem)
    imagemdectec = dectecImagem(limear, imagem)
    exibir(imagem, imagemdectec)


def histogramaImagemOriginal(imagem):
    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('níveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagem.ravel(), bins=256, range=[0, 255])
    plt.show()
    limear = int(input("Digite o valor do limiar: "))
    return limear


def dectecImagem(limear, imagem):
    [altura, largura] = imagem.shape
    imagembi = np.copy(imagem)
    laplaciano = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

    for i in range(altura):
        for j in range(largura):
            if imagem[i][j] <= limear:
                imagembi[i][j] = 255
            else:
                imagembi[i][j] = 0

    imagemdectec = np.copy(imagem)
    for i in range(1, altura - 2):
        for j in range(1, largura - 2):
            regiao = imagem[i:i + 3, j:j + 3]
            laplaciano_resultado = np.sum(regiao * laplaciano)
            imagemdectec[i, j] = np.clip(laplaciano_resultado, 0, 255)

    return imagemdectec


def exibir(imagem, imagemdectec):
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem com Dectecao de Bordas', imagemdectec)

    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('níveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagem.ravel(), bins=256, range=[0, 255])

    plt.subplot(122)
    plt.title('Histograma Detecção de Bordas')
    plt.xlabel('níveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imagemdectec.ravel(), bins=256, range=[0, 255])

    plt.show()
    cv2.waitKey()


main()