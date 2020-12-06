import numpy as np
class CorrelacaoPerseptron4:
  def __init__(self, caminho):
    self.quantidade_linhas = 8012
    peso_incial = 1  # w1, w2, w3, w4, w5, w6, w7, w8,  historico0, historico1, historico2, historico3, w0
    #historico4, historico5, historico6, historico7
    # self.Lista_Predicoes_Predi = [[peso_incial, peso_incial, peso_incial, peso_incial, peso_incial, peso_incial, peso_incial, peso_incial, peso_incial]] * self.quantidade_linhas
    self.Lista_Predicoes_Predi0 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi1 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi2 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi3 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi4 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi5 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi6 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi7 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi8 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi9 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi10 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi11 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi12 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi13 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi14 = np.ones((self.quantidade_linhas, 17), dtype=int)
    self.Lista_Predicoes_Predi15 = np.ones((self.quantidade_linhas, 17), dtype=int)

    self.bias = 1
    self.tamTabHistorico = 4
    self.Alpha = self.tamTabHistorico * 1.96 + 14
    self.previsoes_anteriores = [1, 1, 1, 1]
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

    if self.previsoes_anteriores[0] == -1 and self.previsoes_anteriores[1] == -1 and self.previsoes_anteriores[
      2] == -1 and self.previsoes_anteriores[3] == -1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi0[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi0[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi0[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi0[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi0[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi0[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi0[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi0[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi0[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi0[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi0[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi0[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi0[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi0[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi0[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi0[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi0[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi0[resto][12] = self.Lista_Predicoes_Predi0[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi0[resto][0] = self.Lista_Predicoes_Predi0[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][1] = self.Lista_Predicoes_Predi0[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][2] = self.Lista_Predicoes_Predi0[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][3] = self.Lista_Predicoes_Predi0[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi0[resto][4] = self.Lista_Predicoes_Predi0[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][5] = self.Lista_Predicoes_Predi0[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][6] = self.Lista_Predicoes_Predi0[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][7] = self.Lista_Predicoes_Predi0[resto][7] + tomado * oitavaUltimaPredicao        
      else:
        self.Lista_Predicoes_Predi0[resto][12] = self.Lista_Predicoes_Predi0[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi0[resto][0] = self.Lista_Predicoes_Predi0[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][1] = self.Lista_Predicoes_Predi0[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][2] = self.Lista_Predicoes_Predi0[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][3] = self.Lista_Predicoes_Predi0[resto][3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi0[resto][4] = self.Lista_Predicoes_Predi0[resto][4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][5] = self.Lista_Predicoes_Predi0[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][6] = self.Lista_Predicoes_Predi0[resto][6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][7] = self.Lista_Predicoes_Predi0[resto][7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi0[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][8] = previsao_atual
    elif self.previsoes_anteriores[0] == -1 and self.previsoes_anteriores[1] == -1 and self.previsoes_anteriores[
      2] == -1 and self.previsoes_anteriores[3] == 1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi1[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi1[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi1[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi1[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi1[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi1[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi1[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi1[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi1[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi1[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi1[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi1[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi1[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi1[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi1[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi1[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi1[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi1[resto][12] = self.Lista_Predicoes_Predi1[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi1[resto][0] = self.Lista_Predicoes_Predi1[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][1] = self.Lista_Predicoes_Predi1[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][2] = self.Lista_Predicoes_Predi1[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][3] = self.Lista_Predicoes_Predi1[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi1[resto][4] = self.Lista_Predicoes_Predi1[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][5] = self.Lista_Predicoes_Predi1[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][6] = self.Lista_Predicoes_Predi1[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][7] = self.Lista_Predicoes_Predi1[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi1[resto][12] = self.Lista_Predicoes_Predi1[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi1[resto][0] = self.Lista_Predicoes_Predi1[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][1] = self.Lista_Predicoes_Predi1[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][2] = self.Lista_Predicoes_Predi1[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][3] = self.Lista_Predicoes_Predi1[resto][3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi1[resto][4] = self.Lista_Predicoes_Predi1[resto][4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][5] = self.Lista_Predicoes_Predi1[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][6] = self.Lista_Predicoes_Predi1[resto][6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][7] = self.Lista_Predicoes_Predi1[resto][7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi1[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == -1 and self.previsoes_anteriores[1] == -1 and self.previsoes_anteriores[
      2] == 1 and self.previsoes_anteriores[3] == -1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi2[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi2[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi2[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi2[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi2[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi2[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi2[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi2[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi2[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi2[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi2[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi2[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi2[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi2[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi2[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi2[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi2[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi2[resto][12] = self.Lista_Predicoes_Predi2[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi2[resto][0] = self.Lista_Predicoes_Predi2[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][1] = self.Lista_Predicoes_Predi2[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][2] = self.Lista_Predicoes_Predi2[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][3] = self.Lista_Predicoes_Predi2[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi2[resto][4] = self.Lista_Predicoes_Predi2[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][5] = self.Lista_Predicoes_Predi2[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][6] = self.Lista_Predicoes_Predi2[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][7] = self.Lista_Predicoes_Predi2[resto][7] + tomado * oitavaUltimaPredicao 
      else:
        self.Lista_Predicoes_Predi2[resto][12] = self.Lista_Predicoes_Predi2[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi2[resto][0] = self.Lista_Predicoes_Predi2[resto][
                                                        0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][1] = self.Lista_Predicoes_Predi2[resto][
                                                        1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][2] = self.Lista_Predicoes_Predi2[resto][
                                                        2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][3] = self.Lista_Predicoes_Predi2[resto][
                                                        3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi2[resto][4] = self.Lista_Predicoes_Predi2[resto][
                                                        4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][5] = self.Lista_Predicoes_Predi2[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][6] = self.Lista_Predicoes_Predi2[resto][
                                                        6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][7] = self.Lista_Predicoes_Predi2[resto][
                                                        7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi2[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == -1 and self.previsoes_anteriores[1] == -1 and self.previsoes_anteriores[
      2] == 1 and self.previsoes_anteriores[3] == 1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi3[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi3[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi3[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi3[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi3[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi3[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi3[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi3[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi3[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi3[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi3[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi3[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi3[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi3[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi3[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi3[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi3[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi3[resto][12] = self.Lista_Predicoes_Predi3[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi3[resto][0] = self.Lista_Predicoes_Predi3[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][1] = self.Lista_Predicoes_Predi3[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][2] = self.Lista_Predicoes_Predi3[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][3] = self.Lista_Predicoes_Predi3[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi3[resto][4] = self.Lista_Predicoes_Predi3[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][5] = self.Lista_Predicoes_Predi3[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][6] = self.Lista_Predicoes_Predi3[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][7] = self.Lista_Predicoes_Predi3[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi3[resto][12] = self.Lista_Predicoes_Predi3[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi3[resto][0] = self.Lista_Predicoes_Predi3[resto][
                                                      0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][1] = self.Lista_Predicoes_Predi3[resto][
                                                      1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][2] = self.Lista_Predicoes_Predi3[resto][
                                                      2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][3] = self.Lista_Predicoes_Predi3[resto][
                                                      3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi3[resto][4] = self.Lista_Predicoes_Predi3[resto][
                                                      4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][5] = self.Lista_Predicoes_Predi3[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][6] = self.Lista_Predicoes_Predi3[resto][
                                                      6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][7] = self.Lista_Predicoes_Predi3[resto][
                                                      7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi3[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == -1 and self.previsoes_anteriores[1] == 1 and self.previsoes_anteriores[2] == -1 and self.previsoes_anteriores[3] == -1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi4[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi4[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi4[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi4[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi4[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi4[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi4[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi4[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi4[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi4[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi4[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi4[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi4[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi4[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi4[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi4[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi4[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi4[resto][12] = self.Lista_Predicoes_Predi4[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi4[resto][0] = self.Lista_Predicoes_Predi4[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][1] = self.Lista_Predicoes_Predi4[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][2] = self.Lista_Predicoes_Predi4[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][3] = self.Lista_Predicoes_Predi4[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi4[resto][4] = self.Lista_Predicoes_Predi4[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][5] = self.Lista_Predicoes_Predi4[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][6] = self.Lista_Predicoes_Predi4[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][7] = self.Lista_Predicoes_Predi4[resto][7] + tomado * oitavaUltimaPredicao 
      else:
        self.Lista_Predicoes_Predi4[resto][12] = self.Lista_Predicoes_Predi4[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi4[resto][0] = self.Lista_Predicoes_Predi4[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][1] = self.Lista_Predicoes_Predi4[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][2] = self.Lista_Predicoes_Predi4[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][3] = self.Lista_Predicoes_Predi4[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi4[resto][4] = self.Lista_Predicoes_Predi4[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][5] = self.Lista_Predicoes_Predi4[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][6] = self.Lista_Predicoes_Predi4[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][7] = self.Lista_Predicoes_Predi4[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi4[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == -1 and self.previsoes_anteriores[1] == 1 and self.previsoes_anteriores[2] == -1 and self.previsoes_anteriores[3] == 1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi5[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi5[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi5[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi5[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi5[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi5[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi5[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi5[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi5[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi5[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi5[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi5[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi5[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi5[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi5[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi5[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi5[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi5[resto][12] = self.Lista_Predicoes_Predi5[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi5[resto][0] = self.Lista_Predicoes_Predi5[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][1] = self.Lista_Predicoes_Predi5[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][2] = self.Lista_Predicoes_Predi5[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][3] = self.Lista_Predicoes_Predi5[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi5[resto][4] = self.Lista_Predicoes_Predi5[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][5] = self.Lista_Predicoes_Predi5[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][6] = self.Lista_Predicoes_Predi5[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][7] = self.Lista_Predicoes_Predi5[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi5[resto][12] = self.Lista_Predicoes_Predi5[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi5[resto][0] = self.Lista_Predicoes_Predi5[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][1] = self.Lista_Predicoes_Predi5[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][2] = self.Lista_Predicoes_Predi5[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][3] = self.Lista_Predicoes_Predi5[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi5[resto][4] = self.Lista_Predicoes_Predi5[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][5] = self.Lista_Predicoes_Predi5[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][6] = self.Lista_Predicoes_Predi5[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][7] = self.Lista_Predicoes_Predi5[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi5[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == -1 and self.previsoes_anteriores[1] == 1 and self.previsoes_anteriores[2] == 1 and self.previsoes_anteriores[3] == -1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi6[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi6[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi6[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi6[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi6[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi6[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi6[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi6[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi6[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi6[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi6[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi6[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi6[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi6[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi6[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi6[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi6[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi6[resto][12] = self.Lista_Predicoes_Predi6[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi6[resto][0] = self.Lista_Predicoes_Predi6[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][1] = self.Lista_Predicoes_Predi6[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][2] = self.Lista_Predicoes_Predi6[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][3] = self.Lista_Predicoes_Predi6[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi6[resto][4] = self.Lista_Predicoes_Predi6[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][5] = self.Lista_Predicoes_Predi6[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][6] = self.Lista_Predicoes_Predi6[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][7] = self.Lista_Predicoes_Predi6[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi6[resto][12] = self.Lista_Predicoes_Predi6[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi6[resto][0] = self.Lista_Predicoes_Predi6[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][1] = self.Lista_Predicoes_Predi6[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][2] = self.Lista_Predicoes_Predi6[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][3] = self.Lista_Predicoes_Predi6[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi6[resto][4] = self.Lista_Predicoes_Predi6[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][5] = self.Lista_Predicoes_Predi6[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][6] = self.Lista_Predicoes_Predi6[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][7] = self.Lista_Predicoes_Predi6[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi6[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == -1 and self.previsoes_anteriores[1] == 1 and self.previsoes_anteriores[2] == 1 and self.previsoes_anteriores[3] == 1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi7[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi7[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi7[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi7[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi7[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi7[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi7[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi7[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi7[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi7[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi7[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi7[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi7[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi7[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi7[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi7[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi7[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi7[resto][12] = self.Lista_Predicoes_Predi7[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi7[resto][0] = self.Lista_Predicoes_Predi7[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][1] = self.Lista_Predicoes_Predi7[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][2] = self.Lista_Predicoes_Predi7[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][3] = self.Lista_Predicoes_Predi7[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi7[resto][4] = self.Lista_Predicoes_Predi7[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][5] = self.Lista_Predicoes_Predi7[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][6] = self.Lista_Predicoes_Predi7[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][7] = self.Lista_Predicoes_Predi7[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi7[resto][12] = self.Lista_Predicoes_Predi7[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi7[resto][0] = self.Lista_Predicoes_Predi7[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][1] = self.Lista_Predicoes_Predi7[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][2] = self.Lista_Predicoes_Predi7[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][3] = self.Lista_Predicoes_Predi7[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi7[resto][4] = self.Lista_Predicoes_Predi7[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][5] = self.Lista_Predicoes_Predi7[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][6] = self.Lista_Predicoes_Predi7[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][7] = self.Lista_Predicoes_Predi7[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi7[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == 1 and self.previsoes_anteriores[1] == -1 and self.previsoes_anteriores[2] == -1 and self.previsoes_anteriores[3] == -1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi8[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi8[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi8[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi8[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi8[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi8[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi8[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi8[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi8[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi8[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi8[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi8[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi8[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi8[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi8[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi8[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi8[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi8[resto][12] = self.Lista_Predicoes_Predi8[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi8[resto][0] = self.Lista_Predicoes_Predi8[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi8[resto][1] = self.Lista_Predicoes_Predi8[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi8[resto][2] = self.Lista_Predicoes_Predi8[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi8[resto][3] = self.Lista_Predicoes_Predi8[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi8[resto][4] = self.Lista_Predicoes_Predi8[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi8[resto][5] = self.Lista_Predicoes_Predi8[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi8[resto][6] = self.Lista_Predicoes_Predi8[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi8[resto][7] = self.Lista_Predicoes_Predi8[resto][7] + tomado * oitavaUltimaPredicao 
      else:
        self.Lista_Predicoes_Predi8[resto][12] = self.Lista_Predicoes_Predi8[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi8[resto][0] = self.Lista_Predicoes_Predi8[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi8[resto][1] = self.Lista_Predicoes_Predi8[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi8[resto][2] = self.Lista_Predicoes_Predi8[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi8[resto][3] = self.Lista_Predicoes_Predi8[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi8[resto][4] = self.Lista_Predicoes_Predi8[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi8[resto][5] = self.Lista_Predicoes_Predi8[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi8[resto][6] = self.Lista_Predicoes_Predi8[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi8[resto][7] = self.Lista_Predicoes_Predi8[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi8[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi8[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi8[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi8[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi8[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi8[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi8[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi8[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == 1 and self.previsoes_anteriores[1] == -1 and self.previsoes_anteriores[2] == -1 and self.previsoes_anteriores[3] == 1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi9[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi9[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi9[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi9[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi9[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi9[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi9[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi9[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi9[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi9[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi9[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi9[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi9[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi9[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi9[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi9[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi9[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi9[resto][12] = self.Lista_Predicoes_Predi9[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi9[resto][0] = self.Lista_Predicoes_Predi9[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi9[resto][1] = self.Lista_Predicoes_Predi9[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi9[resto][2] = self.Lista_Predicoes_Predi9[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi9[resto][3] = self.Lista_Predicoes_Predi9[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi9[resto][4] = self.Lista_Predicoes_Predi9[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi9[resto][5] = self.Lista_Predicoes_Predi9[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi9[resto][6] = self.Lista_Predicoes_Predi9[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi9[resto][7] = self.Lista_Predicoes_Predi9[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi9[resto][12] = self.Lista_Predicoes_Predi9[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi9[resto][0] = self.Lista_Predicoes_Predi9[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi9[resto][1] = self.Lista_Predicoes_Predi9[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi9[resto][2] = self.Lista_Predicoes_Predi9[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi9[resto][3] = self.Lista_Predicoes_Predi9[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi9[resto][4] = self.Lista_Predicoes_Predi9[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi9[resto][5] = self.Lista_Predicoes_Predi9[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi9[resto][6] = self.Lista_Predicoes_Predi9[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi9[resto][7] = self.Lista_Predicoes_Predi9[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi9[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi9[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi9[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi9[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi9[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi9[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi9[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi9[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == 1 and self.previsoes_anteriores[1] == -1 and self.previsoes_anteriores[2] == 1 and self.previsoes_anteriores[3] == -1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi10[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi10[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi10[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi10[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi10[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi10[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi10[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi10[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi10[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi10[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi10[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi10[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi10[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi10[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi10[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi10[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi10[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi10[resto][12] = self.Lista_Predicoes_Predi10[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi10[resto][0] = self.Lista_Predicoes_Predi10[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi10[resto][1] = self.Lista_Predicoes_Predi10[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi10[resto][2] = self.Lista_Predicoes_Predi10[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi10[resto][3] = self.Lista_Predicoes_Predi10[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi10[resto][4] = self.Lista_Predicoes_Predi10[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi10[resto][5] = self.Lista_Predicoes_Predi10[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi10[resto][6] = self.Lista_Predicoes_Predi10[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi10[resto][7] = self.Lista_Predicoes_Predi10[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi10[resto][12] = self.Lista_Predicoes_Predi10[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi10[resto][0] = self.Lista_Predicoes_Predi10[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi10[resto][1] = self.Lista_Predicoes_Predi10[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi10[resto][2] = self.Lista_Predicoes_Predi10[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi10[resto][3] = self.Lista_Predicoes_Predi10[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi10[resto][4] = self.Lista_Predicoes_Predi10[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi10[resto][5] = self.Lista_Predicoes_Predi10[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi10[resto][6] = self.Lista_Predicoes_Predi10[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi10[resto][7] = self.Lista_Predicoes_Predi10[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi10[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi10[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi10[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi10[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi10[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi10[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi10[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi10[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == 1 and self.previsoes_anteriores[1] == -1 and self.previsoes_anteriores[2] == 1 and self.previsoes_anteriores[3] == 1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi11[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi11[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi11[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi11[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi11[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi11[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi11[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi11[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi11[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi11[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi11[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi11[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi11[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi11[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi11[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi11[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi11[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi11[resto][12] = self.Lista_Predicoes_Predi11[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi11[resto][0] = self.Lista_Predicoes_Predi11[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi11[resto][1] = self.Lista_Predicoes_Predi11[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi11[resto][2] = self.Lista_Predicoes_Predi11[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi11[resto][3] = self.Lista_Predicoes_Predi11[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi11[resto][4] = self.Lista_Predicoes_Predi11[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi11[resto][5] = self.Lista_Predicoes_Predi11[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi11[resto][6] = self.Lista_Predicoes_Predi11[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi11[resto][7] = self.Lista_Predicoes_Predi11[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi11[resto][12] = self.Lista_Predicoes_Predi11[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi11[resto][0] = self.Lista_Predicoes_Predi11[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi11[resto][1] = self.Lista_Predicoes_Predi11[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi11[resto][2] = self.Lista_Predicoes_Predi11[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi11[resto][3] = self.Lista_Predicoes_Predi11[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi11[resto][4] = self.Lista_Predicoes_Predi11[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi11[resto][5] = self.Lista_Predicoes_Predi11[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi11[resto][6] = self.Lista_Predicoes_Predi11[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi11[resto][7] = self.Lista_Predicoes_Predi11[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi11[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi11[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi11[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi11[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi11[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi11[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi11[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi11[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == 1 and self.previsoes_anteriores[1] == 1 and self.previsoes_anteriores[2] == -1 and self.previsoes_anteriores[3] == -1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi12[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi12[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi12[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi12[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi12[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi12[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi12[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi12[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi12[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi12[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi12[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi12[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi12[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi12[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi12[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi12[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi12[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi12[resto][12] = self.Lista_Predicoes_Predi12[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi12[resto][0] = self.Lista_Predicoes_Predi12[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi12[resto][1] = self.Lista_Predicoes_Predi12[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi12[resto][2] = self.Lista_Predicoes_Predi12[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi12[resto][3] = self.Lista_Predicoes_Predi12[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi12[resto][4] = self.Lista_Predicoes_Predi12[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi12[resto][5] = self.Lista_Predicoes_Predi12[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi12[resto][6] = self.Lista_Predicoes_Predi12[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi12[resto][7] = self.Lista_Predicoes_Predi12[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi12[resto][12] = self.Lista_Predicoes_Predi12[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi12[resto][0] = self.Lista_Predicoes_Predi12[resto][
                                                            0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi12[resto][1] = self.Lista_Predicoes_Predi12[resto][
                                                            1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi12[resto][2] = self.Lista_Predicoes_Predi12[resto][
                                                            2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi12[resto][3] = self.Lista_Predicoes_Predi12[resto][
                                                            3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi12[resto][4] = self.Lista_Predicoes_Predi12[resto][
                                                            4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi12[resto][5] = self.Lista_Predicoes_Predi12[resto][
                                                            5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi12[resto][6] = self.Lista_Predicoes_Predi12[resto][
                                                            6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi12[resto][7] = self.Lista_Predicoes_Predi12[resto][
                                                            7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi12[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi12[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi12[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi12[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi12[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi12[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi12[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi12[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == 1 and self.previsoes_anteriores[1] == 1 and self.previsoes_anteriores[
      2] == -1 and self.previsoes_anteriores[3] == 1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi13[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi13[resto][15]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi13[resto][13]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi13[resto][14]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi13[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi13[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi13[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi13[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi13[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi13[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi13[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi13[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi13[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi13[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi13[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi13[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi13[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi13[resto][12] = self.Lista_Predicoes_Predi13[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi13[resto][0] = self.Lista_Predicoes_Predi13[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi13[resto][1] = self.Lista_Predicoes_Predi13[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi13[resto][2] = self.Lista_Predicoes_Predi13[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi13[resto][3] = self.Lista_Predicoes_Predi13[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi13[resto][4] = self.Lista_Predicoes_Predi13[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi13[resto][5] = self.Lista_Predicoes_Predi13[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi13[resto][6] = self.Lista_Predicoes_Predi13[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi13[resto][7] = self.Lista_Predicoes_Predi13[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi13[resto][12] = self.Lista_Predicoes_Predi13[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi13[resto][0] = self.Lista_Predicoes_Predi13[resto][
                                                      0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi13[resto][1] = self.Lista_Predicoes_Predi13[resto][
                                                      1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi13[resto][2] = self.Lista_Predicoes_Predi13[resto][
                                                      2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi13[resto][3] = self.Lista_Predicoes_Predi13[resto][
                                                      3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi13[resto][4] = self.Lista_Predicoes_Predi13[resto][
                                                      4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi13[resto][5] = self.Lista_Predicoes_Predi13[resto][
                                                      5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi13[resto][6] = self.Lista_Predicoes_Predi13[resto][
                                                      6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi13[resto][7] = self.Lista_Predicoes_Predi13[resto][
                                                      7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi13[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi13[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi13[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi13[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi13[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi13[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi13[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi13[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == 1 and self.previsoes_anteriores[1] == 1 and self.previsoes_anteriores[
        2] == 1 and self.previsoes_anteriores[3] == -1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi14[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi14[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi14[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi14[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi14[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi14[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi14[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi14[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi14[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi14[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi14[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi14[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi14[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi14[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi14[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi14[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi14[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi14[resto][12] = self.Lista_Predicoes_Predi14[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi14[resto][0] = self.Lista_Predicoes_Predi14[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi14[resto][1] = self.Lista_Predicoes_Predi14[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi14[resto][2] = self.Lista_Predicoes_Predi14[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi14[resto][3] = self.Lista_Predicoes_Predi14[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi14[resto][4] = self.Lista_Predicoes_Predi14[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi14[resto][5] = self.Lista_Predicoes_Predi14[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi14[resto][6] = self.Lista_Predicoes_Predi14[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi14[resto][7] = self.Lista_Predicoes_Predi14[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi14[resto][12] = self.Lista_Predicoes_Predi14[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi14[resto][0] = self.Lista_Predicoes_Predi14[resto][
                                                      0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi14[resto][1] = self.Lista_Predicoes_Predi14[resto][
                                                      1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi14[resto][2] = self.Lista_Predicoes_Predi14[resto][
                                                      2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi14[resto][3] = self.Lista_Predicoes_Predi14[resto][
                                                      3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi14[resto][4] = self.Lista_Predicoes_Predi14[resto][
                                                      4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi14[resto][5] = self.Lista_Predicoes_Predi14[resto][
                                                      5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi14[resto][6] = self.Lista_Predicoes_Predi14[resto][
                                                      6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi14[resto][7] = self.Lista_Predicoes_Predi14[resto][
                                                      7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi14[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi14[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi14[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi14[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi14[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi14[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi14[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi14[resto][8] = previsao_atual

    elif self.previsoes_anteriores[0] == 1 and self.previsoes_anteriores[1] == 1 and self.previsoes_anteriores[
        2] == 1 and self.previsoes_anteriores[3] == 1:

      oitavaUltimaPredicao = self.Lista_Predicoes_Predi15[resto][16]
      setimaUltimaPredicao = self.Lista_Predicoes_Predi15[resto][15]
      sextaUltimaPredicao = self.Lista_Predicoes_Predi15[resto][14]
      quintaUltimaPredicao = self.Lista_Predicoes_Predi15[resto][13]
      quartaUltimaPredicao = self.Lista_Predicoes_Predi15[resto][11]
      terceiraUltimaPredicao = self.Lista_Predicoes_Predi15[resto][10]
      segundaUltimaPredicao = self.Lista_Predicoes_Predi15[resto][9]
      primeiraUltimaPredicao = self.Lista_Predicoes_Predi15[resto][8]

      self.numeroDeInstrucoes = self.numeroDeInstrucoes + 1

      Lista0 = (self.Lista_Predicoes_Predi15[resto][0]) * primeiraUltimaPredicao
      Lista1 = (self.Lista_Predicoes_Predi15[resto][1]) * segundaUltimaPredicao
      Lista2 = (self.Lista_Predicoes_Predi15[resto][2]) * terceiraUltimaPredicao
      Lista3 = (self.Lista_Predicoes_Predi15[resto][3]) * quartaUltimaPredicao
      Lista4 = (self.Lista_Predicoes_Predi15[resto][4]) * quintaUltimaPredicao
      Lista5 = (self.Lista_Predicoes_Predi15[resto][5]) * sextaUltimaPredicao
      Lista6 = (self.Lista_Predicoes_Predi15[resto][6]) * setimaUltimaPredicao
      Lista7 = (self.Lista_Predicoes_Predi15[resto][7]) * oitavaUltimaPredicao
      w0 = self.Lista_Predicoes_Predi15[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + w0

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
          self.Lista_Predicoes_Predi15[resto][12] = self.Lista_Predicoes_Predi15[resto][12] + self.bias * tomado
          self.Lista_Predicoes_Predi15[resto][0] = self.Lista_Predicoes_Predi15[resto][0] + tomado * primeiraUltimaPredicao
          self.Lista_Predicoes_Predi15[resto][1] = self.Lista_Predicoes_Predi15[resto][1] + tomado * segundaUltimaPredicao
          self.Lista_Predicoes_Predi15[resto][2] = self.Lista_Predicoes_Predi15[resto][2] + tomado * terceiraUltimaPredicao
          self.Lista_Predicoes_Predi15[resto][3] = self.Lista_Predicoes_Predi15[resto][3] + tomado * quartaUltimaPredicao

          self.Lista_Predicoes_Predi15[resto][4] = self.Lista_Predicoes_Predi15[resto][4] + tomado * quintaUltimaPredicao
          self.Lista_Predicoes_Predi15[resto][5] = self.Lista_Predicoes_Predi15[resto][5] + tomado * sextaUltimaPredicao
          self.Lista_Predicoes_Predi15[resto][6] = self.Lista_Predicoes_Predi15[resto][6] + tomado * setimaUltimaPredicao
          self.Lista_Predicoes_Predi15[resto][7] = self.Lista_Predicoes_Predi15[resto][7] + tomado * oitavaUltimaPredicao 

      else:
        self.Lista_Predicoes_Predi15[resto][12] = self.Lista_Predicoes_Predi15[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi15[resto][0] = self.Lista_Predicoes_Predi15[resto][
                                                      0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi15[resto][1] = self.Lista_Predicoes_Predi15[resto][
                                                      1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi15[resto][2] = self.Lista_Predicoes_Predi15[resto][
                                                      2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi15[resto][3] = self.Lista_Predicoes_Predi15[resto][
                                                      3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi15[resto][4] = self.Lista_Predicoes_Predi15[resto][
                                                      4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi15[resto][5] = self.Lista_Predicoes_Predi15[resto][
                                                      5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi15[resto][6] = self.Lista_Predicoes_Predi15[resto][
                                                      6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi15[resto][7] = self.Lista_Predicoes_Predi15[resto][
                                                      7] + tomado * oitavaUltimaPredicao

      self.Lista_Predicoes_Predi15[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi15[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi15[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi15[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi15[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi15[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi15[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi15[resto][8] = previsao_atual

    self.previsoes_anteriores[3] = self.previsoes_anteriores[2]
    self.previsoes_anteriores[2] = self.previsoes_anteriores[1]
    self.previsoes_anteriores[1] = self.previsoes_anteriores[0]
    self.previsoes_anteriores[0] = previsao_atual



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
      #print(v)
      if v:
        dados = v.split(":")
        #print(v)
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
