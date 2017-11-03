import csv
import codecs
import xlrd #excel表格使用
import openpyxl

#功能：新建一个csv文件，并写入列名，
#传入参数：文件名，包含文件列名的列表
#返回值：无
def newcsvfile(filename,fieldnames):
    with open(filename,'w',newline='') as csvfile:
        writer = csv.writer(csvfile,fieldnames)
        writer.writerow(fieldnames)
    return


#功能：#读取csv文件用户名和密码到字典中，需指定列名,返回字典
#传入参数：文件名，包含文件列名的列表
#返回值：包含用户名和密码的字典

def dictreadcsvdata(filename,rownames):
    
    with open(filename,'r',encoding='gbk') as csvfile:
        reader = csv.DictReader(csvfile)
        names={}
        for row in reader:
            #print(row['first_name'], row['last_name'])
            names[row[rownames[0]]] = row[rownames[1]]

    return names

#功能：读取csv文件,将文件每一行内容作为列表，添加为列表的一项，并返回总列表
#传入参数：文件名,指定要读取列的列名，是否要忽略文件首行
#返回值：包含每一行内容列表的列表
def readcsvdata(filename,rowname='null',ignorefirst=False):
    
    with open(filename,'r',encoding='gbk') as csvfile:
        reader = csv.reader(csvfile)
        print(reader)
        datas=[line for line in reader]
        #如果列名不为空，则表示要读取指定列的值
        if rowname != 'null':
            index = datas[0].index(rowname)
            datas=[datas[i][index] for i in range(len(datas))]
        #for line in reader:
        #   datas.append(list(line))
        #如果要忽略首行标题栏，则删除列表第一个元素
        if ignorefirst == True:
            del datas[0]

    return datas




#功能：写文件到csv文件中
#传入参数：文件名，包含文件列名的列表，要写入的数据列表
#返回值：无
def writecsvdata(filename,fieldnames,datas=[("first","testdata")]):
    with open(filename, 'a+',newline='') as csvfile:
        #fieldnames = list(datas.keys())#['first_name', 'last_name']
        #writer = csv.DictWriter(csvfile, fieldnames)
        writer = csv.writer(csvfile, fieldnames)
        #print(fieldnames)
        #writer.writerow(fieldnames)
        writer.writerows(datas)

    return

#功能：从txt文件中读取用户名和密码
#传入参数：文件名，该文件每一行包括两列，第一列为用户名，第二列为用户密码，用英文逗号分隔
#返回值：无
def readtxtdata(filename,rowname='null',ignorefirst=False):
    with open(filename,'r',encoding="gb18030") as fp:
    #fp=codecs.open(filenames,'r',"gb18030")#添加"gb18030"是为了中文字符能正常显示

        datas = []#新建一个空的列表
        lines=fp.readlines()

        for data in lines:
            #将每行中的中文分隔符替换为英文分隔符
            data = data.replace('，',',')
            value=data.split(',')#将一行的元素分隔组成列表
            #去掉列表元素两头的空格符号换行符等
            value = [value[i].strip(' \t\r\n') for i in range(len(value))]
            #将每行元素列表添加到总列表中
            datas.append(value)
        #如果列名不为空，则表示要读取指定列的值
        if rowname != 'null':
            index = datas[0].index(rowname)
           
            datas=[datas[i][index] for i in range(len(datas))]

        #如果要忽略首行标题栏，则删除列表第一个元素
        if ignorefirst == True:
            del datas[0]

    return datas #返回字典
