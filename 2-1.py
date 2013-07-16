import webapp2
from cgi import escape

form = """\
<form method="POST">
    <textarea name="text">%s</textarea>
    <input type="submit">
</form>
"""

class ROT13(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form % '')

    def post(self):
        def rot13(c):
            return chr(ord(c) + (13 if c.lower() <= 'm' else -13)) if c.isalpha() else c
        self.response.out.write(form % escape(''.join(map(rot13, self.request.get('text')))))

app = webapp2.WSGIApplication([('/rot13/?', ROT13)], debug=True)