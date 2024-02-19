%comprueba version
if(exist('OCTAVE_VERSION','builtin')~=0)
%Estamos en octave
  pkg load signal;
end
% Menù principalS
opcion = 0;
while opcion ~= 5
%opcion = input('Seleccione una opciòn:\n 1.Grabar Audio\n 2.Reproducir Audio\n 4. Salir\n');
% Menù de opciones
disp('Seleccione una opcion:')
disp('1. Grabar')
disp('2. Reproducir')
disp('3. Graficar')
disp('4. Grafica densidad')
disp('5. Salir')
opcion = input('Ingrese su elecciòn ');
      switch opcion
      case 1 %Grabaciòn de audio
      try 
         duracion = input('Ingrese la duraciòn de la grabaciòn en segundos');
         disp('Comenzando la grabaciòn...');
         recObj = audiorecorder;
         recordblocking(recObj, duracion);
         disp('Grabaciòn finalizada.');
         data = getaudiodata(recObj.SampleRate);
         audiowrite('audio.wav', data, recObj.SampleRate);
         disp('Archivo de audio grabada correctamente');
      catch
         disp('Error al grabar el audio');
      end
      case 2 %Reproducciòn de audio
      try 
      	[data, fs] = audioread('audio.wav');
      	sound(data, fs);
      catch
      	disp('Error al reproducir el audio');
      end
      case 3 %Gràfico de audio
      try
      	[data, fs] = audioread('audio.wav');
      	tiempo = linspace(0, length(data)/fs, length(data));
      	plot(tiempo, data);
      	xlabel('Tiempo (s)');
      	ylabel('Amplitud');
      	title('Audio');
      catch
      	disp('Error al graficar el audio');
      end
      case 4 %Graficando espectro de frecuencia
      try
      	disp('Graficando espectro de frecuencia...');
      	[audio, Fs] = audioread('audio.wav'); %Lee la señal desde el archivo .wav
      	N = length(audio); %Nùmero de muestras de la señal
      	f = linspace(0, Fs/2, N/2+1); %Vector de frecuencias
      	ventana = hann(N); % Ventanade Hann para reducir el efecto de las discontinuidades al calcular la FFT
      	Sxx = pwelch(audio, ventana, 0, N, Fs); %Densidad espectral de potencia
      	plot(f, 10*log10(Sxx(1:N/2+1))); %Grafica el espectro de frecuencia en dB
      	xlabel('Frecuencia (Hz)');
      	ylabel('Densidad espectral de potencia (dB/Hz)');
      	title('Espectro de frecuencia de la señal grabada');
      catch
      	disp('Error al graficar el audio.');
      end
      case 5 %Salir
      	disp('Saliendo del programa...');
      otherwise
      	disp('Opciòn no vàlida.');
      end
   end	
