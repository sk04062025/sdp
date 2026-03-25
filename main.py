from fastapi import FastAPI, Request
import logging

# Configure logging to print to the console
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="SDP Webhook Receiver")

@app.post("/webhook")
async def receive_webhook(request: Request):
    try:
        # Parse the JSON payload sent by ServiceDesk Plus
        payload = await request.json()
        
        # Log the raw payload
        logger.info(f"Received Webhook Payload: {payload}")
        
        # Extract specific data (based on the JSON configured in SDP)
        request_id = payload.get("request_id", "N/A")
        status = payload.get("status", "N/A")
        subject = payload.get("subject", "N/A")
        
        logger.info(f"Ticket Processed -> ID: {request_id} | Status: {status} | Subject: {subject}")
        
        # Add your custom business logic here (e.g., database updates, alerting, etc.)
        
        return {"message": "Webhook received successfully", "status": "success"}
    
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        return {"message": "Error processing webhook", "status": "error"}
