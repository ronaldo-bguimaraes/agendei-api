from flask import Flask

from controller.test_controller import test
from controller.user_controller import user

app = Flask(__name__)

app.register_blueprint(test, url_prefix='/')
app.register_blueprint(user, url_prefix='/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
