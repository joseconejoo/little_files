#https://www.codewars.com/kata/54bebed0d5b56c5b2600027f/python

class Debugger(object):
    attribute_accesses = []
    method_calls = []

class Meta(type):
    def __new__(mcs, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                attrs[attr_name] = mcs.deco(attr_value)

        attrs['__getattribute__'] = mcs.getattribute
        attrs['__setattr__'] = mcs.setattr

        return super().__new__(mcs, name, bases, attrs)

    @staticmethod
    def deco(func):
        def wrapper(*args, **kwargs):
            Debugger.method_calls.append({
                'class': args[0].__class__,
                'method': func.__name__,
                'args': args,
                'kwargs': kwargs
            })
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def getattribute(self, item):
        if item != '__class__':
            Debugger.attribute_accesses.append({
                'action': 'get',
                'class': self.__class__,
                'attribute': item,
            })
        return object.__getattribute__(self, item)

    @staticmethod
    def setattr(self, key, value):
        Debugger.attribute_accesses.append({
            'action': 'set',
            'class': self.__class__,
            'attribute': key,
            'value': value
        })
        return object.__setattr__(self, key, value)


