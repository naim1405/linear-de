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


# Function to solve the linear differential equation with no initial value
def solver_func(ddx, c_y, const):
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

        # Returns the solved equation
        soln = (integrate(i_f * const))
        soln = soln + c
        soln = soln / i_f
        soln = Eq(y, soln)
        ans = latex(soln)
        return latex2mathml.converter.convert(ans)
    except ValueError:
        str = "Incorrect equation"
        return str

# Function to solve the linear differential equation with initial value
def initial_val_solver_func(ddx, c_y, const, x_val, y_val):
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

        # # Returns the solved equation
        soln = (integrate(i_f * const))
        soln = soln + c
        soln = soln / i_f
        soln = Eq(y, soln)
        soln_2 = soln.subs(x, x_val)
        soln_2 = soln_2.subs(y, y_val)
        c_val = solve(soln_2, dict=True)[0][c]
        soln = soln.subs(c, c_val)
        ans = latex(soln)
        return latex2mathml.converter.convert(ans)
    except ValueError:
        str = "Incorrect equation"
        return str
