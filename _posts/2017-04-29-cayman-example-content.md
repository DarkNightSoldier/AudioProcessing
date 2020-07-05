---
layout: post
title: "Acerca del módulo"
---

Para abrir el Notebook en **Google Colab**: 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

# [](#header-1) 1. Algunas funciones del módulo
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

    """
```
#### Demostración reproducción audio a velocidad lenta
```python
Speed_Rep("Happy.wav",Velocidad=0.9,"slow.wav")
```
*Se guardó con éxito el archivo como slow.wav*
{% include slow.html %}

### [](#header-3)Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### [](#header-4)Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### [](#header-5)Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### [](#header-6)Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
