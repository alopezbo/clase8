from flask import Flask 
from flask import jsonify 

app=Flask(__name__) 

@app.route('/api/ejemplo') 
def ejemplo2(): 
    return jsonify(Hola='Mundo!') 
if __name__=="__main__": 
    app.run(host='0.0.0.0', 
        debug=True, 
        port=8080) 