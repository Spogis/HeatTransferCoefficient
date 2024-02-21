import pandas as pd
import numpy as np
from fractions import Fraction
from scipy.optimize import curve_fit

from LaTeX_Picture import *

# Passo 1: Leitura dos dados
caminho_do_arquivo = 'Datasets/Case3.xlsx'
dados = pd.read_excel(caminho_do_arquivo)


def ranz_marshall(Re, Pr, C, n, m):
    return C * Re**n * Pr**m


def func_for_fit(X, C, n, m):
    Re, Pr = X
    return ranz_marshall(Re, Pr, C, n, m)


Nu_data = dados['Nu']
Re_data = dados['Re']
Pr_data = dados['Pr']

# Restrições para garantir que os parâmetros sejam positivos
bounds = (0, np.inf)

# Minimização da função objetivo
popt, pcov = curve_fit(func_for_fit, (Re_data, Pr_data), Nu_data)

# Resultados otimizados
C_opt, n_opt, m_opt = popt

# Calculando os desvios padrões dos parâmetros a partir da matriz de covariância
perr = np.sqrt(np.diag(pcov))
# Desempacotando os desvios padrões
C_std, n_std, m_std = perr

n_opt = Fraction(n_opt).limit_denominator(10)
m_opt = Fraction(m_opt).limit_denominator(10)

# Imprimindo parâmetros otimizados e seus desvios padrões
print(f"Parâmetros otimizados: C = {C_opt:.2f} ± {C_std:.2f}, n = {n_opt} ± {n_std:.2f}, m = {m_opt:} ± {m_std:.2f}")

filename = 'assets/Equation.png'
latex_to_png(C_opt, C_std, n_opt, n_std, m_opt, m_std, filename)

img = Image.open(filename)
img.show()
