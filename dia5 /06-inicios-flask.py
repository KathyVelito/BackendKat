from flask import Flask

app = Flask (__name__)

#print(__name__)
@app.route('/')
def inicio():
    print("ME llamaron!!")
    return {
        "message": "Hello World!!"
    }



app.run(debug=True)