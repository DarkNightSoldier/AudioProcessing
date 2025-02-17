[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DarkNightSoldier/AudioProcessing/master?filepath=Procesamiento_Audio.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DarkNightSoldier/AudioProcessing/blob/master/Procesamiento_Audio.ipynb)
[![Open In NbViewer](https://user-images.githubusercontent.com/2791223/29387450-e5654c72-8294-11e7-95e4-090419520edb.png)](https://nbviewer.jupyter.org/github/DarkNightSoldier/AudioProcessing/blob/master/Procesamiento_Audio.ipynb)
[![PyPI version](https://badge.fury.io/py/ColabAudioProcessing.svg)](https://badge.fury.io/py/ColabAudioProcessing)

<p align="center"><img src="https://alejandrohiguera.codes/AudioProcessing/files/banner-cs.svg" width="100%"></p>

# Notebook para la manipulación de audio WAV en Google Colaboratory

**Nombre:** Alejandro Higuera Castro

**Fecha de publicación** 6 de julio de 2020

**Versión** 1.2

### *Link a PyPi:* [pypi.org/project/ColabAudioProcessing](https://pypi.org/project/ColabAudioProcessing)
### *Github Page del proyecto:* [alejandrohiguera.codes/AudioProcessing](https://alejandrohiguera.codes/AudioProcessing/)
### *Repositorio del módulo* [github.com/DarkNightSoldier/ColabAudioProcessing](https://github.com/DarkNightSoldier/ColabAudioProcessing)
### *Repositorio del Notebook de G. Colab* [github.com/DarkNightSoldier/AudioProcessing](https://github.com/DarkNightSoldier/AudioProcessing)


## Contenido

1. [Introducción](#1-introducción)
2. [Instalación del módulo](#2-instalación-del-módulo)
3. [Algunas funcionalidades](#3-algunas-funcionalidades)

## 1. Introducción

Como proyecto para el curso de Introducción a las Ciencias de la Computación en el semestre 2020-1S desarrollé un notebook en Google Colaboratory para el análisis y modificación de audio en un formato wav, que viene acompañado del módulo **colabaudiopr_es** para proveer un diseño modular al Notebook, el cuál está disponible para su instalación desde pip.

El módulo **colabaudiopr_es** provee herramientas básicas y facilidades para la edición y análisis de audio en formato .wav. Puede ser instalado con el instalador de Paquetes de Python (PIP), dado que se encuentra publicado en el Índice de paquetes de Python pipy.org. Este integra las librerias Numpy, Scipy y Matplotlib para desplegar más de 10 funciones integradas que son muy útiles para la manipulación de archivos en el formato .wav.

## 2. Instalación del módulo
Para el instalar el módulo use el Instalador de Paquetes de Python (PIP).

```python
pip install ColabAudioProcessing
```

Posteriormente importe todas las funciones de la libreria:
```python
from ColabAudioProcessing.audio import *
```

## 3. Algunas funcionalidades
Se puede leer en detalle acerca de las funcionalidades del proyecto en [alejandrohiguera.codes/AudioProcessing/acerca.html](https://alejandrohiguera.codes/AudioProcessing/acerca.html).

1. [Reproducción de audio](https://alejandrohiguera.codes/AudioProcessing/acerca.html#1-reproducción-de-audio)
    1. [Código de la función](https://alejandrohiguera.codes/AudioProcessing/acerca.html#11-código-de-la-función)
    2. [Demostración](https://alejandrohiguera.codes/AudioProcessing/acerca.html#12-demostración)
2. [Funciones de lectura y escritura de audio](https://alejandrohiguera.codes/AudioProcessing/acerca.html#2-funciones-de-lectura-y-escritura-de-audio)
    1. [Función de lectura de audio](https://alejandrohiguera.codes/AudioProcessing/acerca.html#21-lectura-de-audio)
    2. [Función de escritura de audio](https://alejandrohiguera.codes/AudioProcessing/acerca.html#22-escritura-de-audio)
    3. [Función de conversión de estéreo a mono](https://alejandrohiguera.codes/AudioProcessing/acerca.html#23-conversión-de-estéreo-a-mono)
3. [Reproducción de audio a velocidad rápida o lenta](https://alejandrohiguera.codes/AudioProcessing/acerca.html#3-reproducción-de-audio-a-velocidad-rápida-o-lenta)
    1. [Funcionamiento](https://alejandrohiguera.codes/AudioProcessing/acerca.html#31-funcionamiento)
    2. [Código de la función](https://alejandrohiguera.codes/AudioProcessing/acerca.html#32-código-de-la-función)
    3. [Demostración reproducción audio a velocidad lenta](https://alejandrohiguera.codes/AudioProcessing/acerca.html#33-demostración-reproducción-audio-a-velocidad-lenta)
    4. [Demostración reproducción audio a velocidad rápida](https://alejandrohiguera.codes/AudioProcessing/acerca.html#34-demostración-reproducción-audio-a-velocidad-rápida)
4. [Reproducción de audio hacia atrás](https://alejandrohiguera.codes/AudioProcessing/acerca.html#4-reproducción-de-audio-hacia-atrás)
    1. [Funcionamiento](https://alejandrohiguera.codes/AudioProcessing/acerca.html#41-funcionamiento)
    2. [Código de la función](https://alejandrohiguera.codes/AudioProcessing/acerca.html#42-código-de-la-función)
    3. [Demostración](https://alejandrohiguera.codes/AudioProcessing/acerca.html#43-demostración)
5. [Graficación comparativa de dos señales y su transformada de fourier](https://alejandrohiguera.codes/AudioProcessing/acerca.html#5-graficación-comparativa-de-dos-señales-y-su-transformada-de-fourier)
    1. [Funcionamiento](https://alejandrohiguera.codes/AudioProcessing/acerca.html#51-funcionamiento)
    2. [Código de la función graficación comparativa](https://alejandrohiguera.codes/AudioProcessing/acerca.html#52-código-de-la-función-de-graficación-comparativa)
    3. [Demostración graficación comparativa](https://alejandrohiguera.codes/AudioProcessing/acerca.html#53-demostración-graficación-comparativa)
    4. [Código de la función graficación comparativa FFT](https://alejandrohiguera.codes/AudioProcessing/acerca.html#54-código-de-la-función-de-graficación-comparativa-fft)
    5. [Demostración graficación comparativa FFT](https://alejandrohiguera.codes/AudioProcessing/acerca.html#55-demostración-graficación-comparativa-fft)
6. [Filtros EMA de paso bajo y paso alto](https://alejandrohiguera.codes/AudioProcessing/acerca.html#6-filtros-ema-de-paso-bajo-y-paso-alto)
    1. [Funcionamiento del filtro de paso bajo](https://alejandrohiguera.codes/AudioProcessing/acerca.html#61-funcionamiento-del-filtro-de-paso-bajo)
        * [Código de la función](https://alejandrohiguera.codes/AudioProcessing/acerca.html#611-código-de-la-función)
    2. [Funcionamiento del filtro de paso alto](https://alejandrohiguera.codes/AudioProcessing/acerca.html#62-funcionamiento-del-filtro-de-paso-alto)
        * [Código de la función](https://alejandrohiguera.codes/AudioProcessing/acerca.html#621-código-de-la-función))
    3. [Factor alpha y la frecuencia de corte en el filtrado](https://alejandrohiguera.codes/AudioProcessing/acerca.html#63-factor-alpha-y-la-frecuencia-de-corte-en-el-filtrado)
        * [Factor alpha y variación del filtrado de paso bajo](https://alejandrohiguera.codes/AudioProcessing/acerca.html#631-factor-alpha-y-variación-del-filtrado-de-paso-bajo)
        * [Factor alpha y variación del filtrado de paso alto](https://alejandrohiguera.codes/AudioProcessing/acerca.html#632-factor-alpha-y-variación-del-filtrado-de-paso-alto)
        * [Relación del factor alpha y la frecuencia de corte](https://alejandrohiguera.codes/AudioProcessing/acerca.html#633-relación-del-factor-alpha-y-la-frecuencia-de-corte)
    4. [Ecualización de frecuencias bajas y altas](https://alejandrohiguera.codes/AudioProcessing/acerca.html#64-ecualización-de-frecuencias-bajas-y-altas)
        * [Demostración](https://alejandrohiguera.codes/AudioProcessing/acerca.html#641-demostración)
    5. [Reducción de ruido de alta frecuencia](https://alejandrohiguera.codes/AudioProcessing/acerca.html#65-reducción-de-ruido-de-alta-frecuencia)
        * [Demostración](https://alejandrohiguera.codes/AudioProcessing/acerca.html#651-demostración)
7. [Combinación de dos archivos de audio](https://alejandrohiguera.codes/AudioProcessing/acerca.html#7-combinación-de-dos-archivos-de-audio)
    1. [Funcionamiento](https://alejandrohiguera.codes/AudioProcessing/acerca.html#71-funcionamiento)
    2. [Código de la función](https://alejandrohiguera.codes/AudioProcessing/acerca.html#72-código-de-la-función)
    3. [Demostración](https://alejandrohiguera.codes/AudioProcessing/acerca.html#73-demostración)
    
8. Ajuste de volumen de audio.
