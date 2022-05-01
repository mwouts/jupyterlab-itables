A tentative extension for JupyterLab that embeds the datatable.net and jquery libraries.

Inspired by https://github.com/jupyter-server/jupyter_server_mathjax

```shell
pip install -ve .
jupyter server extension enable --py itables-jupyterlab
```

After this, one can load the datatables and jquery libraries with e.g. this Python code in Jupyter Lab:
```python
from IPython.display import HTML


HTML("""
<link rel="stylesheet" type="text/css" href="/static/itables-jupyterlab/datatables.net-dt/css/jquery.dataTables.min.css">
<script type="module" src="/static/itables-jupyterlab/jquery/src/jquery.js"></script>
<script type="module" src="/static/itables-jupyterlab/datatables.net-dt/js/dataTables.dataTables.js"></script>
""")
```