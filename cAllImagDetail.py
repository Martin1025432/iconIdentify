# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:12:11 2017

@author: Administrator
"""

# Import the `pyplot` module as `plt`
import matplotlib.pyplot as plt
from aLoadImag_preProcess import*

# Get the unique labels
unique_labels = set(labels)

# Initialize the figure
plt.figure(figsize=(15, 15))

# Set a counter
i = 1

# For each unique label,
for label in unique_labels:
    # You pick the first image for each label
    image = images28[labels.index(label)]
    # Define 64 subplots
    plt.subplot(3, 3, i)

    # Don't include axes
    plt.axis('off')

    # Add a title to each subplot
    plt.title("Label {0} ({1})".format(label, labels.count(label)))

    # Add 1 to the counter
    i += 1

    # And you plot this first image
    plt.imshow(image)

# Show the plot
plt.show()