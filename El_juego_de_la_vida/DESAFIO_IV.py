import time
import sys
import random

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
 


                                                            ____  _____ ____    _    _____ ___ ___    _____     __
                                                            |  _ \| ____/ ___|  / \  |  ___|_ _/ _ \  |_ _\ \   / /
                                                            | | | |  _| \___ \ / _ \ | |_   | | | | |  | | \ \ / / 
                                                            | |_| | |___ ___) / ___ \|  _|  | | |_| |  | |  \ V /  
                                                            |____/|_____|____/_/   \_\_|   |___\___/  |___|  \_/   
      
      
                                                                        TRADUCE LA CADENA PROTEICA

        
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

codigo = [["PHE","UUU","UUC"],
          ["LEU","UUA","UUG","CUU","CUC","CUA","CUG"],
          ["ILE","AUU","AUC","AUA"],
          ["MET","AUG"],
          ["VAL", "GUU", "GUC","GUA","GUG"],
          ["SER","UCU", "UCC", "UCA", "UCG"],
          ["PRO","CUU", "CCC", "CCA", "CCG"],
          ["THR","ACU", "ACC", "ACA", "ACG"],
          ["ALA", "GCU", "GCC","GCA", "GCG"],
          ["TYR", "UAU", "UAC"],
          ["STOP","UAA","UAG","UGA"],
          ["HIS", "CAU", "CAC"],
          ["GLN", "CAA", "CAG"],
          ["ASN", "AAU","ACC"],
          ["LYS","AAA","AAG"],
          ["ASP","GAU","GAC"],
          ["GLU","GAA","GAG"],
          ["CYS", "UGU","UGC"],
          ["TRP", "UGG"],
          ["ARG","CGU", "CGC","CGA","CGG","AGA","AGG"],
          ["SER","AGU","AGC,"],
          ["GLY","GGU","GGC","GGA","GGG"]]

cadena = [("Not", "OoO") , ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO"), ("Not", "OoO")]

def secuence(cadena):
    secuence =(f"""
                                                        {cadena[0][1][0]}       o O       {cadena[3][1][0]} {cadena[3][1][1]}       o O       {cadena[6][1][1]} {cadena[6][1][2]}       o o       {cadena[9][1][2]}
                                                        | {cadena[0][1][1]}   o | | O   {cadena[2][1][2]} | | {cadena[3][1][2]}   o | | o   {cadena[6][1][0]} | | {cadena[7][1][0]}   o | | o   {cadena[9][1][1]} |
                                                        | | {cadena[0][1][2]} | | | | {cadena[2][1][1]} | | | | {cadena[4][1][0]} | | | | {cadena[5][1][2]} | | | | {cadena[7][1][1]} | | | | {cadena[9][1][0]} | |
                                                        | o   {cadena[1][1][0]} | | {cadena[2][1][0]}   O | | o   {cadena[4][1][1]} | | {cadena[5][1][1]}   o | | o   {cadena[7][1][2]} | | {cadena[8][1][2]}   O |
                                                        o       {cadena[1][1][1]} {cadena[1][1][2]}       O o       {cadena[4][1][2]} {cadena[5][1][0]}       O O       {cadena[8][1][0]} {cadena[8][1][1]}       o 
""")
    
    return secuence

def clearBoard():
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'

    loop = range(1, 8)

    for i in reversed(loop):
        print(LINE_UP, end=LINE_CLEAR)
        

def answerIsCorrect(answer, cantAminos):
    aminos = cadena[0][0]
    for i in range(1, cantAminos + 1):
        aminos = aminos + ("-" + cadena[i][0])
    return answer.upper() == aminos
        

    

for i in range (0,10):
    amino = random.randint(0, 21)
    nomenclatura = random.randint(1, len( codigo[amino]) -1 )
    cadena[i] = (codigo[amino][0], codigo[amino][nomenclatura])

    respuesta = input(secuence(cadena))

    
    if (answerIsCorrect(respuesta, i)):
        clearBoard()
    elif (answerIsCorrect(respuesta, i) and i == 9):
        print("CONGRATULATIONS")
        break
    else:
        print("TRY AGAIN")
        break
    

# respuesta = input(secuence(cadena))

# if (respuesta.upper() != cadena[0][0] ):
#     print ("TRY AGAIN")
# else:

#   clearBoard()
#   cadena[1] = (codigo[1][0], codigo[1][1])
#   input(secuence(cadena))