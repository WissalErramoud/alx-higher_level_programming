#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            element1 = my_list_1[i] if i < len(my_list_1) else 0
            element2 = my_list_2[i] if i < len(my_list_2) else 0
            
            if not (isinstance(element1, (int, float)) or
                    isinstance(element2, (int, float))):
                raise TypeError("wrong type")
            
            if element2 == 0:
                raise ZeroDivisionError("division by 0")
            
            div = element1 / element2
        
        except TypeError as e:
            print(e)
            div = 0
        except ZeroDivisionError as e:
            print(e)
            div = 0
        except IndexError as e:
            print(e)
            div = 0
        finally:
            result.append(div)
    
    return result
