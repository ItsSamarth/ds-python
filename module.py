#MODULE

#condide module to be same as code library
#Or a file containing a set of functions you want to include in your application

import helpingModule

helpingModule.greeting('Pearl')

age = helpingModule.person1["age"]
print(age)


#renaming a MODULE
# import helpingModule as hm

# BUILD IN MODULE

import platform

systemDetails=platform.system()
print(systemDetails)

#fetch all the functions inside this module
functionDetails = dir(platform)
print(functionDetails)


#IMPORT PARTIAL FUNCTIONS FROM THE MODULES USING FROM KEYWORD
#from helpingModule import person1
