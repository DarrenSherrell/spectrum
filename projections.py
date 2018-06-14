import file_scraper as fs
from map_hdf5 import *
from emissions import get_emissions
import matplotlib.pyplot as plt



r1 = fs.get_h5py_data('/dls/i24/data/2017/nr16818-47/GoldDigger_170512/Cgrid_2/Cgrid_2_23_zlayer_1.hdf5')
r2 = fs.get_h5py_data('/dls/i24/data/2017/nr16818-47/GoldDigger_170512/Cgrid_2/Cgrid_2_24_zlayer_1.hdf5')
r3 = fs.get_h5py_data('/dls/i24/data/2017/nr16818-47/GoldDigger_170512/Cgrid_2/Cgrid_2_25_zlayer_1.hdf5')

xdim, ydim, x_step_size, y_step_size, x_start, y_start = file_scraper.get_gridscan_data('/dls/i24/data/2017/nr16818-47/GoldDigger_170512/Cgrid_2/Cgrid_2_23_zlayer_1.hdf5')

shp_array1 = shape_array(r1, [xdim,ydim])
shp_array2 = shape_array(r2, [xdim,ydim])
shp_array3 = shape_array(r3, [xdim,ydim])

shp_array = ((shp_array1 + shp_array2 + shp_array3) / 3)# - 0.04

per_tab_dict = fs.get_per_tab_dict()
emission_line = get_emissions(per_tab_dict, 'Au')
llm, hlm = emission_line[1], emission_line[2]
slc_array = slice_and_sum_array(shp_array, [llm, hlm])
print '---------------> slice', slc_array.sum()

hx = slc_array.sum(axis=0)
hy = slc_array.sum(axis=1)

ax = plt.subplot()
ax.plot(hx)
ax.plot(hy)
ax.plot((hx+hy))
plt.show()

