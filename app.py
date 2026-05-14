from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# CONFIGURA TU EMAIL AQUI
TU_EMAIL = "lframosc@gmail.com"
TU_PASSWORD = "AQUI_TU_PASSWORD_DE_APP"  # No tu password normal, sino una "App Password"
DESTINO = "lframosc@gmail.com"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form.get("name")
        contacto = request.form.get("contact")
        mensaje = request.form.get("message")

        cuerpo = f"""
Nuevo mensaje desde tu landing page:

Nombre: {nombre}
Contacto: {contacto}

Mensaje:
{mensaje}
"""

        msg = MIMEText(cuerpo)
        msg["Subject"] = "Nuevo mensaje desde tu página web"
        msg["From"] = TU_EMAIL
        msg["To"] = DESTINO

        # Enviar correo
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(TU_EMAIL, TU_PASSWORD)
            server.sendmail(TU_EMAIL, DESTINO, msg.as_string())

        return "Mensaje enviado. Gracias por contactarnos."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
