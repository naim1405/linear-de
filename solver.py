import sympy as smp
from sympy import *
import latex2mathml.converter

# Saving the equation solve in png file

eqn_path = './static/equation.png'
solve_path = './static/solve.png'

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
    return
    

def get_eqn(ddx, c_y, const):
    x, y, c = smp.symbols('x y c')
    euler_dict = {'e': E}
    ddx = sympify(ddx,locals=euler_dict)
    c_y = sympify(c_y,locals=euler_dict)
    const = sympify(const,locals=euler_dict)
    eq = Eq(Derivative(y,x) * ddx + c_y * y, const)
    eq = latex(eq)
    return latex2mathml.converter.convert(eq)


# Function to solve the linear differential equation
def solve(ddx, c_y, const):
    x, y, c = smp.symbols('x y c')
    euler_dict = {'e': E}
    ddx = sympify(ddx,locals=euler_dict)
    c_y = sympify(c_y,locals=euler_dict)
    const = sympify(const,locals=euler_dict)

    c_y = c_y / ddx
    const = const / ddx
    ddx = 1
    # # integrating factor
    i_f = integrate(c_y, x)
    i_f = smp.exp(i_f)

    # # Prints the solved equation
    solve = (integrate(i_f * const))
    solve = solve + c
    solve = solve / i_f
    solve = Eq(y, solve)
    ans = latex(solve)
    return latex2mathml.converter.convert(ans)




# solve("1 + smp.sin(x)**2", "smp.sin(2*x)", "smp.cos(x)")
# solve("1 + sin(x)**2", "sin(2*x)", "cos(x)")

# solve("1 + sin(x)^2", "sin(2*x)", "cos(x)")
