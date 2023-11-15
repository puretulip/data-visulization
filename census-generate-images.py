# Python
import datashader as ds
import datashader.transfer_functions as tf
import pandas as pd
import dask.dataframe as dd
import colorcet as cc

# Load your data into a DataFrame
df = dd.read_parquet('./data/census2010.parq')

# Compute the minimum and maximum values for easting and northing
xmin, ymin, xmax, ymax = df['easting'].min().compute(), df['northing'].min().compute(), df['easting'].max().compute(), df['northing'].max().compute()

# Define the number of levels and the range for each level
num_levels = 4
ranges = [(xmin, xmax, ymin, ymax) for _ in range(num_levels)]

# For each level of detail
for i in range(num_levels):
    # Define the range for this level
    x_range, y_range = (ranges[i][0], ranges[i][1]), (ranges[i][2], ranges[i][3])

    # Use Datashader to create an image of the data points in this range
    cvs = ds.Canvas(x_range=x_range, y_range=y_range)
    agg = cvs.points(df, 'easting', 'northing')
    img = tf.shade(agg, cmap=cc.fire)

    # Save the image to a file
    img.to_pil().save(f'./images/level_{i}.png')