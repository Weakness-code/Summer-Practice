import matplotlib.pyplot as plt
import matplotlib.image as mpimg


fig = plt.figure()


def image_4split(img):
    """Разбивает изображение на 4 линии остовляя один канал
    для 3 первых полос и усредняет все значения для 4 полосы"""
    ax = fig.add_subplot(2, 2, 1)
    tmp_len = len(img[0])
    for i in range(len(img)):
        for j in range(tmp_len):
            if j > 3 * tmp_len / 4:
                img[i][j] = [sum(img[i][j])/3 for k in range(3)]
            elif j > tmp_len / 2:
                img[i][j] = [0, 0, img[i][j][2]]
            elif j > tmp_len / 4:
                img[i][j] = [0, img[i][j][1], 0]
            else:
                img[i][j] = [img[i][j][0], 0, 0]

    ax.imshow(img)
    ax.axis("off")

def channel_1(img):
    """Оставляет только один канал цветов RGB"""
    ax = fig.add_subplot(2, 2, 2)
    channels = {'r': [1, 0, 0], 'g': [0, 1, 0], 'b': [0, 0, 1]}
    channel = 'r'
    for i in range(len(img)):
        for j in range(len(img[0])):
            img[i][j] = img[i][j] * channels[channel]

    ax.imshow(img)
    ax.axis("off")

def gray_mod2(img):
    """Усредняет все занчения каналов RGB для каждой второй точки"""
    ax = fig.add_subplot(2, 2, 3)
    for i in range(1, len(img), 2):
        for j in range(len(img[0])):
            img[i][j] = [sum(img[i][j])/3 for k in range(3)]

    ax.imshow(img)
    ax.axis("off")
    
def point_color_size(img):
    """Предает оттенок изображению и окрашивает всё
    за пределами окружности в черный"""
    ax = fig.add_subplot(2, 2, 4)
    hand_size = 900                     #Величина кисти
    color = [196, 69, 141]              #Цвет кисти
    colorsize = [i/255 for i in color]
    X, Y = len(img[0]), len(img)

    for i in range(Y):
        for j in range(X):
            if (j - X/2)**2 + (i - Y/2)**2 > (hand_size/2)**2:
                img[i][j] = [0, 0, 0]
            else :
                img[i][j] = img[i][j] * colorsize

    ax.imshow(img)
    ax.axis("off")

def main():
    image = mpimg.imread("girl-painting-abstract-art-img-2048x1152.jpg")
    image_4split(image.copy())
    channel_1(image.copy())
    gray_mod2(image.copy())
    point_color_size(image.copy())
    plt.show()


if __name__ == '__main__':
    main()
