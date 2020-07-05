---
layout: post
title: "Acerca del módulo"
---

Para abrir el Notebook en **Google Colab**:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

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
*Se guardó con éxito el archivo como slow.wav*
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
### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)
