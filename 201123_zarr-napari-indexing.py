import napari
import zarr
from skimage.data import coins

save_path = 'labels'
image = coins()
shape = image.shape
labels = zarr.open_array(
                         save_path, 
                         mode='w', 
                         shape=shape,
                         chunks=None, 
                         fill_value=0
                         )

with napari.gui_qt():
    v = napari.Viewer()
    v.add_image(image)
    v.add_labels(labels)