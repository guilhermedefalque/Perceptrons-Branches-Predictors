/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Entidades;

/**
 *
 * @author guilherme
 */
import java.util.HashMap;

public class PreditorTresBits {

    private Integer predicaoAtual;
    private Long erro;
    private Long acerto;
    private HashMap<Long, Integer> listPredicoes;
    private Long totalChamadas;

    public Long getTotalChamadas() {
        return totalChamadas;
    }

    public PreditorTresBits() {
        this.predicaoAtual = 0;
        this.erro = 0L;
        this.acerto = 0L;
        this.listPredicoes = new HashMap<>();
        this.totalChamadas=0L;
    }
    

    public void analiseLocal(Long enderecoDesvio, boolean tomado, Long enderecoDestino) {
        this.totalChamadas++;

        //se ja não existe predição ainda, ele deve utilizar a default, no caso 0
        Integer predicao = (this.listPredicoes.get(enderecoDesvio % 128) == null) ? 0 : this.listPredicoes.get(enderecoDesvio % 128);

        switch (predicao) {
            //00
            case 0:
                //predicao not taken
                if (!tomado) {
                    //acerta e continua no mesmo estado
                    this.acerto++;
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
                    this.listPredicoes.put((enderecoDesvio % 128), predicao - 1);
                } else {
                    this.erro++;
                    //erra e vai para o estado 11 -> 3 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 2);
                }
                break;

            //11    
            case 3:
                //predicao taken
                if (!tomado) {
                    //acerta e continua no mesmo estado
                    this.acerto++;
                    this.listPredicoes.put((enderecoDesvio % 128), predicao -2);
                } else {
                    this.erro++;
                    //erra e vai para o estado 10 -> 2 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao - 1);
                }
                break;
           
           case 2:
                //predicao taken
                if (!tomado) {
                    //acerta e retorna para o estado anterior(11)
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 1);
                    this.acerto++;
                } else {
                    this.erro++;
                    //erra e vai para o estado 00 -> 0 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 4);
                }
                break;
            case 6:
                //predicao taken
                if (tomado) {
                    //acerta e retorna para o estado anterior(11)
                    this.acerto++;
                } else {
                    this.erro++;
                    //erra e vai para o estado 00 -> 0 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao - 2);
                }
                break;
            case 4:
                //predicao taken
                if (tomado) {
                    //acerta e retorna para o estado anterior(11)
                    this.acerto++;
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 2);
                } else {
                    this.erro++;
                    //erra e vai para o estado 00 -> 0 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 1);
                }
                break;
            case 5:
                //predicao taken
                if (tomado) {
                    //acerta e retorna para o estado anterior(11)
                    this.acerto++;
                    this.listPredicoes.put((enderecoDesvio % 128), predicao - 1);
                } else {
                    this.erro++;
                    //erra e vai para o estado 00 -> 0 dec
                    this.listPredicoes.put((enderecoDesvio % 128), predicao + 2);
                }
                break;
            case 7:
                //predicao taken
                if (tomado) {
                    //acerta e retorna para o estado anterior(11)
                    this.acerto++;
                    this.listPredicoes.put((enderecoDesvio % 128), predicao - 2);
                } else {
                    this.erro++;
                    //erra e vai para o estado 00 -> 0 dec
                    this.listPredicoes.put((enderecoDesvio % 128), 0);
                }
                break; 
        }

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
