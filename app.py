import datetime
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    ahora = datetime.datetime.now()
    
    # Verificamos si es hora de dormir (después de las 10 PM)
    if ahora.hour >= 22:
        resp = MessagingResponse()
        resp.message('Hola, ahora estoy durmiendo')
        return str(resp)
        
    return str(MessagingResponse()) # Respuesta vacía si es de día
if __name__ == '__main__':
    app.run(debug=True)