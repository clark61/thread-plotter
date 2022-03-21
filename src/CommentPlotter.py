import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Range1d
from bokeh.layouts import column
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
        """ Plots the sentiment of a thread and opens the plot in a browser """
        
        self.comments_df = self.comments_df.groupby(pd.Grouper(key="datetimes", freq="30s")).agg({
            "times": "count", 
            "subjectivities": "mean", 
            "polarities": "mean"})
        self.comments_df = self.comments_df.dropna()
        
        source = ColumnDataSource(self.comments_df)
        sentiment_plot = figure(
            title="Mean Sentiment of Comments per 30s Interval", 
            x_axis_label="Time", 
            x_axis_type="datetime", 
            y_axis_label="Sentiment", 
            y_range=Range1d(-1, 1), 
            plot_width=1000, 
            plot_height=550)

        count_plot = figure(
            title="Count of Comments per 30s Interval", 
            x_axis_label="Time", 
            x_axis_type="datetime", 
            y_axis_label="Count", 
            plot_width=1000, 
            plot_height=550)

        try:
            sentiment_plot.line(x="datetimes", y="polarities", source=source)
            count_plot.line(x="datetimes", y="times", source=source)
        except:
            raise ValueError("DataFrame does not have required fields")

        curdoc().theme = "dark_minimal"

        columns = column(sentiment_plot, count_plot)
        columns.sizing_mode = "scale_width"
        show(columns)
