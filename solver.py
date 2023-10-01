import sympy as smp
from sympy import *
import latex2mathml.converter

# generates the equation from coefficient and returns in mathML format
def get_eqn(eqn_str):
    x, y, c = smp.symbols('x y c')
    euler_dict = {'e': E}
    eq_lhs_str, eq_rhs_str = eqn_str.split('=')
    try:
        eqn_lhs = sympify(eq_lhs_str, locals=euler_dict)
        eqn_rhs = sympify(eq_rhs_str, locals=euler_dict)
        eq = Eq(eqn_lhs, eqn_rhs)
        eq = latex(eq)
        return latex2mathml.converter.convert(eq)
    except SympifyError:
        return "Incorrect quation format"


# Function to solve the linear differential equation with no initial value
def solver_func(eqn_str):
    x, y, c = smp.symbols('x y c')
    euler_dict = {'e': E}
    eqn_str = eqn_str.replace("dy/dx", "Derivative(y, x)")
    eq_lhs_str, eq_rhs_str = eqn_str.split('=')
    
    try:
        eqn_lhs = sympify(eq_lhs_str, locals=euler_dict)
        eqn_rhs = sympify(eq_rhs_str, locals=euler_dict)
        eq = Eq(eqn_lhs, eqn_rhs)
        poly_eqn = smp.Poly(eq, [smp.Derivative(y, x), y])
        # Extract the coefficients
        coeffs = poly_eqn.coeffs()
        ddx = coeffs[0]
        c_y = coeffs[1]
        const = coeffs[2] * -1
 
        c_y = c_y / ddx
        const = const / ddx
        ddx = 1
        # # integrating factor
        i_f = integrate(c_y, x)
        i_f = smp.exp(i_f)

        # Returns the solved equation
        soln = (integrate(i_f * const, x))
        soln = soln + c
        soln = soln / i_f
        soln = Eq(y, soln)
        ans = latex(soln)
        return latex2mathml.converter.convert(ans)
        return soln
    except ValueError:
        str = "Incorrect equation Value error"
        return str
    except IndexError:
        str = "Incorrect equation index error"
        return str

# Function to solve the linear differential equation with initial value
def initial_val_solver_func(eqn_str, x_val, y_val):
    x, y, c = smp.symbols('x y c')
    euler_dict = {'e': E}
    eqn_str = eqn_str.replace("dy/dx", "Derivative(y, x)")
    eq_lhs_str, eq_rhs_str = eqn_str.split('=')
    
    try:
        eqn_lhs = sympify(eq_lhs_str, locals=euler_dict)
        eqn_rhs = sympify(eq_rhs_str, locals=euler_dict)
        eq = Eq(eqn_lhs, eqn_rhs)
        poly_eqn = smp.Poly(eq, [smp.Derivative(y, x), y])
        # Extract the coefficients
        coeffs = poly_eqn.coeffs()
        ddx = coeffs[0]
        c_y = coeffs[1]
        const = coeffs[2] * -1
 
        c_y = c_y / ddx
        const = const / ddx
        ddx = 1
        # integrating factor
        i_f = integrate(c_y, x)
        i_f = smp.exp(i_f)

        # Returns the solved equation
        soln = (integrate(i_f * const, x))
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
    except IndexError:
        str = "Incorrect equation"
        return str
