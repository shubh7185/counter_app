from flask import Flask, render_template_string
from replit import db

if 'number' not in db:
  db['number'] = 0

app = Flask(__name__)

home_page = '''
    <link rel="stylesheet" href="./static/counter_styles.css">
    
    <span>{{ number }}</span>
    <div>
    <form action="/decrement">
      <button id='increment'>-</button>
    </form>
    <form action="/increment">
      <button id='decrement'>+</button>
    </form>
    </div>
    '''

@app.route('/')
def cookieeee():
    return render_template_string(home_page, number=db['number'])

@app.route('/increment')
def increment():
  db['number'] += 1
  return render_template_string(home_page, number=db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  return render_template_string(home_page, number=db['number'])
  
app.run(host='0.0.0.0', port=81)