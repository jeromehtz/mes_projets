def bezout_fct(a,b):
    if b == 0:
        return 1,0
    else:
        u , v = bezout_fct(b , a % b)
        return v , u - (a//b)*v

def resoud_equation(a,b,c):
    u,v = bezout_fct(a,b)
    return "Les solutions de l'équation {}x + {}y = {} sont:\n({} + {}k , {} - {}k)".format(a,b,c,u,b,v,a)
print(resoud_equation(368,117,1))