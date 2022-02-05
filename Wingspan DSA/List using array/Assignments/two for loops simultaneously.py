#lex_auth_0127426166978887681375

def merge_list(list1, list2):
    merged_data=""
    for i,j in zip(range(0, len(list1)), reversed(range(0, len(list2)))):
      if list1[i] == None:
        one_word = list2[j] + " "
        merged_data += one_word
      elif list2[j] == None:
        one_word = list1[i] + " "
        merged_data += one_word
      else:
        ele = "".join([list1[i], list2[j]])
        one_word = ele + " "
        merged_data += one_word
      
    
    return merged_data

#Provide different values for the variables and test your program
list1=['T', 'sk', None, 'bl']
list2=['ue', 'is', 'y', 'he']
merged_data=merge_list(list1,list2)
print(merged_data)