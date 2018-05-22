"""
This module provides functionality for plotting in jupyter (http://jupyter.org/) notebooks
based on dygraphs (http://dygraphs.com/) and pandas (https://pandas.pydata.org/).
"""
import json
import uuid
import pandas

from IPython.display import HTML

def dygraphplot(*dataframe, options={"legend":"always"}):
    """
    Plots the given dataframe in a jupyter notebook cell.

    Keyword arguments:
        dataframe: The input data for the plot. The first column contains the x-axis data, while
        the remaining columns contain the series data. All columns except the first one needs to
        be parseable to numeric.

        options: A dict containing the dygraph config options.
    """
    html = """
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/dygraph/2.1.0/dygraph.min.css">
    """
    for df in dataframe:
        # Check all but the first columns. According to dygraphs spec, these columns must contain
        # numeric values.
        for col in df.columns.values[1:]:
            try:
                pandas.to_numeric(df[col])
            except:
                raise Exception("Dataframe contains non-numeric column: {}".format(col))

        html = html+"""
        <div id="{0}"></div>
        <script type="text/javascript">
            requirejs.config({{
                paths: {{
                    "Dygraph": ["//cdnjs.cloudflare.com/ajax/libs/dygraph/2.1.0/dygraph.min"]
                }}
            }});

            require(['Dygraph'], function(Dygraph){{
                new Dygraph(document.getElementById("{0}"), "{1}", {2})
            }})
        </script>
        """.format(
            uuid.uuid4(),
            df.to_csv(index=False).replace("\n", "\\n\"+\""),
            json.dumps(options)
        )

    return HTML(html)
