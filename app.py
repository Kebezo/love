from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from flask_mail import Mail, Message

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jo3592@student.uni-lj.si'
app.config['MAIL_PASSWORD'] = '5ekest4N'
mail: Mail = Mail(app)

Session(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    flash("Termini se prekrivajo, izberite drugega", category='danger')

    return render_template('chat.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    msg = Message('Hello from Flask', sender='jo3592@student.uni-lj.si', recipients=['jo3592@student.uni-lj.si'])
    msg.body = 'This is a test email sent from Flask using Outlook as the email service provider.'
    #mail.send(msg)

    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)