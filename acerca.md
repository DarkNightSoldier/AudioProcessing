---
layout: page
title: Acerca
tagline: Algunas demostraciones e información de las funciones del módulo
permalink: /acerca.html
ref: acerca
order: 0
---

Para abrir el Notebook en **Google Colaboratory**:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DarkNightSoldier/AudioProcessing/blob/master/Procesamiento_Audio.ipynb)

# Contenido:
1. [Reproducción de audio](#1-reproducción-de-audio)
  * [Código de la función](#código-de-la-función)
  * [Demostración](#demostración)
2. [Funciones de lectura y escritura de audio](#2-funciones-de-lectura-y-escritura-de-audio)
  * [Funcionamiento](#funcionamiento)
  * [Código de la función](#código-de-la-función-1)
3. [Reproducción de audio a velocidad rápida o lenta](#3-reproducción-de-audio-a-velocidad-rápida-o-lenta)
  * [Funcionamiento](#funcionamiento-1)
  * [Código de la función](#código-de-la-función-2)
  * [Demostración reproducción audio a velocidad lenta](#demostración-reproducción-audio-a-velocidad-lenta)
  * [Demostración reproducción audio a velocidad rápida](#demostración-reproducción-audio-a-velocidad-rápida)
4. [Reproducción de audio hacia atrás](#4-reproducción-de-audio-hacia-atrás)
  * [Funcionamiento](#funcionamiento-2)
  * [Código de la función](#código-de-la-función-3)
  * [Demostración](#demostración-1)
5. [Graficación comparativa de dos señales y su transformada de fourier](#5-graficación-comparativa-de-dos-señales-y-su-transformada-de-fourier)
  * [Funcionamiento](#funcionamiento-3)
  * [Código de la función graficación comparativa](#código-de-la-función-de-graficación-comparativa)
  * [Demostración graficación comparativa](#demostración-x)
  * [Código de la función graficación comparativa FFT](#código-de-la-función-de-graficación-comparativa-fft)
  * [Demostración graficación comparativa FFT](#demostración-y)
6. [Filtros EMA de paso bajo y paso alto](#6-filtros-ema-de-paso-bajo-y-paso-alto)
  * [Funcionamiento del filtro de paso bajo](#funcionamiento-del-filtro-de-paso-bajo)
    * [Código de la función](#código-de-la-funcion-4)
  * [Funcionamiento del filtro de paso alto](#funcionamiento-del-filtro-de-paso-alto)
    * [Código de la función](#código-de-la-funcion-5)
  * [Factor alpha y la frecuencia de corte en el filtrado](#factor-alpha-y-la-frecuencia-de-corte-en-el-filtrado)
    * [Factor alpha y variación del filtrado de paso bajo](#factor-alpha-y-variación-del-filtrado-de-paso-bajo)
    * [Factor alpha y variación del filtrado de paso bajo](#factor-alpha-y-variación-del-filtrado-de-paso-bajo)
    * [Relación del factor alpha y la frecuencia de corte](#relación-del-factor-alpha-y-la-frecuencia-de-corte)
  * [6.1. Ecualización de frecuencias bajas y altas]()
    * [Demostración](#demostración-2)
  * [6.2. Reducción de ruido de alta frecuencia]()
    * [Demostración](demostración-3)
7. [Combinación de dos archivos de audio](#7-combinación-de-dos-archivos-de-audio)
  * [Funcionamiento](#funcionamiento-3)
  * [Código de la función](#código-de-la-funcion-6)
  * [Demostración](demostración-4)


# [](#header-1) 1. Reproducción de audio
Él módulo incluye un reproductor de IPython Display, que se puede llamar fácilmente con la función: **playAudio("file.wav")**. Para la demostración se usó una parte de la canción Happy de Pharrel Williams en audio estéreo.

##### Código de la función:
```python
def playAudio(file):
    """
    Muestra en pantalla el reproductor de iPython Display para un archivo de
    formato .wav.

    Parámetros
    ----------
    file: string
        Nombre del archivo en formato .wav que contiene audio en formato
        mono o estéreo.
    Retorna
    ----------
    Reproductor en pantalla de iPython con el audio estipulado

    """

    return ipd.Audio(file)

```

#### Demostración
```python
playAudio("Happy.wav")
```
{% include happy.html %}

# 2. Funciones de lectura y escritura de audio

#### Código de la función:

#### Demostración:

# 3. Reproducción de audio a velocidad rápida o lenta

#### Funcionamiento:
Para reproducir el audio a mayor velocidad basta con aumentar la tasa de muestras por segundo y para disminuirla basta con disminuir la tasa de muestras por segundo.

Él módulo permite la reproducción de audio con la velocidad que estipule el usuario. Para hacerlo basta llamar la función: **Speed_Rep(input_filename,speed,output_filename)**. Para la demostración se usó una parte de la canción Happy de Pharrel Williams en audio estéreo a una velocidad de 0.9 y 1.65.

##### Código de la función:

```python
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

    Retorna
    ----------
    Reproductor en pantalla de iPython con el audio con la velocidad deseada.

    """
    rate,data=ReadAudio(input_filename)
    WriteAudio(output_filename,int(rate*speed),data)
    print(f"El archivo se guardo con éxito como {output_filename}")
    return playAudio(output_filename)

```
#### Demostración reproducción audio a velocidad lenta
```python
Speed_Rep("Happy.wav",Velocidad=0.9,"slow.wav")
```
*Se guardó con éxito el archivo como slow.wav*
{% include slow.html %}

#### Demostración reproducción audio a velocidad rápida
```python
Speed_Rep("Happy.wav",Velocidad=1.65,"fast.wav")
```
*Se guardó con éxito el archivo como fast.wav*
{% include fast.html %}


# 4. Reproducción de audio hacia atrás
#### Funcionamiento:
Para reproducir el audio hacia atrás basta con leer la matriz desde atrás hacia adelante, conservando la misma tasa de muestras por segundo.

Él módulo permite la reproducción de audio hacia atrás y guardar el archivo con el audio resultante. Para hacerlo basta llamar la función: **Inverse_Rep(input_filename,output_filename)**.
##### Código de la función:
```python
def Inverse_Rep(input_filename,output_filename):
    """
    Muestra en pantalla el reproductor de audio y guarda el audio reproducido
    desde atrás en el archivo .wav estipulado.

    Parámetros
    ----------
    input_filename: string
         Nombre o localización/path del archivo .wav de entrada.
    output_filename: string
         Nombre o localización/path del archivo .wav de salida
    """

    rate,data=ReadAudio(input_filename)
    #Convertimos a mono el audio original
    data=ConvertToMono(data)
    #Leemos la matriz desde atrás usando la notación de slicing de listas
    WriteAudio(output_filename,rate,data[::-1])
    print(f"El archivo se guardo con éxito como {output_filename}")
    return playAudio(output_filename)
```
#### Demostración:
```python
Inverse_Rep("Happy.wav","inverse.wav")
```
*Se guardó con éxito el archivo como inverse.wav*
{% include inverse.html %}

# 5. Graficación comparativa de dos señales y su transformada de fourier

## Funcionamiento

Ajusta el eje x al dominio y escala correcta (Frecuencia (Hz) y Tiempo (s). Posteriormente grafica los datos del audio/señal de un único canal (mono) con ayuda de la libreria Matplotlib, siendo de fácil configuración pues ya vien con los argumentos necesarios para la comparación de dos archivos de audio.

Para graficar comparativamente dos audios basta con llamar llamar la función **AudioGraphing(Graph_Title,data_1,rate_1,audio1_title,data_2,rate_2,audio2_title)** o si desea comparar su transformada rápida de fourier **FFT_Graphing(Graph_Title,data_1,rate_1,audio1_title,data_2,rate_2,audio2_title)**.

## Código de la función de graficación comparativa
```python
def AudioGraphing(Graph_Title,data_1,rate_1,audio1_title,data_2,rate_2,audio2_title):
        """
        Grafica un audio/señal en el dominio tiempo, en el eje y se muestra la
        señal y en el eje x el tiempo.

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

        Retorna
        --------
        Gráfico de Matplotlib con los audios de entrada, en el eje x la amplitud
        y en el eje y el tiempo en segundos.
        """
        plt.title(Graph_Title)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Amplitud')

        data_1=ConvertToMono(data_1)
        tiempo_1=np.arange(len(data_1))/float(rate_1)

        data_2=ConvertToMono(data_2)
        tiempo_2=np.arange(len(data_2))/float(rate_2)

        plt.fill_between(tiempo_1,data_1,color='b',label=audio1_title)
        plt.fill_between(tiempo_2,data_2,color='m',label=audio2_title)
        plt.legend(loc='upper right', borderaxespad=0.)
        plt.show()
```

## Demostración graficación comparativa
```python
AudioGraphing("Señal filtrada VS sin filtrar",data,rate,"Señal sin filtrar",data_2,rate_2,f"Señal filtrada")
```
![Comparative graphing example](https://alejandrohiguera.codes/files/graph7.png)

## Código de la función de graficación comparativa FFT
```python
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

    Retorna
    --------
    Gráfico de Matplotlib con la Transformada Rápida de Fourier de los audios de
    entrada.
    """
    plt.title(Graph_Title)
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")

    fft_data_1=abs(fft(data_1))
    frecs_1=fftfreq(len(fft_data_1),(1/rate_1))
    x1=frecs_1[:(len(fft_data_1)//2)]
    y1=fft_data_1[:(len(fft_data_1)//2)]

    fft_data_2=abs(fft(data_2))
    frecs_2=fftfreq(len(fft_data_2),(1/rate_2))
    x2=frecs_2[:(len(fft_data_2)//2)]
    y2=fft_data_2[:(len(fft_data_2)//2)]

    plt.plot(x1,y1,color="r",label=audio1_title)
    plt.plot(x2,y2,color="g",label=audio2_title)
    plt.legend(loc='upper right', borderaxespad=0.)
    plt.show()
```

## Demostración graficación comparativa FFT
Poder graficar las frecuencias de dos audios mediante la transformada rápida defourier brinda información valiosa acerca del contenido de los dos audios a comparar.

```python
AudioGraphing("Señal filtrada VS sin filtrar",data,rate,"Señal sin filtrar",data_2,rate_2,f"Señal filtrada")
```
![Comparative fft graphing example](https://alejandrohiguera.codes/files/graph8.png)

# 6. Filtros EMA de paso bajo y paso alto

![Filtros de paso bajo y alto](https://i.stack.imgur.com/UJOhE.gif)

El filtro EMA suaviza la señal en base a los más recientes puntos de datos más recientes y realiza un promedio móvil ponderado.

Un filtro EMA o de media móvil exponencial es uno de los filtros digitales más fáciles de implementar, principalmente por:
1. Su facilidad para implementar.
2. Poco uso de CPU.
3. Se puede configurar fácilmente un filtrado de paso bajo o paso alto.

## Funcionamiento del filtro de paso bajo
![Filtros de paso bajo](http://www.dsprelated.com/josimages_new/filters/img85.png)

Este tipo de filtro se caracteriza por el paso de las frecuencias más bajas y la atenuación de las frecuencias más altas, lo que lo posiciona como útil para la disminución del ruido de alta frecuencia.

El filtro EMA de paso bajo consiste en obtener un valor filtrado a partir de la aplicación de la siguiente expresión con cada uno de los datos de la matriz del audio mono:

y[i]= alpha*x[i] + (1-alpha) * y[i-1]

Donde:
- y[i]=Valor filtrado.
- alpha=Factor de filtrado (0-1).
- x[i]=Valor muestreado de la señal.
- y[i-1]=Valor filtrado anterior.

### Código de la función:
```python
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

    Retorna
    ----------
    filtered: numpy ndarray
        Matriz de Numpy que contiene audio en mono filtrado, con el mismo dtype
        del original.
    """
    f0=alpha*data[0]
    filtered=[f0]
    for i in range (1,len(data)):
        #y[i] := α * x[i] + (1-α) * y[i-1]
        f=alpha*data[i]+(1-alpha)*filtered[i-1]
        filtered.append(f)

    filtered=np.array(filtered,dtype=data.dtype)
    return filtered
```
## Funcionamiento del filtro de paso alto:

![Filtros de paso alto](https://microcontrollerslab.com/wp-content/uploads/2018/11/2-Bode-of-high-pass-filter.jpg)

Este tipo de filtro se caracteriza por el paso de las frecuencias más altas y la atenuación de las frecuencias más bajas, lo que lo posiciona como útil para la disminución del ruido de baja frecuencia.

El filtro EMA de paso alto consiste en obtener un valor filtrado a partir de la aplicación de la siguiente expresión con cada uno de los datos de la matriz del audio mono:

y[i]=x[i]-lowpass[i]

Es decir:

y[i]=x[i]-(alpha*x[i] + (1-alpha) * y[i-1])

Donde:
- y[i]=Valor filtrado.
- alpha=Factor de filtrado (0-1).
- x[i]=Valor muestreado de la señal.
- y[i-1]=Valor filtrado anterior.

### Código de la función:
```python
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

    Retorna
    ----------
    filtered: numpy ndarray
        Matriz de Numpy que contiene audio en mono filtrado, con el mismo dtype
        del original.
    """
    f_Lowpass=Lowpass(data,alpha)
    filtered=[]
    for i in range(len(data)):
        f=data[i]-f_Lowpass[i]
        filtered.append(f)

    filtered=np.array(filtered,dtype=data.dtype)
    return filtered
```
## 4.a) Acerca del factor alpha en el filtrado y la frecuencia de corte:

## Factor alpha y variación del filtrado de paso bajo:
A continuación se muestra algunas variaciones del filtrado al cambiar el factor alpha para el filtro EMA de paso bajo:

![FFT Lowpass alpha=0](https://alejandrohiguera.codes/AudioProcessing/files/fft_low_0.png)
![Lowpass alpha=0](https://alejandrohiguera.codes/AudioProcessing/files/low_0.png)
![FFT Lowpass alpha=0.2](https://alejandrohiguera.codes/AudioProcessing/files/fft_low_01.png)
![Lowpass alpha=0.2](https://alejandrohiguera.codes/AudioProcessing/files/low_01.png)
![FFT Lowpass alpha=0.2](https://alejandrohiguera.codes/AudioProcessing/files/fft_low_02.png)
![Lowpass alpha=0.2](https://alejandrohiguera.codes/AudioProcessing/files/low_02.png)
![FFT Lowpass alpha=0.4](https://alejandrohiguera.codes/AudioProcessing/files/fft_low_04.png)
![Lowpass alpha=0.4](https://alejandrohiguera.codes/AudioProcessing/files/low_04.png)
![FFT Lowpass alpha=0.6](https://alejandrohiguera.codes/AudioProcessing/files/fft_low_06.png)
![Lowpass alpha=0.6](https://alejandrohiguera.codes/AudioProcessing/files/low_06.png)
![FFT Lowpass alpha=0.6](https://alejandrohiguera.codes/AudioProcessing/files/fft_low_06.png)
![Lowpass alpha=0.6](https://alejandrohiguera.codes/AudioProcessing/files/low_06.png)
![FFT Lowpass alpha=0.8](https://alejandrohiguera.codes/AudioProcessing/files/fft_low_08.png)
![Lowpass alpha=0.8](https://alejandrohiguera.codes/AudioProcessing/files/low_08.png)
![FFT Lowpass alpha=1](https://alejandrohiguera.codes/AudioProcessing/files/fft_low_1.png)
![Lowpass alpha=1](https://alejandrohiguera.codes/AudioProcessing/files/low_1.png)

## Factor alpha y variación del filtrado de paso alto:
A continuación se muestra algunas variaciones del filtrado al cambiar el factor alpha para el filtro EMA de paso bajo:

![FFT Highpass alpha=0](https://alejandrohiguera.codes/AudioProcessing/files/fft_hp_0.png)
![Highpass alpha=0](https://alejandrohiguera.codes/AudioProcessing/files/hp_0.png)
![FFT Highpass alpha=0.1](https://alejandrohiguera.codes/AudioProcessing/files/fft_hp_01.png)
![Highpass alpha=0.1](https://alejandrohiguera.codes/AudioProcessing/files/hp_01.png)
![FFT Highpass alpha=0.3](https://alejandrohiguera.codes/AudioProcessing/files/fft_hp_03.png)
![Highpass alpha=0.3](https://alejandrohiguera.codes/AudioProcessing/files/hp_03.png)
![FFT Highpass alpha=0.5](https://alejandrohiguera.codes/AudioProcessing/files/fft_hp_05.png)
![Highpass alpha=0.5](https://alejandrohiguera.codes/AudioProcessing/files/hp_05.png)
![FFT Highpass alpha=0.7](https://alejandrohiguera.codes/AudioProcessing/files/fft_hp_07.png)
![Highpass alpha=0.7](https://alejandrohiguera.codes/AudioProcessing/files/hp_07.png)
![FFT Highpass alpha=0.9](https://alejandrohiguera.codes/AudioProcessing/files/fft_hp_09.png)
![Highpass alpha=0.9](https://alejandrohiguera.codes/AudioProcessing/files/hp_09.png)
![FFT Highpass alpha=1](https://alejandrohiguera.codes/AudioProcessing/files/fft_hp_1.png)
![Highpass alpha=1](https://alejandrohiguera.codes/AudioProcessing/files/hp_1.png)

# [](#header-4b) 4.b) Ecualización de frecuencias bajas y altas.
Para ello se selecciona un factor de filtro alpha y se aplica un filtro EMA LowPass/HighPass.

#### Demostración:
```python
alpha = 0.2 #@param {type:"slider", min:0, max:1, step:0.01}
rate,data=ReadAudio("Happy.wav")
data=ConvertToMono(data)

data_low=Lowpass(data,alpha)
data_high=Highpass(data,alpha)

FFT_Graphing(f"FFT Original vs Low pass α={alpha}",data,rate,"Original",data_low,rate,"Lowpass")
AudioGraphing(f"Original vs Low pass α={alpha}",data,rate,"Original",data_low,rate,"Lowpass")
FFT_Graphing(f"FFT Original vs High pass α={alpha}",data,rate,"Original",data_high,rate,"Highpass")
AudioGraphing(f"Original vs High pass α={alpha}",data,rate,"Original",data_high,rate,"Highpass")
```
![FFT Original VS Low Pass α=0.2](https://alejandrohiguera.codes/AudioProcessing/files/graph1.png)
![Original VS Low Pass α=0.2](https://alejandrohiguera.codes/AudioProcessing/files/graph3.png)
![FFT Original VS High Pass α=0.2](https://alejandrohiguera.codes/AudioProcessing/files/graph2.png)
![Original VS High Pass α=0.2](https://alejandrohiguera.codes/AudioProcessing/files/graph4.png)

##### Ecualización de frecuencias bajas:
```python
print(f"Lowpass α={alpha}")
WriteAudio("lowpass.wav",rate,data_low)
playAudio("lowpass.wav")
```
*Lowpass α=0.2*
{% include lowpass.html %}

##### Ecualización de frecuencias altas:
```python
print(f"Lowpass α={alpha}")
WriteAudio("lowpass.wav",rate,data_low)
playAudio("lowpass.wav")
```
*Highpass α=0.2*
{% include highpass.html %}

# [](#header-4c) 4.c) Limpieza de ruido de alta frecuencia
Para ello se establece una frecuencia (Hz) de corte y se procede a aplicar un filtro EMA de paso bajo.

#### Demostración:
```python
fr=int(input("Especifique la frecuencia de corte en Hz  "))
Frequency_Cutoff("low",fr,"hfnoise.wav","limpieza.wav")
```
*Especifique la frecuencia de corte en Hz* **500**

*α=0.2819698001234662*

*El archivo se guardo con éxito como limpieza.wav*

```python
rate_1,data_1=ReadAudio("hfnoise.wav")
data_1=ConvertToMono(data_1)

rate_2,data_2=ReadAudio("limpieza.wav")
data_2=ConvertToMono(data_2)

FFT_Graphing("FFT Con Ruido VS Lowpass fc",data_1,rate_1,"Audio sin filtrar",data_2,rate_2,f"Lowpass {fr} Hz")
AudioGraphing("Con Ruido VS Lowpass fc",data_1,rate_1,"Audio sin filtrar",data_2,rate_2,f"Lowpass {fr} Hz")
```
![FFT Ruido VS Low Pass 500 Hz](https://alejandrohiguera.codes/AudioProcessing/files/graph5.png)
![Ruido VS Low Pass 500 Hz](https://alejandrohiguera.codes/AudioProcessing/files/graph6.png)

```python
playAudio("hfnoise.wav")
```
{% include hfnoise.html %}

```python
playAudio("limpieza.wav")
```
{% include limpieza.html %}

# 7. Combinación de dos archivos de audio

#### Funcionamiento:
Para reproducir la combinación de dos audios basta con convertir las matrices de los audios a mono, promediar los valores de las matrices de entrada y el número de muestras por segundo.

Él módulo permite la reproducción de un audio que combina los dos audios de entrada y guardar el archivo con el audio resultante. Para hacerlo basta llamar la función: **Inverse_Rep(input_filename,output_filename)**.

##### Código de la función:
```python
def Combinar_Audios(audio1,audio2,output_filename):
    """
    Muestra en pantalla el reproductor de audio y guarda el audio que combina
    los dos audios de entrada.

    Parámetros
    ----------
    audio1: string
         Nombre o localización/path del archivo .wav de entrada.
    audio2: string
         Nombre o localización/path del archivo .wav de entrada.    
    output_filename: string
         Nombre o localización/path del archivo .wav de salida

    Retorna
    ----------
    Reproductor en pantalla de iPython con el audio que comnbina los audios de
    entrada.

    """    
    rate_1,data_1=ReadAudio(audio1)
    rate_2,data_2=ReadAudio(audio2)

    if len(data_1)>len(data_2):
        base_data=data_1.copy()
        insert_data=data_2.copy()
    else:
        base_data=data_2.copy()
        insert_data=data_1.copy()

    for i in range (0,int(len(insert_data))):
        base_data[i]=base_data[i]/2+insert_data[i]/2

    WriteAudio(output_filename,(rate_1+rate_2)//2,base_data)
    print(f"El archivo se guardo con éxito como {output_filename}")
    return playAudio(output_filename)
```
#### Demostración:
Para la demostración se combinó una parte de la canción Happy de Pharrel Williams y de la canción Sweet Lies, en formato mono con una tasa de muestras por segundo de 44100.
```python
Combinar_Audios("Happy.wav","sweet.wav","Combined.wav")
```
{% include combined.html %}


[Volver a la página de inicio]({{ '/' | absolute_url }})
