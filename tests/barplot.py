from myutils.utils import barplot, barplot_autolabel
# import matplotlib.pyplot as plt

if __name__ == "__main__":
    means = [[20, 35, 30, 35, 27], [25, 32, 34, 20, 25], [27, 30, 32, 25, 22]] # asian, american, african
    # std = [[2, 3, 4, 1, 2], [3, 5, 2, 3, 3], [1, 3, 2, 1, 3]] # std (conf. inter.) of above; give None if not avail.
    std = None
    width = 0.2 # width of barplots
    xticklabels = ['BS=128', 'BS=256', 'BS=512', 'BS=1024', 'BS=2048', 'BS=4096']
    ylabel = 'Performance Metric'
    legend = 'Recall@20', 'Precision@20', 'NDCG@20'
    title = 'Hyperparameter tuning for batch size (BS)'
    rects, fig, ax, plt = barplot(means, width, xticklabels, ylabel, legend, std, title)

    # placing text above barplots (center, left - left of std line, right - right of std line)
    xpos = ['center', 'center', 'center']
    for i in range(len(legend)):
        barplot_autolabel(rects[i], ax, xpos[i])

    fig.tight_layout()

    plt.show()
