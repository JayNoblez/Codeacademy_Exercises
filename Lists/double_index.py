def double_index(lst, index):
  new_lst = []
  if index < len(lst) - 1:
    value = lst[index] * 2
    for element in lst:
      if element != lst[index]:
        new_lst.append(element)
      else: new_lst.append(value)
    return new_lst
  else: return new_lst
            
 
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
