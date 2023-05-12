from flask import Flask
import boto3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  s = boto3.Session()
  c = s.client("sts")
  
  asd = c.get_caller_identity()
  return { "identity_caller": asd }

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080)