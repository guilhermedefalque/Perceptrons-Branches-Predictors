# PerceptronsBranchesPredictors
 This repository hosts code for a predictor of branches predictors using perceptrons as the main approach.

Artificial intelligence is an area that has been widely used in several sectors,  due to its competence in creating mathematical models and estimat-ing results.  Branch prediction is one of the most important topics in computerdesign.  It is largely responsible for determining whether a pipeline executionflows is correct on processors when they are executing conditional branch in-structions,  in  order  to  avoid  undesirably  losing  clock  cycles.   Nowadays,  wehave  some  literature  that  shows  the  use  of  some  methods  to  implement  dy-namic branch predictors with artificial intelligence,  but many of these workstry to increase the reduction o Miss Prediction, however, they use methodolo-gies that implement non-causal systems and that do not allow concrete imple-mentation in computational systems, despite having a high success rate.  Thiswork aims to carry out a study of parameters and implementation of branchpredictors  using  artificial  intelligence  with  traces  generated  by  a  MIPS  simulator  designed  with  ArchC.  We  compared  the  results  of  our  work  with  the[Defalque and Thames 2017] approach and had, for some Bechmark programsused, a hit rate greater than 99%.

# Perceptrons

In this work was considered a simple perceptron [Jimenez and Lin 2001], a single-layer perceptron consisting of one artificial neuron connecting several input units by weighted edges to one output unit. A perceptron learns a target Boolean function t(x1,...,xn) of n inputs. In this work, the x_i are the bits of a global branch history shift register, and the target function predicts whether a particular branch will be taken.  The perceptron keeps track of positive and negative correlations between branch outcomes in the global history and the branch being predicted.

A perceptron is represented by avector and the elements are the weights.  For this work, based in work of [Jimenez and Lin 2001], the weights are signed integers. The output is the dot product of the weights, w0,...,wn, and the input, x1,...,xn (x0 is always set to 1, providing a "bias” input). Each x_i is −1 for not taken and  1  for taken. A negative output (y <0) is interpreted as predict not taken. A positive output (y ≥ 0) is interpreted as predict taken.

# Perceptrons Implementations

All implementations below are a correlating predictor. They were implemented based onthe algorithm proposed by [Jim ́enez and Lin 2001]. All our implementations are availableon github: https://github.com/guilhermedefalque/Perceptrons-Branches-Predictor.

- Percptron 1 (P1): This version was implemented using the idea of Global per-ceptron with 4 bits in the global history (16 columns), 4 values in the weight vectorand 1 global bias;

- Percptron 2 (P2): This version was implemented using the idea of Local percep-tron with 4 bits in the local history, 4 values in the weight vector and 1 bias;

- Percptron 3 (P3): This version was implemented using the idea of Hybrid per-ceptron with 4 bits in the global history (16 columns), 4 bits in the local history, 4 values in the weight vector and 1 bias;

- Percptron 4 (P4): This version was implemented using the idea of Hybrid per-ceptron with 4 bits in the global history (16 columns), 8 bits in the local history, 8 values in the weight vector and 1 bias;

- Percptron 5 (P5): This version was implemented using the idea of Hybrid per-ceptron and the prediction table (8 columns) is separated by instruction type. Thisperceptron has 8 bits in the local history, 8 values in the weight vector and 1 bias;

- Percptron 6 (P6): This version was implemented using the idea of Hybrid per-ceptron and the prediction table (8 columns) is separated by instruction type. Thisperceptron has 16 bits in the local history, 16 values in the weight vector and 1 bias.

# Pre-requisites and Instalations:

- Traces ArchC Generation

  - Ubuntu 14.0.4;

  - For Arch C and system C instalation: GCC, G++, python, unzip, gawk, libc6- i386, vim, m4, patch, git, autoconf, libtool, libdw-dev, bison, flex, byacc, pkg-config, build-essential, automake. Em geral, todas podem ser instaladas por apt-get.

  - System C instalation: Download of SystemC 2.3.1 (including TLM): http://
  www.accellera.org/downloads/standards/systemc 

  - Follow the installation steps directly from the official website: http://www.archc.org/doc.quickstart.html

  - Download of Archc Mips Emulator in git clone https://github.com/archc/mips.git

  - Define data caches and instructions on each model. To do so, using the
  MIPS model as an example, you should edit the mips.ac file with the settings of
  cache:

  ```
  AC_ARCH(mips){
   ac_mem DM:512M;
   ac_icache IC("2w", 128, 8, "wt", "lru"); //*
   ac_dcache DC("2w", 128, 8, "wt", "lru"); //*

   ARCH_CTOR(mips) {

   IC.bindTo (DM); //*
   DC.bindTo (DM); //*
   };
  };
  ```
  - Change the mips_isa.cpp file to the one found in our repository.

  - Download Mibench applications from the link: http://archc.lsc.ic.unicamp.br/downloads.html - version 4.8.1.

- Java Predictor Application Run [Defalque and Thames 2017]

  - Install NetBeans and Java SE Development Kit 8: https://www.oracle.com/technetwork/java/javase/downloads/jdk-netbeans-jsp-3413139-esa.html
  
- Running Perpectrons 
  - Python 3.8.6 or +;
