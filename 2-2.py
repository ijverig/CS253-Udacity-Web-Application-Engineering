import webapp2, cgi, re

form = """\
<form style="text-align: center" method="POST">
    <input style="color: %(u_color)s" type="text"     name="username" value="%(u_value)s"><br>
    <input style="color: %(p_color)s" type="password" name="password" value="password"><br>
    <input style="color: %(p_color)s" type="password" name="verify"   value="password"><br>
    <input style="color: %(e_color)s" type="text"     name="email"    value="%(e_value)s"><br>
    <input style="color: orange" type="submit">
</form>
"""

class SignUp(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.out.write(self.request)
        self.response.out.write(form %
                               {'u_color': 'blue', 'u_value': 'username',
                                'p_color': 'blue',
                                'e_color': 'blue', 'e_value': 'e-mail (optional)'})

    def post(self):
        u = self.request.get('username'); u_valid = bool(re.match(r'^[a-zA-Z0-9_-]{3,20}$', u))
        p = self.request.get('password'); p_valid = bool(re.match(r'^.{3,20}$', p)) and p == self.request.get('verify')
        e = self.request.get('email')   ; e_valid = bool(re.match(r'^[\S]+@[\S]+\.[\S]+$', e))

        if u_valid and p_valid and (not e or e_valid):
            self.redirect('welcome?u=%s' % str(u+('&e='+e if e else '')))
        else:
            color = {False: 'red', True: 'blue'}
            self.response.out.write(form %
                                   {'u_color': color[u_valid], 'u_value': u,
                                    'p_color': color[p_valid],
                                    'e_color': color[e_valid], 'e_value': e})

class Welcome(webapp2.RequestHandler):
    def get(self):
        e = self.request.get('e')
        self.response.out.write('Welcome, %s!<br>' % self.request.get('u') + 
                               ('A confirmation e-mail was sent to %s.' % e if e else ''))

app = webapp2.WSGIApplication([('/signup/?', SignUp),
                               ('/welcome/?', Welcome)], debug=True)