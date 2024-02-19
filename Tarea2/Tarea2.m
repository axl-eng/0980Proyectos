% Generar señal senoidal
fs = 1000; % frecuencia de muestreo
t = 0:1/fs:1; % vector de tiempo
f = 100; % frecuencia de la señal
x = sin(2*pi*f*t); % señal senoidal

% Aplicar Transformada de Forier
xf = fft(x);

% Generar filtro pasa-bajo
n = length(x);
fcutoff = 50; % frecuencia de corte
h = ones(n, 1); % Vector de ceros
h(round(n*fcutoff/fs)+1:end) = 0; % aplicar filtro pasa-bajo

% Aplicar filtro a la señal en el dominio de la frecuencia
xf_filtered = xf .* h;

% Convertir la señal filtrada a dominio del tiempo
x_filtered = ifft(xf_filtered);

% Graficar señal original y señal filtrada
figure;
subplot(2,1,1);
plot(t,x);
tittle('Señal original');
xlabel('Tiempo (s)');
ylabel('Amplitud');
subplot(2,1,2);
plot(t, real(x_filtered));
