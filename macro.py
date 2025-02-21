code = "\
	START 100 \
	MACRO\
	INCR &X,&Y,&REG=AREG\
	MOVER &REG,&X\
	ADD &REG,&Y\
	MOVEM &REG,&X\
	MEND\
	MACRO\
	DECR &A,&B,&REG=BREG\
	MOVER &REG,&A\
	SUB &REG,&B\
	MOVEM &REG,&A\
	MEND\
	READ N1\
	READ N2\
	INCR N1,N2,REG=CREG\
	DECR N1,N2\
	STOP\
	N1 DS 1\
	N2 DS 1\
	END"
	
split_code = code.split()
print(split_code)
j = "MACRO"

MDT = []
MNT = []
ALA = {}
mntc=0
for i in range(len(split_code)):
	if split_code[i] == j:
		l = i
		
		MNT.append(split_code[i+1])
		mntc+=1
		ALA[mntc]=split_code[i+2]
		while(split_code[l]!="MEND"):
			
			MDT.append(split_code[l+1])
			l=l+1

print("*********************************************************************")
print(MDT)

print("88888888888888888888888888888888888888888888888888888888888888888888")
print(MNT)
print("MNTC: ",mntc)

mdt = ""
for l in MDT:
	mdt = mdt+l+" "


print("*********************************************************************************************")

print(mdt)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

new_ala = []

for a in range(2):
	print(ALA[a+1].replace("&",",").split(","))
	new_ala.append(ALA[a+1].replace("&",",").split(","))

print(new_ala)

tmp1 = 0
tmp2=0
param=[" "," "]
for j in range(2):
	for r in range(len(split_code)):
		if(split_code[r]== MNT[j]):
			tmp1=tmp1+1
			if(tmp1>=2):
				param[j] = split_code[r+1]
		
				
print(param)		

# for k in range(len(split_code)):
# 	if((split_code[k]==MNT[0]) & param[0]!= split_code[k+1]):
# 		MDT[]
# 		for r in range(len(MDT)):
# 			if(MDT[r][1]=="&"):


# 			print(MDT[r])

		
for r in range(len(MDT)):
	if(MDT[r]==MNT[0]):
		MDT[r+1]=param[0]
			
	
	print(MDT[r])
