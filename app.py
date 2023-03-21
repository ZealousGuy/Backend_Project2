from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key='Papa_ki_Pari'           # Created a secret key to implement session

@app.route('/', methods=["POST","GET"]) # Changed to also accept the GET request since we were getting a method not allowed error
def index():
    if request.method == "POST":
        note = request.form.get("note") # Changed from request.args to request.froms since we are accepting the value via a form.
        if note.strip() != "":          # type:ignore
            if "notes" not in session:
                session["notes"]=[]     # Check if notes key is in the session if it isn't, create an empty list for the key.
            notes = session.get("notes", []) + [note]
            session["notes"] = notes
    else:
        session.pop("notes",None)
    return render_template("home.html", notes=session.get("notes",[]))


if __name__ == '__main__':
    app.run(debug=True)