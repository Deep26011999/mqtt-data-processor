import os
from dotenv import load_dotenv

# ✅ Load environment variables from a `.env` file if it exists
load_dotenv()

# ✅ Database Configuration (Uses Env Variables, Defaults for Local Dev)
DB_CONFIG = {
    "db_name": os.getenv("DB_NAME", "mqtt_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),  # Removed hardcoded password
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
}

# ✅ MQTT Broker Configuration
MQTT_CONFIG = {
    "broker": os.getenv("MQTT_BROKER", "localhost"),
    "port": int(os.getenv("MQTT_PORT", 1883)),
    "topic": os.getenv("MQTT_TOPIC", "sensor/#"),
}

# ✅ Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
