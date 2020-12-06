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

public class PreditorTaken {

    private Long acerto;
    private Long erro;
    private Long totalChamadas;
    //mapeamento de instruções executadas
    // nomeDoDesvio,quantidadeAcerto[0],QuantidadeChamadas[1]
    private HashMap<String, ArrayList<Long>> listaPorTipoDesvio;

    public PreditorTaken() {
        this.acerto = 0L;
        this.erro = 0L;
        this.totalChamadas = 0L;
        this.listaPorTipoDesvio = new HashMap<>();
    }
        public String exibeNumeroBitsInterfaceGlobal() {
        //128 é o tamanho definido para o BPB
        //(2,3), m = 2, e n=3


         return "Número total de bits: " + 0;
    }

    public Long calculaStalls() {
        return this.erro * 3;
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
           // texto = texto + ("" + decimalFormat.format(taxaAcertos) + "%\n");
        }

        return texto;
    }

    public void analiseGlobal(Long enderecoDesvio, boolean tomado, Long enderecoDestino, String nomeDesvio) {
        this.totalChamadas++;
        ArrayList<Long> dados = (this.listaPorTipoDesvio.get(nomeDesvio) != null) ? this.listaPorTipoDesvio.get(nomeDesvio) : new ArrayList<Long>(Arrays.asList(0L, 0L));
        if (tomado) {
            this.acerto++;
            //incrementa o numero de acertos relativos ao tipo de desvio
            dados.set(0, dados.get(0) + 1);

        } else {
            this.erro++;
        }
        //incrementa o numero de chamadas relativas ao tipo de desvio
        dados.set(1, dados.get(1) + 1);
        this.listaPorTipoDesvio.put(nomeDesvio, dados);

    }

    public Long getAcerto() {
        return acerto;
    }

    public void setAcerto(Long acerto) {
        this.acerto = acerto;
    }

    public Long getErro() {
        return erro;
    }

    public void setErro(Long erro) {
        this.erro = erro;
    }

    public Long getTotalChamadas() {
        return totalChamadas;
    }

    public void setTotalChamadas(Long totalChamadas) {
        this.totalChamadas = totalChamadas;
    }

}
