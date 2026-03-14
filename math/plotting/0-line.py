#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def line():
    x = np.arange(0, 11)        # x من 0 إلى 10
    y = x ** 3                   # y مكعب x
    plt.figure(figsize=(6.4, 4.8))

    # رسم الخط الأحمر المكعب
    plt.plot(x, y, 'r', linestyle='-')

    # ضبط حدود x-axis من 0 إلى 10
    plt.xlim(0, 10)

    # عرض الرسم
    plt.show()
