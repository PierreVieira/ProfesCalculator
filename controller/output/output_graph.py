from collections import OrderedDict
from matplotlib import pyplot as plt


def output_graph(deposits_sum_by_period: OrderedDict) -> None:
    x_axis = []
    y_axis = []
    for key, value in deposits_sum_by_period.items():
        x_axis.append(key)
        y_axis.append(value)
    plt.bar(x_axis, y_axis)
    plt.show()
