from fastapi import FastAPI, Request
from twilio.twiml.messaging_response import MessagingResponse

app  =  FastAPI()

@app.post("/whatsapp")
async def whatsapp_reply(request: Request):
    form_data = await request.form()
    body = form_data.get("Body", "").strip().lower()
    
    response = MessagingResponse()
    if body == "ola":
        response.message("Bem-vindo!")
    else:
        response.message("Desculpe, não entendi.")
    
    return str(response)
        