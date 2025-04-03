class MessageProcessor:
    def __init__(self, transformations=None):
        """
        Initialize the processor with optional transformations.
        :param transformations: A list of functions that modify the incoming message.
        """
        self.transformations = transformations if transformations else []

    def add_transformation(self, transform):
        """
        Add a new transformation function dynamically.
        :param transform: A function that takes (topic, payload) and returns (topic, payload).
        """
        self.transformations.append(transform)

    def process_message(self, topic: str, payload: str):
        """
        Apply all transformations to the message before storing it.
        :param topic: MQTT topic
        :param payload: Message payload
        :return: Transformed topic and payload
        """
        for transform in self.transformations:
            topic, payload = transform(topic, payload)  # Apply each transformation in order
        return topic, payload
