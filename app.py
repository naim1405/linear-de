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
            ddx = request.form['ddx']
            c_y = request.form['c_y']
            const = request.form['const']
            eqn = get_eqn(ddx, c_y, const)
            solv = solver_func(ddx, c_y, const)
            return render_template("solution.html", eqn = eqn, soln = solv)

        return render_template("equation-solver.html")
    else:
        if(request.method == 'POST'):
            ddx = request.form['ddx']
            c_y = request.form['c_y']
            const = request.form['const']
            x_val = request.form['x_val']
            y_val = request.form['y_val']
            # print(x_val , "  ", y_val)
            eqn = get_eqn(ddx, c_y, const)
            solv = initial_val_solver_func(ddx, c_y, const, x_val, y_val)
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
