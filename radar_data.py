pcd_file = 'data/v1.0-mini/sweeps/RADAR_FRONT/n008-2018-08-01-15-16-36-0400__RADAR_FRONT__1533151603630245.pcd'



# from pyntcloud import PyntCloud

# # Path to the .pcd file
# pcd_file = 'data/v1.0-mini/sweeps/RADAR_FRONT/n008-2018-08-01-15-16-36-0400__RADAR_FRONT__1533151603630245.pcd'

# # Load the .pcd file using PyntCloud
# cloud = PyntCloud.from_file(pcd_file)

# # Print the data
# print(cloud.points)


from pypcd import pypcd
import numpy as np
pc = pypcd.PointCloud.from_path(pcd_file)
pc_data = pc.pc_data
print(pc_data[0])
print("------------------------------------")
pc_array = np.array([pc_data["x"], pc_data["y"], pc_data["z"]], dtype=np.float32)
print(pc_array.shape)