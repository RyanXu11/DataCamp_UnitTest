import pytest
import numpy as np
from features.as_numpy import get_data_as_numpy_array
import sys              # added in 3.9

""" comments on 4.3 and test the part from import os
class TestGetDataAsNumpyArray(object):
    # Mark as skipped if Python version is greater than 2.7, these 2 lines added in 3.9
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="Works only on Python 2.7 or lower")
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array("example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, actual)
        assert actual == pytest.approx(expected), message
"""

import os

@pytest.fixture
def clean_data_file():
    file_path = "clean.txt"
    with open(file_path, "w") as f:
        f.write("201\t305671\n7892\t298140\n501\t738293\n")
    yield file_path
    os.remove(file_path)

@pytest.fixture
def empty_file():
    file_path = "empty.txt"
    open(file_path, "w").close()
    yield file_path
    os.remove(file_path)

class TestGetDataAsNumpyArray(object):
    def test_on_clean_file(self, clean_data_file):
        expected = np.array([[201.0, 305671.0], [7892.0, 298140.0], [501.0, 738293.0]])
        actual = get_data_as_numpy_array(clean_data_file, 2)
        assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual) 

    def test_on_empty_file(self, empty_file):
        expected = np.empty((0, 2))
        actual = get_data_as_numpy_array(empty_file, 2)
        assert actual == pytest.approx(expected), "Expected: {0}, Actual: {1}".format(expected, actual)
