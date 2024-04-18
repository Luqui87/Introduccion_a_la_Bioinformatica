import time
import sys
import random
import subprocess
from tabulate import tabulate
import time
import argparse

parser = argparse.ArgumentParser(description='Traducí la cadena de ADN de un codón a la vez, con la abreviatura de 3 letras del aminoácido. (Es necesario instalar pip)')
parser.add_argument('-e', '--easyMode',
                    type=str,
                    help='Mostar tabla de aminoácidos (-e y)')

parser.add_argument('-r', '--rounds',
                    type=int,
                    help='Rondas de aminoácidos que habra que traducir',
                    default=10)

args = parser.parse_args()

subprocess.check_call(["pip","install","tabulate"])



input(r"""
                          TTTTT     CCCCC                          TTTTT     CCCCC                          TTTTT     CCCCC                          TTTTT     CCCCC                        
CC                      TT: : :TT CC| | |CC                      TT : : TT CC | | CC                      TT: : :TT CC| | |CC                      TT : : TT CC | | CC                      
| C                   TT: : : : CT| | | | |C                   TT : : : :CT | | | | C                   TT: : : : CT| | | | |C                   TT : : : :CT | | | | C                   T 
| |CC                T: : : : :C  TT| | | | CC                T : : : : C  TT | | | |CC                T: : : : :C  TT| | | | CC                T : : : : C  TT | | | |CC                T: 
| | |C              T : : : : C     T | | | | C              T: : : : :C     T| | | | |C              T : : : : C     T | | | | C              T: : : : :C     T| | | | |C              T : 
| | | C            T: : : : :C       T| | | | |C            T : : : : C       T | | | | C            T: : : : :C       T| | | | |C            T : : : : C       T | | | | C            T: : 
| | | |C         TT : : : :CC         T | | | | C         TT: : : : CC         T| | | | |C         TT : : : :CC         T | | | | C         TT: : : : CC         T| | | | |C         TT : : 
| | | | C       T : : : : C            T| | | | |C       T: : : : :C            T | | | | C       T : : : : C            T| | | | |C       T: : : : :C            T | | | | C       T : : : 
| | | | |C     T: : : : :C              T | | | | C     T : : : : C              T| | | | |C     T: : : : :C              T | | | | C     T : : : : C              T| | | | |C     T: : : : 
TT| | | | CC  T : : : : C                TT | | | |CC  T: : : : :C                TT| | | | CC  T : : : : C                TT | | | |CC  T: : : : :C                TT| | | | CC  T : : : : 
  T | | | | CT: : : : CC                   T| | | | |CT : : : :CC                   T | | | | CT: : : : CC                   T| | | | |CT : : : :CC                   T | | | | CT: : : : C 
   TT | | TT CC : : CC                      TT| | |TT CC: : :CC                      TT | | TT CC : : CC                      TT| | |TT CC: : :CC                      TT | | TT CC : : CC  
 


                                                            ____  _____ ____    _    _____ ___ ___    _____      __
                                                            |  _ \| ____/ ___|  / \  |  ___|_ _/ _ \  |_ _\ \   / /
                                                            | | | |  _| \___ \ / _ \ | |_   | | | | |  | | \ \ / / 
                                                            | |_| | |___ ___) / ___ \|  _|  | | |_| |  | |  \ V /  
                                                            |____/|_____|____/_/   \_\_|   |___\___/  |___|  \_/   
      
      
                                                            TRADUCE LA CADENA PROTEICA DE UN CODON A LA VEZ. Ej:
                                                                          
                                                                                A       
                                                                                | T   
                                                                                | | G = MET
                                                                                | o   
                                                                                o      

                                                        _____ _____ _______ ____ ____  ______ _____ _____ _____ ____       
                                                        |  _ \|  _ \| ____/ ___/ ___|  | ____| \ | |_   _| ____|  _ \ 
                                                        | |_) | |_) |  _| \___ \___ \  |  _| |  \| | | | |  _| | |_) |
                                                        |  __/|  _ <| |___ ___) |__) | | |___| |\  | | | | |___|  _ < 
                                                        |_|   |_| \_\_____|____/____/  |_____|_| \_| |_| |_____|_| \_\
                                                               
      
                          TTTTT     CCCCC                          TTTTT     CCCCC                          TTTTT     CCCCC                          TTTTT     CCCCC                        
CC                      TT: : :TT CC| | |CC                      TT : : TT CC | | CC                      TT: : :TT CC| | |CC                      TT : : TT CC | | CC                      
| C                   TT: : : : CT| | | | |C                   TT : : : :CT | | | | C                   TT: : : : CT| | | | |C                   TT : : : :CT | | | | C                   T 
| |CC                T: : : : :C  TT| | | | CC                T : : : : C  TT | | | |CC                T: : : : :C  TT| | | | CC                T : : : : C  TT | | | |CC                T: 
| | |C              T : : : : C     T | | | | C              T: : : : :C     T| | | | |C              T : : : : C     T | | | | C              T: : : : :C     T| | | | |C              T : 
| | | C            T: : : : :C       T| | | | |C            T : : : : C       T | | | | C            T: : : : :C       T| | | | |C            T : : : : C       T | | | | C            T: : 
| | | |C         TT : : : :CC         T | | | | C         TT: : : : CC         T| | | | |C         TT : : : :CC         T | | | | C         TT: : : : CC         T| | | | |C         TT : : 
| | | | C       T : : : : C            T| | | | |C       T: : : : :C            T | | | | C       T : : : : C            T| | | | |C       T: : : : :C            T | | | | C       T : : : 
| | | | |C     T: : : : :C              T | | | | C     T : : : : C              T| | | | |C     T: : : : :C              T | | | | C     T : : : : C              T| | | | |C     T: : : : 
TT| | | | CC  T : : : : C                TT | | | |CC  T: : : : :C                TT| | | | CC  T : : : : C                TT | | | |CC  T: : : : :C                TT| | | | CC  T : : : : 
  T | | | | CT: : : : CC                   T| | | | |CT : : : :CC                   T | | | | CT: : : : CC                   T| | | | |CT : : : :CC                   T | | | | CT: : : : C 
   TT | | TT CC : : CC                      TT| | |TT CC: : :CC                      TT | | TT CC : : CC                      TT| | |TT CC: : :CC                      TT | | TT CC : : CC 
      
      
""")

codigo = [["PHE","TTT","TTC"],
          ["LET","TTA","TTG","CTT","CTC","CTA","CTG"],
          ["ILE","ATT","ATC","ATA"],
          ["MET","ATG"],
          ["VAL", "GTT", "GTC","GTA","GTG"],
          ["SER","TCT", "TCC", "TCA", "TCG"],
          ["PRO","CTT", "CCC", "CCA", "CCG"],
          ["THR","ACT", "ACC", "ACA", "ACG"],
          ["ALA", "GCT", "GCC","GCA", "GCG"],
          ["TYR", "TAT", "TAC"],
          #["STOP","TAA","TAG","TGA"],
          ["HIS", "CAT", "CAC"],
          ["GLN", "CAA", "CAG"],
          ["ASN", "AAT","ACC"],
          ["LYS","AAA","AAG"],
          ["ASP","GAT","GAC"],
          ["GLU","GAA","GAG"],
          ["CYS", "TGT","TGC"],
          ["TRP", "TGG"],
          ["ARG","CGT", "CGC","CGA","CGG","AGA","AGG"],
          ["SER","AGT","AGC"],
          ["GLY","GGT","GGC","GGA","GGG"]]

times = [ ]
head = ["Usuario","Tiempo"]

def secuence(cadena):
    secuence =(f"""
                                                        {cadena[0][1][0]}       o O       {cadena[3][1][0]} {cadena[3][1][1]}       o O       {cadena[6][1][1]} {cadena[6][1][2]}       o o       {cadena[9][1][2]}
                                                        | {cadena[0][1][1]}   o | | O   {cadena[2][1][2]} | | {cadena[3][1][2]}   o | | o   {cadena[6][1][0]} | | {cadena[7][1][0]}   o | | o   {cadena[9][1][1]} |
                                                        | | {cadena[0][1][2]} | | | | {cadena[2][1][1]} | | | | {cadena[4][1][0]} | | | | {cadena[5][1][2]} | | | | {cadena[7][1][1]} | | | | {cadena[9][1][0]} | |
                                                        | o   {cadena[1][1][0]} | | {cadena[2][1][0]}   O | | o   {cadena[4][1][1]} | | {cadena[5][1][1]}   o | | o   {cadena[7][1][2]} | | {cadena[8][1][2]}   O |
                                                        o       {cadena[1][1][1]} {cadena[1][1][2]}       O o       {cadena[4][1][2]} {cadena[5][1][0]}       O O       {cadena[8][1][0]} {cadena[8][1][1]}       o 
""")
    
    return secuence

def addAmino(index, cadena):
    amino = random.randint(0, 21)
    nomenclatura = random.randint(1, len( codigo[amino]) -1 )
    cadena[index] = (codigo[amino][0], codigo[amino][nomenclatura])
    return cadena


def clearBoard():
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'

    loop = range(1, 8)

    for i in reversed(loop):
        print(LINE_UP, end=LINE_CLEAR)
        

def answerIsCorrect(answer, cantAminos, cadena):
    # aminos = cadena[0][0]
    # for i in range(1, cantAminos + 1):
    #     aminos = aminos + ("-" + cadena[i][0])
    # return answer.upper() == aminos MODO DE JUEGO DIFICIL
    return answer.upper() == cadena[cantAminos][0]
    

    
def win(time, rounds):
    user = input("Ingrese nombre: ")
    times.insert(0, (user, round(time,2)))
    times.sort(key=lambda x: x[1])
    print(tabulate(times, headers=head, tablefmt="grid"))
    replay = input("Jugar de nuevo? (Y-N): ")
    if (replay.upper() == "Y"):
        playGame(rounds)



def playGame(rounds):
    cadena = [("Not", "OoO") , ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO")]

    start = time.time()

    for i in range (0,rounds):
        cadena = addAmino(i, cadena)

        respuesta = input(secuence(cadena))

        clearBoard()

        if (answerIsCorrect(respuesta, i, cadena) and i == rounds -1):
            end = time.time() - start
            win(end, rounds)
            break
        elif (not answerIsCorrect(respuesta, i, cadena)):
            replay = input("ERROR!, jugar de nuevo? (Y-N):")
            if (replay.upper() == "Y"):
                playGame(rounds)
                break
            break
        
if (args.easyMode == "y"):
    print(tabulate(codigo, tablefmt="grid"))
playGame(args.rounds)

