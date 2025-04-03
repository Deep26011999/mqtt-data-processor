import os

# ✅ Database Configuration (Default Values)
DB_CONFIG = {
    "db_name": os.getenv("DB_NAME", "mqtt_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "Deep1234"),
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
