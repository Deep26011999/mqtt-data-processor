import psycopg2
from psycopg2.extras import DictCursor

class PostgreSQLConnector:
    def __init__(self, db_name, user, password, host='localhost', port=5432, table_name="mqtt_messages", table_schema=None):
        """Initialize PostgreSQL connection and create table if needed"""
        self.table_name = table_name
        try:
            self.conn = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cur = self.conn.cursor(cursor_factory=DictCursor)
            self._create_table(table_schema)
        except Exception as e:
            print(f"❌ Error connecting to PostgreSQL: {e}")

    def _create_table(self, table_schema=None):
        """Create a table based on user-provided or default schema"""
        try:
            if table_schema is None:
                # Default table schema
                table_schema = f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id SERIAL PRIMARY KEY,
                    topic TEXT NOT NULL,
                    payload JSONB NOT NULL,
                    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            self.cur.execute(table_schema)
            self.conn.commit()
            print(f"✅ Table '{self.table_name}' is ready!")
        except Exception as e:
            print(f"❌ Error creating table: {e}")

    def insert_message(self, topic, payload):
        """Insert an MQTT message into the database"""
        try:
            insert_query = f"INSERT INTO {self.table_name} (topic, payload) VALUES (%s, %s)"
            self.cur.execute(insert_query, (topic, payload))
            self.conn.commit()
            print(f"✅ Message inserted into {self.table_name}")
        except Exception as e:
            print(f"❌ Error inserting message: {e}")

    def fetch_messages(self, limit=10):
        """Fetch the latest MQTT messages"""
        try:
            self.cur.execute(f"SELECT * FROM {self.table_name} ORDER BY received_at DESC LIMIT %s", (limit,))
            return self.cur.fetchall()
        except Exception as e:
            print(f"❌ Error fetching messages: {e}")
            return []

    def close(self):
        """Close the database connection"""
        self.cur.close()
        self.conn.close()
