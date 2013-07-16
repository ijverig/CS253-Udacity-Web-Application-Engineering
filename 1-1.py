import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.out.write(self.request)
        self.response.out.write('Hello, Udacity! - from Daniel')

app = webapp2.WSGIApplication([('/.*', MainHandler)], debug=True)