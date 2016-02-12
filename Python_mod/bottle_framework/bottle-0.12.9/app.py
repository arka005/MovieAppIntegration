from bottle import route, run
 
@route('/hello/:name')
def index(name='World'):
    return '<strong>Hello %s!</strong>' % name
 
run(host='localhost', port=8181)
