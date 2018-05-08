"""
This module provides functionality for plotting in jupyter (http://jupyter.org/) notebooks
based on dygraphs (http://dygraphs.com/) and pandas (https://pandas.pydata.org/).
"""
import uuid

from IPython.display import HTML

def dygraphplot(dataframe, title="", xlabel="", ylabel="", legend="always"):
    html="""
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/dygraph/2.1.0/dygraph.min.css">
    <div id="{0}"></div>
    <script type="text/javascript">
        requirejs.config({{
            paths: {{
                "Dygraph": ["//cdnjs.cloudflare.com/ajax/libs/dygraph/2.1.0/dygraph.min"]
            }}
        }});

        require(['Dygraph'], function(Dygraph){{
            new Dygraph(document.getElementById("{0}"), "{1}", {{title: "{2}", xlabel: "{3}", ylabel: "{4}", legend: "{5}"}})
        }})
    </script>
    """.format(uuid.uuid4(), dataframe.to_csv(index=False).replace("\n", "\\n\"+\""), title, xlabel, ylabel, legend)

    return HTML(html)
