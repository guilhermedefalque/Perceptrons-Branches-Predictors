import numpy as np
from ClassCorrelacaoPerseptron5 import CorrelacaoPerseptron5

if __name__ == '__main__':
  caminho = "/home/guilherme/Downloads/Tracos/lame/trace_lame_larger.txt"

  c2 = CorrelacaoPerseptron5(caminho)

  print("Perceptron 5 treinando")
  c2.treinaModelo()