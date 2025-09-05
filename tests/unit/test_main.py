"""Test suite for main module."""
import pytest
from src.main import main

def test_main_raises_not_implemented():
    """Test that main function raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        main()