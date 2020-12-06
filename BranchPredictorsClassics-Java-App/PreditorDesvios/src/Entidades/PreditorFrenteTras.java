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

public class PreditorFrenteTras {

    private Integer predicaoAtual;
    private Long erro;
    private Long acerto;
    private HashMap<Long, Integer> listPredicoes;
    private Long totalChamadas;
    private HashMap<String, ArrayList<Long>> listaPorTipoDesvio;

    public PreditorFrenteTras() {
        this.predicaoAtual = 0;
        this.erro = 0L;
        this.acerto = 0L;
        this.listPredicoes = new HashMap<>();
        this.totalChamadas = 0L;
        this.listaPorTipoDesvio = new HashMap<>();
    }

    public Long calculaStalls() {
        return this.erro * 4;
    }

    public String exibeNumeroBitsInterface() {
        //128 é o tamanho definido para o BPB
        Integer numBits = (128 * 1);

        return "Número total de bits: " + numBits;
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

    public void analiseLocal(Long enderecoDesvio, boolean tomado, Long enderecoDestino, String nomeDesvio) {
        this.totalChamadas++;

        //se ja não existe predição ainda, ele deve utilizar a default, no caso 0
        Integer predicao = (this.listPredicoes.get(enderecoDesvio % 128) == null) ? 0 : this.listPredicoes.get(enderecoDesvio % 128);

        ArrayList<Long> dados = (this.listaPorTipoDesvio.get(nomeDesvio) != null) ? this.listaPorTipoDesvio.get(nomeDesvio) : new ArrayList<Long>(Arrays.asList(0L, 0L));

        //salto para frente(not-taken)
        if (enderecoDesvio < enderecoDestino) {
            if (!tomado && (predicao == 0)) {
                this.acerto++;
                //incrementa o numero de acertos relativos ao tipo de desvio
                dados.set(0, dados.get(0) + 1);
            } else {
                this.erro++;
            }
            //predição deve ser taken por causa do if
            this.listPredicoes.put((enderecoDesvio % 128), 0);

            //caso de salto para tras(taken)
        } else {
            if (tomado && (predicao == 1)) {
                this.acerto++;
                //incrementa o numero de acertos relativos ao tipo de desvio
                dados.set(0, dados.get(0) + 1);
            } else {
                this.erro++;
                this.listPredicoes.put((enderecoDesvio % 128), 1);
            }
        }
        //incrementa o numero de chamadas relativas ao tipo de desvio
        dados.set(1, dados.get(1) + 1);
        this.listaPorTipoDesvio.put(nomeDesvio, dados);

    }

    public Integer getPredicaoAtual() {
        return predicaoAtual;
    }

    public void setPredicaoAtual(Integer predicaoAtual) {
        this.predicaoAtual = predicaoAtual;
    }

    public Long getErro() {
        return erro;
    }

    public void setErro(Long erro) {
        this.erro = erro;
    }

    public Long getAcerto() {
        return acerto;
    }

    public void setAcerto(Long acerto) {
        this.acerto = acerto;
    }

    public HashMap<Long, Integer> getListPredicoes() {
        return listPredicoes;
    }

    public void setListPredicoes(HashMap<Long, Integer> listPredicoes) {
        this.listPredicoes = listPredicoes;
    }

}
