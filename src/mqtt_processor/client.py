import paho.mqtt.client as mqtt
from mqtt_processor.db_connector import PostgreSQLConnector
from mqtt_processor.processor import MessageProcessor
from mqtt_processor.utils import log_info, log_error
from mqtt_processor.config import MQTT_CONFIG, DB_CONFIG

class MQTTClient:
    def __init__(self, db_config=DB_CONFIG, process_function=None):
        # Use dynamic config loading via environment variables or default values
        self.broker = MQTT_CONFIG.get("broker", "localhost")
        self.port = MQTT_CONFIG.get("port", 1883)
        self.topic = MQTT_CONFIG.get("topic", "sensor/#")
        self.db = PostgreSQLConnector(**db_config) if db_config else None
        self.client = mqtt.Client()

        self.processor = MessageProcessor()
        if process_function:
            self.processor.add_transformation(process_function)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log_info(f"✅ Connected to MQTT broker at {self.broker}:{self.port}")
            self.client.subscribe(self.topic)
        else:
            log_error(f"❌ Connection failed with code {rc}")

    def on_message(self, client, userdata, msg):
        try:
            payload = msg.payload.decode("utf-8")
            log_info(f"📥 Received message: {msg.topic} -> {payload}")

            # ✅ Process messages using the MessageProcessor
            processed_topic, processed_payload = self.processor.process_message(msg.topic, payload)

            if self.db:
                self.db.insert_message(processed_topic, processed_payload)
                log_info(f"✅ Stored message in database: {processed_topic} -> {processed_payload}")

        except Exception as e:
            log_error(f"❌ Error processing message: {e}")

    def start(self):
        """ User must call this explicitly to start the client """
        log_info("🚀 Starting MQTT Client...")
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def stop(self):
        """ User must call this explicitly to stop the client """
        log_info("🛑 Stopping MQTT Client...")
        self.client.loop_stop()
        self.client.disconnect()
        if self.db:
            self.db.close()
