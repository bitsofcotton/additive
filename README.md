# additive
Calculate the pseudo limit of singuar value in numerically.

# Description
Calculate symmetric matrix A's singular value limit by given equation series.
We can calculate complicated operations as into one matrix operations with the value on this numerical calculations.

We suppose: \[0,1\]x\[0,1\] region dx dy integrated input.

The real limit to this is : m \* m^t \* m^t \* m == QR, R(-1, -1).
In the equation meaning, we can calculatte this with m':=integrate f(x, y) f(y, x) dy, m'' = m'(x, y) m'(y, x) dy,
then, orthogonalize m''(\*,- 1) by m''(x,\*) to the limit as m0, then, integrate m0(x) m''(x, - 1) dx.

In the discrete meaning, this is equivalent to this m.py result, but, to calculate limit, we need to set large enough argv\[1\].
