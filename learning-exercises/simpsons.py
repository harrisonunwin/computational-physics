from scipy.integrate import simpson as scipy_simpson
from numpy import linspace

def f(x):
    return x**4 - 2*x +1


def integral():

    N = 100  # initial step count
    a = 0
    b = 2

    delta = 1e-10   #desired error

    def simpson(N):

        h = (b - a) / N    #h must depend on N
        s = f(a)+f(b)
        for k_odd in range(1,N,2):
            s += 4*f(a+k_odd*h)
        for k_even in range(2,N,2):   #Previous mistake, make sure second loop is not nested inside first.
                s += 2*f(a+k_even*h)

        return (1/3)*h*s       #Should provide initial value

    I_prev = simpson(N)

    while True:
        N2 = N*2
        I_curr = simpson(N2)

        error = (I_curr- I_prev) / 15

        if abs(error) < delta:
            print(f"Value of integral is {I_curr}, N={N2}, error={error}")
            break

        N, I_prev = N2, I_curr

    x = linspace(a,b,N2+1)
    y = f(x)
    scipy_result = scipy_simpson(y,x)
    print("Result from scipy is",scipy_result)

integral()
