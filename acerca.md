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

# [](#header-1) 1. Mostrar el reproductor de audio
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


# [](#header-2) 2. Reproducción de audio a velocidad rápida o lenta:

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


# [](#header-3) 3. Reproducción de audio desde atrás:
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
##### Demostración:
```python
Inverse_Rep("Happy.wav","inverse.wav")
```
*Se guardó con éxito el archivo como inverse.wav*
{% include inverse.html %}

# [](#header-4) 4. Filtros EMA de paso bajo y paso alto

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

# [](#header-4a) 4.a) Ecualización de frecuencias bajas y altas.
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

# [](#header-4b) 4.b) Limpieza de ruido de alta frecuencia
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

# [](#header-5) 5. Combinación de dos archivos de audio

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
