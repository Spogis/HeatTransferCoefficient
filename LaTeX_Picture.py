import matplotlib.pyplot as plt
from PIL import Image


def crop_image(filename, top, bottom):
    # Abre a imagem salva
    img = Image.open(filename)

    # Calcula as dimensões para o corte
    width, height = img.size
    left = 0
    right = width
    upper = top
    lower = height - bottom

    # Corta a imagem
    cropped_img = img.crop((left, upper, right, lower))

    # Salva a imagem cortada, substituindo a original
    cropped_img.save(filename)

def latex_to_png(C_opt, C_std, n_opt, n_std, m_opt, m_std, filename):
    # Configura o matplotlib para usar sua própria renderização de LaTeX
    plt.rc('text', usetex=False)
    plt.rc('font', family='serif')

    # Formata a equação com os valores de A_value e B_value
    #equation = rf"$Nu = {C_opt:.2f} \pm{C_std:.2f} * Re^{n_opt} * Pr^{m_opt}$"
    #equation = rf"$Nu = {C_opt:.2f} \pm {C_std:.2f} \cdot Re^{{\frac{{{n_opt.numerator}}}{{{n_opt.denominator}}}}} \cdot Pr^{{\frac{{{m_opt.numerator}}}{{{m_opt.denominator}}}}}$"

    equation = rf"$Nu = {C_opt:.2f} \pm {C_std:.2f} \cdot Re^{{({n_opt.numerator}/{n_opt.denominator} \pm {n_std:.2f})}} \cdot Pr^{{({m_opt.numerator}/{m_opt.denominator} \pm {m_std:.2f})}}$"

    dpi = 300
    width_in = 500 / dpi
    height_in = 450 / dpi

    # Configurando o tamanho da figura em polegadas e a resolução em DPI
    fig, ax = plt.subplots(figsize=(width_in, height_in), dpi=dpi)

    # Cria uma figura e um eixo
    #fig, ax = plt.subplots()

    # Adiciona a equação ao eixo
    ax.text(0.5, 0.5, equation, fontsize=15, va='center', ha='center', color='white')

    # Remove os eixos
    ax.axis('off')

    # Salva a figura
    plt.savefig(filename, bbox_inches='tight', pad_inches=0, transparent=True)

    # Fecha a figura para liberar recursos
    plt.close(fig)

    crop_image(filename, top=100, bottom=100)

