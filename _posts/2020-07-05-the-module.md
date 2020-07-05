---
layout: post
title: "Acerca del módulo"
---

Para abrir el Notebook en **Google Colab**:

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


# [](#header-2) Reproducción de audio a velocidad rápida o lenta:

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


# [](#header-3) Reproducción de audio desde atrás:
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

# [](#header-4) Filtros EMA de paso bajo y paso alto

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
