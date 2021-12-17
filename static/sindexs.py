

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!']


def application(environ, start_response):
    response = Response('Hello World!', mimetype='text/plain')
    return response(environ, start_response)


def application(environ, start_response):
    request = Request(environ)
    text = f"Hello {request.args.get('name', 'World')}!"
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)
















from flask import  Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>hello_world!</p>"

from markupsafe import Markup, escape
# escape replaces special characters and wraps in Markup
escape('<script>alert(document.cookie);</script>')
Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')
# wrap in Markup to mark text "safe" and prevent escaping
Markup('<strong>Hello</strong>')
Markup('<strong>hello</strong>')
escape(Markup('<strong>Hello</strong>'))
Markup('<strong>hello</strong>')
# Markup is a text subclass (str on Python 3, unicode on Python 2)
# methods and operators escape their arguments
template = Markup("Hello <em>%s</em>")
template % '"World"'
Markup('Hello <em>&#34;World&#34;</em>')


from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response("Hello, World!")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application)




from itsdangerous import URLSafeSerializer
auth_s = URLSafeSerializer("secret key", "auth")
token = auth_s.dumps({"id": 5, "name": "itsdangerous"})

print(token)
# eyJpZCI6NSwibmFtZSI6Iml0c2Rhbmdlcm91cyJ9.6YP6T0BaO67XP--9UzTrmurXSmg

data = auth_s.loads(token)
print(data["name"])
# itsdangerous
