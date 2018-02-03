def create_controllers(app):
    @app.route('/')
    def index():
        return "Hello World"
