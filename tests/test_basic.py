def test_pandas_import():
    import pandas as pd
    assert pd.__version__ is not None

def test_numpy_import():
    import numpy as np
    assert np.__version__ is not None

def test_environment():
    import sys
    assert sys.version_info.major == 3