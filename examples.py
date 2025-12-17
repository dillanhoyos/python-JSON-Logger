import logging
import sys
from datetime import datetime
from json_logger import JSONFormatter

def setup_logger(name, include_fields=None):
    """Helper to create a logger with our JSONFormatter"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Avoid adding multiple handlers if setup is called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        # Configure the formatter
        formatter = JSONFormatter(include_fields=include_fields)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

def run_basic_example():
    print("--- Basic Usage ---")
    logger = setup_logger("basic_app")
    
    logger.info("Application started")
    logger.warning("Disk space low", extra={"disk_space": "10%", "mount": "/var"})
    logger.info("User login", extra={"user_id": 42, "ip": "192.168.1.1"})

def run_exception_example():
    print("\n--- Exception Handling ---")
    logger = setup_logger("error_app")
    
    try:
        # Simulate a crash
        x = 1 / 0
    except ZeroDivisionError:
        logger.error("Calculation failed", exc_info=True, extra={"input_value": 0})

def run_configuration_example():
    print("\n--- Configuration: Including Process & Thread IDs ---")
    # Enable process and thread fields
    logger = setup_logger("system_app", include_fields={"process", "thread", "taskName"})
    
    logger.info("Processing data in worker", extra={"job_id": "job-123"})

def run_complex_types_example():
    print("\n--- Complex Types (Datetime, Objects) ---")
    logger = setup_logger("complex_app")
    
    class User:
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return f"User({self.name})"
            
    context = {
        "event_time": datetime.now(),
        "users": [User("Alice"), User("Bob")],
        "metadata": {"version": 1.0, "active": True}
    }
    
    logger.info("Complex data logged", extra=context)

if __name__ == "__main__":
    run_basic_example()
    run_configuration_example()
    run_complex_types_example()
    run_exception_example()

