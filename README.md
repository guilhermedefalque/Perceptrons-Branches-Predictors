# PerceptronsBranchesPredictors
 This repository hosts code for a predictor of branches predictors using perceptrons as the main approach.

Artificial intelligence is an area that has been widely used in several sectors,  due to its competence in creating mathematical models and estimat-ing results.  Branch prediction is one of the most important topics in computerdesign.  It is largely responsible for determining whether a pipeline executionflows is correct on processors when they are executing conditional branch in-structions,  in  order  to  avoid  undesirably  losing  clock  cycles.   Nowadays,  wehave  some  literature  that  shows  the  use  of  some  methods  to  implement  dy-namic branch predictors with artificial intelligence,  but many of these workstry to increase the reduction o Miss Prediction, however, they use methodolo-gies that implement non-causal systems and that do not allow concrete imple-mentation in computational systems, despite having a high success rate.  Thiswork aims to carry out a study of parameters and implementation of branchpredictors  using  artificial  intelligence  with  traces  generated  by  a  MIPS  simulator  designed  with  ArchC.  We  compared  the  results  of  our  work  with  the[Defalque and Thames 2017] approach and had, for some Bechmark programsused, a hit rate greater than 99%.

# Perceptrons

In this work was considered a simple perceptron [Jimenez and Lin 2001], a single-layer perceptron consisting of one artificial neuron connecting several input units by weighted edges to one output unit. A perceptron learns a target Boolean function t(x1,...,xn) of n inputs. In this work, the x_i are the bits of a global branch history shift register, and the target function predicts whether a particular branch will be taken.  The perceptron keeps track of positive and negative correlations between branch outcomes in the global history and the branch being predicted.

A perceptron is represented by avector and the elements are the weights.  For this work, based in work of [Jimenez and Lin 2001], the weights are signed integers. The output is the dot product of the weights, w0,...,wn, and the input, x1,...,xn (x0 is always set to 1, providing a "bias” input). Each x_i is −1 for not taken and  1  for taken. A negative output (y <0) is interpreted as predict not taken. A positive output (y ≥ 0) is interpreted as predict taken.

# Perceptrons Implementations

All implementations below are a correlating predictor. They were implemented based onthe algorithm proposed by [Jim ́enez and Lin 2001]. All our implementations are availableon github: https://github.com/guilhermedefalque/Perceptrons-Branches-Predictor.

-> Percptron 1 (P1): This version was implemented using the idea of Global per-ceptron with 4 bits in the global history (16 columns), 4 values in the weight vectorand 1 global bias;

-> Percptron 2 (P2): This version was implemented using the idea of Local percep-tron with 4 bits in the local history, 4 values in the weight vector and 1 bias;

-> Percptron 3 (P3): This version was implemented using the idea of Hybrid per-ceptron with 4 bits in the global history (16 columns), 4 bits in the local history, 4 values in the weight vector and 1 bias;

-> Percptron 4 (P4): This version was implemented using the idea of Hybrid per-ceptron with 4 bits in the global history (16 columns), 8 bits in the local history, 8 values in the weight vector and 1 bias;

-> Percptron 5 (P5): This version was implemented using the idea of Hybrid per-ceptron and the prediction table (8 columns) is separated by instruction type. Thisperceptron has 8 bits in the local history, 8 values in the weight vector and 1 bias;

-> Percptron 6 (P6): This version was implemented using the idea of Hybrid per-ceptron and the prediction table (8 columns) is separated by instruction type. Thisperceptron has 16 bits in the local history, 16 values in the weight vector and 1 bias.

# Methodology

# Pre-requisites:

ArchC 

Ubuntu 14.0.4;

For Arch C and system C instalation: GCC, G++, python, unzip, gawk, libc6- i386, vim, m4, patch, git, autoconf, libtool, libdw-dev, bison, flex, byacc, pkg-config, build-essential, automake. Em geral, todas podem ser instaladas por apt-get.

System C instalation: Download of SystemC 2.3.1 (including TLM): http://
www.accellera.org/downloads/standards/systemc 

Follow the installation steps directly from the official website: http://www.archc.org/doc.quickstart.html

Download of Archc Mips Emulator in git clone https://github.com/archc/mips.git

Define data caches and instructions on each model. To do so, using the
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
Change the mips_isa.cpp file to the one found in our repository.

Download Mibench applications from the link: http://archc.lsc.ic.unicamp.br/downloads.html - version 4.8.1.

# Installation

Download the latest [Linux/MacOS binaries](https://github.com/GATB/bcalm/releases), or compile from source as follows:

    git clone --recursive https://github.com/GATB/bcalm 
    cd bcalm
    mkdir build;  cd build;  cmake ..;  make -j 8
    
You can also install bcalm from [bioconda](https://bioconda.github.io/) with [conda](https://docs.conda.io/en/latest/):

    conda install -c conda-forge -c bioconda bcalm

# Input formats

File input format can be fasta, fastq, either gzipped or not. BCALM 2 does not care about paired-end information, all given reads contribute to k-mers in the graph (as long as such k-mers pass the abundance threshold).

To pass several files as input:

    ls -1 *.fastq > list_reads
    ./bcalm -in list_reads [..]
   
# Output

BCALM 2 outputs the set of unitigs of the de Bruijn graph.
A unitig is the sequence of a non-branching path. Unitigs that are connected by an edge in the graph overlap by exactly (k-1) nucleotides. For a formal description of what BCALM2 outputs, see [here](bidirected-graphs-in-bcalm2/bidirected-graphs-in-bcalm2.md)

We have two output formats: FASTA and GFA.

**GFA** output: use `scripts/convertToGFA.py` to convert the output of BCALM 2 to GFA (contributed by Mayank Pahadia).


FASTA output header: 

    ><id> LN:i:<length> KC:i:<abundance> km:f:<abundance> L:<+/->:<other id>:<+/-> [..]

Where:

* `LN` field is the length of the unitig
    
* `KC` and `km` fields are for total abundance and mean abundance of kmers inside the unitig, respectively.

* Edges between unitigs are reported as `L:x:y:z` entries in the FASTA header (1 entry per edge). A classic forward-forward outcoming edge is labeled `L:+:[next node]:+`. A forward-reverse, `L:+:[next node]:-`. Incoming edges are encoded as outcoming edges of the reverse-complement node. E.g. `L:-:[previous node]:+` means that if you reverse-complemented the current node, then there would be an edge from the last k-mer of current node to the first k-mer of the forward strand of [previous node].

# Reverse-complements and double-strandedness

BCALM 2 converts all k-mers into their canonical representation with respect to reverse-complements.
In other words, a k-mer and its reverse complement are considered to be the same object, appearing only once in the output, either in forward or reverse orientation.

Note: in the output of BCALM 2, each unitig may be either be returned in forward or reverse orientation, with no guarantee that the orientation will stay the same across identical runs of the software.

For a formal description of how BCALM2 handles double-strandedness of DNA, see [here](bidirected-graphs-in-bcalm2/bidirected-graphs-in-bcalm2.md)

# Larger k values

BCALM 2 supports arbitrary large k-mer lengths. You need to recompile it from sources. For k up to, say, 320, type this in the build folder:

    rm -Rf CMake* && cmake -DKSIZE_LIST="32 64 96 128 160 192 224 256 320" .. && make -j 8

For compilation, list of kmers should only contain multiples of 32. Also, for technical reason, keep 32 in the list. Of course, for higher k's, BCALM will run slower. Intermediate values create optimized code for smaller $k$'s. You could specify just `KSIZE_LIST="32 320"` but then using k values above would 32 be as slow as if k was equal to 320.

After that, BCALM 2 can be run with any k value up to the largest one specified during compilation.

# Intermediate files

BCALM 2 produces some intermediate files: a .h5 file (or a _gatb/ folder), which contain the k-mer counts. The "\*glue\*" files contain compacted sequences that needs to be glued together (see BCALM 2 paper). Those files can be safely deleted after an execution, as the actual output is just the FASTA file containing the unitigs.

Acknowledgements
========
If using BCALM 2, please cite:
Rayan Chikhi, Antoine Limasset and Paul Medvedev, Compacting de Bruijn graphs from sequencing data quickly and in low memory, Proceedings of ISMB 2016, Bioinformatics, 32 (12): i201-i208.  ([Bibtex](https://academic.oup.com/Citation/Download?resourceId=2289008&resourceType=3&citationFormat=2))

This project has been supported in part by NSF awards DBI-1356529, CCF-1439057, IIS-1453527, and IIS-1421908.
