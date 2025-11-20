import datetime
# Agregamos 'request' para poder leer los mensajes que llegan
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    # 1. CAPTURAR DATOS
    # request.values.get('Body') obtiene el texto del mensaje
    # .lower() lo convierte a minúsculas para que "Ayuda" y "ayuda" sean iguales
    mensaje_recibido = request.values.get('Body', '').lower()
    
    # 2. OBTENER HORA (Render ya sabe que es hora de Perú gracias a la variable TZ)
    ahora = datetime.datetime.now()
    hora_actual = ahora.hour
    
    # Creamos el objeto para responder
    resp = MessagingResponse()

    # 3. LÓGICA DE SUEÑO (De 10 PM a 5 AM)
    # Usamos 'or' porque la hora no puede ser mayor a 22 y menor a 5 al mismo tiempo
    if hora_actual >= 22 or hora_actual < 5:
        resp.message("Hola, estoy durmiendo 😴. En cuanto despierte responderé a tu mensaje.")
    
    # 4. LÓGICA DE DÍA (Si no está durmiendo)
    else:
        # Verificamos si el mensaje contiene palabras clave
        if 'necesito' in mensaje_recibido or 'ayuda' in mensaje_recibido:
            # RESPUESTA DE ALERTA AL REMITENTE
            resp.message("⚠️ Veo que es un tema urgente. Me llegará una notificación y trataré de responderte lo antes posible.")
            
            # NOTA DE INGENIERÍA:
            # Por ahora, el bot responde esto a la persona que escribe.
            # Para que te mande un mensaje A TI (al dueño), necesitamos configurar
            # credenciales extra (SID y Token), lo cual podemos ver en una fase futura.
            
        else:
            # Si es de día y no es urgente, no respondemos nada (respuesta vacía)
            # así puedes chatear normal sin que el bot interrumpa.
            pass

    return str(resp)