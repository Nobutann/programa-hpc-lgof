# PBRT v4 em Docker e Apptainer

## Integração com o host

A renderização usa apenas CPU, sem MPI ou GPU. O código, a cena [esfera.pbrt](esfera.pbrt) e os PNGs ficam no host, em um diretório montado em `/pbrt` por volume no Docker e por bind mount no Apptainer.

## Comparação de desempenho

No mesmo host, a cena de 640 × 480 foi renderizada com quatro threads, 32 amostras por pixel e compilação `Release`. A tabela mostra a mediana de cinco execuções. O tempo inclui a inicialização do contêiner e a gravação do PNG. O nativo usou GCC 15.2.0 e os contêineres usaram GCC 11.4.0.

| Execução | Mediana | Variação ante o nativo |
|---|---:|---:|
| Nativo | 5,100 s | Referência |
| Docker manual | 5,628 s | +10,4% |
| Apptainer manual | 5,584 s | +9,5% |
| Docker gerado pelo HPCCM | 5,648 s | +10,7% |
| Apptainer gerado pelo HPCCM | 5,452 s | +6,9% |

## Tamanho das imagens e otimizações

As duas imagens Docker têm 201,5 MiB cada, e as duas SIFs do Apptainer têm 195,1 MiB cada. As receitas dispensam pacotes recomendados pelo APT, removem suas listas após a instalação e mantêm código e resultados no host. As SIFs usam compressão SquashFS.

## Dificuldades e soluções

O GLFW exigiu `wayland-scanner`. A compilação foi configurada com `GLFW_BUILD_WAYLAND=OFF` para usar o backend X11 disponível.
