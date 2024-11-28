import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Render the index.html file when a GET request is made to the root URL
        self.render("web/index.html")

    def post(self):
        # Handle POST request and retrieve the 'title' argument
        options = self.get_arguments("options")  # Returns a list of selected options
        # title = self.get_arguments("title")
        # If any options were selected, display them
        if options:
            self.write(f"You selected: {', '.join(options)}")
        else:
            self.write("No options selected.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web/static"}),  # Serving static files
    ])

if __name__ == "__main__":
    # Set up the application to listen on port 4567
    app = make_app()
    app.listen(4567)
    print("Listening on port 4567")
    tornado.ioloop.IOLoop.current().start()
