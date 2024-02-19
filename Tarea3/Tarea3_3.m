n = -50:50;
x = cos(pi*0.1*n);
y = cos(pi*0.9*n);
z = cos(pi*2.1*n);
subplot(311)
plot(n,x);
title('x[n]=cos(0.1\pin)')
grid
subplot(312)
plot(n,y);
title('y[n]=cos(0.9\pin)')
grid
subplot(313)
plot(n,z)
grid
title('z[n]=cos(2.1\pin)')
xlabel('n')
