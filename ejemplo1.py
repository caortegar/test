print('This is an example')
for n in range (9): 
  print(n)
  
    
class listfilter:
    def f(x):
        i = 0
        while i <= len(x)-1:
             if bool(x[i]) == True:
                print(x[i])
             i = i + 1

x = ['v', [], '3', 'a', []]

listfilter.f(x)
