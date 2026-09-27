import math

# math.pi: Returns the value of pi (3.14159...)
print("Pi:", math.pi)  # Output: 3.141592653589793

# math.e: Returns Euler's number (2.71828...)
print("Euler's number:", math.e)  # Output: 2.718281828459045

# math.tau: Returns tau (6.28318...), which is equal to 2 * pi
print("Tau:", math.tau)  # Output: 6.283185307179586

# math.inf: Returns a floating-point positive infinity
print("Infinity:", math.inf)  # Output: inf

# math.nan: Returns a floating-point "Not a Number" value
print("NaN:", math.nan)  # Output: nan

#------------------------------------------------------

# math.ceil(x): Rounds a number UP to the nearest integer
print(math.ceil(4.2))   # Output: 5
print(math.ceil(-4.2))  # Output: -4

# math.floor(x): Rounds a number DOWN to the nearest integer
print(math.floor(4.7))  # Output: 4
print(math.floor(-4.7)) # Output: -5

# math.comb(n, k): Returns the number of ways to choose k items from n items without repetition (Combinations)
print(math.comb(5, 2))  # Output: 10

# math.perm(n, k): Returns the number of ways to choose k items from n items with order (Permutations)
print(math.perm(5, 2))  # Output: 20

# math.fabs(x): Returns the absolute (positive) value of a number as a float
print(math.fabs(-7.5))  # Output: 7.5

# math.factorial(x): Returns the factorial of a number
print(math.factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)

# math.gcd(*integers): Returns the Greatest Common Divisor of the given integers
print(math.gcd(24, 36))  # Output: 12

# math.lcm(*integers): Returns the Least Common Multiple of the given integers (Python 3.9+)
print(math.lcm(12, 18))  # Output: 36

# math.isclose(a, b): Checks if two values are close to each other
print(math.isclose(0.1 + 0.2, 0.3))  # Output: True

# math.isnan(x): Checks if a value is NaN (Not a Number)
print(math.isnan(math.nan))  # Output: True

#-------------------------------------------------------

# math.pow(x, y): Returns x raised to the power y (as a float)
print(math.pow(2, 3))  # Output: 8.0

# math.sqrt(x): Returns the square root of a number
print(math.sqrt(25))  # Output: 5.0

# math.cbrt(x): Returns the cube root of a number (Python 3.11+)
print(math.cbrt(27))  # Output: 3.0

# math.exp(x): Returns e raised to the power x
print(math.exp(1))  # Output: 2.718281828459045 (same as math.e)

# math.log(x, [base]): Returns the logarithm of x. Defaults to natural log (base e) if base is omitted.
print(math.log(math.e))  # Output: 1.0
print(math.log(100 , 10)) # Output: 2.0 (log base 10)

# math.log10(x): Returns the base-10 logarithm of x
print(math.log10(100))  # Output: 2.0

# math.log2(x): Returns the base-2 logarithm of x
print(math.log2(8))  # Output: 3.0

#----------------------------------------------

# math.radians(x): Converts an angle from degrees to radians
rad = math.radians(180)
print(rad)  # Output: 3.141592653589793 (equal to Pi)

# math.degrees(x): Converts an angle from radians to degrees
deg = math.degrees(math.pi)
print(deg)  # Output: 180.0

# math.sin(x): Returns the sine of x (x in radians)
print(math.sin(math.radians(90)))  # Output: 1.0

# math.cos(x): Returns the cosine of x (x in radians)
print(math.cos(math.radians(0)))   # Output: 1.0

# math.tan(x): Returns the tangent of x (x in radians)
print(math.tan(math.radians(45)))  # Output: 0.9999999999999999 (essentially 1.0)

# Inverse Trigonometric Functions (Returns value in radians)
# math.asin(x): Arc sine
print(math.degrees(math.asin(1.0)))  # Output: 90.0

# math.acos(x): Arc cosine
print(math.degrees(math.acos(1.0)))  # Output: 0.0

# math.atan(x): Arc tangent
print(math.degrees(math.atan(1.0)))  # Output: 45.0

#----------------------------------------------

# math.sinh(x): Returns the hyperbolic sine of x
print(math.sinh(1))  # Output: 1.1752011936438014

# math.cosh(x): Returns the hyperbolic cosine of x
print(math.cosh(1))  # Output: 1.5430806348152437

# math.tanh(x): Returns the hyperbolic tangent of x
print(math.tanh(1))  # Output: 0.7615941559557649

#----------------------------------------------

# math.dist(p, q): Returns the Euclidean distance between two points p and q (Python 3.8+)
point1 = (1, 2)
point2 = (4, 6)
print(math.dist(point1, point2))  # Output: 5.0 (Calculates sqrt((4-1)^2 + (6-2)^2))

# math.hypot(*coordinates): Returns the Euclidean norm/hypotenuse sqrt(sum(x^2))
print(math.hypot(3, 4))  # Output: 5.0


#----------------------------------------------

