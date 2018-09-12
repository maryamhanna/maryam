# orginally taken from udacity nanodegree for self-driving cars: part1:
# lesson3: part 4
# with my own personal modifications 
# import necessary libraries: matplotlib and numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# read in the image and print out some stats
image = mpimg.imread('test.jpg')
print('This image is: ', type(image), 'with dimensions: ', image.shape)

# grab the x and y size and make copy of image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)

# define our color selection criteria
# rgb_threshold = [red_threshold, green_threshold, blue_threshold]
rgb_thres = [200, 200, 200]

# identiy pixels below threshold
threshold = (image[:,:,0] < rgb_thres[0]) /            
	| (image[:,:,1] < rgb_thres[1]) /            
	| (image[:,:,2] < rgb_thres[2]) 
color_select[threshold] = [0,0,0]

# display the image and save it
plt.imshow(color_select)
plt.show()
mpimg.imsave("test-after.png", color_select)

# I tried to run this with one of data-set images and it didn't work as desired

