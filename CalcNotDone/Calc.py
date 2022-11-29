from ast import Lambda
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget): ##inherites mn qtwidget 
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator') ##for window title
        self.setLayout(qtw.QVBoxLayout()) ##for vertical layout
        self.keypad()
        self.temp_nums=[]
        self.fin_nums=[]

        self.show()  ## display all elements of the object
    def keypad(self): 
        container=qtw.QWidget() ## holds all other elemnts
        container.setLayout(qtw.QGridLayout()) ##grid layout
        #Buttons
        result_field=qtw.QLineEdit()
        btn_result=qtw.QPushButton('Enter',clicked=self.func_result)
        btn_clear=qtw.QPushButton('Clear',clicked=self.clear_calc)
        btn_9=qtw.QPushButton('9', clicked = Lambda:self.num_press('9'))
        btn_8=qtw.QPushButton('8',clicked=Lambda:self.num_press('8'))
        btn_7=qtw.QPushButton('7',clicked=Lambda:self.num_press('7'))
        btn_6=qtw.QPushButton('6',clicked=Lambda:self.num_press('6'))
        btn_5=qtw.QPushButton('5',clicked=Lambda:self.num_press('5'))
        btn_4=qtw.QPushButton('4',clicked=Lambda:self.num_press('4'))
        btn_3=qtw.QPushButton('3',clicked=Lambda:self.num_press('3'))
        btn_2= qtw.QPushButton('2',clicked=Lambda:self.num_press('2'))
        btn_1=qtw.QPushButton('1',clicked=Lambda:self.num_press('1'))
        btn_0=qtw.QPushButton('0',clicked=Lambda:self.num_press('0'))
        btn_plus = qtw.QPushButton('+',clicked=Lambda:self.func_press('+'))
        btn_minus = qtw.QPushButton('-',clicked=Lambda:self.func_press('-'))
        btn_multi=qtw.QPushButton('*',clicked=Lambda:self.func_press('*'))
        btn_div=qtw.QPushButton('/',clicked=Lambda:self.func_press('/'))

        #add buttons to layout
        container.layout().addWidget(result_field,0,0,1,4)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2,1,2)
        container.layout().addWidget(btn_9,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_7,2,2)
        container.layout().addWidget(btn_plus,2,3)
        container.layout().addWidget(btn_6,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_4,3,2)
        container.layout().addWidget(btn_minus,3,3)
        container.layout().addWidget(btn_3,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_1,4,2)
        container.layout().addWidget(btn_multi,4,3)
        container.layout().addWidget(btn_0,5,0,1,3)
        container.layout().addWidget(btn_div,5,3)
        self.layout().addWidget(container)

    def num_press(self,key_number):
        self.temp_nums.append(key_number)
        temp_string=''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums)+temp_string)
        else:
            self.result_field.setText(temp_string)
    def func_press(self,operator):
        temp_string=''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.temp_nums=[]
        self.result_field.setText(''.join(self.fin_nums))
    def func_result(self):
        fin_string=''.join(self.fin_nums)+ ''.join(self.temp_nums)
        result_string=eval(fin_string)
        fin_string+='='
        fin_string +=str(result_string)
        self.result_field.setText(fin_string)
    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums=[]
        self.fin_nums=[]
app=qtw.QApplication([]) ## creates the app
mw=MainWindow() ## object to maintain app
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_() ##run the app
