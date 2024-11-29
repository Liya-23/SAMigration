import tornado.ioloop
import tornado.web
import os
import requests
import webbrowser  # Import the webbrowser module
import time

# All URLs and their respective platform names
social_urls = {
    "Post Haven": 'https://posthaven.com/',
    "Facebook": 'https://www.facebook.com',
    "Pinterest": 'https://za.pinterest.com/',
    "Instagram": 'https://www.instagram.com/',
    "LinkedIn": 'https://www.linkedin.com',
    "Twitter": 'https://x.com/',
    "BlueSky": 'https://bsky.app/'
}
# posthaven_url = 'https://posthaven.com/'
# fb_url = 'https://www.facebook.com'
# pinterest_url = 'https://za.pinterest.com/'
# insta_url = 'https://www.instagram.com/'
# linkedin_url = 'https://www.linkedin.com'
# twitter_url = 'https://x.com/'
# bluesky_url = 'https://bsky.app/'

# Send GET requests and check the response status
for platform, url in social_urls.items():
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Successfully fetched {platform}'s homepage!")
    else:
        print(f"Failed to fetch {platform}'s page. Status code: {response.status_code}")

# Send a GET request to all socials
# fb_response = requests.get(fb_url)
# pinterest_response = requests.get(pinterest_url)
# insta_response = requests.get(insta_url)
# linkedin_response = requests.get(linkedin_url)
# twitter_response = requests.get(twitter_url)
# bluesky_response = requests.get(bluesky_url)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Render the index.html file when a GET request is made to the root URL
        self.render("web/index.html")

    def post(self):
        # Handle text inputs
        title = self.get_argument("title")
        intro_text = self.get_argument("introText")
        main_text = self.get_argument("mainText")

        # Handle file upload
        upload_file = self.request.files.get("uploadFile")  # File input
        if upload_file:
            for file in upload_file:
                # Handle file saving or processing here
                with open(os.path.join("uploads", file['filename']), 'wb') as f:
                    f.write(file['body'])
        # Handle POST request and retrieve the 'options' argument (a list of selected options)
        options = self.get_arguments("options")  # List of selected options
        if options:
            for option in options:
                option_lower = option.lower()
                if option_lower in social_urls:
                    webbrowser.open(social_urls[option_lower])
                    self.write(f"Opening {option_lower.capitalize()}...<br>")
                    # Check and output the text values
                    self.write(f"Title: {title}<br>")
                    self.write(f"Intro Text: {intro_text}<br>")
                    self.write(f"Main Text: {main_text}<br>")

                else:
                    self.write(f"Option '{option}' is not supported.<br>")
            else:
                self.write("No options selected.<br>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/web/static/(.*)", tornado.web.StaticFileHandler, {"path": "web/static"}),  # Serving static files
    ])

if __name__ == "__main__":
    # Set up the application to listen on port 2040
    app = make_app()
    app.listen(2040)
    print("Listening on port 2040")
    tornado.ioloop.IOLoop.current().start()
