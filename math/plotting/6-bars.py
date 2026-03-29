#!/usr/bin/env python3
"""
Module that plots a stacked bar graph of fruit quantities per person.
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Plots a stacked bar graph representing the number of fruit
    each person possesses.
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))

    plt.figure(figsize=(6.4, 4.8))

    x = np.arange(fruit.shape[1])

    bottom = np.zeros(fruit.shape[1])

    labels = ['apples', 'bananas', 'oranges', 'peaches']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

    for i in range(fruit.shape[0]):
        plt.bar(x, fruit[i],
                bottom=bottom,
                width=0.5,
                color=colors[i],
                label=labels[i])
        bottom += fruit[i]

    plt.xticks(x, ['Farrah', 'Fred', 'Felicia'])

    plt.ylabel("Quantity of Fruit")
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))

    plt.title("Number of Fruit per Person")

    plt.legend()

    plt.show()
