import pytest
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(currentdir)
sys.path.append(parentdir)

from mednet import MedNet


@pytest.mark.parametrize(
    "type",
    [
        (["64", 64, 6]),
        ([64, "64", 6]),
        ([64, 64, "6"]),
    ])
def test_mednet_type(type):
    with pytest.raises(TypeError):
        model = MedNet(type[0], type[1], type[2])


@pytest.mark.parametrize(
    "arguments",
    [
        ([-64, 64, 6]),
        ([64, -64, 6]),
        ([64, 64, -6]),
        ([6, 6, 6]),
    ])
def test_mednet_argumets(arguments):
    with pytest.raises(ValueError):
        model = MedNet(arguments[0], arguments[1], arguments[2])
