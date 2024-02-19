t = -0.04:0.001:0.04;
x = 20*exp(j*(80*pi*t-0.4*pi));

% 3D plot of real and imaginary parts
plot3(t, real(x), imag(x));
grid on;

title('20*e^{j*(80\pit-0.4\pi)}');
xlabel('Tiempo, s');
ylabel('Real');
zlabel('Imag');

% 2D plot of real and imaginary parts separately
figure;
plot(t, real(x), 'b');
hold on;
plot(t, imag(x), 'r');
grid on;

title('Rojo - Componente Imaginario, Azul - Componente Real de la Exponencial');
xlabel('Tiempo');
ylabel('Amplitud');

