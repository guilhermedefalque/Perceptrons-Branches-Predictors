import numpy as np
class CorrelacaoPerseptron6:
  def __init__(self, caminho):
    self.quantidade_linhas = 4096
    # w1, w2, w3, w4, w5, w6, w7, w8,  historico0, historico1, historico2, historico3, w0
    #historico4, historico5, historico6, historico7
    # w9 w10 w11 w12 w13 w14 w15 w16 historico8 historico9 historico10 historico11 historico12 historico13 historico14 historico15
    self.Lista_Predicoes_Predi0 = np.ones((self.quantidade_linhas, 33), dtype=int)
    self.Lista_Predicoes_Predi1 = np.ones((self.quantidade_linhas, 33), dtype=int)
    self.Lista_Predicoes_Predi2 = np.ones((self.quantidade_linhas, 33), dtype=int)
    self.Lista_Predicoes_Predi3 = np.ones((self.quantidade_linhas, 33), dtype=int)
    self.Lista_Predicoes_Predi4 = np.ones((self.quantidade_linhas, 33), dtype=int)
    self.Lista_Predicoes_Predi5 = np.ones((self.quantidade_linhas, 33), dtype=int)
    self.Lista_Predicoes_Predi6 = np.ones((self.quantidade_linhas, 33), dtype=int)
    self.Lista_Predicoes_Predi7 = np.ones((self.quantidade_linhas, 33), dtype=int)
    self.bias = 1
    self.tamTabHistorico = 33
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

    if (tipo_Instrucao == 0):
      dezesseisUltimaPredicao = self.Lista_Predicoes_Predi0[resto][32]
      quinzeUltimaPredicao = self.Lista_Predicoes_Predi0[resto][31]
      quartozeUltimaPredicao = self.Lista_Predicoes_Predi0[resto][30]
      trezeUltimaPredicao = self.Lista_Predicoes_Predi0[resto][29]
      dozeUltimaPredicao = self.Lista_Predicoes_Predi0[resto][28]
      onzeUltimaPredicao = self.Lista_Predicoes_Predi0[resto][27]
      decimaUltimaPredicao = self.Lista_Predicoes_Predi0[resto][26]
      nonaUltimaPredicao = self.Lista_Predicoes_Predi0[resto][25]

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

      Lista8 = (self.Lista_Predicoes_Predi0[resto][17]) * nonaUltimaPredicao
      Lista9 = (self.Lista_Predicoes_Predi0[resto][18]) * decimaUltimaPredicao
      Lista10 = (self.Lista_Predicoes_Predi0[resto][19]) * onzeUltimaPredicao
      Lista11 = (self.Lista_Predicoes_Predi0[resto][20]) * dozeUltimaPredicao
      Lista12 = (self.Lista_Predicoes_Predi0[resto][21]) * trezeUltimaPredicao
      Lista13 = (self.Lista_Predicoes_Predi0[resto][22]) * quartozeUltimaPredicao
      Lista14 = (self.Lista_Predicoes_Predi0[resto][23]) * quinzeUltimaPredicao
      Lista15 = (self.Lista_Predicoes_Predi0[resto][24]) * dezesseisUltimaPredicao

      w0 = self.Lista_Predicoes_Predi0[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + Lista8 + Lista9 + Lista10 + Lista11 + Lista12 + Lista13 + Lista14 + Lista15 + w0

      if (soma > 0):
        previsao_atual = 1
      else:
        previsao_atual = -1
      if previsao_atual == tomado:
        self.acertos = self.acertos + 1
        self.quantidade_instruction_0 = self.quantidade_instruction_0 + 1

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
          
          self.Lista_Predicoes_Predi0[resto][17] = self.Lista_Predicoes_Predi0[resto][17] + tomado * nonaUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][18] = self.Lista_Predicoes_Predi0[resto][18] + tomado * decimaUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][19] = self.Lista_Predicoes_Predi0[resto][19] + tomado * onzeUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][20] = self.Lista_Predicoes_Predi0[resto][20] + tomado * dozeUltimaPredicao

          self.Lista_Predicoes_Predi0[resto][21] = self.Lista_Predicoes_Predi0[resto][21] + tomado * trezeUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][22] = self.Lista_Predicoes_Predi0[resto][22] + tomado * quartozeUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][23] = self.Lista_Predicoes_Predi0[resto][23] + tomado * quinzeUltimaPredicao
          self.Lista_Predicoes_Predi0[resto][24] = self.Lista_Predicoes_Predi0[resto][24] + tomado * dezesseisUltimaPredicao        
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
        
        self.Lista_Predicoes_Predi0[resto][17] = self.Lista_Predicoes_Predi0[resto][17] + tomado * nonaUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][18] = self.Lista_Predicoes_Predi0[resto][18] + tomado * decimaUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][19] = self.Lista_Predicoes_Predi0[resto][19] + tomado * onzeUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][20] = self.Lista_Predicoes_Predi0[resto][20] + tomado * dozeUltimaPredicao

        self.Lista_Predicoes_Predi0[resto][21] = self.Lista_Predicoes_Predi0[resto][21] + tomado * trezeUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][22] = self.Lista_Predicoes_Predi0[resto][22] + tomado * quartozeUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][23] = self.Lista_Predicoes_Predi0[resto][23] + tomado * quinzeUltimaPredicao
        self.Lista_Predicoes_Predi0[resto][24] = self.Lista_Predicoes_Predi0[resto][24] + tomado * dezesseisUltimaPredicao  

      self.Lista_Predicoes_Predi0[resto][32] = quinzeUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][31] = quartozeUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][30] = trezeUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][29] = dozeUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][28] = onzeUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][27] = decimaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][26] = nonaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][25] = oitavaUltimaPredicao
      
      self.Lista_Predicoes_Predi0[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi0[resto][8] = previsao_atual

    elif tipo_Instrucao == 1:
      dezesseisUltimaPredicao = self.Lista_Predicoes_Predi1[resto][32]
      quinzeUltimaPredicao = self.Lista_Predicoes_Predi1[resto][31]
      quartozeUltimaPredicao = self.Lista_Predicoes_Predi1[resto][30]
      trezeUltimaPredicao = self.Lista_Predicoes_Predi1[resto][29]
      dozeUltimaPredicao = self.Lista_Predicoes_Predi1[resto][28]
      onzeUltimaPredicao = self.Lista_Predicoes_Predi1[resto][27]
      decimaUltimaPredicao = self.Lista_Predicoes_Predi1[resto][26]
      nonaUltimaPredicao = self.Lista_Predicoes_Predi1[resto][25]

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

      Lista8 = (self.Lista_Predicoes_Predi1[resto][17]) * nonaUltimaPredicao
      Lista9 = (self.Lista_Predicoes_Predi1[resto][18]) * decimaUltimaPredicao
      Lista10 = (self.Lista_Predicoes_Predi1[resto][19]) * onzeUltimaPredicao
      Lista11 = (self.Lista_Predicoes_Predi1[resto][20]) * dozeUltimaPredicao
      Lista12 = (self.Lista_Predicoes_Predi1[resto][21]) * trezeUltimaPredicao
      Lista13 = (self.Lista_Predicoes_Predi1[resto][22]) * quartozeUltimaPredicao
      Lista14 = (self.Lista_Predicoes_Predi1[resto][23]) * quinzeUltimaPredicao
      Lista15 = (self.Lista_Predicoes_Predi1[resto][24]) * dezesseisUltimaPredicao

      w0 = self.Lista_Predicoes_Predi1[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + Lista8 + Lista9 + Lista10 + Lista11 + Lista12 + Lista13 + Lista14 + Lista15 + w0

      if (soma > 0):
        previsao_atual = 1
      else:
        previsao_atual = -1
      if previsao_atual == tomado:
        self.acertos = self.acertos + 1
        self.quantidade_instruction_1 = self.quantidade_instruction_1 + 1

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
          
          self.Lista_Predicoes_Predi1[resto][17] = self.Lista_Predicoes_Predi1[resto][17] + tomado * nonaUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][18] = self.Lista_Predicoes_Predi1[resto][18] + tomado * decimaUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][19] = self.Lista_Predicoes_Predi1[resto][19] + tomado * onzeUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][20] = self.Lista_Predicoes_Predi1[resto][20] + tomado * dozeUltimaPredicao

          self.Lista_Predicoes_Predi1[resto][21] = self.Lista_Predicoes_Predi1[resto][21] + tomado * trezeUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][22] = self.Lista_Predicoes_Predi1[resto][22] + tomado * quartozeUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][23] = self.Lista_Predicoes_Predi1[resto][23] + tomado * quinzeUltimaPredicao
          self.Lista_Predicoes_Predi1[resto][24] = self.Lista_Predicoes_Predi1[resto][24] + tomado * dezesseisUltimaPredicao        
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
        
        self.Lista_Predicoes_Predi1[resto][17] = self.Lista_Predicoes_Predi1[resto][17] + tomado * nonaUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][18] = self.Lista_Predicoes_Predi1[resto][18] + tomado * decimaUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][19] = self.Lista_Predicoes_Predi1[resto][19] + tomado * onzeUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][20] = self.Lista_Predicoes_Predi1[resto][20] + tomado * dozeUltimaPredicao

        self.Lista_Predicoes_Predi1[resto][21] = self.Lista_Predicoes_Predi1[resto][21] + tomado * trezeUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][22] = self.Lista_Predicoes_Predi1[resto][22] + tomado * quartozeUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][23] = self.Lista_Predicoes_Predi1[resto][23] + tomado * quinzeUltimaPredicao
        self.Lista_Predicoes_Predi1[resto][24] = self.Lista_Predicoes_Predi1[resto][24] + tomado * dezesseisUltimaPredicao  

      self.Lista_Predicoes_Predi1[resto][32] = quinzeUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][31] = quartozeUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][30] = trezeUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][29] = dozeUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][28] = onzeUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][27] = decimaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][26] = nonaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][25] = oitavaUltimaPredicao
      
      self.Lista_Predicoes_Predi1[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi1[resto][8] = previsao_atual

    elif tipo_Instrucao == 2:

      dezesseisUltimaPredicao = self.Lista_Predicoes_Predi2[resto][32]
      quinzeUltimaPredicao = self.Lista_Predicoes_Predi2[resto][31]
      quartozeUltimaPredicao = self.Lista_Predicoes_Predi2[resto][30]
      trezeUltimaPredicao = self.Lista_Predicoes_Predi2[resto][29]
      dozeUltimaPredicao = self.Lista_Predicoes_Predi2[resto][28]
      onzeUltimaPredicao = self.Lista_Predicoes_Predi2[resto][27]
      decimaUltimaPredicao = self.Lista_Predicoes_Predi2[resto][26]
      nonaUltimaPredicao = self.Lista_Predicoes_Predi2[resto][25]

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

      Lista8 = (self.Lista_Predicoes_Predi2[resto][17]) * nonaUltimaPredicao
      Lista9 = (self.Lista_Predicoes_Predi2[resto][18]) * decimaUltimaPredicao
      Lista10 = (self.Lista_Predicoes_Predi2[resto][19]) * onzeUltimaPredicao
      Lista11 = (self.Lista_Predicoes_Predi2[resto][20]) * dozeUltimaPredicao
      Lista12 = (self.Lista_Predicoes_Predi2[resto][21]) * trezeUltimaPredicao
      Lista13 = (self.Lista_Predicoes_Predi2[resto][22]) * quartozeUltimaPredicao
      Lista14 = (self.Lista_Predicoes_Predi2[resto][23]) * quinzeUltimaPredicao
      Lista15 = (self.Lista_Predicoes_Predi2[resto][24]) * dezesseisUltimaPredicao

      w0 = self.Lista_Predicoes_Predi2[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + Lista8 + Lista9 + Lista10 + Lista11 + Lista12 + Lista13 + Lista14 + Lista15 + w0

      if (soma > 0):
        previsao_atual = 1
      else:
        previsao_atual = -1
      if previsao_atual == tomado:
        self.acertos = self.acertos + 1
        self.quantidade_instruction_2 = self.quantidade_instruction_2 + 1

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
          
          self.Lista_Predicoes_Predi2[resto][17] = self.Lista_Predicoes_Predi2[resto][17] + tomado * nonaUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][18] = self.Lista_Predicoes_Predi2[resto][18] + tomado * decimaUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][19] = self.Lista_Predicoes_Predi2[resto][19] + tomado * onzeUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][20] = self.Lista_Predicoes_Predi2[resto][20] + tomado * dozeUltimaPredicao

          self.Lista_Predicoes_Predi2[resto][21] = self.Lista_Predicoes_Predi2[resto][21] + tomado * trezeUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][22] = self.Lista_Predicoes_Predi2[resto][22] + tomado * quartozeUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][23] = self.Lista_Predicoes_Predi2[resto][23] + tomado * quinzeUltimaPredicao
          self.Lista_Predicoes_Predi2[resto][24] = self.Lista_Predicoes_Predi2[resto][24] + tomado * dezesseisUltimaPredicao        
      else:
        self.Lista_Predicoes_Predi2[resto][12] = self.Lista_Predicoes_Predi2[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi2[resto][0] = self.Lista_Predicoes_Predi2[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][1] = self.Lista_Predicoes_Predi2[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][2] = self.Lista_Predicoes_Predi2[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][3] = self.Lista_Predicoes_Predi2[resto][3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi2[resto][4] = self.Lista_Predicoes_Predi2[resto][4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][5] = self.Lista_Predicoes_Predi2[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][6] = self.Lista_Predicoes_Predi2[resto][6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][7] = self.Lista_Predicoes_Predi2[resto][7] + tomado * oitavaUltimaPredicao 
        
        self.Lista_Predicoes_Predi2[resto][17] = self.Lista_Predicoes_Predi2[resto][17] + tomado * nonaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][18] = self.Lista_Predicoes_Predi2[resto][18] + tomado * decimaUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][19] = self.Lista_Predicoes_Predi2[resto][19] + tomado * onzeUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][20] = self.Lista_Predicoes_Predi2[resto][20] + tomado * dozeUltimaPredicao

        self.Lista_Predicoes_Predi2[resto][21] = self.Lista_Predicoes_Predi2[resto][21] + tomado * trezeUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][22] = self.Lista_Predicoes_Predi2[resto][22] + tomado * quartozeUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][23] = self.Lista_Predicoes_Predi2[resto][23] + tomado * quinzeUltimaPredicao
        self.Lista_Predicoes_Predi2[resto][24] = self.Lista_Predicoes_Predi2[resto][24] + tomado * dezesseisUltimaPredicao  

      self.Lista_Predicoes_Predi2[resto][32] = quinzeUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][31] = quartozeUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][30] = trezeUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][29] = dozeUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][28] = onzeUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][27] = decimaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][26] = nonaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][25] = oitavaUltimaPredicao
      
      self.Lista_Predicoes_Predi2[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi2[resto][8] = previsao_atual

    elif tipo_Instrucao == 3:

      dezesseisUltimaPredicao = self.Lista_Predicoes_Predi3[resto][32]
      quinzeUltimaPredicao = self.Lista_Predicoes_Predi3[resto][31]
      quartozeUltimaPredicao = self.Lista_Predicoes_Predi3[resto][30]
      trezeUltimaPredicao = self.Lista_Predicoes_Predi3[resto][29]
      dozeUltimaPredicao = self.Lista_Predicoes_Predi3[resto][28]
      onzeUltimaPredicao = self.Lista_Predicoes_Predi3[resto][27]
      decimaUltimaPredicao = self.Lista_Predicoes_Predi3[resto][26]
      nonaUltimaPredicao = self.Lista_Predicoes_Predi3[resto][25]

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

      Lista8 = (self.Lista_Predicoes_Predi3[resto][17]) * nonaUltimaPredicao
      Lista9 = (self.Lista_Predicoes_Predi3[resto][18]) * decimaUltimaPredicao
      Lista10 = (self.Lista_Predicoes_Predi3[resto][19]) * onzeUltimaPredicao
      Lista11 = (self.Lista_Predicoes_Predi3[resto][20]) * dozeUltimaPredicao
      Lista12 = (self.Lista_Predicoes_Predi3[resto][21]) * trezeUltimaPredicao
      Lista13 = (self.Lista_Predicoes_Predi3[resto][22]) * quartozeUltimaPredicao
      Lista14 = (self.Lista_Predicoes_Predi3[resto][23]) * quinzeUltimaPredicao
      Lista15 = (self.Lista_Predicoes_Predi3[resto][24]) * dezesseisUltimaPredicao

      w0 = self.Lista_Predicoes_Predi3[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + Lista8 + Lista9 + Lista10 + Lista11 + Lista12 + Lista13 + Lista14 + Lista15 + w0

      if (soma > 0):
        previsao_atual = 1
      else:
        previsao_atual = -1
      if previsao_atual == tomado:
        self.acertos = self.acertos + 1
        self.quantidade_instruction_3 = self.quantidade_instruction_3 + 1

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
          
          self.Lista_Predicoes_Predi3[resto][17] = self.Lista_Predicoes_Predi3[resto][17] + tomado * nonaUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][18] = self.Lista_Predicoes_Predi3[resto][18] + tomado * decimaUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][19] = self.Lista_Predicoes_Predi3[resto][19] + tomado * onzeUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][20] = self.Lista_Predicoes_Predi3[resto][20] + tomado * dozeUltimaPredicao

          self.Lista_Predicoes_Predi3[resto][21] = self.Lista_Predicoes_Predi3[resto][21] + tomado * trezeUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][22] = self.Lista_Predicoes_Predi3[resto][22] + tomado * quartozeUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][23] = self.Lista_Predicoes_Predi3[resto][23] + tomado * quinzeUltimaPredicao
          self.Lista_Predicoes_Predi3[resto][24] = self.Lista_Predicoes_Predi3[resto][24] + tomado * dezesseisUltimaPredicao        
      else:
        self.Lista_Predicoes_Predi3[resto][12] = self.Lista_Predicoes_Predi3[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi3[resto][0] = self.Lista_Predicoes_Predi3[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][1] = self.Lista_Predicoes_Predi3[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][2] = self.Lista_Predicoes_Predi3[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][3] = self.Lista_Predicoes_Predi3[resto][3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi3[resto][4] = self.Lista_Predicoes_Predi3[resto][4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][5] = self.Lista_Predicoes_Predi3[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][6] = self.Lista_Predicoes_Predi3[resto][6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][7] = self.Lista_Predicoes_Predi3[resto][7] + tomado * oitavaUltimaPredicao 
        
        self.Lista_Predicoes_Predi3[resto][17] = self.Lista_Predicoes_Predi3[resto][17] + tomado * nonaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][18] = self.Lista_Predicoes_Predi3[resto][18] + tomado * decimaUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][19] = self.Lista_Predicoes_Predi3[resto][19] + tomado * onzeUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][20] = self.Lista_Predicoes_Predi3[resto][20] + tomado * dozeUltimaPredicao

        self.Lista_Predicoes_Predi3[resto][21] = self.Lista_Predicoes_Predi3[resto][21] + tomado * trezeUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][22] = self.Lista_Predicoes_Predi3[resto][22] + tomado * quartozeUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][23] = self.Lista_Predicoes_Predi3[resto][23] + tomado * quinzeUltimaPredicao
        self.Lista_Predicoes_Predi3[resto][24] = self.Lista_Predicoes_Predi3[resto][24] + tomado * dezesseisUltimaPredicao  

      self.Lista_Predicoes_Predi3[resto][32] = quinzeUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][31] = quartozeUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][30] = trezeUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][29] = dozeUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][28] = onzeUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][27] = decimaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][26] = nonaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][25] = oitavaUltimaPredicao
      
      self.Lista_Predicoes_Predi3[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi3[resto][8] = previsao_atual

    elif tipo_Instrucao == 4:

      dezesseisUltimaPredicao = self.Lista_Predicoes_Predi4[resto][32]
      quinzeUltimaPredicao = self.Lista_Predicoes_Predi4[resto][31]
      quartozeUltimaPredicao = self.Lista_Predicoes_Predi4[resto][30]
      trezeUltimaPredicao = self.Lista_Predicoes_Predi4[resto][29]
      dozeUltimaPredicao = self.Lista_Predicoes_Predi4[resto][28]
      onzeUltimaPredicao = self.Lista_Predicoes_Predi4[resto][27]
      decimaUltimaPredicao = self.Lista_Predicoes_Predi4[resto][26]
      nonaUltimaPredicao = self.Lista_Predicoes_Predi4[resto][25]

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

      Lista8 = (self.Lista_Predicoes_Predi4[resto][17]) * nonaUltimaPredicao
      Lista9 = (self.Lista_Predicoes_Predi4[resto][18]) * decimaUltimaPredicao
      Lista10 = (self.Lista_Predicoes_Predi4[resto][19]) * onzeUltimaPredicao
      Lista11 = (self.Lista_Predicoes_Predi4[resto][20]) * dozeUltimaPredicao
      Lista12 = (self.Lista_Predicoes_Predi4[resto][21]) * trezeUltimaPredicao
      Lista13 = (self.Lista_Predicoes_Predi4[resto][22]) * quartozeUltimaPredicao
      Lista14 = (self.Lista_Predicoes_Predi4[resto][23]) * quinzeUltimaPredicao
      Lista15 = (self.Lista_Predicoes_Predi4[resto][24]) * dezesseisUltimaPredicao

      w0 = self.Lista_Predicoes_Predi4[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + Lista8 + Lista9 + Lista10 + Lista11 + Lista12 + Lista13 + Lista14 + Lista15 + w0

      if (soma > 0):
        previsao_atual = 1
      else:
        previsao_atual = -1
      if previsao_atual == tomado:
        self.acertos = self.acertos + 1
        self.quantidade_instruction_4 = self.quantidade_instruction_4 + 1

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
          
          self.Lista_Predicoes_Predi4[resto][17] = self.Lista_Predicoes_Predi4[resto][17] + tomado * nonaUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][18] = self.Lista_Predicoes_Predi4[resto][18] + tomado * decimaUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][19] = self.Lista_Predicoes_Predi4[resto][19] + tomado * onzeUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][20] = self.Lista_Predicoes_Predi4[resto][20] + tomado * dozeUltimaPredicao

          self.Lista_Predicoes_Predi4[resto][21] = self.Lista_Predicoes_Predi4[resto][21] + tomado * trezeUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][22] = self.Lista_Predicoes_Predi4[resto][22] + tomado * quartozeUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][23] = self.Lista_Predicoes_Predi4[resto][23] + tomado * quinzeUltimaPredicao
          self.Lista_Predicoes_Predi4[resto][24] = self.Lista_Predicoes_Predi4[resto][24] + tomado * dezesseisUltimaPredicao        
      else:
        self.Lista_Predicoes_Predi4[resto][12] = self.Lista_Predicoes_Predi4[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi4[resto][0] = self.Lista_Predicoes_Predi4[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][1] = self.Lista_Predicoes_Predi4[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][2] = self.Lista_Predicoes_Predi4[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][3] = self.Lista_Predicoes_Predi4[resto][3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi4[resto][4] = self.Lista_Predicoes_Predi4[resto][4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][5] = self.Lista_Predicoes_Predi4[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][6] = self.Lista_Predicoes_Predi4[resto][6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][7] = self.Lista_Predicoes_Predi4[resto][7] + tomado * oitavaUltimaPredicao 
        
        self.Lista_Predicoes_Predi4[resto][17] = self.Lista_Predicoes_Predi4[resto][17] + tomado * nonaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][18] = self.Lista_Predicoes_Predi4[resto][18] + tomado * decimaUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][19] = self.Lista_Predicoes_Predi4[resto][19] + tomado * onzeUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][20] = self.Lista_Predicoes_Predi4[resto][20] + tomado * dozeUltimaPredicao

        self.Lista_Predicoes_Predi4[resto][21] = self.Lista_Predicoes_Predi4[resto][21] + tomado * trezeUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][22] = self.Lista_Predicoes_Predi4[resto][22] + tomado * quartozeUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][23] = self.Lista_Predicoes_Predi4[resto][23] + tomado * quinzeUltimaPredicao
        self.Lista_Predicoes_Predi4[resto][24] = self.Lista_Predicoes_Predi4[resto][24] + tomado * dezesseisUltimaPredicao  

      self.Lista_Predicoes_Predi4[resto][32] = quinzeUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][31] = quartozeUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][30] = trezeUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][29] = dozeUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][28] = onzeUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][27] = decimaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][26] = nonaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][25] = oitavaUltimaPredicao
      
      self.Lista_Predicoes_Predi4[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi4[resto][8] = previsao_atual

    elif tipo_Instrucao == 5:

      dezesseisUltimaPredicao = self.Lista_Predicoes_Predi5[resto][32]
      quinzeUltimaPredicao = self.Lista_Predicoes_Predi5[resto][31]
      quartozeUltimaPredicao = self.Lista_Predicoes_Predi5[resto][30]
      trezeUltimaPredicao = self.Lista_Predicoes_Predi5[resto][29]
      dozeUltimaPredicao = self.Lista_Predicoes_Predi5[resto][28]
      onzeUltimaPredicao = self.Lista_Predicoes_Predi5[resto][27]
      decimaUltimaPredicao = self.Lista_Predicoes_Predi5[resto][26]
      nonaUltimaPredicao = self.Lista_Predicoes_Predi5[resto][25]

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

      Lista8 = (self.Lista_Predicoes_Predi5[resto][17]) * nonaUltimaPredicao
      Lista9 = (self.Lista_Predicoes_Predi5[resto][18]) * decimaUltimaPredicao
      Lista10 = (self.Lista_Predicoes_Predi5[resto][19]) * onzeUltimaPredicao
      Lista11 = (self.Lista_Predicoes_Predi5[resto][20]) * dozeUltimaPredicao
      Lista12 = (self.Lista_Predicoes_Predi5[resto][21]) * trezeUltimaPredicao
      Lista13 = (self.Lista_Predicoes_Predi5[resto][22]) * quartozeUltimaPredicao
      Lista14 = (self.Lista_Predicoes_Predi5[resto][23]) * quinzeUltimaPredicao
      Lista15 = (self.Lista_Predicoes_Predi5[resto][24]) * dezesseisUltimaPredicao

      w0 = self.Lista_Predicoes_Predi5[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + Lista8 + Lista9 + Lista10 + Lista11 + Lista12 + Lista13 + Lista14 + Lista15 + w0

      if (soma > 0):
        previsao_atual = 1
      else:
        previsao_atual = -1
      if previsao_atual == tomado:
        self.acertos = self.acertos + 1
        self.quantidade_instruction_5 = self.quantidade_instruction_5 + 1

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
          
          self.Lista_Predicoes_Predi5[resto][17] = self.Lista_Predicoes_Predi5[resto][17] + tomado * nonaUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][18] = self.Lista_Predicoes_Predi5[resto][18] + tomado * decimaUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][19] = self.Lista_Predicoes_Predi5[resto][19] + tomado * onzeUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][20] = self.Lista_Predicoes_Predi5[resto][20] + tomado * dozeUltimaPredicao

          self.Lista_Predicoes_Predi5[resto][21] = self.Lista_Predicoes_Predi5[resto][21] + tomado * trezeUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][22] = self.Lista_Predicoes_Predi5[resto][22] + tomado * quartozeUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][23] = self.Lista_Predicoes_Predi5[resto][23] + tomado * quinzeUltimaPredicao
          self.Lista_Predicoes_Predi5[resto][24] = self.Lista_Predicoes_Predi5[resto][24] + tomado * dezesseisUltimaPredicao        
      else:
        self.Lista_Predicoes_Predi5[resto][12] = self.Lista_Predicoes_Predi5[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi5[resto][0] = self.Lista_Predicoes_Predi5[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][1] = self.Lista_Predicoes_Predi5[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][2] = self.Lista_Predicoes_Predi5[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][3] = self.Lista_Predicoes_Predi5[resto][3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi5[resto][4] = self.Lista_Predicoes_Predi5[resto][4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][5] = self.Lista_Predicoes_Predi5[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][6] = self.Lista_Predicoes_Predi5[resto][6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][7] = self.Lista_Predicoes_Predi5[resto][7] + tomado * oitavaUltimaPredicao 
        
        self.Lista_Predicoes_Predi5[resto][17] = self.Lista_Predicoes_Predi5[resto][17] + tomado * nonaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][18] = self.Lista_Predicoes_Predi5[resto][18] + tomado * decimaUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][19] = self.Lista_Predicoes_Predi5[resto][19] + tomado * onzeUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][20] = self.Lista_Predicoes_Predi5[resto][20] + tomado * dozeUltimaPredicao

        self.Lista_Predicoes_Predi5[resto][21] = self.Lista_Predicoes_Predi5[resto][21] + tomado * trezeUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][22] = self.Lista_Predicoes_Predi5[resto][22] + tomado * quartozeUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][23] = self.Lista_Predicoes_Predi5[resto][23] + tomado * quinzeUltimaPredicao
        self.Lista_Predicoes_Predi5[resto][24] = self.Lista_Predicoes_Predi5[resto][24] + tomado * dezesseisUltimaPredicao  

      self.Lista_Predicoes_Predi5[resto][32] = quinzeUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][31] = quartozeUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][30] = trezeUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][29] = dozeUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][28] = onzeUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][27] = decimaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][26] = nonaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][25] = oitavaUltimaPredicao
      
      self.Lista_Predicoes_Predi5[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi5[resto][8] = previsao_atual

    elif tipo_Instrucao == 6:

      dezesseisUltimaPredicao = self.Lista_Predicoes_Predi6[resto][32]
      quinzeUltimaPredicao = self.Lista_Predicoes_Predi6[resto][31]
      quartozeUltimaPredicao = self.Lista_Predicoes_Predi6[resto][30]
      trezeUltimaPredicao = self.Lista_Predicoes_Predi6[resto][29]
      dozeUltimaPredicao = self.Lista_Predicoes_Predi6[resto][28]
      onzeUltimaPredicao = self.Lista_Predicoes_Predi6[resto][27]
      decimaUltimaPredicao = self.Lista_Predicoes_Predi6[resto][26]
      nonaUltimaPredicao = self.Lista_Predicoes_Predi6[resto][25]

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

      Lista8 = (self.Lista_Predicoes_Predi6[resto][17]) * nonaUltimaPredicao
      Lista9 = (self.Lista_Predicoes_Predi6[resto][18]) * decimaUltimaPredicao
      Lista10 = (self.Lista_Predicoes_Predi6[resto][19]) * onzeUltimaPredicao
      Lista11 = (self.Lista_Predicoes_Predi6[resto][20]) * dozeUltimaPredicao
      Lista12 = (self.Lista_Predicoes_Predi6[resto][21]) * trezeUltimaPredicao
      Lista13 = (self.Lista_Predicoes_Predi6[resto][22]) * quartozeUltimaPredicao
      Lista14 = (self.Lista_Predicoes_Predi6[resto][23]) * quinzeUltimaPredicao
      Lista15 = (self.Lista_Predicoes_Predi6[resto][24]) * dezesseisUltimaPredicao

      w0 = self.Lista_Predicoes_Predi6[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + Lista8 + Lista9 + Lista10 + Lista11 + Lista12 + Lista13 + Lista14 + Lista15 + w0

      if (soma > 0):
        previsao_atual = 1
      else:
        previsao_atual = -1
      if previsao_atual == tomado:
        self.acertos = self.acertos + 1
        self.quantidade_instruction_6 = self.quantidade_instruction_6 + 1

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
          
          self.Lista_Predicoes_Predi6[resto][17] = self.Lista_Predicoes_Predi6[resto][17] + tomado * nonaUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][18] = self.Lista_Predicoes_Predi6[resto][18] + tomado * decimaUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][19] = self.Lista_Predicoes_Predi6[resto][19] + tomado * onzeUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][20] = self.Lista_Predicoes_Predi6[resto][20] + tomado * dozeUltimaPredicao

          self.Lista_Predicoes_Predi6[resto][21] = self.Lista_Predicoes_Predi6[resto][21] + tomado * trezeUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][22] = self.Lista_Predicoes_Predi6[resto][22] + tomado * quartozeUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][23] = self.Lista_Predicoes_Predi6[resto][23] + tomado * quinzeUltimaPredicao
          self.Lista_Predicoes_Predi6[resto][24] = self.Lista_Predicoes_Predi6[resto][24] + tomado * dezesseisUltimaPredicao        
      else:
        self.Lista_Predicoes_Predi6[resto][12] = self.Lista_Predicoes_Predi6[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi6[resto][0] = self.Lista_Predicoes_Predi6[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][1] = self.Lista_Predicoes_Predi6[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][2] = self.Lista_Predicoes_Predi6[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][3] = self.Lista_Predicoes_Predi6[resto][3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi6[resto][4] = self.Lista_Predicoes_Predi6[resto][4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][5] = self.Lista_Predicoes_Predi6[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][6] = self.Lista_Predicoes_Predi6[resto][6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][7] = self.Lista_Predicoes_Predi6[resto][7] + tomado * oitavaUltimaPredicao 
        
        self.Lista_Predicoes_Predi6[resto][17] = self.Lista_Predicoes_Predi6[resto][17] + tomado * nonaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][18] = self.Lista_Predicoes_Predi6[resto][18] + tomado * decimaUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][19] = self.Lista_Predicoes_Predi6[resto][19] + tomado * onzeUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][20] = self.Lista_Predicoes_Predi6[resto][20] + tomado * dozeUltimaPredicao

        self.Lista_Predicoes_Predi6[resto][21] = self.Lista_Predicoes_Predi6[resto][21] + tomado * trezeUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][22] = self.Lista_Predicoes_Predi6[resto][22] + tomado * quartozeUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][23] = self.Lista_Predicoes_Predi6[resto][23] + tomado * quinzeUltimaPredicao
        self.Lista_Predicoes_Predi6[resto][24] = self.Lista_Predicoes_Predi6[resto][24] + tomado * dezesseisUltimaPredicao  

      self.Lista_Predicoes_Predi6[resto][32] = quinzeUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][31] = quartozeUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][30] = trezeUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][29] = dozeUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][28] = onzeUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][27] = decimaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][26] = nonaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][25] = oitavaUltimaPredicao
      
      self.Lista_Predicoes_Predi6[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi6[resto][8] = previsao_atual

    elif tipo_Instrucao == 7:

      dezesseisUltimaPredicao = self.Lista_Predicoes_Predi7[resto][32]
      quinzeUltimaPredicao = self.Lista_Predicoes_Predi7[resto][31]
      quartozeUltimaPredicao = self.Lista_Predicoes_Predi7[resto][30]
      trezeUltimaPredicao = self.Lista_Predicoes_Predi7[resto][29]
      dozeUltimaPredicao = self.Lista_Predicoes_Predi7[resto][28]
      onzeUltimaPredicao = self.Lista_Predicoes_Predi7[resto][27]
      decimaUltimaPredicao = self.Lista_Predicoes_Predi7[resto][26]
      nonaUltimaPredicao = self.Lista_Predicoes_Predi7[resto][25]

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

      Lista8 = (self.Lista_Predicoes_Predi7[resto][17]) * nonaUltimaPredicao
      Lista9 = (self.Lista_Predicoes_Predi7[resto][18]) * decimaUltimaPredicao
      Lista10 = (self.Lista_Predicoes_Predi7[resto][19]) * onzeUltimaPredicao
      Lista11 = (self.Lista_Predicoes_Predi7[resto][20]) * dozeUltimaPredicao
      Lista12 = (self.Lista_Predicoes_Predi7[resto][21]) * trezeUltimaPredicao
      Lista13 = (self.Lista_Predicoes_Predi7[resto][22]) * quartozeUltimaPredicao
      Lista14 = (self.Lista_Predicoes_Predi7[resto][23]) * quinzeUltimaPredicao
      Lista15 = (self.Lista_Predicoes_Predi7[resto][24]) * dezesseisUltimaPredicao

      w0 = self.Lista_Predicoes_Predi7[resto][12]

      soma = Lista0 + Lista1 + Lista2 + Lista3 + Lista4 + Lista5 + Lista6 + Lista7 + Lista8 + Lista9 + Lista10 + Lista11 + Lista12 + Lista13 + Lista14 + Lista15 + w0

      if (soma > 0):
        previsao_atual = 1
      else:
        previsao_atual = -1
      if previsao_atual == tomado:
        self.acertos = self.acertos + 1
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
          
          self.Lista_Predicoes_Predi7[resto][17] = self.Lista_Predicoes_Predi7[resto][17] + tomado * nonaUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][18] = self.Lista_Predicoes_Predi7[resto][18] + tomado * decimaUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][19] = self.Lista_Predicoes_Predi7[resto][19] + tomado * onzeUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][20] = self.Lista_Predicoes_Predi7[resto][20] + tomado * dozeUltimaPredicao

          self.Lista_Predicoes_Predi7[resto][21] = self.Lista_Predicoes_Predi7[resto][21] + tomado * trezeUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][22] = self.Lista_Predicoes_Predi7[resto][22] + tomado * quartozeUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][23] = self.Lista_Predicoes_Predi7[resto][23] + tomado * quinzeUltimaPredicao
          self.Lista_Predicoes_Predi7[resto][24] = self.Lista_Predicoes_Predi7[resto][24] + tomado * dezesseisUltimaPredicao        
      else:
        self.Lista_Predicoes_Predi7[resto][12] = self.Lista_Predicoes_Predi7[resto][12] + self.bias * tomado
        self.Lista_Predicoes_Predi7[resto][0] = self.Lista_Predicoes_Predi7[resto][0] + tomado * primeiraUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][1] = self.Lista_Predicoes_Predi7[resto][1] + tomado * segundaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][2] = self.Lista_Predicoes_Predi7[resto][2] + tomado * terceiraUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][3] = self.Lista_Predicoes_Predi7[resto][3] + tomado * quartaUltimaPredicao

        self.Lista_Predicoes_Predi7[resto][4] = self.Lista_Predicoes_Predi7[resto][4] + tomado * quintaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][5] = self.Lista_Predicoes_Predi7[resto][5] + tomado * sextaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][6] = self.Lista_Predicoes_Predi7[resto][6] + tomado * setimaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][7] = self.Lista_Predicoes_Predi7[resto][7] + tomado * oitavaUltimaPredicao 
        
        self.Lista_Predicoes_Predi7[resto][17] = self.Lista_Predicoes_Predi7[resto][17] + tomado * nonaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][18] = self.Lista_Predicoes_Predi7[resto][18] + tomado * decimaUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][19] = self.Lista_Predicoes_Predi7[resto][19] + tomado * onzeUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][20] = self.Lista_Predicoes_Predi7[resto][20] + tomado * dozeUltimaPredicao

        self.Lista_Predicoes_Predi7[resto][21] = self.Lista_Predicoes_Predi7[resto][21] + tomado * trezeUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][22] = self.Lista_Predicoes_Predi7[resto][22] + tomado * quartozeUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][23] = self.Lista_Predicoes_Predi7[resto][23] + tomado * quinzeUltimaPredicao
        self.Lista_Predicoes_Predi7[resto][24] = self.Lista_Predicoes_Predi7[resto][24] + tomado * dezesseisUltimaPredicao  

      self.Lista_Predicoes_Predi7[resto][32] = quinzeUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][31] = quartozeUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][30] = trezeUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][29] = dozeUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][28] = onzeUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][27] = decimaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][26] = nonaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][25] = oitavaUltimaPredicao
      
      self.Lista_Predicoes_Predi7[resto][16] = setimaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][15] = sextaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][14] = quintaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][13] = quartaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][11] = terceiraUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][10] = segundaUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][9] = primeiraUltimaPredicao
      self.Lista_Predicoes_Predi7[resto][8] = previsao_atual

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
