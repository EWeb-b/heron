import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

def weeklyBAR(date):
    n_groups = 3

    means_men = [20, 35, 30]


    means_women = [25, 32, 34]


    means_cat = [40, 25, 32]


    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.2

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, means_men, bar_width,
                     color='b',
                    error_kw=error_config,
                    label='Adult')

    rects2 = ax.bar(index + bar_width, means_women, bar_width,
                     color='r',
                    error_kw=error_config,
                    label='Student')

    rects3 = ax.bar(index + 2*bar_width, means_cat, bar_width,
                     color='g',
                    error_kw=error_config,
                    label='Child')

    ax.set_xlabel('Movies')
    ax.set_ylabel('Ticket sales')
    ax.set_title('Daily breakdown for: '+date)
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(['Black Panther', 'The Sound of Water', 'The Greatest Showman'])
    ax.legend()

    fig.tight_layout()
    plt.show()
weeklyBAR('06/04/2018')
