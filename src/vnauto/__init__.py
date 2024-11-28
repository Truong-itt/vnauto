import os
from .vnauto_score import Vnauto

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def get_vnauto_instance():
    if not os.path.exists(DATA_DIR):
        raise FileNotFoundError(f"Data directory not found: {DATA_DIR}")
    return Vnauto(DATA_DIR)
