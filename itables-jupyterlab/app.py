from pathlib import Path
from jupyter_server.extension.application import ExtensionApp

STATIC_ASSETS_PATH = Path(__file__).parent / "static"

class DataTablesExtension(ExtensionApp):

    name = "itables-jupyterlab"

    # By listing the path to the assets here, jupyter_server
    # automatically creates a static file handler at
    # /static/itables-jupyterlab/...
    static_paths = [str(STATIC_ASSETS_PATH)]
