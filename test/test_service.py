import pytest
from source import services
import unittest.mock as mock
import requests

@mock.patch("source.services.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Pukar"
    username = services.get_user_from_db(1)
    
    assert username == "Mocked Pukar"
    


#for API
@mock.patch("requests.get")

def test_get_user(mock_get):
    mock_responses = mock.Mock()
    mock_responses.status_code = 200
    mock_responses.json.return_value = {"id":1, "name":"John Doe"}
    mock_get.return_value = mock_responses
    data = services.get_user()
    assert data == {"id":1, "name":"John Doe"}
    
@mock.patch("requests.get")
def test_get_User_error(mock_get):
    mock_responses = mock.Mock()
    mock_responses.status_code = 400
    mock_get.return_value = mock_responses
    with pytest.raises(requests.HTTPError):
        services.get_user()
    
    
    
    
    
