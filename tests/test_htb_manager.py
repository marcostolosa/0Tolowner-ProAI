import pytest
from app.services.htb_manager import start_machine

def test_start_machine(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success"}
    mocker.patch('app.services.htb_manager.requests.post', return_value=mock_response)

    response = start_machine("meow")
    assert response["status"] == "success"