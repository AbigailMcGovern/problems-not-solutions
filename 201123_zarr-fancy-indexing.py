import zarr
import numpy as np

shape = (20, 20)
array  = zarr.zeros(shape)
idx = ([1, 2, 3], [1, 2, 3])
array[idx] = 1
