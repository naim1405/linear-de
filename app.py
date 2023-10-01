from flask import Flask , redirect, url_for, render_template, request
from solver import *


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/solve/<initial_value>", methods=["POST", "GET"])
def solver(initial_value):
    if(initial_value == 'False'):
        if(request.method == 'POST'):
            eqn_str = request.form['eqn']
            eqn = get_eqn(eqn_str)
            solv = solver_func(eqn_str)
            return render_template("solution.html", eqn = eqn, soln = solv)

        return render_template("equation-solver.html")
    else:
        if(request.method == 'POST'):
            eqn_str = request.form['eqn']
            x_val = request.form['x_val']
            y_val = request.form['y_val']
            eqn = get_eqn(eqn_str)
            solv = initial_val_solver_func(eqn_str, x_val, y_val)
            return render_template("initial-value-solution.html", eqn = eqn, soln = solv)

        return render_template("initial-value-equation-solver.html")
 

@app.route("/about")
def about():
    return render_template("about-our-team.html")

@app.route("/manual")
def manual():
    return render_template("user-manual.html")

if __name__ == "__main__":
    app.run(debug=True)
