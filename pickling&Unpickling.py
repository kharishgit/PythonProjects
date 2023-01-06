import pickle
lst = ['A',1,'SO','Hai How are you']
nfile = open("newfile","wb")
pickle.dump(lst,nfile)

nfile.close()