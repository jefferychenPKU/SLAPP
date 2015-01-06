import random
import os

"""
A memo from
http://www.devshed.com/c/a/Python/Python-Parameters-Functions-and-Arguments/
At the end of the parameters, you may optionally use either or both
of the special forms *identifier1 and **identifier2 .
If both forms are present, the form with two asterisks must
be last. *identifier1 specifies that any call to the function may
supply any number of extra positional arguments, while **identifier2
specifies that any call to the function may supply any number of
extra named arguments (positional and named arguments are covered
in "Calling Functions" on page 73). Every call to the function
binds identifier1  to a tuple whose items are the extra positional
arguments (or the empty tuple, if there are none). Similarly,
identifier2  gets bound to a dictionary whose items are the names
and values of the extra named arguments (or the empty dictionary,
if there are none). 
"""

# dictionary of the action groups
actionDictionary={}

# applying a method to a collection of instances
def askEachAgentInCollection(collection,method,**k):
    """ collection, method, dict. of the parameters (may be empty)"""

    for a in collection:
            #print "\naskEachAgentInCollection", a.agType, a.number, method
            """ 
            if a.agType=="recipes" and a.factoryInWhichRecipeIs!=None:
               print "askEachAgentInCollection", a.number, "is in", a.factoryInWhichRecipeIs.number
            if a.agType=="recipes" and a.factoryInWhichRecipeIs==None:
               print "askEachAgentInCollection", a.number, "is in", a.factoryInWhichRecipeIs
            """
            try:
                method(a,**k)
            except:
              print 'cannot apply (case 0) ', method, ' to agent number', \
                    a.number, 'of type ',a.agType
              if a.agType=="recipes": print "first step", a.content[0]
              pass
            # if we use k (a dictionary), the same notation has to
            # be placed into the agent methods

# applying a method to a collection of instances
def askEachAgentInCollectionAndExecLocalCode(collection,method,**k):
    """ collection, method, dict. of the parameters (may be empty)"""

    setLocalCode("")

    for a in collection:
            try: method(a,**k)
            except:
              print 'cannot apply (case 1) ', method, ' to agent number', \
                    a.number
              pass
            # if we use k (a dictionary), the same notation has to
            # be placed into the agent methods

            execLocalCode()
            


# applying a method to an instance of a class
def askAgent(agent,method,**k):
    """ agent, method, dict. of the parameters (may be empty)"""
    try: method(agent,**k)
    except:
        print 'cannot apply (case 2) ', method, ' to agent number', \
              a.number
        pass

# applying a method to an instance of a class
def askAgentAndExecLocalCode(agent,method,**k):
    """ agent, method, dict. of the parameters (may be empty)"""
    setLocalCode("")
    
    try: method(agent,**k)
    except:
        print 'cannot apply (case 3) ', method, ' to agent number', \
              a.number
        pass

    execLocalCode()



# extracting a step and rotating a list (obsolete)
"""
def extractAStepAndRotate(aList):
        if len(aList)==0:
            print "Error: action list is empty"
            os.sys.exit(1)

        aSubList=aList.pop(0)
        if type(aSubList)!=list:
            print "Error: the elements of the action list need to be a list"
            os.sys.exit(1)
        aList.append(aSubList)

        return aSubList[:] # with [:] we return the elements
                           # of aSubList, not the address
"""

# extracting a subStep
def extractASubStep(aSubList):
        if len(aSubList)>0: return aSubList.pop(0)
        else: return []

# insert an element in next position
def insertElementNextPosition(aList,what):
    aList.insert(0,what)


# exec("instruction 1; instruction 2; ...")
# pay attention to the semicolon
def execLocalCode():
      global localCode
      exec(localCode)
      cleanLocalCode()

def cleanLocalCode():
      global localCode
      localCode=""

def getLocalCode():
      global localCode
      return localCode

def setLocalCode(code):
      global localCode
      localCode=code

