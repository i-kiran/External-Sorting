import random
import string
import math
import os
def random_string(string_length = 3):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for x in range(string_length))

def generate_dataset(lis,n):
	TID_list = random.sample(range(50000 , 200001),n)
	for i in range(n):
		single_rec = []
		single_rec.append(TID_list[i])
		single_rec.append(random_string())
		single_rec.append(random.randint(0,60000)+1)
		single_rec.append(random.randint(0,1500)+1)
		lis.append(single_rec)
	return lis

def write_to_file(lis):
	with open('dataset.txt','w') as f:
		for record in lis:
			f.writelines(str(record))
			f.write("\n")

def generate_data(lis_size):
	lis = generate_dataset([] , lis_size)
	write_to_file(lis)

def simulate_sec_memory(file_name , alpha):
	with open(file_name , 'r') as fin :
		fin.seek(0)
		i = j = 1
		for line in fin:
			line_new = line[1:].rstrip(']\n').split(', ')
			line_new = [int(line_new[i]) if i!=1 else line_new[i].strip("\'") for i in range(len(line_new))]
			with open(str(j)+'.txt','a+') as fout:
				fout.write(str(line_new))
				fout.write("\n")
			if i!=alpha:
				i+=1
			else:
				i=1
				j=j+1

def case1():
	for r in range(no_runs):
		with open(str(r+1)+'.txt' , 'r') as fd:
			sorted_list=[]
			sorted_list_new=[]
			for line in fd:
				x = line[1:].rstrip(']\n').split(', ')
				sorted_list.append(x[2])
			for x in sorted_list:
				z = int(x)
				sorted_list_new.append(z)
			sorted_list_new.sort()
#			print(sorted_list_new)
		
			for i in sorted_list_new:
				with open(str(r+1)+'.txt' , 'r') as fd:
					for line in fd:
						x = line[1:].rstrip(']\n').split(', ')
						if(i == int(x[2])):
#							print("i=",i,"x=",x[2])
							with open(str(r+1)+'a.txt' , 'a') as fp:
								lin = line
								fp.write(str(lin))
	list = []							
	for r in range(no_runs):
		with open(str(r+1)+'a.txt' , 'r') as fp:
			for line in fp:
				z = line[1:].rstrip(']\n').split(', ')
				z[2]
				list.append(int(z[2]))
	
				with open('middle_s.txt' , 'a') as ap:
					ap.write(str(line))
					
	list.sort()
	set(list)
#	print(list)
	for item in list:
		with open('middle_s.txt' , 'r') as f:
			for line in f:
				z = line[1:].rstrip(']\n').split(', ')
				if(int(z[2])==item):
					with open('final.txt','a') as fd:
						fd.write(str(line))
						fd.write("\n")

def case2(M,no_runs):
	'''creates disk blocks list form'''
	for r in range(no_runs):
		with open(str(r+1)+'.txt' , 'r') as fd:
			sorted_list=[]
			sorted_list_new=[]
			for line in fd:
				x = line[1:].rstrip(']\n').split(', ')
				sorted_list.append(x[2])
			for x in sorted_list:
				z = int(x)
				sorted_list_new.append(z)
			sorted_list_new.sort()
			print(sorted_list_new)
		'''creates sorted runs'''	
		for i in sorted_list_new:
			with open(str(r+1)+'.txt' , 'r') as fd:
				for line in fd:
					x = line[1:].rstrip(']\n').split(', ')
					if(i == int(x[2])):
						#print("i=",i,"x=",x[2])
						with open(str(r+1)+'a.txt' , 'a') as fp:
							lin = line
							fp.write(str(lin))
	c=1
	nxt = r+2
	print('nxtfile',nxt)	
	while(no_runs>=1):
		list1_new=[]
		list1=[]
		for i in range(M-1):
			print("i :",i)
			#list1=[]
			with open(str(c)+'a.txt','r') as f:
				print("current file:",c)
				for line in f:
					x = line[1:].rstrip(']\n').split(', ')
					with open("mm.txt" , 'a') as fm:
						fm.write(line)
						list1.append(x[2])
			c+=1
			#print("unsorterd:",list1)
		for item in list1:
			z = int(item)
			list1_new.append(z)
		list1_new.sort()
		set(list1_new)
		print(list1_new)

		with open(str(nxt)+'a.txt' , 'a')as f:
			print("created New")
			for item in list1_new:
				with open("mm.txt",'r') as fm:
					for line in fm:
						x = line[1:].rstrip(']\n').split(', ')
						z=int(x[2])
						if(z==item):
							f.write(line)
		nxt+=1
		no_runs = no_runs/2
		os.remove("mm.txt")
	


l = int(input("\nEnter no. of records for dataset:"))
generate_data(l)
print("!!!DATA GENERATED!!!")
b_size = int(input("\nEnter a block size:"))
simulate_sec_memory('dataset.txt',b_size)
print("!!!SECONDARY MEMORY SIMULATED!!!")
M = int(input("\nEnter no. of disk blocks in Main Memory:"))
print(M)
no_runs = math.ceil(l / b_size)
print("no. of runs : ",no_runs)
if(M > no_runs):
	case1()
elif(M <= no_runs):
	case2(M , no_runs)
