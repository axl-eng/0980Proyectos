n= -1000:1000;

x= exp(j*2*pi*0.01*n);
plot(n, real(x))

y= exp(j*2*pi*2.01*n); %note que wy[n]= wx[n]J+2n
hold

plot(n, real(y), 'r');
