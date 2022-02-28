import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import curdoc

class CommentPlotter:
    """ A class to plot the sentiment of comments through the duration
    of a Reddit thread

    Attributes
    ----------
    comments_df : dict
        Holds comment information
    """

    def __init__(self, comments):
        try:
            self.comments_df = pd.DataFrame(
                comments, 
                columns=comments.keys()).sort_values(by=["times"])
        except:
            raise ValueError("Could not create a DataFrame from the given input")

    def create_plot(self):
        """ Plots the sentiment of a thread and opens the plot in a browser
        """
        plot = figure(title="Sentiment Through Time", x_axis_label="Time", y_axis_label="Sentiment")
        
        try:
            plot.line(self.comments_df["times"], self.comments_df["polarities"])
        except:
            raise ValueError("DataFrame does not have required fields")

        curdoc().theme = "dark_minimal"

        show(plot)
