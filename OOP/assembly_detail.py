# Apply knowledge of Abstract, Encapsulation,...to manage Machine detail: Create a detail in the machine. Detail have 3 part: head, body and tail. 
#head and body are the shape like Triangle, Retangle, Square, Circle
#tail is a list of shapes.


from shape_component import *

#assembly components

class Director:
    __builder = None
   
    def setBuilder(self, builder):
      self.__builder = builder
   
    def getDetail(self):
        detail = Detail()
        #name
        name = self.__builder.get_name()
        detail.set_name(name)

        # First Piece
        head = self.__builder.get_head()
        detail.set_head(head)
        
        # Second Peice
        body = self.__builder.get_body()
        detail.set_body(body)
        
        # Third Peice
        i = 0
        while i < 3:
            tail = self.__builder.get_tails()
            tail.get_name()
            detail.set_tail(tail)
            i += 1
        return detail


class Detail:
    def __init__(self):
        self.__name = None
        self.__head = None
        self.__body = None
        self.__tail = []

    def set_name(self, name):
        self.__name = name

    def set_head(self, head):
        self.__head = head
    
    def set_body(self, body):
        self.__body = body
    
    def set_tail(self, tail):
        self.__tail.append(tail)

    
    def describe(self):
        print('----Name-----')
        print(self.__name)

        print('----Head-----')
        print((self.__head).get_name())

        print('----Body-----')
        print((self.__body).get_name())

        print('----Tails-----')
        print(self.__tail)


        
class Builder:
    def get_name(self): 
        pass
    def get_head(self): 
        pass
    def get_body(self): 
        pass
    def get_tail(self): 
        pass


class DetailBuilder001(Builder):
    def get_name(self):
        return 'Chi tiet 1'

    def get_head(self):
        head = Triangle('Dau chi tiet 001', 6, 6, 6)
        return head
    
    def get_body(self):
        body = Retangle('Than chi tiet 001', 6, 8)
        return body
    
    def get_tails(self):
        sq = Square('abcd', 9)
        print(sq.get_name())
        return sq
    

chitiet1 = DetailBuilder001()

director = Director()

director.setBuilder(chitiet1)

product = director.getDetail()
product.describe()


