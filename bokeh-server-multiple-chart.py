# Python
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure
from tornado.ioloop import IOLoop

def make_plot(doc, dataset):
    # Create a new plot
    plot = figure(title="My plot", x_axis_label='x', y_axis_label='y')

    # Add a line renderer with the given data
    plot.line(range(len(dataset)), dataset, line_width=2)

    # Add the plot to the document
    doc.add_root(plot)

# Create datasets
dataset1 = [1, 2, 3, 4, 5]
dataset2 = [5, 4, 3, 2, 1]

# Create applications
app1 = Application(FunctionHandler(lambda doc: make_plot(doc, dataset1)))
app2 = Application(FunctionHandler(lambda doc: make_plot(doc, dataset2)))

# Create a Bokeh server with the applications
server = Server({'/app1': app1, '/app2': app2}, io_loop=IOLoop.current())

# Start the Bokeh server
server.start()
server.io_loop.start()