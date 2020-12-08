/**
 * @file      mips_isa.cpp
 * @author    Sandro Rigo
 *            Marcus Bartholomeu
 *            Alexandro Baldassin (acasm information)
 *
 *            The ArchC Team
 *            http://www.archc.org/
 *
 *            Computer Systems Laboratory (LSC)
 *            IC-UNICAMP
 *            http://www.lsc.ic.unicamp.br/
 *
 * @version   1.0
 * @date      Mon, 19 Jun 2006 15:50:52 -0300
 * 
 * @brief     The ArchC i8051 functional model.
 * 
 * @attention Copyright (C) 2002-2006 --- The ArchC Team
 *
 */

#include  "mips_isa.H"
#include  "mips_isa_init.cpp"
#include  "mips_bhv_macros.H"

#include <iostream>
#include <fstream>
//If you want debug information for this model, uncomment next line
//#define DEBUG_MODEL
#include "ac_debug_model.H"

//!User defined macros to reference registers.
#define Ra 31
#define Sp 29

// 'using namespace' statement to allow access to all
// mips-specific datatypes
using namespace mips_parms;

//shift right aritmetical
static long long int contadorSraGenerico = 0;
//static int contadorSrl = 0;
//static int contadorSll = 0;
static long long int contadorRT = 0;
static long long int contadorRS = 0;
static long long int contadorRD = 0;
static long long int contadorSllGenerico = 0;
static long long int contadorJGenerico = 0;
static long long int contadorJRGenerico = 0;
static long long int contadorSrlGenerico = 0;
static long long int contadorAddGenerico = 0;
static long long int contadorNorGenerico = 0;
static long long int contadorNop = 0;
static long long int contadorBranchGenerico = 0;
static long long int contadorDesviosTomados = 0;
static long long int contadorDesviosNaoTomados = 0;
static long long int contadorLoadGenerico = 0;
static long long int contadorStoreGenerico = 0;
static long long int contadorSltGenerico = 0;
static long long int contadorAndGenerico = 0;
static long long int contadorOrGenerico = 0;
static long long int contadorXorGenerico = 0;
static long long int contadorSubGenerico = 0;
static long long int contadorMulGenerico = 0;
static long long int contadorDivGenerico = 0;

static long long int contadorTipoR = 0;
static long long int contadorTipoI = 0;
static long long int contadorTipoJ = 0;
static long long int contadorSyscall = 0;
static long long int enderecoDesvio = 0;

static long long int contadorOpLogica=0;
static long long int contadorOpAritmetica=0;

static long long int contRegs[32];
static long long int contadorInstrucoesGlobal = 0;
static long long int contInstDesvios = 0;

static long long int processors_started = 0;

static long long int  contadorDesviosIncondicionais=0;

//ofstream arquivo("trace_basicmath_small.txt");
//ofstream arquivo("trace_bitcnts_small.txt");
//ofstream arquivo("trace_qsort_small.txt");
ofstream arquivo("trace_susan_edges_small.txt");
//ofstream arquivo("trace_susan_corners_small.txt");
//ofstream arquivo("trace_susan_smoothing_small.txt");
//ofstream arquivo("trace_dijkstra_small.txt");
//ofstream arquivo("trace_patricia_small.txt");
//ofstream arquivo("trace_sha_small.txt");
//ofstream arquivo("trace_rijndael_small.txt");

#define DEFAULT_STACK_SIZE (256*1024)

//!Generic instruction behavior method.
void ac_behavior( instruction ){
dbg_printf("----- PC=%#x ----- %lld\n", (int) ac_pc, ac_instr_counter);
//  dbg_printf("----- PC=%#x NPC=%#x ----- %lld\n", (int) ac_pc, (int)npc, ac_instr_counter);
#ifndef NO_NEED_PC_UPDATE
ac_pc = npc;
npc = ac_pc + 4;
#endif 
};

//! Instruction Format behavior methods.
void ac_behavior( Type_R ){contadorTipoR++;}
void ac_behavior( Type_I ){contadorTipoI++;}
void ac_behavior( Type_J ){contadorTipoJ++;}

//!Behavior called before starting simulation
void ac_behavior(begin){
dbg_printf("@@@ begin behavior @@@\n");

//arquivo.open ("trace_basicmath_small.txt",ios::out);
if (!arquivo.is_open())
  {
	printf("Não foi possivel abrir o arquivo");
	exit(1);
  }else{
	  printf("ARQUIVO CRIADO COM SUCESSO\n\n\n\n");
  }

RB[0] = 0;
npc = ac_pc + 4;

// Is is not required by the architecture, but makes debug really easier
for (int regNum = 0; regNum < 32; regNum ++) {
	RB[regNum] = 0;
	contRegs[regNum]=0;
}
hi = 0;
lo = 0;

RB[29] = AC_RAM_END - 1024 - processors_started++ * DEFAULT_STACK_SIZE;
}

//!Behavior called after finishing simulation
void ac_behavior(end){
	arquivo.close();
printf("\nStatísticas por instrução:\n");
printf("Total de Adds Executados(Genérico): %lld\n",contadorAddGenerico);
printf("Total de Loads Executados(Genérico): %lld\n",contadorLoadGenerico);
printf("Total de Branchess Executados(Genérico): %lld\n",contadorBranchGenerico);
printf("Total de J Executados: %lld\n",contadorJGenerico);
printf("Total de JR Executados: %lld\n",contadorJRGenerico);
printf("Total de Store Executados: %lld\n",contadorStoreGenerico);
printf("Total de Sra Executados: %lld\n",contadorSraGenerico);
printf("Total de SLL Executados: %lld\n",contadorSllGenerico);
printf("Total de NOR Executados: %lld\n",contadorNorGenerico);
printf("Total de NOP Executados: %lld\n",contadorNop);
printf("Total de XOR Executados: %lld\n",contadorXorGenerico);
printf("Total de SLT Executados: %lld\n",contadorSltGenerico);
printf("Total de AND Executados: %lld\n",contadorAndGenerico);
printf("Total de OR Executados: %lld\n",contadorOrGenerico);
printf("Total de SUB Executados: %lld\n",contadorSubGenerico);
printf("Total de MUL Executados: %lld\n",contadorMulGenerico);
printf("Total de DIV Executados: %lld\n",contadorDivGenerico);
printf("Total de Operações Aritmeticas: %lld\n",contadorOpAritmetica);
printf("Total de Operações Lógicas: %lld\n",contadorOpLogica);

//printf("\nStatísticas de Desvios instrução:\n");
printf("Quantidade de instruções entre desvios: %lld\n",contInstDesvios);
printf("Total de Desvios tomados: %lld\n",contadorDesviosTomados);
printf("Total de Desvios não tomados: %lld\n",contadorDesviosNaoTomados);
printf("Total de Desvios Incondicionais: %lld\n",contadorDesviosIncondicionais);
printf("\n\nTotal de Syscalls Executados: %lld\n",contadorSyscall);

printf("\nStatísticas por typo:\n");
printf("Tipo R: %lld\n",contadorTipoR);
printf("Tipo I: %lld\n",contadorTipoI);
printf("Tipo J: %lld\n",contadorTipoJ);

printf("\nStatísticas de acesso em registradores:\n");
printf("RT: %lld\n",contadorRT);
printf("RS: %lld\n",contadorRS);
printf("RD: %lld\n",contadorRD);


long long int totalRegs=0;
for (int regNum = 0; regNum < 32; regNum ++) {
	printf("Registrador %d: %lld\n",regNum, contRegs[regNum]);
	totalRegs=contRegs[regNum]+totalRegs;
}
printf("total registrdores:%lld\n",totalRegs);

dbg_printf("@@@ end behavior @@@\n");
}

//!Instruction lb behavior method.
void ac_behavior( lb ){
char byte;
dbg_printf("lb r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
byte = DATA_PORT->read_byte(RB[rs]+ imm);
RB[rt] = (ac_Sword)byte;
dbg_printf("Result = %#x\n", RB[rt]);
contadorRT++;
contadorRS++;
contadorLoadGenerico++;
contRegs[rt]++;
contRegs[rs]++;
contadorInstrucoesGlobal++;
};

//!Instruction lbu behavior method.
void ac_behavior( lbu ){
unsigned char byte;
dbg_printf("lbu r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
byte = DATA_PORT->read_byte(RB[rs]+ imm);
RB[rt] = byte;
dbg_printf("Result = %#x\n", RB[rt]);
contadorRT++;
contadorRS++;
contadorLoadGenerico++;
contRegs[rt]++;
contRegs[rs]++;
contadorInstrucoesGlobal++;
};

//!Instruction lh behavior method.
void ac_behavior( lh ){
short int half;
dbg_printf("lh r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
half = DATA_PORT->read_half(RB[rs]+ imm);
RB[rt] = (ac_Sword)half;
dbg_printf("Result = %#x\n", RB[rt]);
contadorRT++;
contadorRS++;
contadorLoadGenerico++;
contadorInstrucoesGlobal++;
};

//!Instruction lhu behavior method.
void ac_behavior( lhu ){
unsigned short int half;
half = DATA_PORT->read_half(RB[rs]+ imm);
RB[rt] = half;
dbg_printf("Result = %#x\n", RB[rt]);
contadorRT++;
contadorRS++;
contadorLoadGenerico++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction lw behavior method.
void ac_behavior( lw ){
dbg_printf("lw r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
RB[rt] = DATA_PORT->read(RB[rs]+ imm);
dbg_printf("Result = %#x\n", RB[rt]);
contadorRT++;
contadorRS++;
contadorLoadGenerico++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction lwl behavior method.
void ac_behavior( lwl ){
dbg_printf("lwl r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
unsigned int addr, offset;
ac_Uword data;

addr = RB[rs] + imm;
offset = (addr & 0x3) * 8;
data = DATA_PORT->read(addr & 0xFFFFFFFC);
data <<= offset;
data |= RB[rt] & ((1<<offset)-1);
RB[rt] = data;
dbg_printf("Result = %#x\n", RB[rt]);
contadorRT++;
contadorRS++;
contadorLoadGenerico++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction lwr behavior method.
void ac_behavior( lwr ){
dbg_printf("lwr r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
unsigned int addr, offset;
ac_Uword data;

addr = RB[rs] + imm;
offset = (3 - (addr & 0x3)) * 8;
data = DATA_PORT->read(addr & 0xFFFFFFFC);
data >>= offset;
data |= RB[rt] & (0xFFFFFFFF << (32-offset));
RB[rt] = data;
dbg_printf("Result = %#x\n", RB[rt]);
contadorRT++;
contadorRS++;
contadorLoadGenerico++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction sb behavior method.
void ac_behavior( sb ){
unsigned char byte;
dbg_printf("sb r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
byte = RB[rt] & 0xFF;
DATA_PORT->write_byte(RB[rs] + imm, byte);
dbg_printf("Result = %#x\n", (int) byte);
contadorRT++;
contadorRS++;
contadorStoreGenerico++;
contRegs[rt]++;
contRegs[rs]++;
contadorInstrucoesGlobal++;
};

//!Instruction sh behavior method.
void ac_behavior( sh ){
unsigned short int half;
dbg_printf("sh r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
half = RB[rt] & 0xFFFF;
DATA_PORT->write_half(RB[rs] + imm, half);
dbg_printf("Result = %#x\n", (int) half);
contadorRT++;
contadorRS++;
contadorStoreGenerico++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction sw behavior method.
void ac_behavior( sw ){
dbg_printf("sw r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
DATA_PORT->write(RB[rs] + imm, RB[rt]);
dbg_printf("Result = %#x\n", RB[rt]);
contadorRT++;
contadorRS++;
contadorStoreGenerico++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction swl behavior method.
void ac_behavior( swl ){
dbg_printf("swl r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
unsigned int addr, offset;
ac_Uword data;

addr = RB[rs] + imm;
offset = (addr & 0x3) * 8;
data = RB[rt];
data >>= offset;
data |= DATA_PORT->read(addr & 0xFFFFFFFC) & (0xFFFFFFFF << (32-offset));
DATA_PORT->write(addr & 0xFFFFFFFC, data);
contadorRT++;
contadorRS++;
contadorStoreGenerico++;
dbg_printf("Result = %#x\n", data);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

};

//!Instruction swr behavior method.
void ac_behavior( swr ){
dbg_printf("swr r%d, %d(r%d)\n", rt, imm & 0xFFFF, rs);
unsigned int addr, offset;
ac_Uword data;

addr = RB[rs] + imm;
offset = (3 - (addr & 0x3)) * 8;
data = RB[rt];
data <<= offset;
data |= DATA_PORT->read(addr & 0xFFFFFFFC) & ((1<<offset)-1);
DATA_PORT->write(addr & 0xFFFFFFFC, data);
contadorRT++;
contadorRS++;
contadorStoreGenerico++;
dbg_printf("Result = %#x\n", data);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

};

//!Instruction addi behavior method.
void ac_behavior( addi ){
dbg_printf("addi r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
RB[rt] = RB[rs] + imm;
dbg_printf("Result = %#x\n", RB[rt]);

contadorRT++;
contadorRS++;
contadorAddGenerico++;
contRegs[rt]++;
contRegs[rs]++;
contadorInstrucoesGlobal++;

//Test overflow
if ( ((RB[rs] & 0x80000000) == (imm & 0x80000000)) &&
		((imm & 0x80000000) != (RB[rt] & 0x80000000)) ) {
	fprintf(stderr, "EXCEPTION(addi): integer overflow.\n"); exit(EXIT_FAILURE);
}

};

//!Instruction addiu behavior method.
void ac_behavior( addiu ){
dbg_printf("addiu r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
RB[rt] = RB[rs] + imm;
dbg_printf("Result = %#x\n", RB[rt]);
contadorAddGenerico++;
contadorRT++;
contadorRS++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction slti behavior method.
void ac_behavior( slti ){
dbg_printf("slti r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
// Set the RD if RS< IMM
if( (ac_Sword) RB[rs] < (ac_Sword) imm )
RB[rt] = 1;
// Else reset RD
else
RB[rt] = 0;

contadorSltGenerico++;
contadorRT++;
contadorRS++;
dbg_printf("Result = %#x\n", RB[rt]);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction sltiu behavior method.
void ac_behavior( sltiu ){
dbg_printf("sltiu r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
// Set the RD if RS< IMM
if( (ac_Uword) RB[rs] < (ac_Uword) imm )
RB[rt] = 1;
// Else reset RD
else
RB[rt] = 0;

contadorRT++;
contadorRS++;
contadorSltGenerico++;
dbg_printf("Result = %#x\n", RB[rt]);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction andi behavior method.
void ac_behavior( andi ){
dbg_printf("andi r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
RB[rt] = RB[rs] & (imm & 0xFFFF);

contadorRT++;
contadorRS++;
contadorAndGenerico++;
dbg_printf("Result = %#x\n", RB[rt]);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

};

//!Instruction ori behavior method.
void ac_behavior( ori ){
dbg_printf("ori r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
RB[rt] = RB[rs] | (imm & 0xFFFF);

contadorRT++;
contadorRS++;
contadorOrGenerico++;
dbg_printf("Result = %#x\n", RB[rt]);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction xori behavior method.
void ac_behavior( xori ){
dbg_printf("xori r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
RB[rt] = RB[rs] ^ (imm & 0xFFFF);
contadorRT++;
contadorRS++;
contadorXorGenerico++;
dbg_printf("Result = %#x\n", RB[rt]);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction lui behavior method.
void ac_behavior( lui ){
dbg_printf("lui r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
// Load a constant in the upper 16 bits of a register
// To achieve the desired behaviour, the constant was shifted 16 bits left
// and moved to the target register ( rt )
RB[rt] = imm << 16;

contadorRT++;
contadorRS++;
contadorLoadGenerico++;
dbg_printf("Result = %#x\n", RB[rt]);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction add behavior method.
void ac_behavior( add ){
dbg_printf("add r%d, r%d, r%d\n", rd, rs, rt);
RB[rd] = RB[rs] + RB[rt];
contadorRT++;
contadorRS++;
contadorRD++;
contadorAddGenerico++;
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

contadorOpAritmetica++;

dbg_printf("Result = %#x\n", RB[rd]);
//Test overflow
if ( ((RB[rs] & 0x80000000) == (RB[rd] & 0x80000000)) &&
		((RB[rd] & 0x80000000) != (RB[rt] & 0x80000000)) ) {
	fprintf(stderr, "EXCEPTION(add): integer overflow.\n"); exit(EXIT_FAILURE);
}
};

//!Instruction addu behavior method.
void ac_behavior( addu ){
dbg_printf("addu r%d, r%d, r%d\n", rd, rs, rt);
RB[rd] = RB[rs] + RB[rt];
//cout << "  RS: " << (unsigned int)RB[rs] << " RT: " << (unsigned int)RB[rt] << endl;
//cout << "  Result =  " <<  (unsigned int)RB[rd] <<endl;

contadorRT++;
contadorRS++;
contadorRD++;
contadorAddGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorOpAritmetica++;

contadorInstrucoesGlobal++;
};

//!Instruction sub behavior method.
void ac_behavior( sub ){
dbg_printf("sub r%d, r%d, r%d\n", rd, rs, rt);
RB[rd] = RB[rs] - RB[rt];

contadorRT++;
contadorRS++;
contadorRD++;
contadorSubGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;

contadorOpAritmetica++;

contadorInstrucoesGlobal++;
//TODO: test integer overflow exception for sub
};

//!Instruction subu behavior method.
void ac_behavior( subu ){
dbg_printf("subu r%d, r%d, r%d\n", rd, rs, rt);
RB[rd] = RB[rs] - RB[rt];

contadorRT++;
contadorRS++;
contadorRD++;
contadorSubGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;

contadorOpAritmetica++;

contadorInstrucoesGlobal++;
};

//!Instruction slt behavior method.
void ac_behavior( slt ){
dbg_printf("slt r%d, r%d, r%d\n", rd, rs, rt);
// Set the RD if RS< RT
if( (ac_Sword) RB[rs] < (ac_Sword) RB[rt] )
RB[rd] = 1;
// Else reset RD
else
RB[rd] = 0;

contadorRT++;
contadorRS++;
contadorRD++;
contadorSltGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;

contadorInstrucoesGlobal++;
};

//!Instruction sltu behavior method.
void ac_behavior( sltu ){
dbg_printf("sltu r%d, r%d, r%d\n", rd, rs, rt);
// Set the RD if RS < RT
if( RB[rs] < RB[rt] )
RB[rd] = 1;
// Else reset RD
else
RB[rd] = 0;

contadorRT++;
contadorRS++;
contadorRD++;
contadorSltGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction instr_and behavior method.
void ac_behavior( instr_and ){
dbg_printf("instr_and r%d, r%d, r%d\n", rd, rs, rt);
RB[rd] = RB[rs] & RB[rt];

contadorRT++;
contadorRS++;
contadorRD++;
contadorAndGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

contadorOpLogica++;

};

//!Instruction instr_or behavior method.
void ac_behavior( instr_or ){
dbg_printf("instr_or r%d, r%d, r%d\n", rd, rs, rt);
RB[rd] = RB[rs] | RB[rt];

contadorRT++;
contadorRS++;
contadorRD++;
contadorOrGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

contadorOpLogica++;

};

//!Instruction instr_xor behavior method.
void ac_behavior( instr_xor ){
dbg_printf("instr_xor r%d, r%d, r%d\n", rd, rs, rt);
RB[rd] = RB[rs] ^ RB[rt];

contadorRT++;
contadorRS++;
contadorRD++;
contadorXorGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

contadorOpLogica++;

};

//!Instruction instr_nor behavior method.
void ac_behavior( instr_nor ){
dbg_printf("nor r%d, r%d, r%d\n", rd, rs, rt);
RB[rd] = ~(RB[rs] | RB[rt]);

contadorRT++;
contadorRS++;
contadorRD++;
contadorNorGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

contadorOpLogica++;

};

//!Instruction nop behavior method.
void ac_behavior( nop ){
contadorNop++;
dbg_printf("nop\n");
};

//!Instruction sll behavior method.
void ac_behavior( sll ){
dbg_printf("sll r%d, r%d, %d\n", rd, rs, shamt);
RB[rd] = RB[rt] << shamt;

contadorRT++;
contadorRS++;
contadorRD++;
contadorSllGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction srl behavior method.
void ac_behavior( srl ){
dbg_printf("srl r%d, r%d, %d\n", rd, rs, shamt);
RB[rd] = RB[rt] >> shamt;

contadorRT++;
contadorRS++;
contadorRD++;
contadorSrlGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction sra behavior method.
void ac_behavior( sra ){
dbg_printf("sra r%d, r%d, %d\n", rd, rs, shamt);
RB[rd] = (ac_Sword) RB[rt] >> shamt;

contadorRT++;
contadorRS++;
contadorRD++;
contadorSraGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction sllv behavior method.
void ac_behavior( sllv ){
dbg_printf("sllv r%d, r%d, r%d\n", rd, rt, rs);
RB[rd] = RB[rt] << (RB[rs] & 0x1F);

contadorRT++;
contadorRS++;
contadorRD++;
contadorSllGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction srlv behavior method.
void ac_behavior( srlv ){
dbg_printf("srlv r%d, r%d, r%d\n", rd, rt, rs);
RB[rd] = RB[rt] >> (RB[rs] & 0x1F);

contadorRT++;
contadorRS++;
contadorRD++;
contadorSrlGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction srav behavior method.
void ac_behavior( srav ){
dbg_printf("srav r%d, r%d, r%d\n", rd, rt, rs);
RB[rd] = (ac_Sword) RB[rt] >> (RB[rs] & 0x1F);

contadorRT++;
contadorRS++;
contadorRD++;
contadorSraGenerico++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
};

//!Instruction mult behavior method.
void ac_behavior( mult ){
dbg_printf("mult r%d, r%d\n", rs, rt);

long long result;
int half_result;

result = (ac_Sword) RB[rs];
result *= (ac_Sword) RB[rt];

half_result = (result & 0xFFFFFFFF);
// Register LO receives 32 less significant bits
lo = half_result;

half_result = ((result >> 32) & 0xFFFFFFFF);
// Register HI receives 32 most significant bits
hi = half_result;

contadorRT++;
contadorRS++;
contadorMulGenerico++;
dbg_printf("Result = %#llx\n", result);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
contadorOpAritmetica++;

};

//!Instruction multu behavior method.
void ac_behavior( multu ){
dbg_printf("multu r%d, r%d\n", rs, rt);

unsigned long long result;
unsigned int half_result;

result = RB[rs];
result *= RB[rt];

half_result = (result & 0xFFFFFFFF);
// Register LO receives 32 less significant bits
lo = half_result;

half_result = ((result>>32) & 0xFFFFFFFF);
// Register HI receives 32 most significant bits
hi = half_result;

contadorRT++;
contadorRS++;
contadorMulGenerico++;
dbg_printf("Result = %#llx\n", result);
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;
contadorOpAritmetica++;

};

//!Instruction div behavior method.
void ac_behavior( div ){
dbg_printf("div r%d, r%d\n", rs, rt);
// Register LO receives quotient
lo = (ac_Sword) RB[rs] / (ac_Sword) RB[rt];
// Register HI receives remainder
hi = (ac_Sword) RB[rs] % (ac_Sword) RB[rt];

contadorRT++;
contadorRS++;
contadorDivGenerico++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

contadorOpAritmetica++;

};

//!Instruction divu behavior method.
void ac_behavior( divu ){
dbg_printf("divu r%d, r%d\n", rs, rt);
// Register LO receives quotient
lo = RB[rs] / RB[rt];
// Register HI receives remainder
hi = RB[rs] % RB[rt];

contadorRT++;
contadorRS++;
contadorDivGenerico++;
contRegs[rs]++;
contRegs[rt]++;
contadorInstrucoesGlobal++;

contadorOpAritmetica++;

};

//!Instruction mfhi behavior method.
void ac_behavior( mfhi ){
dbg_printf("mfhi r%d\n", rd);
RB[rd] = hi;

contadorRD++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contadorInstrucoesGlobal++;
};

//!Instruction mthi behavior method.
void ac_behavior( mthi ){
dbg_printf("mthi r%d\n", rs);
hi = RB[rs];

contadorRS++;
dbg_printf("Result = %#x\n", (unsigned int) hi);

contRegs[rs]++;
contadorInstrucoesGlobal++;
};

//!Instruction mflo behavior method.
void ac_behavior( mflo ){
dbg_printf("mflo r%d\n", rd);
RB[rd] = lo;

contadorRD++;
dbg_printf("Result = %#x\n", RB[rd]);
contRegs[rd]++;
contadorInstrucoesGlobal++;
};

//!Instruction mtlo behavior method.
void ac_behavior( mtlo ){
dbg_printf("mtlo r%d\n", rs);
lo = RB[rs];

contadorRS++;
dbg_printf("Result = %#x\n", (unsigned int) lo);
contRegs[rs]++;
contadorInstrucoesGlobal++;
};

//!Instruction j behavior method.
void ac_behavior( j ){
dbg_printf("j %d\n", addr);
contadorJGenerico++;
contadorDesviosIncondicionais++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

addr = addr << 2;
#ifndef NO_NEED_PC_UPDATE
npc = (ac_pc & 0xF0000000) | addr;
#endif 
dbg_printf("Target = %#x\n", (ac_pc & 0xF0000000) | addr );
};

//!Instruction jal behavior method.
void ac_behavior( jal ){
dbg_printf("jal %d\n", addr);
contadorDesviosIncondicionais++;

contadorJGenerico++;
contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

// Save the value of PC + 8 (return address) in $ra ($31) and
// jump to the address given by PC(31...28)||(addr<<2)
// It must also flush the instructions that were loaded into the pipeline
RB[Ra] = ac_pc+4;//ac_pc is pc+4, we need pc+8

addr = addr << 2;
#ifndef NO_NEED_PC_UPDATE
npc = (ac_pc & 0xF0000000) | addr;
#endif 

dbg_printf("Target = %#x\n", (ac_pc & 0xF0000000) | addr );
dbg_printf("Return = %#x\n", ac_pc+4);
contRegs[Ra]++;

};

//!Instruction jr behavior method.
void ac_behavior( jr ){
dbg_printf("jr r%d\n", rs);
contadorJRGenerico++;
contadorDesviosIncondicionais++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;
// Jump to the address stored on the register reg[RS]
// It must also flush the instructions that were loaded into the pipeline
#ifndef NO_NEED_PC_UPDATE
npc = RB[rs], (void) 1;
#endif 

contadorRS++;
dbg_printf("Target = %#x\n", RB[rs]);
contRegs[rs]++;
};

//!Instruction jalr behavior method.
void ac_behavior( jalr ){
dbg_printf("jalr r%d, r%d\n", rd, rs);
contadorDesviosIncondicionais++;

// Save the value of PC + 8(return address) in rd and
// jump to the address given by [rs]
contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;
#ifndef NO_NEED_PC_UPDATE
npc = RB[rs], (void) 1;
#endif 
dbg_printf("Target = %#x\n", RB[rs]);

if( rd == 0 )  //If rd is not defined use default
rd = Ra;
RB[rd] = ac_pc+4;

contadorRS++;
contadorRD++;

dbg_printf("Return = %#x\n", ac_pc+4);
contRegs[rd]++;
contRegs[rs]++;
};

//!Instruction beq behavior method.
void ac_behavior( beq ){
dbg_printf("beq r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
contadorBranchGenerico++;
contadorRT++;
contadorRS++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

if( RB[rs] == RB[rt] ) {
	contadorDesviosTomados++;
#ifndef NO_NEED_PC_UPDATE
	npc = ac_pc + (imm<<2);
#endif 
	arquivo << ac_pc<<":1:"<<npc<<":0"<<"\n";
	dbg_printf("Taken to %#x\n", ac_pc + (imm<<2));
} else {
	arquivo << ac_pc<<":0:"<<ac_pc + (imm<<2)<<":0"<<"\n";
	contadorDesviosNaoTomados++;
}
contRegs[rs]++;
contRegs[rt]++;
};

//!Instruction bne behavior method.
void ac_behavior( bne ){
dbg_printf("bne r%d, r%d, %d\n", rt, rs, imm & 0xFFFF);
contadorBranchGenerico++;
contadorRT++;
contadorRS++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

if( RB[rs] != RB[rt] ) {
	contadorDesviosTomados++;
#ifndef NO_NEED_PC_UPDATE
	npc = ac_pc + (imm<<2);
#endif 
	arquivo << ac_pc<<":1:"<<npc<<":1"<<"\n";
	dbg_printf("Taken to %#x\n", ac_pc + (imm<<2));
} else {
	arquivo << ac_pc<<":0:"<<ac_pc + (imm<<2)<<":1"<<"\n";
	contadorDesviosNaoTomados++;}


contRegs[rs]++;
contRegs[rt]++;
};

//!Instruction blez behavior method.
void ac_behavior( blez ){
dbg_printf("blez r%d, %d\n", rs, imm & 0xFFFF);
contadorBranchGenerico++;
contadorRS++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

if( (RB[rs] == 0 ) || (RB[rs]&0x80000000 ) ) {
	contadorDesviosTomados++;
#ifndef NO_NEED_PC_UPDATE
	npc = ac_pc + (imm<<2), (void) 1;
#endif 
	arquivo << ac_pc<<":1:"<<npc<<":2"<<"\n";
	dbg_printf("Taken to %#x\n", ac_pc + (imm<<2));
} else {
	arquivo << ac_pc<<":0:"<<ac_pc + (imm<<2)<<":2"<<"\n";
	contadorDesviosNaoTomados++;
}
contRegs[rs]++;
};

//!Instruction bgtz behavior method.
void ac_behavior( bgtz ){
dbg_printf("bgtz r%d, %d\n", rs, imm & 0xFFFF);
contadorBranchGenerico++;
contadorRS++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

if( !(RB[rs] & 0x80000000) && (RB[rs]!=0) ) {
	contadorDesviosTomados++;
#ifndef NO_NEED_PC_UPDATE
	npc = ac_pc + (imm<<2);
#endif 
	arquivo << ac_pc<<":1:"<<npc<<":3"<<"\n";
	dbg_printf("Taken to %#x\n", ac_pc + (imm<<2));
} else {
	arquivo << ac_pc<<":0:"<<ac_pc + (imm<<2)<<":3"<<"\n";
	contadorDesviosNaoTomados++;
}
contRegs[rs]++;
};

//!Instruction bltz behavior method.
void ac_behavior( bltz ){
dbg_printf("bltz r%d, %d\n", rs, imm & 0xFFFF);
contadorBranchGenerico++;
contadorRS++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

if( RB[rs] & 0x80000000 ) {
	contadorDesviosTomados++;
#ifndef NO_NEED_PC_UPDATE
	npc = ac_pc + (imm<<2);
#endif 
	arquivo << ac_pc<<":1:"<<npc<<":4"<<"\n";
	dbg_printf("Taken to %#x\n", ac_pc + (imm<<2));
} else {
	arquivo << ac_pc<<":0:"<<ac_pc + (imm<<2)<<":4"<<"\n";
	contadorDesviosNaoTomados++;
}
contRegs[rs]++;
};

//!Instruction bgez behavior method.
void ac_behavior( bgez ){
dbg_printf("bgez r%d, %d\n", rs, imm & 0xFFFF);
contadorBranchGenerico++;
contadorRS++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

if( !(RB[rs] & 0x80000000) ) {
	contadorDesviosTomados++;
#ifndef NO_NEED_PC_UPDATE
	npc = ac_pc + (imm<<2);
#endif 
	arquivo << ac_pc<<":1:"<<npc<<":5"<<"\n";
	dbg_printf("Taken to %#x\n", ac_pc + (imm<<2));
} else {
	arquivo << ac_pc<<":0:"<<ac_pc + (imm<<2)<<":5"<<"\n";
	contadorDesviosNaoTomados++;
}
contRegs[rs]++;
};

//!Instruction bltzal behavior method.
void ac_behavior( bltzal ){
dbg_printf("bltzal r%d, %d\n", rs, imm & 0xFFFF);
contadorBranchGenerico++;
contadorRS++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

RB[Ra] = ac_pc+4; //ac_pc is pc+4, we need pc+8
if( RB[rs] & 0x80000000 ) {
	contadorDesviosTomados++;
#ifndef NO_NEED_PC_UPDATE
	npc = ac_pc + (imm<<2);
#endif 
	arquivo << ac_pc<<":1:"<<npc<<":6"<<"\n";
	dbg_printf("Taken to %#x\n", ac_pc + (imm<<2));
} else {
	arquivo << ac_pc<<":0:"<<ac_pc + (imm<<2)<<":6"<<"\n";
	contadorDesviosNaoTomados++;
}
dbg_printf("Return = %#x\n", ac_pc+4);
contRegs[rs]++;
};

//!Instruction bgezal behavior method.
void ac_behavior( bgezal ){
dbg_printf("bgezal r%d, %d\n", rs, imm & 0xFFFF);
contadorBranchGenerico++;
contadorRS++;

contInstDesvios= contadorInstrucoesGlobal+contInstDesvios;
contadorInstrucoesGlobal=0;

RB[Ra] = ac_pc+4; //ac_pc is pc+4, we need pc+8
if( !(RB[rs] & 0x80000000) ) {
	contadorDesviosTomados++;
#ifndef NO_NEED_PC_UPDATE
	npc = ac_pc + (imm<<2);
#endif 
	arquivo << ac_pc<<":1:"<<npc<<":7"<<"\n";
	dbg_printf("Taken to %#x\n", ac_pc + (imm<<2));
} else {
	arquivo << ac_pc<<":0:"<<ac_pc + (imm<<2)<<":7"<<"\n";
	contadorDesviosNaoTomados++;
}
dbg_printf("Return = %#x\n", ac_pc+4);
contRegs[rs]++;
};

//!Instruction sys_call behavior method.
void ac_behavior( sys_call ){
contadorInstrucoesGlobal++;
contadorSyscall++;
dbg_printf("syscall\n");
stop();

};

//!Instruction instr_break behavior method.
void ac_behavior( instr_break ){
fprintf(stderr, "instr_break behavior not implemented.\n");
exit(EXIT_FAILURE);
};
