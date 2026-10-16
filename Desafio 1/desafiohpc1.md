# DESAFIO 1 - PROGRAMA HPC

## 1. Área escolhida e utilização de HPC

A área de aplicação escolhida foi a **Computação Gráfica**

A renderização é o processo de transformar dados estruturais e matemáticos como modelos tridimensionais, coordenadas, texturas e informações de luz em uma imagem 2D, considerando elementos como geometria, iluminação, materiais, sombras e reflexos.

Nesse contexto, HPC é importante porque a geração de imagens realistas exige uma grande quantidade de cálculos matemáticos. Dependendo da complexidade da cena, esses cálculos podem demandar muito tempo de processamento.

O HPC permite acelerar esse processo por meio de técnicas como o processamento paralelo, utilizando múltiplos núcleos de CPU ou GPUs para distribuir o trabalho computacional.

## 2. Software escolhido e problema que resolve

O software selecionado foi o **pbrt-v4**, um renderizador de código aberto desenvolvido em C++.

Seu principal objetivo é gerar imagens realistas a partir de cenas tridimensionais, utilizando algoritmos que simulam o comportamento físico da luz.

O pbrt-v4 é utilizado principalmente em estudos e pesquisas sobre renderização fisicamente baseada, permitindo experimentar diferentes técnicas de iluminação, materiais e processamento de imagens.

Repositório oficial: https://github.com/mmp/pbrt-v4

## 3. Por que esse problema se beneficia de HPC?

A renderização de imagens pode envolver milhões de pixels, sendo necessário realizar diversos cálculos para determinar a iluminação e a cor de cada um.

Em técnicas como o Path Tracing, são simulados caminhos percorridos pela luz, incluindo reflexões e interações com diferentes superfícies.

Como boa parte desse trabalho pode ser distribuída entre unidades de processamento, a utilização de paralelismo permite reduzir o tempo de renderização.

## 4. Tecnologias e bibliotecas utilizadas

O pbrt-v4 é desenvolvido principalmente em C++ e utiliza o CMake para fazer a compilação.

O projeto também utiliza bibliotecas como OpenEXR, Ptex, Zlib e GLFW, relacionadas a funcionalidades como processamento de imagens, texturas, compressão e suporte gráfico.

O software também possui suporte a CUDA e NVIDIA OptiX para aceleração em GPU.

## 5. Como o software explora o paralelismo

O pbrt-v4 implementa mecanismos de paralelismo que permitem distribuir tarefas de renderização entre diferentes threads da CPU.

Durante a renderização, o processamento da imagem pode ser dividido em blocos, permitindo que diferentes núcleos trabalhem simultaneamente em partes da cena.

O programa também disponibiliza o parâmetro `--nthreads`, que permite controlar a quantidade de threads utilizadas na renderização.

Dessa forma, é possível experimentar diferentes configurações de processamento e avaliar o impacto do paralelismo no tempo necessário para gerar uma imagem.

## 6. Compilação, execução e dificuldades encontradas

A implementação foi realizada em um computador com Windows e GCC/G++ como compilador. Mas não houve dificuldades na compilação, apenas clonei o repositório, utilizei o CMake e foi compilado com sucesso.

## Conclusão

A experiência permitiu compreender como a Computação de Alto Desempenho pode ser aplicada à renderização gráfica.

A utilização do pbrt-v4 demonstrou o funcionamento de um software open source voltado a cálculos computacionalmente intensivos, além de permitir identificar tecnologias e mecanismos utilizados para explorar o processamento paralelo.

Embora o exemplo executado tenha sido relativamente simples, o software possui recursos que permitem trabalhar com cenas mais complexas e explorar diferentes configurações de desempenho.

---

## Diferença de tempo entre execuções

### Execução com 1 thread(29.4s)

```bash
PS C:\Users\luizg\Documents\pbrt-v4> .\build\pbrt.exe --nthreads 1 .\cena.pbrt 
pbrt version 4 (built Oct 14 2026 at 19:33:41)
Copyright (c)1998-2021 Matt Pharr, Wenzel Jakob, and Greg Humphreys.
The source code to pbrt (but *not* the book contents) is covered by the Apache 2.0 License.
See the file LICENSE.txt for the conditions of the license.
Rendering: [++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]  (29.4s)
```
---
### Execução com 8 threads(5.8s)

```bash
PS C:\Users\luizg\Documents\pbrt-v4> .\build\pbrt.exe --nthreads 8 .\cena.pbrt
pbrt version 4 (built Oct 14 2026 at 19:33:41)
Copyright (c)1998-2021 Matt Pharr, Wenzel Jakob, and Greg Humphreys.
The source code to pbrt (but *not* the book contents) is covered by the Apache 2.0 License.
See the file LICENSE.txt for the conditions of the license.
Rendering: [++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]  (5.8s)
``` 