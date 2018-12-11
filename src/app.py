import cherrypy

cherrypy.config.update({'server.socket_host' : '127.0.0.1', 'server.socket_port': 10001})


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"


if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
