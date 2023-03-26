import counter_app
from counter_app import home_page, app, show, db

@app.route('/')
def home():
  return show(number=db['number'])

@app.route('/increment')
def increment():
  db['number'] += 1
  return show(number=db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  return show(number=db['number'])
  
app.run(host='0.0.0.0', port=81)