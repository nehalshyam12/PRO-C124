from flask import Flask ,jsonify,request 

app = Flask(__name__)

contacts = [
    {
       "name":u"Raju",
       "contact": "9987644456",
       "done": False,
       "id": 1 
    },
    {
       "name":u"Rahul",
       "contact": "9876543222",
       "done": False,
       "id": 2 
    },
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods =["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status": "error", 
            "message": "Provide the data"
        }, 400)

    contact ={
        "id": contacts[-1]['id']+1, 
        "title": request.json['title'],
        "description": request.json.get('description', ""),
        "done": False
    }
    contacts.append(contact)    
    return jsonify({
        "status": "Success!",
        "message": "Contact added successfully!"
    })    


@app.route("/get-data")
def get_contact():
    return jsonify({
        "data": contacts
    })


if __name__ =="__main__":
    app.run()