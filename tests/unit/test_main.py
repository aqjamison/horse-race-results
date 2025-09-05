"""Unit tests for main module."""
import pytest
from src.main import main

@pytest.mark.unit
def test_main_raises() -> None:
    """Test that main function raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        main()