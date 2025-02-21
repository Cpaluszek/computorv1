#!/usr/bin/python3

import sys
import re
import math
import cmath

def parse_equation(equation: str):
    """Parses the input equation and returns a dictionnary of coefficients"""

    if "=" not in equation:
        print("Error: Invalid equation format. The equation must contains '='.")
        sys.exit(1)

    # Normalize equation: remove spaces and split by =
    lhs, rhs = equation.replace(" ", "").split("=")

    # Check for invalid characters
    if not re.match(r'^[-+0-9X\^*.]*$', lhs) or not re.match(r'^[-+0-9X\^*.]*$', rhs):
        print("Error: Equation contains invalid characters.")
        sys.exit(1)

    # Convert to coefficient dictionnary
    coefficients = {0:0, 1:0, 2:0}
    parse_side(lhs, coefficients, sign=1)
    parse_side(rhs, coefficients, sign=-1)

    return coefficients

def parse_side(expression: str, coefficients: dict, sign: int):
    """Parses one side of the equation and updates coefficient dictionnary."""
    terms = re.findall(r'([+-]?\d*\.?\d*)\*?X\^([+-]?\d*\.?\d+)', expression)

    for coef, power in terms:
        if power == '':
            power = '1'
        if '.' in power or float(power) < 0:
            print("Error: Powers must be non-negative integers.")
            sys.exit(1)

        power = int(power)
        coef = float(coef) if coef not in ["", "+", "-"] else (1.0 if coef == "+" else -1.0)

        if power in coefficients:
            coefficients[power] += sign * coef
        else:
            coefficients[power] = sign * coef

def solve(coefficients):
    """Solves the polynomial equation based on its degree."""
    degree = max(k for k,v in coefficients.items() if v != 0)

    # Format the reduced form of the equation
    terms = []
    for k, v in sorted(coefficients.items()):
        if v == 0:
            continue
        sign = "+" if v > 0 else "-"
        coef = abs(v)
        if k == 0:
            terms.append(f"{sign} {coef:.3f}".rstrip("0").rstrip("."))
        elif k == 1:
            terms.append(f"{sign} {coef:.3f} * X".rstrip("0").rstrip("."))
        else:
            terms.append(f"{sign} {coef:.3f} * X^{k}".rstrip("0").rstrip("."))

    reduced_form = " ".join(terms).replace("+ -", "- ")
    print("Reduced form:", reduced_form, "= 0")

    print(f"Polynomial degree: {degree}")

    if degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
        return
    elif degree == 2:
        solve_quadratic(coefficients[2], coefficients[1], coefficients[0])
    elif degree == 1:
        solve_linear(coefficients[1], coefficients[0])
    else :
        solve_constant(coefficients[0])

def solve_quadratic(a, b, c):
    """Solves a quadratic equation ax^2 + bx + c = 0."""

    delta = b**2 - 4*a*c

    if delta > 0:
        root1 = (-b - math.sqrt(delta)) / (2 * a)
        root2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Discriminant is strictly positive: {delta}, the two solutions are:")
        print(root1)
        print(root2)
    elif delta == 0:
        root = -b / (2 * a)
        print("Discriminant is zero, the solution is:")
        print(root)
    else:
        root1 = (-b + cmath.sqrt(delta)) / (2 * a)
        root2 = (-b - cmath.sqrt(delta)) / (2 * a)
        print(f"Discriminant is strictly negative: {delta} , the two complex solutions are:")
        print(root1)
        print(root2)

def solve_linear(b, c):
    """Solves a linear equation bx + c = 0"""
    if b == 0:
        if c == 0:
            print("Any real number is a solution.")
        else:
            print("No solution.")
    else:
        print("The solution is:")
        print(f"{-c / b}")

def solve_constant(c):
    """Handles a constant equation c = 0."""
    if c == 0:
        print("Any real number is a solution.")
    else:
        print("No solution.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} \"equation\"")
        sys.exit(1)

    equation = sys.argv[1]
    print(f"Equation: {equation}")
    coefficients = parse_equation(equation)
    solve(coefficients)

