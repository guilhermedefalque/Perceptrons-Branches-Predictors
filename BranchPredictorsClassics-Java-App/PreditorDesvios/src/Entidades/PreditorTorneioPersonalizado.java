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
 * @author dougl
 */
public class PreditorTorneioPersonalizado {

    private Integer preditor;
    private Long erro;
    private Long acerto;
    //private HashMap<Long, Integer> listPredicoes;
    private Long totalChamadas;
    private HashMap<String, ArrayList<Long>> listaPorTipoDesvio;

    private PreditorDoisBits preditorDoisBits;
    private PreditorCorrelacao preditorCorrelacao;

    public PreditorTorneioPersonalizado() {
        this.preditor = 0;
        this.erro = 0L;
        this.acerto = 0L;
        this.totalChamadas = 0L;
        this.preditorDoisBits = new PreditorDoisBits();
        this.preditorCorrelacao = new PreditorCorrelacao();
        this.listaPorTipoDesvio = new HashMap<>();

    }

    public String calculaTaxaAcerto() {
        Double taxaAcertos = this.acerto.doubleValue() / totalChamadas.doubleValue();
        taxaAcertos = taxaAcertos * 100;
        DecimalFormat decimalFormat = new DecimalFormat();
        decimalFormat.setMinimumFractionDigits(2);
        decimalFormat.setMaximumFractionDigits(2);

        return "Taxa de Acerto:" + decimalFormat.format(taxaAcertos) + "%\n";
    }

    public String exibeNumeroBitsInterface() {
        //128 é o tamanho definido para o BPB
        //tamanho do de dois bits
        
        Double numBitsCorrelacao = (128 * Math.pow(2, 2)) * 3;
        Integer numBitsHistorico = 2;
        Double tamanhoCorrelacao= numBitsHistorico+numBitsCorrelacao;
   
        //+2 pelo global de dois bits
        return "Número total de bits: " + (tamanhoCorrelacao+2);
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
           // texto = texto + ("" + decimalFormat.format(taxaAcertos) + "%\n");
        }

        return texto;
    }

    public void analise(Long enderecoDesvio, boolean tomado, Long enderecoDestino, boolean predicaoAnterior, boolean predicaoAnteriorAnterior, String nomeDesvio) {
        ArrayList<Long> dados = (this.listaPorTipoDesvio.get(nomeDesvio) != null) ? this.listaPorTipoDesvio.get(nomeDesvio) : new ArrayList<Long>(Arrays.asList(0L, 0L));

        boolean acertoGlobal = preditorDoisBits.analiseGlobalPreditorTorneio(tomado);
        boolean acertoLocal = preditorCorrelacao.analiseLocalPreditorTorneio(enderecoDesvio, tomado, enderecoDestino, predicaoAnterior, predicaoAnteriorAnterior, nomeDesvio);

        switch (this.preditor) {
            case 0:
                if (acertoGlobal == false && acertoLocal == true) {
                    this.preditor = 1;
                }
                if (acertoGlobal) {
                    dados.set(0, dados.get(0) + 1);
                }
                preditorDoisBits.analiseGlobal(enderecoDesvio, tomado, enderecoDestino, nomeDesvio);
                break;
            case 1:
                if (acertoGlobal == true && acertoLocal == false) {
                    this.preditor = 0;
                } else if (acertoGlobal == false && acertoLocal == true) {
                    this.preditor = 3;
                }
                if (acertoGlobal) {
                    dados.set(0, dados.get(0) + 1);
                }
                preditorDoisBits.analiseGlobal(enderecoDesvio, tomado, enderecoDestino, nomeDesvio);
                break;
            case 2:
                if (acertoGlobal == true && acertoLocal == false) {
                    this.preditor = 3;
                }
                if (acertoLocal) {
                    dados.set(0, dados.get(0) + 1);
                }
                preditorCorrelacao.analiseLocal(enderecoDesvio, tomado, enderecoDestino, predicaoAnterior, predicaoAnteriorAnterior, nomeDesvio);
                break;
            case 3:
                if (acertoGlobal == false && acertoLocal == true) {
                    this.preditor = 2;
                } else if (acertoGlobal == true && acertoLocal == false) {
                    this.preditor = 1;
                }

                if (acertoLocal) {
                    dados.set(0, dados.get(0) + 1);
                }

                preditorCorrelacao.analiseLocal(enderecoDesvio, tomado, enderecoDestino, predicaoAnterior, predicaoAnteriorAnterior, nomeDesvio);
                break;
        }
        setAcerto();
        setErro();
        totalChamadas++;
        //incrementa o numero de chamadas relativas ao tipo de desvio
        dados.set(1, dados.get(1) + 1);
        this.listaPorTipoDesvio.put(nomeDesvio, dados);
    }

    public Long getErro() {
        return erro;
    }

    public void setErro() {
        this.erro = preditorDoisBits.getErro()+preditorCorrelacao.getErro();
    }

    public Long getAcerto() {
        return acerto;
    }

    public void setAcerto() {
        this.acerto = preditorDoisBits.getAcerto()+ preditorCorrelacao.getAcerto();
    }

    public Long getTotalChamadas() {
        return totalChamadas;
    }

    public Long calculaStalls() {
        return this.erro * 10;
    }

}
