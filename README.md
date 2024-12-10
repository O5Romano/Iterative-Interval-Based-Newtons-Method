# Iterative-Interval-Based-Newtons-Method
Work in progress, lots of troubles without the intercept

My attempt at finding roots of polynomials. We take the derivative of the original function until we get the quadratic function which can easily be solved analytically, then roots of said function are extremes of the higher degree (integral of the quadratic) we eliminate intervals that do not contain roots and use newton's method on the rest to approximate its roots which later serve us as extremes of the polynomial of the higher order. We repeat those steps until we work our way back to the original function
