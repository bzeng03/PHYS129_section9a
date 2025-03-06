# Change of Variables for Evaluating the Integral

The integral we need to evaluate is:

\[
I = \int_0^{\infty} \frac{x^3}{e^x - 1} dx
\]

To transform the integral from an infinite range to a finite range, we use the change of variables:

\[
z = \frac{x}{1 + x}
\]

which implies:

\[
x = \frac{z}{1 - z}
\]

### Computing the Differential
Differentiating both sides,

\[
dx = \frac{dz}{(1 - z)^2}
\]

### Transforming the Integral
Rewriting the integral in terms of \( z \):

\[
I = \int_0^1 \frac{\left( \frac{z}{1 - z} \right)^3}{e^{\frac{z}{1 - z}} - 1} \cdot \frac{dz}{(1 - z)^2}
\]

Simplifying:

\[
I = \int_0^1 \frac{z^3}{(1 - z)^5 (e^{z / (1 - z)} - 1)} dz
\]

This transformed integral is now in a finite range \( z \in [0,1] \) and can be evaluated numerically using quadrature methods.