# -*- coding: utf-8 -*-
# @Time    : 2024/5/26 17:59
# @Author  : 霍格沃兹小学徒

'''
定义学生类 Student，学生信息包含：

编号: sid
姓名: name
年龄: age
性别: gender
'''

class Student(object):

    def __init__(self,sid,name,age,gender):
        self.sid=sid
        self.name=name
        self.age=age
        self.gender=gender
    # __str__函数定义之后，当打印输出对象时，会将 return 的信息打印出来，而不是打印对象的内存地址
    def __str__(self):
       return "学号:{},\n 姓名:{}\n 年龄:{}\n 性别:{}".format(self.sid, self.name, self.age, self.gender)

class StudentManement(object):

    def __init__(self):
        self.stu_info=[]

    def menu(self):
        print("*****************************")
        print("*      学生管理系统           *")
        print("* 1. 添加新学生信息           *")
        print("* 2. 通过学号修改学生信息      *")
        print("* 3. 通过学号删除学生信息      *")
        print("* 4. 通过姓名删除学生信息      *")
        print("* 5. 通过学号查询学生信息      *")
        print("* 6. 通过姓名查询学生信息      *")
        print("* 7. 显示所有学生信息         *")
        print("* 8. 退出系统                *")
        print("*****************************")
        menu_id=input(" 请输入您想操作的菜单编号：")
        return  menu_id
    # 获取编号方法 __getSid, 输入编号并返回（字符串类型）eg. s01
    def __getsid(self):
        sid=input(" 请输入学号(e.g. S01)：\n")
        return sid

    #获取姓名方法__getName, 输入姓名并返回（字符串类型）
    def __getName(self):
        name=input("请输入学员姓名：\n")
        return name
    #获取年龄方法__getAge, 输入年龄并返回（整型）
    def __getAge(self):
        while True:
            age=input("请输入学员年龄：\n")
            try:
                if 0<int(age)<=100:
                    return age
                else:
                    print("您输入的数字超出 100，请重新输入")
            except ValueError as e:
                print("您输入的年龄不是数字，请重新输入")
    #获取性别方法__getGender, 输入性别并返回（字符串类型）
    def __getGender(self):
        while True:
            gender=input("请输入学员性别, 请用 Male 和 Female 来表示学员性别\n:")
            if gender in ["Male" ,"Female",'male','female']:
                return gender
            else:
                print(" 您输入的信息不合法，请重新输入！")

    '''
    实现添加学生方法 addStudent
    方法参数为 编号，姓名，年龄，性别四个参数
    输出添加操作的结果提示信息
    返回对应结果信息
    要求编号不可重复。
    '''
    def addStudent(self,sid,name,age,gender):
        students=Student(sid,name,age,gender)
        for s in self.stu_info:
            if s.sid==sid:
                print("您输入的学号已存在，无法重复添加")
                return " 您输入的学号已存在，无法重复添加"
        else:
            self.stu_info.append(students)
            print("您输入的学员信息已经成功录入")
            return " 添加成功"
    '''
    实现通过编号修改学生信息方法 modifyStudentByID
    参数为 学号
    如果学生存在，则进行修改，不存在输出提示信息
    返回是否修改成功

    '''
    def modifyByID(self,sid,name,age,gender):

        for s in self.stu_info:
            if s.sid==sid:
                s.name=name
                s.age=age
                s.gender=gender
                print(" 您的信息已修改")
                return " 修改成功"
        else:
            print(" 您输入的学号不存在，无法修改该学员相关信息")
            return "修改失败"
    '''
    实现通过学号删除学生方法 deleteStudentByID
    参数为 学号
    如果学生存在，则进行删除并输出提示信息，不存在则仅输出提示
    返回是否删除成功
    '''
    def deleteByID(self,sid):
        for s in  self.stu_info:
            if s.sid==sid:
                self.stu_info.remove(s)
                print('学号为{}的学生信息已经被删除'.format(sid))
                return ('删除成功')
        else:
            print(" 您输出的学号不存在")
            return '删除失败'
        '''
        实现通过姓名删除学生方法 deleteStudentByName

        参数为 姓名
        如果学生存在，则进行删除（同名学生全部删除）并输出提示信息，不存在则仅输出提示
        返回是否删除成功
        '''
    def deleteByName(self,name):
        to_remove = []
        for s in  self.stu_info:
            if s.name==name:
                to_remove.append(s)
        print(to_remove)
        if to_remove:
            for s in to_remove:
                self.stu_info.remove(s)
            print('姓名为{}的学生信息已经被删除'.format(name))
            return ('删除成功')
        else:
            print(" 您输入的姓名不存在")
            return '删除失败'
    '''
    实现通过学号查询学生方法 queryStudentByID

    参数为 学号
    如果学生存在，则输出学生信息，不存在输出提示信息
    返回是否查询成功

    '''
    def queryByID(self,sid):
        for s in  self.stu_info:
            if s.sid==sid:
                print(" 您查询的学生信息为：\n{}".format(s))
                return "查询成功"
        else:
            print(" 您查询的学号不存在")
            return '查询失败'
    '''
    实现通过姓名查询学生方法 queryStudentByName

    参数为 姓名
    如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示信息
    返回是否查询成功
    '''
    def queryByName(self,name):
        to_query = []
        for s in self.stu_info:
            if s.name == name:
                to_query.append(s)
        if to_query:
            for s in to_query:
                print(' 您查询的学生信息为{}'.format(s))
            return ('查询成功')
        else:
            print(" 您输入的姓名不存在")
            return '查询失败'
    '''
    实现显示所有学生信息方法 __show

    输出所有学生信息
    '''
    def show(self):
        if len(self.stu_info)==0:
            print('您的学员系统中还没有学员，去添加一个吧')
        else:
            print("所有学生的信息如下：")
            for s in self.stu_info:
                print(s)
                print("----------------")


    def manager(self):
        while True:
            menu_id = self.menu()
            if len(menu_id)==1 and menu_id in '12345678':
                if menu_id=='1':
                    sid=self.__getsid()
                    name=self.__getName()
                    age=self.__getAge()
                    gender=self.__getGender()
                    self.addStudent(sid,name,age,gender)
                elif menu_id=='2':
                    sid = self.__getsid()
                    name = self.__getName()
                    age = self.__getAge()
                    gender = self.__getGender()
                    self.modifyByID(sid,name,age,gender)
                elif menu_id=='3':
                    sid=self.__getsid()
                    self.deleteByID(sid)
                elif menu_id=='4':
                    name=self.__getName()
                    self.deleteByName(name)
                elif menu_id=='5':
                    sid=self.__getsid()
                    self.queryByID(sid)
                elif menu_id=='6':
                    name=self.__getName()
                    self.queryByName(name)
                elif menu_id=='7':
                    self.show()
                else:
                    break
        else:
            print("您输入的菜单 id 有误，请重新输入")









if __name__ == '__main__':
   '''
    #student1=Student('03071627',"cindy",20,'female')
    stu1=StudentManement()
    stu1.addStudent('03071627',"cindy",20,'female')
    stu1.addStudent('03071628',"cindy",20,'female')
    stu1.addStudent('03071629',"tim",20,'female')
    stu1.addStudent('03071650',"jerry",20,'female')*/
    # stu1.modifyByID('03071628',"cindy",20,'female')
    #for s in stu1.stu_info:
        #print(s)
    #print('---------------------')
    #stu1.queryByID('03071640')
    #stu1.queryByName('json')
   
    stu1.deleteByName('cindy')
    for s in stu1.stu_info:
        print(s)
    stu1.show() '''

   stu1 = StudentManement()
   stu1.manager()


    #print(gender)



