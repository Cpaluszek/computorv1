# computorv1

A program that solves polynomial equations of second degree or lower.

**Example:**
```bash
$>./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131

$>./computor "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1 * X^0 + 4 * X^1 = 0
Polynomial degree: 1
The solution is:
-0.25

$>./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is strictly greater than 2, I can't solve.

$>./computor "6 * X^0 = 6 * X^0"
Reduced form: 0 * X^0 = 0
Any real number is a solution.

$>./computor "10 * X^0 = 15 * X^0"
Reduced form: -5 * X^0 = 0
No solution.

$>./computor "1 * X^0 + 2 * X^1 + 5 * X^2 = 0"
Reduced form: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly negative, the two complex solutions are:
-1/5 + 2i/5
-1/5 - 2i/5
```

## Resolution explanation

### Degree 2 - quadratic equation
A quadratic equation follows this form:

$ax2+bx+c=0$

where:
- $a$, $b$, $c$ are coefficients.
- $x$ is the unknown variable.

To find the solutions, we compute the discriminant:
$\Delta = b^2 - 4ac$

![Discriminant signs](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Quadratic_eq_discriminant.svg/330px-Quadratic_eq_discriminant.svg.png)

- If $\Delta > 0$: Two distinct real solutions exist, given by:
    - $X_1 = \frac{-b+\sqrt{\Delta}}{2a}$
    - $X_2 = \frac{-b-\sqrt{\Delta}}{2a}$
- If $\Delta = 0$: One real solution (a double root) exists:
    - $X = \frac{-b}{2a}$
- If $\Delta < 0$: Two complex conjugate solutions exist:
    - $X_1 = \frac{-b}{2a}+i\frac{\sqrt{-\Delta}}{2a}$
    - $X_1 = \frac{-b}{2a}-i\frac{\sqrt{-\Delta}}{2a}$



### Degree 1 - linear equation
A linear equation follows this form:

$bX=c=0$

Solving for $X$:

$X=-\frac{c}{b}$

### Degree 0 - constant equation
The program checks if the constant term is zero.
- If it is 0, any real number is a solution
- If it is non-zero, there is no solution

---
## Resources
- [Visualizing Complex Roots of Quadratic Equations](https://www.geogebra.org/m/U2HRUfDr)

