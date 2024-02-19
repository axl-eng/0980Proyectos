import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt


# Menú principal
opcion = 0
while opcion != 5:
    # Menú de opciones
    print('Seleccione una opción:')
    print('1. Grabar')
    print('2. Reproducir')
    print('3. Graficar')
    print('4. Graficar densidad')
    print('5. Salir')

    opcion = int(input('Ingrese su elección: '))

    if opcion == 1:  # Grabación de audio
        try:
            duracion = float(input('Ingrese la duración de la grabación en segundos:  '))
            print('Comenzando la grabación...')
            fs = 44100  # Frecuencia de muestreo
            audio_data = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype=np.int16)
            sd.wait()
            print('Grabación finalizada.')
            sd.write('audio.wav', audio_data, fs)
            print('Archivo de audio grabado correctamente')
        except:
            print('Error al grabar el audio')

    elif opcion == 2:  # Reproducción de audio
        try:
            data, fs = sd.read('audio.wav')
            sd.play(data, fs)
            sd.wait()
        except:
            print('Error al reproducir el audio')

    elif opcion == 3:  # Gráfico de audio
        try:
            data, fs = sd.read('audio.wav')
            tiempo = np.linspace(0, len(data) / fs, len(data))
            plt.plot(tiempo, data)
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Amplitud')
            plt.title('Audio')
            plt.show()
        except:
            print('Error al graficar el audio')

    elif opcion == 4:  # Graficando espectro de frecuencia
        try:
            print('Graficando espectro de frecuencia...')
            audio, fs = sd.read('audio.wav')
            N = len(audio)
            f = np.linspace(0, fs / 2, N // 2 + 1)
            ventana = np.hanning(N)
            Sxx, _ = plt.psd(audio, NFFT=N, Fs=fs, window=ventana, noverlap=0)
            plt.xlabel('Frecuencia (Hz)')
            plt.ylabel('Densidad espectral de potencia (dB/Hz)')
            plt.title('Espectro de frecuencia de la señal grabada')
            plt.show()
        except:
            print('Error al graficar el audio.')

    elif opcion == 5:  # Salir
        print('Saliendo del programa...')
    else:
        print('Opción no válida.')

