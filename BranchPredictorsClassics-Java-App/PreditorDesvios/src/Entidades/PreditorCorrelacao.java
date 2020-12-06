/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Entidades;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author guilherme
 */
public class PreditorCorrelacao {

    private Integer preditor;
    private Long erro;
    private Long acerto;
    //private HashMap<Long, Integer> listPredicoes;
    private Long totalChamadas;
    private HashMap<String, ArrayList<Long>> listaPorTipoDesvio;
    private PreditorTresBits preditor0;
    private PreditorTresBits preditor1;
    private PreditorTresBits preditor2;
    private PreditorTresBits preditor3;

    public PreditorCorrelacao() {
        this.preditor = 0;
        this.erro = 0L;
        this.acerto = 0L;
        //this.listPredicoes = new HashMap<>();
        this.totalChamadas = 0L;
        preditor0 = new PreditorTresBits();
        preditor1 = new PreditorTresBits();
        preditor2 = new PreditorTresBits();
        preditor3 = new PreditorTresBits();
        this.listaPorTipoDesvio = new HashMap<>();
    }

    public Long calculaStalls() {
        return this.erro * 10;
    }

    public String exibeNumeroBitsInterface() {
        //128 é o tamanho definido para o BPB
        //(2,3), m = 2, e n=3
        Double numBits = (128 * Math.pow(2, 2)) * 3;
        Integer numBitsHistorico = 2;

        return "Número total de bits(bpb+histórico): " + (numBits + numBitsHistorico);
    }

    public String calculaTaxaAcerto() {
        Double taxaAcertos = this.acerto.doubleValue() / totalChamadas.doubleValue();
        taxaAcertos = taxaAcertos * 100;
        DecimalFormat decimalFormat = new DecimalFormat();
        decimalFormat.setMinimumFractionDigits(2);
        decimalFormat.setMaximumFractionDigits(2);

        return "Taxa de Acerto:" + decimalFormat.format(taxaAcertos) + "%\n";
    }

    public void exibeTaxaAcertoPorTipo() {
        listaPorTipoDesvio.entrySet().forEach((entry) -> {
            String key = entry.getKey();
            ArrayList<Long> value = entry.getValue();
            Double taxaAcertos = value.get(0).doubleValue() / value.get(1).doubleValue();
            taxaAcertos = taxaAcertos * 100;
            DecimalFormat decimalFormat = new DecimalFormat();
            decimalFormat.setMinimumFractionDigits(2);
            decimalFormat.setMaximumFractionDigits(2);

            System.out.println("Instrução:" + key + " Taxa de Acertos(aproximadamente): " + decimalFormat.format(taxaAcertos) + "%");
        });
    }

    public String exibeTaxaAcertoPorTipoInterface() {
        String texto = "Taxa de acerto em relação ao tipo de instrução:\n";

        for (Map.Entry<String, ArrayList<Long>> entry : listaPorTipoDesvio.entrySet()) {
            String key = entry.getKey();
            ArrayList<Long> value = entry.getValue();

            Double taxaAcertos = value.get(0).doubleValue() / value.get(1).doubleValue();
            taxaAcertos = taxaAcertos * 100;
            DecimalFormat decimalFormat = new DecimalFormat();
            decimalFormat.setMinimumFractionDigits(2);
            decimalFormat.setMaximumFractionDigits(2);
            texto = texto + (key + ":" + decimalFormat.format(taxaAcertos) + "%\n");
            //texto = texto + ("" + decimalFormat.format(taxaAcertos) + "%\n");
        }

        return texto;
    }

    public void analiseLocal(Long enderecoDesvio, boolean tomado, Long enderecoDestino, boolean predicaoAnterior, boolean predicaoAnteriorAnterior, String nomeDesvio) {
        ArrayList<Long> dados = (this.listaPorTipoDesvio.get(nomeDesvio) != null) ? this.listaPorTipoDesvio.get(nomeDesvio) : new ArrayList<Long>(Arrays.asList(0L, 0L));
        Long quantidadeAcertos = 0L;

        if (predicaoAnteriorAnterior == false && predicaoAnterior == false) {
            this.preditor = 0;
            // System.out.println("entrou no preditor 0");
        } else if (predicaoAnteriorAnterior == false && predicaoAnterior == true) {
            this.preditor = 1;
            // System.out.println("entrou no preditor 1");
        } else if (predicaoAnteriorAnterior == true && predicaoAnterior == true) {
            this.preditor = 3;
            // System.out.println("entrou no preditor 3");
        } else if (predicaoAnteriorAnterior == true && predicaoAnterior == false) {
            this.preditor = 2;
            //System.out.println("entrou no preditor 2");
        }

        switch (this.preditor) {
            case 0:
                quantidadeAcertos = preditor0.getAcerto();
                preditor0.analiseLocal(enderecoDesvio, tomado, enderecoDestino);
                if (quantidadeAcertos < preditor0.getAcerto()) {
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                }
                setErro();
                setAcerto();

                setTotalChamadas();
                break;
            case 1:
                quantidadeAcertos = preditor1.getAcerto();
                preditor1.analiseLocal(enderecoDesvio, tomado, enderecoDestino);
                if (quantidadeAcertos < preditor1.getAcerto()) {
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                }
                setErro();
                setAcerto();
                setTotalChamadas();
                break;
            case 2:
                quantidadeAcertos = preditor2.getAcerto();
                preditor2.analiseLocal(enderecoDesvio, tomado, enderecoDestino);
                if (quantidadeAcertos < preditor2.getAcerto()) {
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                }
                setErro();
                setAcerto();
                setTotalChamadas();
                break;
            case 3:
                quantidadeAcertos = preditor3.getAcerto();
                preditor3.analiseLocal(enderecoDesvio, tomado, enderecoDestino);
                if (quantidadeAcertos < preditor3.getAcerto()) {
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                }
                setErro();
                setAcerto();
                setTotalChamadas();
                break;
        }

        //incrementa o numero de chamadas relativas ao tipo de desvio
        dados.set(1, dados.get(1) + 1);
        this.listaPorTipoDesvio.put(nomeDesvio, dados);

    }

    public boolean analiseLocalPreditorTorneio(Long enderecoDesvio, boolean tomado, Long enderecoDestino, boolean predicaoAnterior, boolean predicaoAnteriorAnterior, String nomeDesvio) {
        ArrayList<Long> dados = (this.listaPorTipoDesvio.get(nomeDesvio) != null) ? this.listaPorTipoDesvio.get(nomeDesvio) : new ArrayList<Long>(Arrays.asList(0L, 0L));
        Long quantidadeAcertosAnterior = 0L;
        Long quantidadeErrosAnterior = 0L;
        Long totalChamadaAnterior = 0L;
        HashMap<Long, Integer> listPredicoesAnterior = new HashMap<>();

        if (predicaoAnteriorAnterior == false && predicaoAnterior == false) {
            this.preditor = 0;
            // System.out.println("entrou no preditor 0");
        } else if (predicaoAnteriorAnterior == false && predicaoAnterior == true) {
            this.preditor = 1;
            // System.out.println("entrou no preditor 1");
        } else if (predicaoAnteriorAnterior == true && predicaoAnterior == true) {
            this.preditor = 3;
            // System.out.println("entrou no preditor 3");
        } else if (predicaoAnteriorAnterior == true && predicaoAnterior == false) {
            this.preditor = 2;
            //System.out.println("entrou no preditor 2");
        }

        switch (this.preditor) {
            case 0:
                quantidadeAcertosAnterior = preditor0.getAcerto();
                quantidadeErrosAnterior = preditor0.getErro();
                listPredicoesAnterior=preditor0.getListPredicoes();
                preditor0.analiseLocal(enderecoDesvio, tomado, enderecoDestino);
                if (quantidadeAcertosAnterior < preditor0.getAcerto()) {
                    preditor0.setErro(quantidadeErrosAnterior);
                    preditor0.setAcerto(quantidadeAcertosAnterior);
                    preditor0.setListPredicoes(listPredicoesAnterior);
                    return true;
                }
                preditor0.setErro(quantidadeErrosAnterior);
                preditor0.setAcerto(quantidadeAcertosAnterior);
                preditor0.setListPredicoes(listPredicoesAnterior);
                break;
            case 1:
                quantidadeAcertosAnterior = preditor1.getAcerto();
                quantidadeErrosAnterior = preditor1.getErro();
                listPredicoesAnterior=preditor1.getListPredicoes();
                preditor1.analiseLocal(enderecoDesvio, tomado, enderecoDestino);
                if (quantidadeAcertosAnterior < preditor1.getAcerto()) {
                    preditor1.setErro(quantidadeErrosAnterior);
                    preditor1.setAcerto(quantidadeAcertosAnterior);
                    preditor1.setListPredicoes(listPredicoesAnterior);
                    return true;
                }
                preditor1.setErro(quantidadeErrosAnterior);
                preditor1.setAcerto(quantidadeAcertosAnterior);
                preditor1.setListPredicoes(listPredicoesAnterior);
                break;
            case 2:
                quantidadeAcertosAnterior = preditor2.getAcerto();
                quantidadeErrosAnterior = preditor2.getErro();
                listPredicoesAnterior=preditor2.getListPredicoes();
                preditor2.analiseLocal(enderecoDesvio, tomado, enderecoDestino);
                if (quantidadeAcertosAnterior < preditor2.getAcerto()) {
                    preditor2.setErro(quantidadeErrosAnterior);
                    preditor2.setAcerto(quantidadeAcertosAnterior);
                    preditor2.setListPredicoes(listPredicoesAnterior);
                    return true;
                }
                preditor2.setErro(quantidadeErrosAnterior);
                preditor2.setAcerto(quantidadeAcertosAnterior);
                preditor2.setListPredicoes(listPredicoesAnterior);
                break;
            case 3:
                quantidadeAcertosAnterior = preditor3.getAcerto();
                quantidadeErrosAnterior = preditor3.getErro();
                listPredicoesAnterior=preditor3.getListPredicoes();
                preditor3.analiseLocal(enderecoDesvio, tomado, enderecoDestino);
                if (quantidadeAcertosAnterior < preditor3.getAcerto()) {
                    preditor3.setErro(quantidadeErrosAnterior);
                    preditor3.setAcerto(quantidadeAcertosAnterior);
                    preditor3.setListPredicoes(listPredicoesAnterior);
                    return true;
                }
                preditor3.setErro(quantidadeErrosAnterior);
                preditor3.setAcerto(quantidadeAcertosAnterior);
                preditor3.setListPredicoes(listPredicoesAnterior);
                break;
        }

        return false;

    }

    public Long getErro() {
        return erro;
    }

    public void setErro() {
        this.erro = preditor0.getErro() + preditor1.getErro() + preditor2.getErro() + preditor3.getErro();
    }

    public Long getAcerto() {
        return acerto;
    }

    public void setAcerto() {
        this.acerto = preditor0.getAcerto() + preditor1.getAcerto() + preditor2.getAcerto() + preditor3.getAcerto();
    }

    public Long getTotalChamadas() {
        return totalChamadas;
    }

    public void setTotalChamadas() {
        this.totalChamadas = preditor0.getTotalChamadas() + preditor1.getTotalChamadas() + preditor2.getTotalChamadas() + preditor3.getTotalChamadas();
    }

}
