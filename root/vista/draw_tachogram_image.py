import io
from root.controller.generate_image.generate_tachogram_figure import generate_tachogram_image
from root import constants
def draw_tachogram_image(tachograms_list, window):
    image = generate_tachogram_image(tachograms_list)

    image.thumbnail((constants.THUMBNAIL_TACHOGRAM_PLOT_WIDTH, constants.THUMBNAIL_TACHOGRAM_PLOT_HEIGHT))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window[constants.IMAGE_KEY].update(data=bio.getvalue())

    return image

