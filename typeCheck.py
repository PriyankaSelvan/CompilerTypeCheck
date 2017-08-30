import sys
import compiler
import enum

global variable_name

class pytypes(enum.Enum):
      int_ = 0
      bool_ = 1
      error_ = 2

def type_check(node):
    global variable_name
    print "-----node is-----"
    print node
    children = node.getChildNodes()
    for child in children:
        print "------child is-------"
        print child
        if str(child).startswith("AssName"):
           print "Its an assign node"
           variable_name = child.name
        elif str(child).startswith("Add"):
           print "Its a add node"
           print "caling typechecks "
           typeleft = type_check(child.getChildNodes()[0])
           typeright = type_check(child.getChildNodes()[1])
           print typeleft, typeright
           if typeleft != pytypes.error_ and typeright != pytypes.error_:
                return pytypes.int_
        elif str(child).startswith("And"):
           print "its an and node"
           typeleft = type_check(child.getChildNodes()[0])
           typeright = type_check(child.getChildNodes()[1])
           if typeleft == pytypes.error_ or typeright == pytypes.error_:
              return pytypes.error_
           elif typeleft == pytypes.int_ and typeright == pytypes.int_:
              return pytypes.int_
           else:
              return pytypes.bool_
           
        elif str(child).startswith("Not"):
           print "its a not node"
           typedown = type_check(child.getChildNodes()[0])
           if typedown == pytypes.error_:
              return pytypes.error_
           else: return pytypes.bool_
    
        elif str(child).startswith("Const"):
           return type_check(child)
           
    if str(node).startswith("Const"):
        print "found the number"
        print node.value
        print type(node.value)
        if isinstance(node.value,int):
          return pytypes.int_
        elif isinstance(node.value,bool):
          return pytypes.bool_
        else: return pytypes.error_
      
           

tree = compiler.parseFile("code.py")
nodes =  tree.node.nodes
strings = ["int", "bool", "error"]
for node in nodes:
   type_exp = type_check(node)
   print "Type of "+variable_name+" is "+str(strings[type_exp])
