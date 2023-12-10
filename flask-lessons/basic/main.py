from flask import Flask, request

app = Flask(__name__)

#one example of dynamic content/variable rather than just hard code content
greeting = 'Hello, world, again'

@app.route('/')
def index():
    # return '<h3>Hello, world, again</h3>'
    return f'<h3>{greeting}</h3>'

# creating a new route: incl decorator, endpoint and then a function
@app.route('/spam')
def spam():
    person = { 'name': 'John', 'age': 21}
    return person

@app.route('/hello/<name>')
def hello(name):
    print(request.args.get('name'))
    #name = 'Jack'
    return { 'message': f'Hello, {name}'}

@app.route('/add/<int:num1>/<int:num2>') #not cast interger here possible, this means that both params must be present and integers in order for the function to be called, so the error would never occur. 
def add(num1, num2):
    #try:
        # num1 = int(request.args.get('num1'))
        # num2 = int(request.args.get('num2'))
        return { 'result': num1 + num2 }
    #except ValueError or TypeError:
        #return { 'error': 'num1 and num2 are required and must be integers'}, 400a
        #now if you run it with an error, you get a detailed error message from the framework/server without the handling
        #but you could still add one with an error message if needed.

@app.errorhandler(TypeError)
def type_error(error):
    return { 'error': str(error) }, 400

@app.errorhandler(404)
def not_found(error):
    #return { 'error': '404 Not Found' }, 404
    return { 'error': str(error) }, 404

if __name__ == '__main__':
    app.run(debug=True)