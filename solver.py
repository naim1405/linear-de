import sympy as smp
from sympy import *
import latex2mathml.converter

# generates the equation from coefficient and returns in mathML format
def get_eqn(ddx, c_y, const):
    x, y, c = smp.symbols('x y c')
    euler_dict = {'e': E}
    try:
        ddx = sympify(ddx,locals=euler_dict)
        c_y = sympify(c_y,locals=euler_dict)
        const = sympify(const,locals=euler_dict)
        eq = Eq(Derivative(y,x) * ddx + c_y * y, const)
        eq = latex(eq)
        return latex2mathml.converter.convert(eq)
    except SympifyError:
        return "Incorrect quation format"


# Function to solve the linear differential equation
def solve(ddx, c_y, const):
    x, y, c = smp.symbols('x y c')
    euler_dict = {'e': E}
    try:
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
    except ValueError:
        str = "Incorrect equation"
        return str
