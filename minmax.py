import math 

def minimax (curDepth, nodeIndex, 
             maxTurn, scores,  
             targetDepth): 

    
    if (curDepth == targetDepth):  
        return scores[nodeIndex] 

    if (maxTurn): 
        return max(minimax(curDepth + 1, nodeIndex * 2,  
                    False, scores, targetDepth),  
                   minimax(curDepth + 1, nodeIndex * 2 + 1,  
                    False, scores, targetDepth)) 

    else: 
        return min(minimax(curDepth + 1, nodeIndex * 2,  
                     True, scores, targetDepth),  
                   minimax(curDepth + 1, nodeIndex * 2 + 1,  
                     True, scores, targetDepth)) 

scores = [10,-3,-19,11,11,0,-2,-2,-2,14,-16,2,17,15,-14,15,-15,13,-19,-9,4,-9,2,9,-14,2,-18] 

treeDepth = math.log(len(scores), 3) 

print("The optimal value is : ", end = "") 
print(minimax(0, 0, True, scores, treeDepth))
