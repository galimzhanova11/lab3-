def my_function(legs,heads):
 ans='cant solve'
 for i in range (heads +1):
  j=heads-i
  if 2*i+4*j==legs:
    return i,j
 return ans,ans


legs=94     
heads=35
answer=my_function(legs,heads)
print (answer)
