import numpy as np
import geometry_tools as gt
from functools import cmp_to_key

def cmp_segments(p, q, r):
    '''
    Compara os segmentos para serem ordenados
    '''
    d = gt.direction(p, q, r)
    # Se o segmento p-q estiver no sentido anti-horario de p-r 
    if d < 0:
        return -1
    if d > 0:
        return 1
    # Se forem colineres obtem o ponto mais longe de p
    if d == 0:
        if gt.distance(q, p) < gt.distance(r, p):
            return -1
        else:
            return 1

def remove_duplicates(P, p0):
    '''
    Verifica quais segmentos são colineares e
    mantem o mais longe de p0
    '''
    n = len(P)
    m = 0
    remove = []
    for i in range(n-1):
        while(i < n-1 and gt.direction(p0, P[i], P[i+1]) == 0):
            i += 1
        if(P[m] != P[i]):
            if(gt.distance(P[m], p0) > gt.distance(P[i], p0)):
                remove.append(P[i])
            else:
                remove.append(P[m])
        m += 1
    for i in remove:
        P.remove(i)

def graham_scan(P):
    '''
    Graham_scan mantem uma pilha com os segmentos da envoltoria.
    '''
    p0 = gt.min_point(P) # Pega o ponto mais baixo

    P_s = sorted(P, key=cmp_to_key(lambda x,y: cmp_segments(x,y,p0))) # Ordena os segmentos
    remove_duplicates(P_s,p0)
    
    s = [] # Inicializa a pilha
    s.append(p0)
    s.append(P_s[0])
    s.append(P_s[1])
    size = 3

    for i in range(2, len(P_s)): # Percorre todos os segments
        while gt.direction(P_s[i], s[size-2], s[size-1]) > 0: # Enquanto um segmento faz uma curva para direita
            s.pop() # remove o segmento da pilha
            size -= 1
        s.append(P_s[i])
        size += 1
    return s

def gift_wrap(P):
    p0 = min(P, key = lambda p: p.x) # Acha o ponto mais a esquerda
    index = P.index(p0) # Encontra o indice de p0
    
    hull = [] # Lista contendo a envoltoria convexa
    hull.append(p0) # p0 por definiçao faz parte da envoltoria convexa
    
    j = index
    n = len(P)
    
    # Equivalente ao do-while(j != index)
    while(True):
        k = (j + 1) % n # Pega o proximo ponto
        for i in range(n): # Percorre todos os pontos de P
            if i == j:
                continue
            d = gt.direction(P[j], P[i], P[k]) # Calcula a curva
            if d > 0 or (d == 0 and gt.distance(P[i], P[j]) > gt.distance(P[k], P[j])): # Calcula a maior curva para esquerda
                k = i
        j = k
        if j == index:
            break
        hull.append(P[k])
    return hull
