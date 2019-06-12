v=['a','e','i','o','u']
E=['a','b','c','d','e','f','g','h','i','j','k','l','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z']
c=input()
if c in E:
  if c in v:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")      
