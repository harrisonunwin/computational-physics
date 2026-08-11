
def f(x):
    return x**4 - 2*x +1

def main():

    N_i = 2        #initial number of points
    a = 0          #a and b are limits of integration
    b = 2
    h_i = (b-a)/N_i   #inital step size

    delta = 1e-10

    def Integral(N,h):
        'function which performs simpson method, allows for part of integral to be reused rather than recalculating'

        s_intial = (1/3) * (f(a) + f(b))
        for k in range(2, N,2):
            s_intial += (2/3) * f(a+k*h)

        t_initial = 0
        for k in range(1, N,2):
            t_initial += (2/3) * f(a+k*h)

        return h * (s_intial + 2*t_initial)

    I_initial = Integral(N_i, h_i)       #Calculates the intial value of integral with N=2

    while True:           #loops indefinitely until error condition is satisfied
        N_curr = 2*N_i
        h_curr = (b-a) / N_curr
        I_curr = Integral(N_curr,h_curr)

        delta_curr = (1/15)*(I_curr - I_initial)

        if abs(delta_curr) < delta:
            print(f"Value of integral is {I_curr}, N={N_curr}, error={delta_curr}")
            break

        N_i, h_i = N_curr, h_curr
        I_initial = I_curr           #reuses integral rather than recalculating

main()








