class Animals:
    emp_count=0

    def __init__(self,name='NoName',klass='NoKlass',ves='NoVes'):
        self.name = name
        self.klass = klass
        self.ves = ves
        Animals.emp_count +=1
    def output(self):
        print("Имя: {}.|| Класс животного : {}.||Средний вес : {}кг.".format(self.name,self.klass,self.ves))



anim1=Animals (input(),input(),input())
anim2=Animals (input(),input(),input())
anim3=Animals (input(),input(),input())
anim4=Animals (input(),input(),input())

anim1.output()
anim2.output()
anim3.output()
anim4.output()
print('Всего животных:%d'% Animals.emp_count)
