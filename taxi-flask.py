# Python
from flask import Flask, render_template
from bokeh.embed import components
import pandas as pd
import datashader as ds
import hvplot.pandas  # adds hvplot method to pandas objects
import holoviews as hv
from holoviews.operation.datashader import datashade, spread, dynspread
import panel as pn

hv.extension('bokeh')

app = Flask(__name__)

@app.route('/')
def home():
    # Load the NYC taxi data into a Pandas DataFrame
    df = pd.read_csv('./data/nyc_taxi.csv')

    # Create a datashaded plot
    points = hv.Points(df, ['pickup_x', 'pickup_y'])
    datashaded = datashade(points, x_sampling=1, y_sampling=1, cmap='Viridis')

    # Set the width and height of the plot
    datashaded = datashaded.opts(width=1000, height=800)
    spreaded = spread(datashaded, px=2)

    # Create a Panel object with the plot
    panel = pn.panel(spreaded)

    # Convert the Panel object to a Bokeh model
    plot = panel.get_root()

    # Embed the Bokeh model in the HTML page
    script, div = components(plot)

    # Render the HTML page with the plot
    return render_template('index.html', script=script, div=div)

if __name__ == '__main__':
    app.run(debug=True)