if __package__ == '': 
    # first dirname call strips of '/__main__.py', second strips off '/src'
    # Resulting path is the name of the wheel itself
    # Add that to sys.path so we can import src
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

import src  # noqa

