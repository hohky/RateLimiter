from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Configurar o Limiter usando o endereço IP do cliente para identificação
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["5 per second"]
)

# Anexar o limiter ao app Flask
limiter.init_app(app)

@app.route('/')
@limiter.limit("5 per second")
def index():
    return "Hello, World!"

@app.errorhandler(429)
def ratelimit_handler(e):
    return "Too Many Requests", 429

if __name__ == '__main__':
    app.run()
