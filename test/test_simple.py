import pytest

from template import template_module


def test_simple():
    assert template_module.is_true()
