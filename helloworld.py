import webapp2

form="""
	<form action="http://www.google.com/search">
		<input name="q">
		<input type="submit">
	</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Hello World!')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)