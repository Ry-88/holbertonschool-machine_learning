#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def line():
    y = np.arange(0, 11) ** 3
    x = np.arange(0, 11)  # x من 0 إلى 10
    plt.figure(figsize=(6.4, 4.8))

    # رسم y مقابل x كخط أحمر متصل
    plt.plot(x, y, color='red', linestyle='solid')

    # عرض الرسم
    plt.show()
