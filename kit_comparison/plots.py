from io import StringIO

import matplotlib.pyplot as plt


def plot_focal_range(full_names, focal_lengths):
    plt.style.use('_mpl-gallery')

    fig, ax = plt.subplots()
    for i, fl in enumerate(focal_lengths):
        if len(fl) == 1:
            ax.broken_barh([(fl[0], 5)], ((1 + i) * 10 + 2.5, 5), facecolors='tab:blue')
        else:
            ax.broken_barh([(fl[0], fl[1] - fl[0])], ((1 + i) * 10 + 2.5, 5), facecolors='tab:blue')
    ax.set_ylim(5, 45)
    ax.set_xlim(0, 400)
    ax.set_yticks([15 + i * 10 for i in range(len(full_names))], labels=full_names)
    ax.grid(True)
    i = StringIO()
    plt.savefig(i, format="svg")
    return i.getvalue()