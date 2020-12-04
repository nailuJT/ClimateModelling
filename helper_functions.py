import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op


def format_plot(axes_object, y_label='dT/dt', y_fontsize=15,  x_label='Time [years]', x_fontsize=15, tick_fontsize=13, tick_size=6, legend_fontsize=13):
    axes_object.set_ylabel(y_label, fontsize=y_fontsize)
    axes_object.set_xlabel(x_label, fontsize=x_fontsize)

    axes_object.tick_params(labelsize=tick_fontsize, length=tick_size, width=tick_size/3)

    axes_object.yaxis.get_offset_text().set_fontsize(tick_fontsize)
    axes_object.xaxis.get_offset_text().set_fontsize(tick_fontsize)

    axes_object.legend(fontsize=legend_fontsize, bbox_to_anchor=(1.01, 1))
    return axes_object


def basic_solve(scalar_function, lower_bound, upper_bound, steps=500, decimals=1):
    solutions = set()
    for x_start in np.linspace(lower_bound, upper_bound, steps):
        root = op.root(scalar_function, x_start)
        root.x = np.around(root.x, decimals)
        solutions.add(float(root.x))
    return solutions
