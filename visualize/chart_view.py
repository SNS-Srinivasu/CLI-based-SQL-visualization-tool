import plotext as plt

def bar_chart(x, y, title="Chart"):
    plt.clear_data()
    plt.bar(x, y)
    plt.title(title)
    plt.show()

