import os

import shutil
var2 = "Mexican"
def Rename(path:str):
    var = "D:/ProjectsPyCharm/HackaTons/DigEm_2_0/NewDataBase/"
    for i in os.listdir(path):
        f = os.path.join(path,i)
        if os.path.isfile(f) and i.endswith('.wav'):
            if(i[0]=='a'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_angry.wav")
                pass

            elif(i[0]=='d'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_disgust.wav")
                pass

            elif (i[0] == 'f'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_fear.wav")
                pass
            elif (i[0] == 'h'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_happy.wav")
                pass

            elif (i[0] == 'n'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_neutral.wav")
                pass

            elif(i[0:1]=="sa"):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_sad.wav")
                pass

            elif(i[0:1]=="su"):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_ps.wav")
                pass

        pass

def RenameM(path:str):
    var = "D:/ProjectsPyCharm/HackaTons/DigEm_2_0/NewDataBase/"
    for i in os.listdir(path):
        f = os.path.join(path, i)
        if os.path.isfile(f) and i.endswith('.wav'):
            if (i[0] == 'A'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_angry.wav")
                pass

            elif (i[0] == 'D'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_disgust.wav")
                pass

            elif (i[0] == 'F'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_fear.wav")
                pass
            elif (i[0] == 'H'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_happy.wav")
                pass

            elif (i[0] == 'N'):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_neutral.wav")
                pass

            elif (i[0:1] == "Sa"):
                shutil.copyfile(f, f"{var}{var2}{i[:i.find('.')]}_sad.wav")
                pass

        pass

var = "D:/ProjectsPyCharm/HackaTons/DigEm_2_0/NewDataBase/"
ptest = "D:/ProjectsPyCharm/HackaTons/DigEm_2_0/data/test-custom/"
ptrain = "D:/ProjectsPyCharm/HackaTons/DigEm_2_0/data/train-custom/"
qwerty = 0
for i in os.listdir(var):
    f = os.path.join(var, i)
    if os.path.isfile(f) and i.endswith('.wav'):
        if (qwerty == 9):
            qwerty=0
            shutil.copyfile(f, f"{ptest}{i}")
            os.remove(f)
        else:
            shutil.copyfile(f, f"{ptrain}{i}")
            os.remove(f)
            qwerty+=1

#RenameM(f"db/{var2}")
#Rename(f"db/{var2}")