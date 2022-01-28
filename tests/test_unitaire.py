import pytest
import io
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(currentdir)
sys.path.append(parentdir)

from predict import *
from imgs import *


@pytest.mark.parametrize(
    "img",
    [
        ([IMG1, TARGET1]),
        ([IMG2, TARGET2]),
        ([IMG3, TARGET3]),
    ])
def test_link(img):
    assert link(io.BufferedReader(io.BytesIO(img[0]))) == img[1]

@pytest.mark.parametrize(
    "img",
    [
        ([IMG1, CLASS1]),
        ([IMG2, CLASS2]),
        ([IMG3, CLASS3]),
    ])
def test_predict(img):
    assert predict(io.BufferedReader(io.BytesIO(img[0]))) == img[1]
