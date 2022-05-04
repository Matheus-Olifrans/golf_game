from math import floor


def show(ballpos):
    pixels = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    pixels[floor(ballpos[1])][floor(ballpos[0])] = 1
    draw(pixels)


def draw(pixels):
    chars = {(0, 0): "█",
             (1, 0): "▄",
             (0, 1): "▀",
             (1, 1): " "}
    for line in range(5):
        for colunn in range(10):
            print(chars[pixels[2*line][colunn], pixels[2*line + 1][colunn]])
        print("\n")
