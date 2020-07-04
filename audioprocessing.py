from scipy.io import wavfile
import numpy as np
import IPython.display as ipd
from scipy.fftpack import *
import matplotlib.pyplot as plt

# Creado: 3rd July 2020
#         por: Alejandro Higuera Castro

# Módulo para la edicion de audio en formato WAV
# Usa las funciones de la libreria Numpy y Scipy para la edición de audio

def playAudio(file):
    """
    Muestra en pantalla el reproductor de iPython Display para un archivo de
    formato .wav.

    Parámetros
    ----------
    file: string
        Nombre del archivo en formato .wav que contiene audio en formato
        mono o estéreo.
    """
    ipd.audio(file)

def ReadAudio(file):
    """
    Retorna la tasa de muestras por minuto y la matriz con los datos del audio}
    en formato mono o estéreo.

    Parámetros
    ----------
    file: string
        Nombre del archivo en formato .wav que contiene audio en formato
        mono o estéreo.
    """
    rate,data=wavfile.read(file)
    return [rate,data]

def WriteAudio(filename,matrix,rate):
    """
    Escribe un archivo de audio .wav a partir de una matriz numpy con los datos
    del audio en mono o estéreo y la tasa de muestras por segundo.

    Parámetros
    ----------
    filename: string
        Nombre del archivo de salida .wav.
    matrix: numpy ndarray
        Matriz con audio en mono o estéreo.
    rate: int
        Tasa de muestras por minuto del audio.
    """
    wavfile.write(filename,rate,matrix)

def ConvertToMono(file):
    """
    Retorna un array de Numpy con la matriz de audio convertida a mono con el
    mismo dtype de Numpy que el original.

    Parámetros
    ----------
    file: string
        Nombre del archivo en formato .wav que contiene audio en formato
        mono o estéreo.
    """
    #Se procede a leer el audio
    rate,data=ReadAudio(file)
    canales=data.shape[1]

    if canales==1:
        pass
    #En caso de que el audio sea de formato estéreo procede a su conversión
    elif canales==2:
        mono=[]
        stereo_dtype=data.dtype
        #Se obtienen los vectores correspondientes a cada canal de audio
        l=data[:,0]
        r=data[:,1]
        data=data.astype(float)
        #Se suma cada canal de audio para obtener uno solo
        for i in range(len(original)):
            d=(l[i]/2)+(r[i]/2)
            mono.append(d)
        data=np.array(mono,dtype=stereo_dtype)
        WriteAudio(file,rate,data)
    print(f"El archivo se convirtió con éxito y se guardó como {file}")

def Speed_Rep(input_filename,speed,output_filename):
    """
    Muestra en pantalla el reproductor de audio y guarda el audio con la
    velocidad dada por el usuario para el archivo .wav estipulado.

    Parámetros
    ----------
    input_filename: string
         Nombre o localización/path del archivo .wav de entrada.
    speed: float
        Velocidad con la que se va a reproducir el audio de destino.
    output_filename: string
         Nombre o localización/path del archivo .wav de salida
    """
    data,rate=ReadAudio(file)
    actual_speed=1/speed
    wavfile.write(output_filename,int(rate/Velocidad),data)
    print(f"El archivo se guardo con éxito como {output_filename}")
    playAudio(output_filename)

def Lowpass(data,alpha):
    """
    Filtro exponencial EMA de paso bajo que recibe una matriz con audio en
    mono y retorna una matriz con audio en mono del mismo tipo con el Filtro
    aplicado.

    Parámetros
    ----------
    data: Matriz Numpy ndarray
         Matriz con los datos de un audio mono.
    alpha: float
         Factor entre 0 y 1 que determina el suavizado y aplicación del filtro.
    """
    f0=alpha*data[0]
    filtered=[f0]
    for i in range (1,len(data)):
        #y[i] := α * x[i] + (1-α) * y[i-1]
        f=alpha*data[i]+(1-alpha)*filtered[i-1]
        filtered.append(f)
    return np.array(filtered,dtype=data.dtype)

def Highpass(data,alpha):
    """
    Filtro exponencial EMA de paso alto que recibe una matriz con audio en
    mono y retorna una matriz con audio en mono del mismo tipo con el Filtro
    aplicado.

    Parámetros
    ----------
    data: Matriz Numpy ndarray
         Matriz con los datos de un audio mono.
    alpha: float
         Factor entre 0 y 1 que determina el suavizado y aplicación del filtro.
    """
    f_Lowpass=Lowpass(data,alpha)
    filtered=[]
    for i in range(len(data)):
        f=data[i]-f_Lowpass[i]
        filtered.append(f)
    return np.array(filtered,dtype=data.dtype)

def Frequency_Cutoff(type,frequency,input_filename,output_filename):
    """
    Aplica el filtro exponencial EMA de acuerdo al tipo especificado por el
    usuario (Lowpass o Highpass).

    Parámetros
    ----------
    type: string
        Tipo de filtro (Paso bajo o paso alto).
    frequency: float
        Frecuencia de corte para aplicación de filtro.
    input_filename: string
         Nombre o localización/path del archivo .wav de entrada.
    output_filename: string
         Nombre o localización/path del archivo .wav de salida
    """
    pass

def FFT_Graphing(Graph_Title,data_1,rate_1,audio1_title,data_2,rate_2,audio2_title):
    """
    Grafica la transformada de fourier de dos audios, donde el eje x se
    muestra como la frecuencia en Hertz y el eje y la amplitud. Esto permite
    comparar de manera objetiva dos audios en su dominio frecuencia.

    Parámetros
    ----------
    Graph_Title: string
        Título de la gráfica.
    data_1: numpy ndarray
        Matriz con audio en mono.
    rate_1: int
        Muestras por segundo del audio.
    audio1_title: string
        Nombre a mostrar en la gráfica.
    data_2: numpy ndarray
        Matriz con audio en mono.
    rate_2: int
            Muestras por segundo del audio.
    audio2_title: string
        Nombre a mostrar en la gráfica.
    """
    plt.title("Graph_Title")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")

    fft_data_1=abs(fft(data_1))
    frecs_1=fftfreq(len(fft_data_1),(1/rate_1))
    plt.plot(frecs_1[:(len(fft_data_1)//2)],fft_data_1[:(len(fft_data_1)//2)])

    fft_data_2=abs(fft(data_2))
    frecs_2=fftfreq(len(fft_data_2),(1/rate_2))
    plt.plot(freqs[:(len(fft_data_2)//2)],fft_data_2[:(len(fft_data_2)//2)])
    plt.show()
