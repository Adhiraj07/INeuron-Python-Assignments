#!/usr/bin/env python
# coding: utf-8
1. Create an assert statement that throws an AssertionError if the variable spam is a negative
integer.

the assert statement is a powerful tool that helps with debugging and handling errors during development. It allows you to make assumptions about the code and catch potential issues early on.

The assert statement works by evaluating a boolean condition and raising an AssertionError if the expression is false. If the specified condition evaluates to True then it continues to execute next statements, otherwise it raises the AssertionError exception with the specified error message.
# In[2]:


def positive_num(spam):
    assert spam>0, "spam cannot be negative"
    
    return spam
 
positive_num(2)   
positive_num(-10)

2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same). 
# In[13]:


def check(string1, string2):
    assert string1.__eq__(string2),"both strings are not same"
    
    return ("both strings are same")

str1="I am string"
str2="I Am String"

check(str1.casefold(),str2.casefold())

3. Create an assert statement that throws an AssertionError every time. 
assert False, "This is an AssertionError"4. What are the two lines that must be present in your software in order to call logging.debug()? 

# In[19]:


import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

logging.debug("Starting the program....")

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    logging.debug(f'factorial of {num} is :-{fact}')
    
    logging.debug("End of program.")
    
fact(5)

5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt? 
# In[20]:


import logging
logging.basicConfig(filename='ProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

6. What are the five levels of logging? 
DEBUG: logging.debug()
INFO: logging.info()
Warning: logging.warning()
ERROR: logging.error()
CRITICAL: logging.critical()7. What line of code would you add to your software to disable all logging messages? 

logging.disable() -It is used to desable all the logging message
8.Why is using logging messages better than using print() to display the same message? 

The print() statement fails if our code does not have access to the console.

The print() statement only displays messages on the console. Recording logging data inside a file or sending it over the internet needs additional works.9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

Step In
Clicking the Step In button will cause the debugger to execute the next line of code and then pause again. If the next line of code is a function call, the debugger will “step into” that function and jump to the first line of code of that function.

Step Over
Clicking the Step Over button will execute the next line of code, similar to the Step In button. However, if the next line of code is a function call, the Step Over button will “step over” the code in the function. The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns. 

Step Out
Clicking the Step Out button will cause the debugger to execute lines of code at full speed until it returns from the current function. If we have stepped into a function call with the Step In button and now simply want to keep executing instructions until we get back out, click the Out button to “step out” of the current function call.

10.After you click Continue, when will the debugger stop ? 
Continue
Clicking the Continue button will cause the program to execute normally until it terminates or reaches a breakpoint. If we are done debugging and want the program to continue normally, click the Continue button.11. What is the concept of a breakpoint? 
A breakpoint can be set on a specific line of code and forces the debugger to pause whenever the program execution reaches that line.
# In[ ]:




