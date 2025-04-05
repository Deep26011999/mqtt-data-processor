# 📦 mqtt-processor-deep

[![PyPI version](https://badge.fury.io/py/mqtt-processor-deep.svg)](https://badge.fury.io/py/mqtt-processor-deep)
[![Build Status](https://github.com/yourusername/mqtt-data-processor/actions/workflows/python-package.yml/badge.svg)](https://github.com/yourusername/mqtt-data-processor/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight and extensible Python package for processing MQTT messages and storing them in PostgreSQL. Ideal for IoT data pipelines, sensor networks, and real-time applications.

---

## ✨ Features

- 🔗 MQTT broker integration
- 🛠️ Plug-and-play message transformations
- 🗃️ PostgreSQL message storage
- ✅ Clean, testable architecture
- 🧪 Built-in pytest compatibility
- 🐳 Docker-friendly

---

## 📦 Installation

From PyPI:

```bash
pip install mqtt-processor

git clone https://github.com/Deep26011999/mqtt-data-processor.git
cd mqtt-data-processor
pip install .

🚀 Basic Usage

from mqtt_processor_deep.client import MQTTClient

client = MQTTClient()
client.start()

# Your app logic here

client.stop()


🔄 Custom Message Transformation

def uppercase_payload(topic, payload):
    return topic, payload.upper()

client = MQTTClient(process_function=uppercase_payload)
client.start()


⚙️ Configuration
You can configure MQTT and PostgreSQL either via environment variables or by editing the default config.py.


# MQTT
export MQTT_BROKER="localhost"
export MQTT_PORT=1883
export MQTT_TOPIC="sensor/#"

# PostgreSQL
export DB_HOST="localhost"
export DB_PORT=5432
export DB_NAME="mqtt_db"
export DB_USER="your_user"
export DB_PASSWORD="your_password"


🧪 Running Tests
Install development requirements:


pip install -r requirements-dev.txt
Run all tests:


pytest tests/
To test a specific file:


pytest tests/test_client.py


📁 Project Structure
arduino
Copy
Edit
mqtt-data-processor/
├── src/
│   └── mqtt_processor_deep/
│       ├── __init__.py
│       ├── client.py
│       ├── config.py
│       ├── db_connector.py
│       ├── processor.py
│       └── utils.py
├── tests/
│   └── test_client.py
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md

🔐 Security
Always store sensitive credentials like database passwords in environment variables or secure vaults — avoid hardcoding them in config.py.

📜 License
MIT © [Deep Shikhar Singh]
See LICENSE for details.

🙌 Contributing
Contributions are welcome! Feel free to open issues or pull requests.
If you find this project helpful, give it a ⭐ on GitHub!


🌍 Links
📦 PyPI: mqtt-processor-deep

🛠️ GitHub Repo
