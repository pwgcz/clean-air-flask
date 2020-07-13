from . import send_static


@send_static.route('/')
def index():
    return send_static.send_static_file('index.html')
