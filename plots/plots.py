"""
Monitoring plots
"""

import os
import pandas as pd

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models import Band
from bokeh.layouts import column

FIGWIDTH = 1200
FIGHEIGHT = 500
TITLE_FONT_SIZE = "18px"
TITLE_COLOR = "gray"
LEGEND_ALPHA = 0.8
LEGEND_LINE_WIDTH = 3
STANDARD_TOOLS = ["box_select", "pan", "wheel_zoom", "reset", "save"]
TSERIES_WIDTH = 2
TSERIES_DEFAULT_ALPHA = 0.8


def tseries():
    """Time series plots of sensor reading"""

    df = pd.read_csv("")
