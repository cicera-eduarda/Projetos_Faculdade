##COMANDO FOR ##

##medir o tamanho e retornar
#words = ['cat','window','defenestrate']
#for w in words:
#    print(w,len(w))
    
##Criando uma nova coleção
users = {'Cissa': 'active', 'Carla':'inactive','Ana':'active','Dani':'active','Julia':'inactive'}
print(users)

##Strategy: Iterate over a copy
#for user, status in users.copy().items():
 #   if status == 'inactive':
  #      del users[user]

print(users)
##Strategy: Create a new collection
active_users={}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

inactive_users={}
for user, status in users.items():
    if status == 'inactive':
        inactive_users[user] = status
        
print(inactive_users)