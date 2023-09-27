from flask import Flask , redirect, url_for, render_template, request
from solver import *




app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if(request.method == 'POST'):
        # print("POST REQ")

        ddx = request.form['ddx']
        c_y = request.form['c_y']
        const = request.form['const']
        solve(ddx, c_y, const)
        return redirect('/soln')
    
    return render_template("form.html")
    
@app.route("/soln")
def soln():
    return render_template("soln.html")

if __name__ == "__main__":
    app.run(debug=True)
