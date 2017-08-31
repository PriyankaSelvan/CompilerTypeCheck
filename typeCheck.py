import sys
import compiler
import enum

global variable_name

#Tags for types
class pytypes(enum.Enum):
      int_ = 0
      bool_ = 1
      error_ = 2

def type_check(node):
    global variable_name

    #Checking each type of node and performing actions

    if str(node).startswith("Assign"):
           variable_name =  node.getChildNodes()[0].name
           return type_check(node.getChildNodes()[1])

    elif str(node).startswith("Add"):
           typeleft = type_check(node.getChildNodes()[0])
           typeright = type_check(node.getChildNodes()[1])
           if typeleft != pytypes.error_ and typeright != pytypes.error_:
                return pytypes.int_
           else: return pytypes.error_

    elif str(node).startswith("And"):
           typeleft = type_check(node.getChildNodes()[0])
           typeright = type_check(node.getChildNodes()[1])
           if typeleft == pytypes.error_ or typeright == pytypes.error_:
              return pytypes.error_
           elif typeleft == pytypes.int_ and typeright == pytypes.int_:
              return pytypes.int_
           elif typeleft == pytypes.bool_ and typeright == pytypes.int_:
              return pytypes.int_
           else:
              return pytypes.bool_
           
    elif str(node).startswith("Not"):
           typedown = type_check(node.getChildNodes()[0])
           if typedown == pytypes.error_:
              return pytypes.error_
           else: return pytypes.bool_
    
    elif str(node).startswith("Const"):
        if isinstance(node.value,int):
          return pytypes.int_
        else: return pytypes.error_
 
    elif str(node).startswith("Name"):
        if node.name == "True" or node.name == "False":
           return pytypes.bool_
        else:
           return pytypes.error_
           

tree = compiler.parseFile("code.py")
nodes =  tree.node.nodes
strings = ["int", "bool", "error"]
for node in nodes:
   type_exp = type_check(node)
   print "Type of "+variable_name+" is "+str(strings[type_exp])
