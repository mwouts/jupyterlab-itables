from .app import DataTablesExtension


def _jupyter_server_extension_points():
    return [
        {"module": "itables-jupyterlab", "app": DataTablesExtension},
    ]
