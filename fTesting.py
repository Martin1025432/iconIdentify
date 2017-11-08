# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:19:18 2017

@author: Administrator
"""

# Import `skimage`
from skimage import transform
from dTrainning import*

# Load the test data
test_images, test_labels = load_data(test_data_directory)

# Transform the images to 28 by 28 pixels
test_images28 = [transform.resize(image, (128, 100)) for image in test_images]

# Convert to grayscale
from skimage.color import rgb2gray

test_images28 = rgb2gray(np.array(test_images28))
test_images28 = np.array(test_images28)
# Run predictions against the full test set.
predicted = sess.run([correct_pred], feed_dict={x: test_images28})[0]

# Calculate correct matches
match_count = sum([int(y == y_) for y, y_ in zip(test_labels, predicted)])

# Calculate the accuracy
accuracy = match_count / len(test_labels)

# Print the accuracy
print("Accuracy: {:.3f}".format(accuracy))