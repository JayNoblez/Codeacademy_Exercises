#Write your function here
def remove_middle(lst, start, end):
  new_lst = lst[start:end+1]
  print(new_lst)
  for element in new_lst:
      lst.remove(element)
  return lst
  
  
#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
