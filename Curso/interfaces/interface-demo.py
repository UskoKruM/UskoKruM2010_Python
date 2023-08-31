from abc import ABC, abstractmethod


class MyInterface(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class ClassA(MyInterface):

    def method1(self):
        print("Class A - method1")

    def method2(self):
        print("Class A - method2")


class ClassB(MyInterface):
    
    def method1(self):
        print("Class B - method1")

    def method2(self):
        print("Class B - method2")


objA = ClassA()
objA.method1()
objB = ClassB()
objB.method1()
