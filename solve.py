import sympy as smp
from sympy import *
import matplotlib.pyplot as plt
import io

# Saving the equation ans solve in png file

eqn_path = './equation.png'
solve_path = './solve.png'

def latex_to_png(latex_str, file_path):
    fig = plt.figure()
    fig.set_figheight(1)
    plt.axis("off")
    plt.text(0.5, 0.5, f"${latex_str}$", size = 25, ha="center", va="center")
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=300)
    plt.close(fig)
    with open(file_path, 'wb') as f:
        f.write(buffer.getvalue())
    
# Function to solve the linear differential equation

x, y, c = smp.symbols('x y c')

def solve(ddx, c_y, const):
    ddx = ddx.replace('^', "**")
    c_y = c_y.replace('^', "**")
    const = const.replace('^', "**")
    ddx = parse_expr(ddx)
    c_y = parse_expr(c_y)
    const = parse_expr(const)

    eq = Eq(Derivative(y,x) * ddx + c_y * y, const)
    latex_to_png(latex(eq), eqn_path)

    c_y = c_y / ddx
    const = const / ddx
    ddx = 1
    i_f = integrate(c_y, x)
    i_f = smp.exp(i_f)

    # Prints the solved equation
    solve = (integrate(i_f * const))
    solve = solve + c
    solve = solve / i_f
    solve = Eq(y, solve)

    ans = latex(solve)
    latex_to_png(ans, solve_path)




# solve("1 + smp.sin(x)**2", "smp.sin(2*x)", "smp.cos(x)")
# solve("1 + sin(x)**2", "sin(2*x)", "cos(x)")

solve("1 + sin(x)^2", "sin(2*x)", "cos(x)")
