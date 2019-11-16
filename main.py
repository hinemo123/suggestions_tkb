import pandas as pd 
import random


def find_course_id(id_s,df1):
	"""a=[]
	for i in df1["MÃ MH"]:
		if i== id_s:
			a.append(i)
	return a"""
	#return [i for i in df1["MÃ MH"] if i == id_s]
	return list(df1.index[df1["MÃ MH"]==id_s].tolist())
def get_id_class(id_course,df1):
	index=find_course_id(id_course,df1)
	if index is not None:
		array=[df1.at[i,"MÃ LỚP"] for i in index]
		return array
	else:
		return None
def get_name_teacher(id_course,df1,kind):
	index=find_course_id(id_course,df1)
	if kind==1:
		name="TÊN GIẢNG VIÊN"
	else:
		name="TÊN TRỢ GIẢNG"
	if index is not None:
		array=[df1.at[i,name] for i in index]
		return array
	else:
		return None

def get_lesson(id_course,df1):
	index=find_course_id(id_course,df1)
	if index is not None:
		array=[df1.at[i,"TIẾT"] for i in index]
		return array
	else:
		return None

def get_date(id_course,df1):
	index=find_course_id(id_course,df1)
	if index is not None:
		array=[df1.at[i,"THỨ"] for i in index]
		return array
	else:
		return None
def dic(id_course,df1,id_t):
	_class=get_id_class(id_course,df1)
	name_teacher=get_name_teacher(id_course,df1,id_t)
	lesson=get_lesson(id_course,df1)
	date=get_date(id_course,df1)
	dic={}
	for i in range(len(_class)):
		dic1={"Tên_gv" :name_teacher[i]}
		dic2={"tiết ":lesson[i]}
		dic3={"thứ ":date[i]}
		array=[dic1,dic3,dic2]
		dic[_class[i]]=array
	return dic

"""for i,j in dic("IT004").items():
	print(i,j)"""
def check_toan_tai_nang(array):
	for key,val in array.items():
		if "ANTN" not in key:
			return False
	return True
def pick_mon(array):
	choice=[]
	for a in array:
		if not a:
			continue
		else:
			i,j=random.choice(list(a.items()))
			if  len(a)==1 and "ANTN" in i:
				print(f"lớp {i} này chỉ mở cho tài năng")
				continue
			else:
				if check_toan_tai_nang(a):
					print(f"lớp {i} này chỉ mở cho tài năng")
					continue					
				else:
					while "ANTN" in i:
						i,j=random.choice(list(a.items()))
			choice.append({i:j})
	return choice




def check_trung(a,b):
	for i in a:
		if i in b:
			return True
	return False
def check_va_cham(choice):
	dic_time={"thứ 2":False,
			   "thứ 3":False,
			   "thứ 4":False,
			   "thứ 5":False,
			   "thứ 6":False,
			   "thứ 7":False}
	for c in choice:
		for i,j in c.items():
			for a,b in j[1].items():
				if dic_time[a+b]==False:
					dic_time[a+b]=j[2]["tiết "]
				else:	
					#dic_time[a+b]=j[2]["tiết "]	
					if check_trung(j[2]["tiết "],dic_time[a+b]):
						return False
					else:
						dic_time[a+b]+=j[2]["tiết "]
	return True



def main(a):
	df2=pd.read_excel('tkb.xlsx',encoding ="cp1258",sheet_name ="TKB TH")
	df1=pd.read_excel('tkb.xlsx',encoding ="cp1258",sheet_name ="TKB LT")

	
	#a=["MA005","SS004","IT007","ENG03"]
	list_sub=[]
	for i in a:
		tada=dic(i,df1,1)
		tudu=dic(i,df2,2)
		if not tada:
			print(f"không thấy môn {i}")
			continue
		else:
			list_sub.append(tada)
		if not tudu:
			print(f"không thấy môn {i} thực hành")
			continue
		else:
			list_sub.append(tudu)
	#print(list_sub)
	pick=pick_mon(list_sub)
	print(pick)
	if check_va_cham(pick)==True:
		for a in pick:
			for key,val in a.items():
				print(key,end=" ")
				print(val[1],val[2])
	else:
		print("list này không được")



if __name__ == '__main__':
	a=int(input("nhập số to vào để xác xuất tìm được list phù hợp cao,tầm 100 thôi nhé không đơ máy đó <3:"))
	b=input("nhập danh sách môn muốn học:").split()
	for i in range(a):
		main(b)
		print("_______________________________________")