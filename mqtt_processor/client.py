import paho.mqtt.client as mqtt
from mqtt_processor.db_connector import PostgreSQLConnector
from mqtt_processor.processor import MessageProcessor
from mqtt_processor.utils import log_info, log_error  # ✅ Import logging functions

class MQTTClient:
    def __init__(self, broker="localhost", port=1883, topic="sensor/#", db_config=None, process_function=None):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.db = PostgreSQLConnector(**db_config) if db_config else None
        self.client = mqtt.Client()

        # ✅ Initialize the processor and add user-defined function if provided
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

            # ✅ Always process messages through MessageProcessor
            processed_topic, processed_payload = self.processor.process_message(msg.topic, payload)

            if self.db:
                self.db.insert_message(processed_topic, processed_payload)
                log_info(f"✅ Stored message in database: {processed_topic} -> {processed_payload}")

        except Exception as e:
            log_error(f"❌ Error processing message: {e}")

    def start(self):
        log_info("🚀 Starting MQTT Client...")
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def stop(self):
        log_info("🛑 Stopping MQTT Client...")
        self.client.loop_stop()
        self.client.disconnect()
        if self.db:
            self.db.close()
