print('Hello world!')# создаем класс с водда имени 
class Four: #имя класса
    def __init__(self,fild_one,fild_two): #метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two #передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("калорийность 100г продукта-",self.fild_one) #выводим значения атрибутов
        print("вес продукта в граммах-",self.fild_two) #выводим значения атрибутов
    #методы для обработки
    def result(self):
        print("общая каллорийность продукта-",self.fild_one*self.fild_two/100)
# Класс потомок
class FourTwo(Four):
    def __init__(self,fild_one,fild_two,quantity):
        super().__init__(fild_one,fild_two)
        self._quantity = quantity
        self._fild_one = fild_one
        self._fild_two = fild_two
    @property
    def quantityy(self):
        return f"количества витамина с в продукте-{self._fild_two*self._quantity}"
result = FourTwo(200,5,1)
print(result.quantityy)
# создание класса начинается с ввода ИМЕНИ

class Five(): # - Имя класса
    def __init__(self, left_border_of_range,right_border_of_range): # метод инициализации - при создании экземпляра КЛАССА в скобке указываются значения параметров
        self.left_border = left_border_of_range # передаём значения параметров из скобки атрибутам КЛАССА
        self.right_border = right_border_of_range # передаём значения параметров из скобки атрибутам КЛАССА

    # методы - функции (действия) над атрибутами и другими методами
    # геттер - метод вывода значения атрибута (свойства, поля) или результата выполнения другого метода - 
    # у геттера нет пораметров только в скобках ссылка self
     
    def get_left_border(self):
        print("Левая граница диапазона равна ", self.left_border)
    def get_right_border(self):
        # передать результать метода
        return f"Правая граница диапазона равна {self.right_border}"
    # методы для обработки - вычислить квадрат длины длины диапазона
    def squre_lenght_range(self):
        return f"Kвадрат длины длины диапазона = {(self.right_border - self.left_border) ** 2}"
        
    
# Класс потомок
class FiveTwo(Five):
    def __init__(self, left_border_of_range,right_border_of_range,number):
        super().__init__(left_border_of_range,right_border_of_range)
        self._number = number
    @property
    def examination_number_of_range(self):
        if self._number >= self.left_border and self._number <= self.right_border:
            return 'Входит'
        else:
            return 'Не входит'
        
result = FiveTwo(4,12,12)
print(result.examination_number_of_range)

# создаем класс с водда имени 
class Six: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two #передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("количество секунд-",self.fild_one)#выводим значения атрибутов
        print("количество минут-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("общее количество секунд-",self.fild_one+60*self.fild_two)
# Класс потомок
class SixTwo(Six):
    def __init__(self,fild_one,fild_two,speed):
        super().__init__(fild_one,fild_two)
        self._speed = speed
        self._fild_one = fild_one
        self._fild_two = fild_two
    @property
    def distance(self):
        return f"расстояние пройденное объектом-{self._speed*self._fild_one}"
result = SixTwo(60,5,5)
print(result.distance)

# создаем класс с водда имени 
class Seven: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two #передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("количество часов-",self.fild_one)#выводим значения атрибутов
        print("количество минут-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("общее количество минут-",self.fild_one*60+self.fild_two)
# Класс потомок
class SevenTwo(Seven):
    def __init__(self,fild_one,fild_two,minute):
        super().__init__(fild_one,fild_two)
        self._minute = minute
        self._fild_one = fild_one
        self._fild_two = fild_two
    @property
    def quantityy(self):
        return f"сколько операций можно выполнить за указанное время-{self._fild_one/self._minute}"
result = SevenTwo(20,15,5)
print(result.quantityy)

# создаем класс с водда имени 
class Eight: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two #передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("первый катет-",self.fild_one)#выводим значения атрибутов
        print("второй катет-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("площадь прямоугольного треугольника-",self.fild_one*self.fild_two/2)
# Класс потомок
class EightTwo(Eight):
    def __init__(self,fild_one,fild_two,hight):
        super().__init__(fild_one,fild_two)
        self._hight = hight
        self._fild_one = fild_one
        self._fild_two = fild_two
    @property
    def volume(self):
        return f"объем призмы-{self._fild_two*self._hight}"
result = EightTwo(7,5,4)
print(result.volume)

# создаем класс с водда имени 
class Nine: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two #передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("скорость движения-",self.fild_one)#выводим значения атрибутов
        print("время движения-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("пройденное расстояние-",self.fild_one*self.fild_two)
# Класс потомок
class NineTwo(Nine):
    def __init__(self,fild_one,fild_two,sila):
        super().__init__(fild_one,fild_two)
        self._sila = sila
        self._fild_one = fild_one
        self._fild_two = fild_two
    @property
    def quantityy(self):
        return f"количество работы-{self._fild_one*self._sila}"
result = NineTwo(200,5,3)
print(result.quantityy)

# создаем класс с водда имени 
class Ten: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two #передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("первый катет-",self.fild_one)#выводим значения атрибутов
        print("второй катет-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("длинна гипотенузы-",self.fild_one**2+self.fild_two**2)
# Класс потомок
class TenTwo(Ten):
    def __init__(self,fild_one,fild_two,hight):
        super().__init__(fild_one,fild_two)
        self._hight = hight
        self._fild_one = fild_one
        self._fild_two = fild_two
    @property
    def ploshad(self):
        return f"площадь трапеции-{(self._fild_one+self._fild_two)/2*self._hight}"
result = TenTwo(2,5,5)
print(result.ploshad)

# создаем класс с водда имени 
class Eleven: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("нижнее основание трапеции-",self.fild_one)#выводим значения атрибутов
        print("верхнее основание трапеции-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("полу-сумма оснований трапеции-",(self.fild_one+self.fild_two)/2)
# Класс потомок
class ElevenTwo(Eleven):
    def __init__(self,fild_one,fild_two,hight):
        super().__init__(fild_one,fild_two)
        self._hight = hight
        self._fild_one = fild_one
        self._fild_two = fild_two
    @property
    def ploshad(self):
        return f"площадь трапеции-{(self._fild_one+self._fild_two)/2*self._hight}"
result = ElevenTwo(3,5,7)
print(result.ploshad)

# создаем класс с водда имени 
class Twelve: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("первый катет-",self.fild_one)#выводим значения атрибутов
        print("второй катет-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("тангенс угла а-",self.fild_two/self.fild_one)
# Класс потомок
class TwelveTwo(Twelve):
    #метод инициализации
    def __init__(self,fild_one,fild_two,corner):
        #супер возвращает объект посредник
        super().__init__(fild_one,fild_two)
        self._corner = corner
        self._fild_one = fild_one
        self._fild_two = fild_two
        #добавляем метод защищенных элементов (декоратор) проперти
    @property
    def difference(self):
        #так как метод проперти возвращаемый мы используем ретерн
        return f"разность угла b и a-{self._corner-(self.fild_two/self.fild_one)}"
result = TwelveTwo(3,5,5)
print(result.difference)

# создаем класс с водда имени 
class Thirteen: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("вещественное число-",self.fild_one)#выводим значения атрибутов
        print("вещественное число-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("полу разность чисел-",(self.fild_one-self.fild_two)/2)
# Класс потомок
class ThirteenTwo(Thirteen):
    #метод инициализации
    def __init__(self,fild_one,fild_two,number):
        #супер возвращает объект посредник
        super().__init__(fild_one,fild_two)
        self._number = number
        self._fild_one = fild_one
        self._fild_two = fild_two
        #добавляем метод защищенных элементов (декоратор) проперти
    @property
    def work(self):
        #так как метод проперти возвращаемый мы используем ретерн
        return f"произведение полусуммы на с-{((self.fild_one-self.fild_two)/2)*self._number}"
result = ThirteenTwo(10,3,7)
print(result.work)

# создаем класс с водда имени 
class Fourteen: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("вещественное число-",self.fild_one)#выводим значения атрибутов
        print("вещественное число-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("вычислить квадратный корень-",(self.fild_one*self.fild_two)**0.5)
# Класс потомок
class FourteenTwo(Fourteen):
    #метод инициализации
    def __init__(self,fild_one,fild_two,number):
        #супер возвращает объект посредник
        super().__init__(fild_one,fild_two)
        self._number = number
        self._fild_one = fild_one
        self._fild_two = fild_two
        #добавляем метод защищенных элементов (декоратор) проперти
    @property
    def work(self):
        #так как метод проперти возвращаемый мы используем ретерн
        return f"вычислить выражение-{((self.fild_one*self.fild_two)+self._number)**0.5}"
result = FourteenTwo(5,5,0)
print(result.work)

# создаем класс с водда имени 
class Fifteen: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("x-",self.fild_one)#выводим значения атрибутов
        print("y-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("вычислить целую часть от деления x на y-",self.fild_one//self.fild_two)
# Класс потомок
class FifteenTwo(Fifteen):
    #метод инициализации
    def __init__(self,fild_one,fild_two,number):
        #супер возвращает объект посредник
        super().__init__(fild_one,fild_two)
        self._number = number
        self._fild_one = fild_one
        self._fild_two = fild_two
        #добавляем метод защищенных элементов (декоратор) проперти
    @property
    def work(self):
        #так как метод проперти возвращаемый мы используем ретерн
        return f"вычислить выражение-{(self.fild_one/self._number)+(self.fild_two/self._number)}"
result = FifteenTwo(5,7,3)
print(result.work)

# создаем класс с водда имени 
class Sixteen: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("x-",self.fild_one)#выводим значения атрибутов
        print("y-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        if self.fild_one**0.5>self.fild_two**0.5:
            print(self.fild_two)
        else:
            print(self.fild_one)
# Класс потомок
class SixteenTwo(Sixteen):
    #метод инициализации
    def __init__(self,fild_one,fild_two,number):
        #супер возвращает объект посредник
        super().__init__(fild_one,fild_two)
        self._number = number
        self._fild_one = fild_one
        self._fild_two = fild_two
        #добавляем метод защищенных элементов (декоратор) проперти
    @property
    def work(self):
            if self.fild_one<self.fild_two:
                print(self.fild_one*self._number)
            else:
                print(self.fild_two*self._number)
result = SixteenTwo(10,3,7)
print(result.work)

# создаем класс с водда имени 
class Seventeen: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("x-",self.fild_one)#выводим значения атрибутов
        print("y-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        if self.fild_one>self.fild_two:
            print(self.fild_one**(1./3.))
        else:
            print(self.fild_two**(1./3.))
# Класс потомок
class SeventeenTwo(Seventeen):
    #метод инициализации
    def __init__(self,fild_one,fild_two,number):
        #супер возвращает объект посредник
        super().__init__(fild_one,fild_two)
        self._number = number
        self._fild_one = fild_one
        self._fild_two = fild_two
        #добавляем метод защищенных элементов (декоратор) проперти
    @property
    def work(self):
        if (self.fild_one**(1./3.))>(self.fild_two**(1./3.)):
            print((self._number**(1./3.))+(self.fild_one**(1./3.)))
        else:
            print((self._number**(1./3.))+(self.fild_two**(1./3.)))
result = SeventeenTwo(10,3,7)
print(result.work)

# создаем класс с водда имени 
class Eighteen: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("продолжительность разговора в минутах-",self.fild_one)#выводим значения атрибутов
        print("стоимость одной минуты разговора-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("стоимость разговора-",self.fild_one*self.fild_two)
# Класс потомок
class EighteenTwo(Fifteen):
    #метод инициализации
    def __init__(self,fild_one,fild_two,quantity):
        #супер возвращает объект посредник
        super().__init__(fild_one,fild_two)
        self._quantity = quantity
        self._fild_one = fild_one
        self._fild_two = fild_two
        #добавляем метод защищенных элементов (декоратор) проперти
    @property
    def price(self):
        #так как метод проперти возвращаемый мы используем ретерн
        return f"общая стоимость разговоров за сутки-{(self.fild_one*self.fild_two)*self._quantity}"
result = EighteenTwo(25,5,7)
print(result.price)

# создаем класс с водда имени 
class Nineteen: #имя класса
    def __init__(self,fild_one,fild_two):#метод инициализации при создании экземпляра класса в скобках указывается значение параметров
        self.fild_one = fild_one #передаем значения параметров из скобки атрибутам класса
        self.fild_two = fild_two#передаем значения параметров из скобки атрибутам класса
        #начинаются методы (это функции над атрибутами)
        #геттер-метод вывода значения атрибутов
        #у геттера нет параметров только ссылка self
    def get(self):
        print("координаты точки(по горизонтали)-",self.fild_one)#выводим значения атрибутов
        print("координаты точки(по вертикали)-",self.fild_two)#выводим значения атрибутов
        #методы для обработки
    def result(self):
        print("определить периметр прямоугольника-",self.fild_one*self.fild_two)
# Класс потомок
class NineteenTwo(Nineteen):
    #метод инициализации
    def __init__(self,fild_one,fild_two,number):
        #супер возвращает объект посредник
        super().__init__(fild_one,fild_two)
        self._number = number
        self._fild_one = fild_one
        self._fild_two = fild_two
        #добавляем метод защищенных элементов (декоратор) проперти
    @property
    def work(self):
        #так как метод проперти возвращаемый мы используем ретерн
        return f"увеличить точки на с и найти их произведение-{(self.fild_one+self._number)*(self.fild_two+self._number)}"
result = NineteenTwo(3,8,2)
print(result.work)