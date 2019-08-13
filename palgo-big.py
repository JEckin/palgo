import os

var1=[]
var2=[]
var3=[]
var4=[]
def pasadd (add) :
#        print(add)
        temp="echo " +  add + " >> palgo-big.txt"
        os.system(temp)

def main() :
	os.system("clear")

	print "---------------------------------------------------------------------------------------"
	print "          __________        .__                  "
	print "          \\______   \\_____  |  |    ____   ____ "
	print "           |     ___/\\__  \\ |  |   / ___\\ /  _ \\ "
	print "           |    |     / __ \\|  |__/ /_/  >  <_> )"
	print "           |____|    (____  /____/\\___  / \\____/"
	print "                          \\/     /_____/        "
	print "                                                   By JEckin"
	print "---------------------------------------------------------------------------------------"
	print "Write some informations about the target person like his/her names, family names,  "
	print "initials, significant dates, numbers, pets, birthdays, hometown, school name or mascot"
	print "---------------------------------------------------------------------------------------"


	x="false"
	while x != "true":
	        temp = raw_input("Variable: ")
	       	if temp == "":
        	       	x="true"
		if x != "true":
			var1.append(temp)
	var1.append("!")
	var1.append("?")
	var1.append("@")
	var2 = var1
	var3 = var1
	var4 = var1
	print"Variablen:        ",var2

def func() :
	print("Just Wait...")
	try:
		os.remove("palgo-big.txt")
		os.system("touch palgo-big.txt")
	except OSError:
		pass


	for a in xrange(len(var1)) :
        	#1
        	pasadd(var1[a])
        	for b in xrange(len(var2)):

                	temp = var1[a] + var2[b]
                	#12z
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
	end()
def end() :
	os.system("clear")
	print "-------------------------------------------------------------------------"
	print "                           finished > palgo-big.txt"
	print "-------------------------------------------------------------------------"
	os.system("ls -lh palgo-big.txt")
try:
	main()
	var2 = var1
	var3 = var1
	var4 = var1
	func()
except KeyboardInterrupt:
	os.system("clear")
	end()
