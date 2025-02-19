import tornado.ioloop
import tornado.web
import os
import requests

# all url's
fburl = 'https://www.facebook.com'
# Send a GET request to Facebook
response = requests.get(fburl)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully fetched Facebook's homepage!")
    # Print a snippet of the page content (HTML)
    print(response.text[:500])  # Print the first 500 characters of the HTML content
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
    
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
            # self.write(f"You selected: {', '.join(options)}")
            if options == "facebook":
                self.write("this may work")
        else:
            self.write("No options selected.")

        # Check and output the text values
        self.write(f"Title: {title}<br>")
        self.write(f"Intro Text: {intro_text}<br>")
        self.write(f"Main Text: {main_text}<br>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web/static"}),  # Serving static files
    ])

if __name__ == "__main__":
    # Set up the application to listen on port 4567
    app = make_app()
    app.listen(2040)
    print("Listening on port 2040")
    tornado.ioloop.IOLoop.current().start()

