import logging
import time

# 1. Configure standard logging (The "Old Way")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger("payment_service")

def process_payment(user_id, amount):
    logger.info(f"Processing payment for user_id={user_id} amount={amount}")
    
    try:
        # Simulate an error
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        
        # Simulate successful processing
        time.sleep(0.1)
        logger.info(f"Payment successful for user_id={user_id}")
        
    except Exception as e:
        # The Issue: Passing a dictionary or extra context often gets stringified 
        # awkwardly or requires custom formatting strings.
        context = {"user_id": user_id, "amount": amount, "currency": "USD"}
        logger.error(f"Payment failed: {e} Context: {context}", exc_info=True)

if __name__ == "__main__":
    logger.info("Starting payment processing...")
    process_payment(12345, 99.99)
    process_payment(67890, -50.00)
    logger.info("Finished processing.")