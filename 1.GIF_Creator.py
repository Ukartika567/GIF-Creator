

from moviepy.editor import *

# Convert video to GIF(Graphical Interchange format)
'''
# loading video clip 
v_clip = VideoFileClip('VIP.mp4')


#getting only 2 sec from video clip
v_clip = v_clip.subclip(0,2) 
# v_clip = v_clip.add_mask()

# Saving video clip as our gif
v_clip.write_gif('VIP_Engineer.gif')

'''

# Convert Png to gif using imageio 

import os
import imageio

png_directory = '../Graphics/png_dir'
images_list = []

for file_name in sorted(os.listdir(png_directory)):
    if file_name.endswith('.jpg'):
        file_path = os.path.join(png_directory, file_name)
        # print(file_path)
        images_list.append(imageio.imread(file_path))
    imageio.mimsave('mygif.gif', images_list, duration=0.4)    



# print(sorted(os.listdir(png_directory)))