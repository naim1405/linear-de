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
        # print(const)
        eqn = get_eqn(ddx, c_y, const)

        solv = solve(ddx, c_y, const)
        # return redirect(url_for('soln',eqn = eqn, soln = solv))
        return render_template("soln.html", eqn = eqn, soln = solv)
    
    return render_template("form.html")
    
@app.route("/soln")
def soln(eqn, soln):
    return render_template("soln.html", eqn = eqn, soln = soln)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
