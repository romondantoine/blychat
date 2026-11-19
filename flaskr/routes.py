from flask import Flask

def deploy_routes(server: Flask):
    """ Déclare les routes du serveur Flask. """

    @server.route("/")
    def home_page():
        return "Hello World!"
