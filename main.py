from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "WhatsApp Bot is live!"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Received message:", data)
    
    # For now just send a dummy response
    return {"reply": "Thanks for your message! Bot is under setup."}
