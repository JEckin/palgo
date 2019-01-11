import time
import os


def pasadd (add) :
        print(add)
        temp="echo " +  add + " >> palgo.txt"
        #print(temp)
        os.system(temp)


os.system("clear")

print "---------------------------------------------------------------------------------------"
print "          __________        .__                  "
print "          \\______   \\_____  |  |    ____   ____ " 
print "           |     ___/\\__  \\ |  |   / ___\\ /  _ \\ " 
print "           |    |     / __ \\|  |__/ /_/  >  <_> )"
print "           |____|    (____  /____/\\___  / \\____/" 
print "                          \\/     /_____/        " 
print "                                                   By BreaBrain"
print "---------------------------------------------------------------------------------------"
print "Write some informations about the target person like his/her names, family names,  "
print "initials, significant dates, numbers, pets, birthdays, hometown, school name or mascot"
print "---------------------------------------------------------------------------------------"





x="false"
var1 = []
while x != "true":
        temp = raw_input("Names: ")
        if temp == "":
                x="true"
        #print(temp)
        var1.append(temp)
if x == "true":
        var1.remove("")
#print(var1)

x="false"
var2 = []
while x != "true":
        temp = raw_input("Numbers: ")
        if temp == "":
                x="true"
        #print(temp)
        var2.append(temp)
if x == "true":
        var2.remove("")
#print(var2)

x="false"
var3 = []
while x != "true":
        temp = raw_input("others: ")
        if temp == "":
                x="true"
        var3.append(temp)
if x == "true":
        var3.remove("")

var4 = ["!","?","@"]

print"Variable1:        ",var1
print"Variable2:        ",var2
print"Variable3:        ",var3
print"Sonderzeichen:    ",var4

os.system("rm password.txt")
os.system("touch password.txt")


for a in xrange(len(var1)) :
        #1
        pasadd(var1[a])
        for b in xrange(len(var2)):

                temp = var1[a] + var2[b]
                #12
                pasadd(temp)
                for c in xrange(len(var3)):
                        temp = var1[a] + var2[b] + var3[c]
                        #123
                        pasadd(temp)
                        for d in xrange(len(var4)):
                                temp = var1[a] + var2[b] + var3[c] + var4[d]
                                #1234
                                pasadd(temp)
                for c in xrange(len(var4)):
                        temp = var1[a] + var2[b] + var4[c]
                        #124
                        pasadd(temp)
                        for d in xrange(len(var3)):
                                temp = var1[a] + var2[b] + var4[c] + var3[d]
                                #1243
                                pasadd(temp)
        for b in xrange(len(var3)):

                temp = var1[a] + var3[b]
                #13
                pasadd(temp)
                for c in xrange(len(var2)):
                        temp = var1[a] + var3[b] + var2[c]
                        #132
                        pasadd(temp)
                        for d in xrange(len(var4)):
                                temp = var1[a] + var3[b] + var2[c] + var4[d]
                                #1324
                                pasadd(temp)
                for c in xrange(len(var4)):
                        temp = var1[a] + var3[b] + var4[c]
                        #134
                        pasadd(temp)
                        for d in xrange(len(var2)):
                                temp = var1[a] + var3[b] + var4[c] + var2[d]
                                #1342
                                pasadd(temp)
        for b in xrange(len(var4)):
                temp = var1[a] + var4[b]
                #14
                pasadd(temp)
                for c in xrange(len(var2)):
                        temp = var1[a] + var4[b] + var2[c]
                        #142
                        pasadd(temp)
                        for d in xrange(len(var3)):
                                temp = var1[a] + var4[b] + var2[c] + var3[d]
                                #1423
                                pasadd(temp)
                for c in xrange(len(var3)):
                        temp = var1[a] + var4[b] + var3[c]
                        #143
                        pasadd(temp)
                        for d in xrange(len(var2)):
                                temp = var1[a] + var4[b] + var3[c] + var2[d]
                                #1432
                                pasadd(temp)


for a in xrange(len(var2)) :
        #2
        pasadd(var2[a])
        for b in xrange(len(var1)):

                temp = var2[a] + var1[b]
                #21
                pasadd(temp)
                for c in xrange(len(var3)):
                        temp = var2[a] + var1[b] + var3[c]
                        #213
                        pasadd(temp)
                        for d in xrange(len(var4)):
                                temp = var2[a] + var1[b] + var3[c] + var4[d]
                                #2134
                                pasadd(temp)
                for c in xrange(len(var4)):
                        temp = var2[a] + var1[b] + var4[c]
                        #214
                        pasadd(temp)
                        for d in xrange(len(var3)):
                                temp = var2[a] + var1[b] + var4[c] + var3[d]
                                #2143
                                pasadd(temp)
        for b in xrange(len(var3)):

                temp = var2[a] + var3[b]
                #23
                pasadd(temp)
                for c in xrange(len(var1)):
                        temp = var2[a] + var3[b] + var1[c]
                        #231
                        pasadd(temp)
                        for d in xrange(len(var4)):
                                temp = var2[a] + var3[b] + var1[c] + var4[d]
                                #2314
                                pasadd(temp)
                for c in xrange(len(var4)):
                        temp = var2[a] + var3[b] + var4[c]
                        #234
                        pasadd(temp)
                        for d in xrange(len(var1)):
                                temp = var2[a] + var3[b] + var4[c] + var1[d]
                                #2341
                                pasadd(temp)
        for b in xrange(len(var4)):
                temp = var2[a] + var4[b]
                #24
                pasadd(temp)
                for c in xrange(len(var1)):
                        temp = var2[a] + var4[b] + var1[c]
                        #241
                        pasadd(temp)
                        for d in xrange(len(var3)):
                                temp = var2[a] + var4[b] + var1[c] + var3[d]
                                #2413
                                pasadd(temp)
                for c in xrange(len(var3)):
                        temp = var2[a] + var4[b] + var3[c]
                        #243
                        pasadd(temp)
                        for d in xrange(len(var1)):
                                temp = var2[a] + var4[b] + var3[c] + var1[d]
                                #2431
                                pasadd(temp)



for a in xrange(len(var3)) :
        #3
        pasadd(var3[a])
        for b in xrange(len(var1)):

                temp = var3[a] + var1[b]
                #31
                pasadd(temp)
                for c in xrange(len(var2)):
                        temp = var3[a] + var1[b] + var2[c]
                        #312
                        pasadd(temp)
                        for d in xrange(len(var4)):
                                temp = var3[a] + var1[b] + var2[c] + var4[d]
                                #3124
                                pasadd(temp)
                for c in xrange(len(var4)):
                        temp = var3[a] + var1[b] + var4[c]
                        #314
                        pasadd(temp)
                        for d in xrange(len(var2)):
                                temp = var3[a] + var1[b] + var4[c] + var2[d]
                                #3142
                                pasadd(temp)
        for b in xrange(len(var2)):

                temp = var3[a] + var2[b]
                #32
                pasadd(temp)
                for c in xrange(len(var1)):
                        temp = var3[a] + var2[b] + var1[c]
                        #321
                        pasadd(temp)
                        for d in xrange(len(var4)):
                                temp = var3[a] + var2[b] + var1[c] + var4[d]
                                #3214
                                pasadd(temp)
                for c in xrange(len(var4)):
                        temp = var3[a] + var2[b] + var4[c]
                        #324
                        pasadd(temp)
                        for d in xrange(len(var1)):
                                temp = var3[a] + var2[b] + var4[c] + var1[d]
                                #3241
                                pasadd(temp)
        for b in xrange(len(var4)):
                temp = var3[a] + var4[b]
                #34
                pasadd(temp)
                for c in xrange(len(var1)):
                        temp = var3[a] + var4[b] + var1[c]
                        #341
                        pasadd(temp)
                        for d in xrange(len(var2)):
                                temp = var3[a] + var4[b] + var1[c] + var2[d]
                                #3412
                                pasadd(temp)
                for c in xrange(len(var2)):
                        temp = var3[a] + var4[b] + var2[c]
                        #342
                        pasadd(temp)
                        for d in xrange(len(var1)):
                                temp = var3[a] + var4[b] + var2[c] + var1[d]
                                #3421
                                pasadd(temp)



for a in xrange(len(var4)) :
        #4
        pasadd(var4[a])
        for b in xrange(len(var1)):

                temp = var4[a] + var1[b]
                #41
                pasadd(temp)
                for c in xrange(len(var2)):
                        temp = var4[a] + var1[b] + var2[c]
                        #412
                        pasadd(temp)
                        for d in xrange(len(var3)):
                                temp = var4[a] + var1[b] + var2[c] + var3[d]
                                #4123
                                pasadd(temp)
                for c in xrange(len(var3)):
                        temp = var4[a] + var1[b] + var3[c]
                        #413
                        pasadd(temp)
                        for d in xrange(len(var2)):
                                temp = var4[a] + var1[b] + var3[c] + var2[d]
                                #4132
                                pasadd(temp)
        for b in xrange(len(var2)):

                temp = var4[a] + var2[b]
                #42
                pasadd(temp)
                for c in xrange(len(var1)):
                        temp = var4[a] + var2[b] + var1[c]
                        #421
                        pasadd(temp)
                        for d in xrange(len(var3)):
                                temp = var4[a] + var2[b] + var1[c] + var3[d]
                                #4213
                                pasadd(temp)
                for c in xrange(len(var3)):
                        temp = var4[a] + var2[b] + var3[c]
                        #423
                        pasadd(temp)
                        for d in xrange(len(var1)):
                                temp = var4[a] + var2[b] + var3[c] + var1[d]
                                #4231
                                pasadd(temp)
        for b in xrange(len(var3)):
                temp = var4[a] + var3[b]
                #43
                pasadd(temp)
                for c in xrange(len(var1)):
                        temp = var4[a] + var3[b] + var1[c]
                        #431
                        pasadd(temp)
                        for d in xrange(len(var2)):
                                temp = var4[a] + var3[b] + var1[c] + var2[d]
                                #4312
                                pasadd(temp)
                for c in xrange(len(var2)):
                        temp = var4[a] + var3[b] + var2[c]
                        #432
                        pasadd(temp)
                        for d in xrange(len(var1)):
                                temp = var4[a] + var3[b] + var2[c] + var1[d]
                                #4321
                                pasadd(temp)
os.system("clear")
print "-------------------------------------------------------------------------"
print "                           finished > palgo.txt"
print "-------------------------------------------------------------------------"
os.system("ls -l")

