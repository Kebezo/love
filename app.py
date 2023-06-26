from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from flask_mail import Mail, Message
from redmail import outlook


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jernej.ozebek@gmail.com'
app.config['MAIL_PASSWORD'] = '5ekest4N'
mail: Mail = Mail(app)

Session(app)

outlook.username = 'jernej.ozebek@gmail.com'
outlook.password = '5ekest4N'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    flash("Termini se prekrivajo, izberite drugega", category='danger')

    return render_template('chat.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    msg = Message('Hello from Flask', sender='jernej.ozebek@gmail.com', recipients=['jernej.ozebek@gmail.com'])
    msg.body = 'This is a test email sent from Flask using Outlook as the email service provider.'
    #mail.send(msg)
    outlook.send(
        subject="Example email",
        receivers=['jernej.ozebek@gmail.com'],
        text="Hi, this is an email."
    )
    return render_template('chat.html')

if __name__ == '__main__':
    app.run()
