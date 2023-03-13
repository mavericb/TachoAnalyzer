from root.controller.utils.fig2img import fig2img

def generate_tachogram_image(tachograms_list):
    plot_figure = generate_tachogram_plot(tachograms_list)
    image = fig2img(plot_figure)
    return image

def generate_tachogram_plot(tachograms_list):
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    #tachograms_list = tachograms_list[0:100]
    x = list(range(0, len(tachograms_list)))
    y = tachograms_list

    fig = plt. figure()
    plt.plot(x, y, linewidth=2.0)
    plt.ylabel('Interval length in ms', fontsize='xx-small', labelpad=5)
    plt.xlabel('Interval Number', fontsize='xx-small', labelpad=5)

    return fig