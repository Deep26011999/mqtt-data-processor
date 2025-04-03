from setuptools import setup, find_packages

setup(
    name="mqtt_processor",  # Package name (should match your import name)
    version="0.1.0",  # Version number
    author="Deep Shikhar Singh",
    author_email="deepshikharsingh@gmail.com",
    description="A Python package for real-time MQTT data processing with database integration",
    long_description=open("README.md").read(),  # Uses README for PyPI description
    long_description_content_type="text/markdown",
    url="https://github.com/Deep26011999/mqtt-data-processor",  # Replace with your GitHub repo
    packages=find_packages(),  # Automatically finds all Python packages
    install_requires=[
        "paho-mqtt==2.1.0",
        "psycopg2==2.9.10",
        "python-dotenv==1.1.0",
        "dnspython==2.7.0",
    ],  # Dependencies (should match requirements.txt)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version
)
