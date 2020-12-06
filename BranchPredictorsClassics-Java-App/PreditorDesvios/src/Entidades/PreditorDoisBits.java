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
public class PreditorDoisBits {

    private Integer predicaoAtual;
    private Long erro;

    private Long acerto;

    private HashMap<Long, Integer> listPredicoes;
    private Long totalChamadas;
    private HashMap<String, ArrayList<Long>> listaPorTipoDesvio;

    public PreditorDoisBits() {
        this.predicaoAtual = 0;
        this.acerto = 0L;
        this.erro = 0L;
        this.listPredicoes = new HashMap<>();
        this.totalChamadas = 0L;
        this.listaPorTipoDesvio = new HashMap<>();
    }

    public Long calculaStalls() {
        return this.erro * 6;
    }

    public String exibeNumeroBitsInterfaceLocal() {
        //128 é o tamanho definido para o BPB
        Integer numBits = (128 * 2);

        return "Número total de bits: " + numBits;
    }
        public String exibeNumeroBitsInterfaceGlobal() {
        //128 é o tamanho definido para o BPB
        //(2,3), m = 2, e n=3


         return "Número total de bits: " + 2;
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

        switch (this.predicaoAtual) {
            //00
            case 0:
                //predicao not taken
                if (!tomado) {
                    //acerta e continua no mesmo estado
                    this.acerto++;
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                } else {
                    this.erro++;
                    this.predicaoAtual++;
                }
                break;
            //01    
            case 1:
                //predicao not taken
                if (!tomado) {
                    //acerta e retorna para o estado anterior(00)
                    this.acerto++;
                    this.predicaoAtual--;
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                } else {
                    this.erro++;
                    //erra e vai para o estado 11 -> 3 dec
                    this.predicaoAtual = 3;
                }
                break;

            //11    
            case 3:
                //predicao taken
                if (tomado) {
                    //acerta e continua no mesmo estado
                    this.acerto++;
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                } else {
                    this.erro++;
                    //erra e vai para o estado 10 -> 2 dec
                    this.predicaoAtual = 2;
                }
                break;

            case 2:
                //predicao taken
                if (tomado) {
                    //acerta e retorna para o estado anterior(11)
                    this.predicaoAtual++;
                    this.acerto++;
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                } else {
                    this.erro++;
                    //erra e vai para o estado 00 -> 0 dec
                    this.predicaoAtual = 0;
                }
                break;
        }
        //incrementa o numero de chamadas relativas ao tipo de desvio
        dados.set(1, dados.get(1) + 1);
        this.listaPorTipoDesvio.put(nomeDesvio, dados);

    }

    public void analiseLocal(Long enderecoDesvio, boolean tomado, Long enderecoDestino, String nomeDesvio) {
        this.totalChamadas++;

        //se ja não existe predição ainda, ele deve utilizar a default, no caso 0
        Integer predicao = (this.listPredicoes.get(enderecoDesvio % 128) == null) ? 0 : this.listPredicoes.get(enderecoDesvio % 128);

        ArrayList<Long> dados = (this.listaPorTipoDesvio.get(nomeDesvio) != null) ? this.listaPorTipoDesvio.get(nomeDesvio) : new ArrayList<Long>(Arrays.asList(0L, 0L));

        switch (predicao) {
            //00
            case 0:
                //predicao not taken
                if (!tomado) {
                    //acerta e continua no mesmo estado
                    this.acerto++;
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                } else {
                    this.erro++;
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 1);
                }
                break;
            //01    
            case 1:
                //predicao not taken
                if (!tomado) {
                    //acerta e retorna para o estado anterior(00)
                    this.acerto++;
                    //predicao--;//Do HashMap? como?
                    this.listPredicoes.put((enderecoDesvio % 128), predicao - 1);
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);

                } else {
                    this.erro++;
                    //erra e vai para o estado 11 -> 3 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 2);
                }
                break;

            //11    
            case 3:
                //predicao taken
                if (tomado) {
                    //acerta e continua no mesmo estado
                    this.acerto++;
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                } else {
                    this.erro++;
                    //erra e vai para o estado 10 -> 2 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao - 1);
                }
                break;

            case 2:
                //predicao taken
                if (tomado) {
                    //acerta e retorna para o estado anterior(11)
                    // predicao++;
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 1);
                    this.acerto++;
                    //incrementa o numero de acertos relativos ao tipo de desvio
                    dados.set(0, dados.get(0) + 1);
                } else {
                    this.erro++;
                    //erra e vai para o estado 00 -> 0 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao - 2);
                }
                break;
        }
        //incrementa o numero de chamadas relativas ao tipo de desvio
        dados.set(1, dados.get(1) + 1);
        this.listaPorTipoDesvio.put(nomeDesvio, dados);

    }

    public boolean analiseGlobalPreditorTorneio(boolean tomado) {

        switch (this.predicaoAtual) {
            //00
            case 0:
                //predicao not taken
                if (!tomado) {
                    return true;
                }
                break;
            //01    
            case 1:
                //predicao not taken
                if (!tomado) {
                    return true;
                }
                break;

            //11    
            case 3:
                //predicao taken
                if (tomado) {
                    return true;
                }
                break;

            case 2:
                //predicao taken
                if (tomado) {
                    return true;

                }
                break;
        }
        return false;
    }

    public boolean analiseLocalPreditorTorneio(Long enderecoDesvio, boolean tomado) {

        //se ja não existe predição ainda, ele deve utilizar a default, no caso 0
        Integer predicao = (this.listPredicoes.get(enderecoDesvio % 128) == null) ? 0 : this.listPredicoes.get(enderecoDesvio % 128);

        switch (predicao) {
            //00
            case 0:
                //predicao not taken
                if (!tomado) {
                    //acerta e continua no mesmo estado
                    return true;
                }
                break;
            //01    
            case 1:
                //predicao not taken
                if (!tomado) {
                    //acerta e retorna para o estado anterior(00)
                    return true;

                }
                break;

            //11    
            case 3:
                //predicao taken
                if (tomado) {
                    return true;
                }
                break;

            case 2:
                //predicao taken
                if (tomado) {
                    return true;
                }
                break;
        }
        return false;

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
