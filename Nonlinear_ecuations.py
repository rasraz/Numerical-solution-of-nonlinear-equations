import sympy

class method():

    def Newton(x0,number):
        """
        x0 : نقطه شروع
        number : تعداد ارقام اعشار
        """
        s_x = sympy.symbols("x")
        s_f = sympy.exp(s_x)-2 # معادله تابع [(e^x)-2]
        f = lambda x: sympy.lambdify(s_x, s_f)(x) 
        fp = lambda x: sympy.lambdify(s_x, sympy.diff(s_f, s_x))(x) 
        list_CA=[x0]
        x0_new=x0+1
        while True:
            x0_new = x0 - f(x0) / fp(x0)
            list_CA.append(x0_new)
            if (int(abs(x0)*10**number)/10**number)==(int(abs(x0_new)*10**number)/10**number):break
            x0 = x0_new 
        return list_CA

    def halve(a,b,number):
        """
        a : نقطه ابتدا بازه
        b : نقطه انتهای بازه
        number : تعداد ارقام اعشار
        """
        s_x = sympy.symbols("x") 
        s_f = sympy.sin(s_x) # معادله تابع  sin(x)
        f = lambda x: sympy.lambdify(s_x, s_f)(x) 
        if f(a)*f(b)<0:
            list_CA=list()
            while True:
                z=(a+b)/2
                try:
                    if (int(abs(z)*10**number)/10**number)==(int(abs(list_CA[-1])*10**number)/10**number):list_CA.append(z);break;
                except IndexError :pass
                if f(a)*f(z)<0:b=z
                elif f(a)*f(z)==0:list_CA.append(z);break;
                else:a=z
                list_CA.append(z)
            return list_CA

    def chord(x0,x1,number):
        """
        x0: نقطه اولیه
        x1: نقطه ثانویه
        number: تعداد ارقام با معنا بعد ممیز
        """
        s_x = sympy.symbols("x") 
        s_f = sympy.cos(s_x)-s_x # معادله تابع  cos(x)-x
        f = lambda x: sympy.lambdify(s_x, s_f)(x)
        list_CA=list()
        while True:
            xn= ( (x1*f(x0)) - (x0*f(x1)) ) / ( f(x0)-f(x1) )
            list_CA.append(xn)
            x0,x1=x1,xn
            try:
                if (int(abs(xn)*10**number)/10**number)==(int(abs(list_CA[-1])*10**number)/10**number):list_CA.append(xn);break;
            except IndexError :pass
        return list_CA

    def impropriety(x0,x1,number):
        """
        x0: نقطه اولیه
        x1: نقطه ثانویه
        number: تعداد ارقام با معنا بعد ممیز
        """
        s_x = sympy.symbols("x") 
        s_f = sympy.cos(s_x)-s_x  # معادله تابع  cos(x)-x
        f = lambda x: sympy.lambdify(s_x, s_f)(x)
        if f(x0)*f(x1)<0:
            list_CA=list()
            while True:
                xn= ( (x1*f(x0)) - (x0*f(x1)) ) / ( f(x0)-f(x1) )
                try:
                    if (int(abs(xn)*10**number)/10**number)==(int(abs(list_CA[-1])*10**number)/10**number):list_CA.append(xn);break;
                except IndexError :pass
                if f(x0)*f(xn)<0:x1=xn
                elif f(x0)*f(xn)==0:list_CA.append(xn);break;
                else:x0=xn
                list_CA.append(xn)
        return list_CA

    def fixed_point(x0,number):
        """
        x0: نقطه اولیه
        number: تعداد ارقام با معنا بعد ممیز
        """
        s_x = sympy.symbols("x") 
        s_f = s_x**0.5+2 # معادله تابع (x^0.5)+2
        f = lambda x: sympy.lambdify(s_x, s_f)(x) 
        list_CA=list()
        while True:
            xn=f(x0)
            try:
                if (int(abs(xn)*10**number)/10**number)==(int(abs(list_CA[-1])*10**number)/10**number):list_CA.append(xn);break;
            except IndexError :pass
            x0=xn
            list_CA.append(xn)

        return list_CA
