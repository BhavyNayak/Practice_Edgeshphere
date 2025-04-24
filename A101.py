# 101. Use environment variables in Python.
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("API_KEY"))
