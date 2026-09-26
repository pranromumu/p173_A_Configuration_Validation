import sys
import os
sys.path.insert(0, os.path.dirname(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from framework.config.settings import Settings

def test_valid_configuration():
    settings = Settings()
    settings.validate()
def test_enpty_base_url_failes():
    settings = Settings(BASE_URL="")
    with pytest.raises(ValueError,match="BASE_URL cannot be empty"):
        settings.validate()
def test_invalid_browser_failes():
    settings = Settings(BROWSER="chrome123")
    with pytest.raises(ValueError,match="BROWSER must be one of"):
        settings.validate()
def test_nevigate_timeout_fails():
    settings = Settings(TIMEOUT=-500)
    with pytest.raises(ValueError, match="TIMEOUT must be an integer greater than 0"):
        settings.validate()
def test_multiple_invalid_configurations():
    settings = Settings(
        BASE_URL="",
        BROWSER="chrome123",
        HEADLESS="yes",
        TIMEOUT=-500
    )
    with pytest.raises(ValueError) as exc_info:
        settings.validate()

    error_message = str(exc_info.value)

    assert "BASE_URL cannot be empty" in error_message
    assert "BROWSER must be one of" in error_message
    assert "HEADLESS must be a boolean" in error_message
    assert "TIMEOUT must be an integer greater than 0" in error_message


