from unittest.mock import MagicMock, patch
from mqtt_processor.client import MQTTClient

@patch("mqtt_processor.client.log_info")
@patch("mqtt_processor.client.log_error")
def test_on_message_success(mock_log_error, mock_log_info):
    # Create a fake message
    msg = MagicMock()
    msg.payload.decode.return_value = "temperature: 25"
    msg.topic = "sensor/temp"

    client = MQTTClient()
    
    # Mock the processor and DB
    client.processor.process_message = MagicMock(return_value=("sensor/temp", "processed: 25"))
    client.db = MagicMock()
    client.db.insert_message = MagicMock()

    # Call the on_message handler
    client.on_message(client.client, None, msg)

    client.processor.process_message.assert_called_once_with("sensor/temp", "temperature: 25")
    client.db.insert_message.assert_called_once_with("sensor/temp", "processed: 25")

    # Optional: Check logging
    assert any("📥 Received message" in str(call) for call in mock_log_info.call_args_list)
    assert any("✅ Stored message in database" in str(call) for call in mock_log_info.call_args_list)

    mock_log_error.assert_not_called()
