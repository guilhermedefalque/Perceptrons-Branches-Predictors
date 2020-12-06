import numpy as np
class CorrelacaoPerseptron2:
  def __init__(self, caminho):
    self.quantidade_linhas = 8012
    # w1, w2, w3, w4, historico0, historico1, historico2, historico3, w0
    # self.Lista_Predicoes_Predi = [[peso_incial, peso_incial, peso_incial, peso_incial, peso_incial, peso_incial, peso_incial, peso_incial, peso_incial]] * self.quantidade_linhas
    self.Lista_Predicoes_Predi = np.ones((self.quantidade_linhas, 9), dtype=int)
    self.bias = 1
    self.tamTabHistorico = 4
    self.Alpha = self.tamTabHistorico * 1.96 + 14

    self.caminhoEntradaTreino = caminho


    self.acertos = 0
    self.numeroDeInstrucoes = 0

    self.quantidade_instruction_0 = 0
    self.quantidade_instruction_1 = 0
    self.quantidade_instruction_2 = 0
    self.quantidade_instruction_3 = 0
    self.quantidade_instruction_4 = 0
    self.quantidade_instruction_5 = 0
    self.quantidade_instruction_6 = 0
    self.quantidade_instruction_7 = 0

  def analiseGeral(self, endereco_instrucao, tipo_Instrucao, tomado):
    resto = endereco_instrucao % (self.quantidade_linhas)
    if tomado == 0:
      tomado = -1

    quartaUltimaPredicao = self.Lista_Predicoes_Predi[resto][7]
    terceiraUltimaPredicao = self.Lista_Predicoes_Predi[resto][6]
    segundaUltimaPredicao = self.Lista_Predicoes_Predi[resto][5]
    primeiraUltimaPredicao = self.Lista_Predicoes_Predi[resto][4]

    self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

    Lista0 = (self.Lista_Predicoes_Predi[resto][0]) * primeiraUltimaPredicao
    Lista1 = (self.Lista_Predicoes_Predi[resto][1]) * segundaUltimaPredicao
    Lista2 = (self.Lista_Predicoes_Predi[resto][2]) * terceiraUltimaPredicao
    Lista3 = (self.Lista_Predicoes_Predi[resto][3]) * quartaUltimaPredicao
    w0 = self.Lista_Predicoes_Predi[resto][8]

    soma = Lista0 + Lista1 + Lista2 + Lista3 + w0

    if (soma > 0):
      previsao_atual = 1
    else:
      previsao_atual = -1
    if previsao_atual == tomado:
      self.acertos = self.acertos + 1
      if (tipo_Instrucao == 0):
        self.quantidade_instruction_0 = self.quantidade_instruction_0 + 1
      elif (tipo_Instrucao == 1):
        self.quantidade_instruction_1 = self.quantidade_instruction_1 + 1
      elif (tipo_Instrucao == 2):
        self.quantidade_instruction_2 = self.quantidade_instruction_2 + 1
      elif (tipo_Instrucao == 3):
        self.quantidade_instruction_3 = self.quantidade_instruction_3 + 1
      elif (tipo_Instrucao == 4):
        self.quantidade_instruction_4 = self.quantidade_instruction_4 + 1
      elif (tipo_Instrucao == 5):
        self.quantidade_instruction_5 = self.quantidade_instruction_5 + 1
      elif (tipo_Instrucao == 6):
        self.quantidade_instruction_6 = self.quantidade_instruction_6 + 1
      elif (tipo_Instrucao == 7):
        self.quantidade_instruction_7 = self.quantidade_instruction_7 + 1
      
      if (soma < 0):
        soma = soma * -1
      if (soma < self.Alpha):
        self.Lista_Predicoes_Predi[resto][8] = self.Lista_Predicoes_Predi[resto][8] + self.bias * tomado
        self.Lista_Predicoes_Predi[resto][0] = self.Lista_Predicoes_Predi[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi[resto][1] = self.Lista_Predicoes_Predi[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi[resto][2] = self.Lista_Predicoes_Predi[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi[resto][3] = self.Lista_Predicoes_Predi[resto][3] + tomado * quartaUltimaPredicao
    else:
        self.Lista_Predicoes_Predi[resto][8] = self.Lista_Predicoes_Predi[resto][8] + self.bias * tomado
        self.Lista_Predicoes_Predi[resto][0] = self.Lista_Predicoes_Predi[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi[resto][1] = self.Lista_Predicoes_Predi[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi[resto][2] = self.Lista_Predicoes_Predi[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi[resto][3] = self.Lista_Predicoes_Predi[resto][3] + tomado * quartaUltimaPredicao

    self.Lista_Predicoes_Predi[resto][7] = terceiraUltimaPredicao
    self.Lista_Predicoes_Predi[resto][6] = segundaUltimaPredicao
    self.Lista_Predicoes_Predi[resto][5] = primeiraUltimaPredicao
    self.Lista_Predicoes_Predi[resto][4] = previsao_atual

  def retornaAcerto(self, cont0, cont1, cont2, cont3, cont4, cont5, cont6, cont7):
    print("Total de instrucoes", self.numeroDeInstrucoes, (float(self.acertos) / (self.numeroDeInstrucoes)) * 100)

    if cont0 != 0:
      print("Tipo 0", cont0, (self.quantidade_instruction_0 / float(cont0)) * 100)
    if cont1 != 0:
      print("Tipo 1", cont1, (self.quantidade_instruction_1 / float(cont1)) * 100)
    if cont2 != 0:
      print("Tipo 2", cont2, (self.quantidade_instruction_2 / float(cont2)) * 100)
    if cont3 != 0:
      print("Tipo 3", cont3, (self.quantidade_instruction_3 / float(cont3)) * 100)
    if cont4 != 0:
      print("Tipo 4", cont4, (self.quantidade_instruction_4 / float(cont4)) * 100)
    if cont5 != 0:
      print("Tipo 5", cont5, (self.quantidade_instruction_5 / float(cont5)) * 100)
    if cont6 != 0:
      print("Tipo 6", cont6, (self.quantidade_instruction_6 / cont6) * 100)
    if cont7 != 0:
      print("Tipo 7", cont7, (self.quantidade_instruction_7 / cont7) * 100)

  def treinaModelo(self):
    ref_arquivo = open(self.caminhoEntradaTreino, "r")
    cont0 = 0
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0

    while True:
      v = ref_arquivo.readline()
      # print(v)
      if v:
        dados = v.split(":")
        # print(v)
        self.analiseGeral(int(dados[0]), int(dados[3]), int(dados[1]))
        if (dados[3] == "0\n"):
          cont0 = cont0 + 1
        if (dados[3] == "1\n"):
          cont1 = cont1 + 1
        if (dados[3] == "2\n"):
          cont2 = cont2 + 1
        if (dados[3] == "3\n"):
          cont3 = cont3 + 1
        if (dados[3] == "4\n"):
          cont4 = cont4 + 1
        if (dados[3] == "5\n"):
          cont5 = cont5 + 1
        if (dados[3] == "6\n"):
          cont6 = cont6 + 1
        if (dados[3] == "7\n"):
          cont7 = cont7 + 1

      else:
        break
    ref_arquivo.close()
    print("Retorna Acerto: ")
    self.retornaAcerto(cont0, cont1, cont2, cont3, cont4, cont5, cont6, cont7)