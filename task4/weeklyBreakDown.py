import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

def weeklyBAR(date,movies,data):
    # ARGUMENTS: date = date of the bar chart,
    #            data = [[adult],[student],[child],[OAP],[VIP]] a list(length = 5) of lists(length = number of movies this week)
    n_groups = len(data[0])

    ADULT = data[0]

    STUDENT = data[1]

    CHILD = data[2]

    OAP = data[3]

    VIP = data[4]

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.2

    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, ADULT, bar_width,
                     color='b',
                    error_kw=error_config,
                    label='Adult')

    rects2 = ax.bar(index + bar_width, STUDENT, bar_width,
                     color='r',
                    error_kw=error_config,
                    label='Student')

    rects3 = ax.bar(index + 2*bar_width, CHILD, bar_width,
                     color='g',
                    error_kw=error_config,
                    label='Child')
    rects4 = ax.bar(index + 3*bar_width, OAP, bar_width,
                     color='y',
                    error_kw=error_config,
                    label='OAP')
    rects5 = ax.bar(index + 4*bar_width, VIP, bar_width,
                     color='maroon',
                    error_kw=error_config,
                    label='VIP')

    ax.set_xlabel('Movies')
    ax.set_ylabel('Ticket sales')
    ax.set_title('Daily breakdown for: '+date)
    ax.set_xticks(index + 2*bar_width)
    ax.set_xticklabels(movies)
    ax.legend()

    fig.tight_layout()
    plt.show()
#weeklyBAR('06/04/2018',['Black Panther', 'The Sound of Water', 'The Greatest Showman','hey'],[[20, 35, 30,10],[25, 32, 34,13],[40, 25, 32,12],[10, 15, 17,10],[5, 2, 10,9]])
