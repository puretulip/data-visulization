# Python
import datashader as ds
import datashader.transfer_functions as tf
import pandas as pd
import dask.dataframe as dd
import colorcet as cc
import numpy as np

# Load your data into a DataFrame
df = dd.read_parquet('./data/census2010.parq')

# Compute the minimum and maximum values for easting and northing
xmin, ymin, xmax, ymax = df['easting'].min().compute(), df['northing'].min().compute(), df['easting'].max().compute(), df['northing'].max().compute()

# Define the number of levels
num_levels = 4

# For each level of detail
for i in range(num_levels):
    # Calculate the number of tiles per side for this level
    tiles_per_side = 2**i

    # Calculate the size of each tile
    tile_size_x = (xmax - xmin) / tiles_per_side
    tile_size_y = (ymax - ymin) / tiles_per_side

    # For each tile
    for x in range(tiles_per_side):
        for y in range(tiles_per_side):
            # Calculate the range for this tile
            x_range = (xmin + x * tile_size_x, xmin + (x + 1) * tile_size_x)
            y_range = (ymin + y * tile_size_y, ymin + (y + 1) * tile_size_y)

            # Use Datashader to create an image of the data points in this range
            cvs = ds.Canvas(x_range=x_range, y_range=y_range, plot_width=256, plot_height=256)
            agg = cvs.points(df, 'easting', 'northing')
            # img = tf.shade(agg, cmap=cc.fire)
            img = tf.shade(agg, cmap=cc.fire, how='eq_hist')

            # Save the image to a file
            img.to_pil().save(f'./images/level_{i}_tile_{x}_{y}.png')