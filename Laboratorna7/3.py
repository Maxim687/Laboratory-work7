from numpy import *
import matplotlib.pyplot as plt
import numpy as np
import pylab
text = str("1. Які засоби мова Python надає для роботи з 2D графікою? Які бібліотеки призначені для роботи з графікою?Яким чином можна відобразити графік математичної функції?Як можна налаштувати колір та тип лінії на графіку математичної функції?Яким чином можна відобразити гісторграму?Яким чином можна зберегти зображення у файл?")
def count_sign():
    symbols = ["—", "!", ".", ",", "?", "..."]
    for i in range(0, len(symbols)):
        xdata = [symbols[i]]
        ydata = [text.count(symbols[i])]
        pylab.bar(xdata, ydata)
    pylab.show()
count_sign()
