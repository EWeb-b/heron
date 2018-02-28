import matplotlib.pyplot as plt
import numpy as np


# Initial function to plot a weeks takings by each film
# When finished should be able to take a given week as
# a perameter and display the takings in a pie chart

def pie_plot_week():

    # Method to take generated
    # titles, takings = np.loadtxt('example.txt',
    #                              delimiter=',',
    #                              unpack=True)

    # Hardcoded financial info for the moment.
    titles = ['The Shape of Water', 'The Martian', 'Mad Max']
    takings = ['1320', '1222', '950']
    cols = ['c', 'r', 'b']

    # Plot the pie chart with
    plt.pie(takings,
            labels=titles,
            colors=cols,
            startangle=90,
            explode=(0, 0.1, 0),
            autopct='%1.1f%%')
    plt.axis('equal')
    plt.xlabel('Week 10')
    plt.ylabel('Takings £')
    plt.title('Weekl 10 takings\nper film')
    plt.show()


# pie_plot_week()
