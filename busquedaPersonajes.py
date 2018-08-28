from flask import Flask
from flask import render_template
from flask import request
import redis
import json 

app = Flask(__name__)


r = redis.Redis(
    host = 'redis',
    port = 6379
)

default = r.get('aliens').decode('utf-8')



@app.route('/')
def inicio():
    return render_template('index.html', result = default)


@app.route('/', methods=['POST', 'GET'])
def resultado():
    try:
        if request.method == 'POST':
            resultados = request.form['nombre']
            resultados = resultados.lower() 
            final = r.get(resultados).decode('utf-8')
            return render_template('index.html', result = final)
    except:
        return render_template('index.html', result = default)


app.run(host = "0.0.0.0",port = 5000)