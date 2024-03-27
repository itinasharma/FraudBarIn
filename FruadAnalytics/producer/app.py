from flask import Flask
from flask import request
from kafka import KafkaProducer
import os
import json

app = Flask(__name__)

   
@app.route("/add", methods = ['POST'])
def add_contact() :
    data = json.loads(request.data)
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    producer.send('my-topic', json.dumps(data).encode('utf-8'))
    return "ok"
    
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')

