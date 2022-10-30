from functools import cmp_to_key
import red_black_tree as rbt
import geometry_tools as gt


def cmp_points(p1, p2):
    '''
    Compara qual ponto esta mais a esquerda
    se ambos tiverem coodernada x iguais
    compara o tipo de ponto que cada um é, se é final = 1
    ou inicial = 0, se os tipos forem iguais compara qual é o mais baixo
    '''
    if p1.x < p2.x:
        return -1
    elif p1.x > p2.x:
        return 1
    if p1.x == p2.x:
        if p1.p_type == p2.p_type:
            if p1.y < p2.y:
                return -1
            else:
                return 1
        else:
            if p1.p_type == 0:
                return -1
            else:
                return 1

def naive_alg(H1, H2):
    for i in H1:
        for j in H2:
            if gt.intersect(i, i.other_end, j, j.other_end):
                return True
    return False

def any_segments_intersect(H1, H2):
    '''
    Verifica se quaisquer dois segmentos de um conjunto
    se interseptam.
    '''
    T = rbt.RedBlackTree() # Inicializa a arvore rubro-negra
    S = H1 + H2
    sorted_segments = sorted(S, key=cmp_to_key(cmp_points)) # Ordena os pontos usando a funçao de comparação
    sorted_segments = map(lambda x: rbt.Node(x), sorted_segments) # Faz com que os pontos sejam nós de uma arvore
    
    for i in sorted_segments: # Percorre os segmentos ordenados
        if i.key.p_type == 0: # Se o ponto do segmento for inicial
            
            T.insert(i) # Insere o segmento na arvore
            x = T.search(i)
            pred = T.predecessor(x) # Pega o segmento q esta acima de i
            suc = T.successor(x) # Pega o segmento q esta abaixo de i
            
            # Verifica se existem os segmentos que estão acima de i ou abaixo de i e interceptam i
            
            if(pred and ((i.key not in H1 and pred.key not in H1) or (i.key not in H2 and pred.key not in H2))):
                if(pred and gt.intersect(i.key, i.key.other_end, pred.key, pred.key.other_end)):
                    return True
            
            if(suc and ((i.key not in H1 and suc.key not in H1) or (i.key not in H2 and suc.key not in H2))):
                if(suc and gt.intersect(i.key, i.key.other_end, suc.key, suc.key.other_end)):
                    return True
            
        
        if i.key.p_type == 1: # Se o ponto do segmento for final
            
            x = T.search(i)
            pred = T.predecessor(x) # Pega o segmento q esta acima de i
            suc = T.successor(x) # Pega o segmento q esta abaixo de i
            
            # Verifica se existem os segmentos que estão acima de i ou abaixo de i e se interceptam
            if pred and suc:
                if gt.intersect(pred.key, pred.key.other_end, suc.key, suc.key.other_end):
                    return True
            
            # Deleta o segmento i
            T.delete(i)
    
    return False

