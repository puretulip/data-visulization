# Python
import pandas as pd
import datashader as ds
import hvplot.pandas  # adds hvplot method to pandas objects
import holoviews as hv
from holoviews.operation.datashader import datashade, spread, dynspread
import panel as pn
import dask.dataframe as dd

hv.extension('bokeh')

df = dd.read_parquet('./data/census2010.parq')

# Create a datashaded plot
points = hv.Points(df, ['easting', 'northing'])
datashaded = datashade(points, x_sampling=1, y_sampling=1, cmap='Viridis')

# Set the width and height of the plot
datashaded = datashaded.opts(width=1600, height=1000)
spreaded = spread(datashaded, px=2)

# Create a Panel object with the plot
panel = pn.panel(spreaded)

# Serve the Panel object
panel.servable()