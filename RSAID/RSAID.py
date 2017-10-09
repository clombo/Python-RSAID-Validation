"""
    TODO:

    Reset when ChangeID is called. Have a look at decorators and the example on the below link
    https://stackoverflow.com/questions/4866587/pythonic-way-to-reset-an-objects-variables

    Pythonic way to return attributes in specific data structure or type
    https://stackoverflow.com/questions/2553354/how-to-get-a-variable-name-as-a-string-in-python
    https://stackoverflow.com/questions/9058305/getting-attributes-of-a-class

    
"""
from datetime import date
import datetime


WEEKDAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
CITIZ = ['RSA','Other']

class IDValid:
    
    def __init__(self,IDNum=None):
        self._ID = IDNum
        self._Valid = False
        self._Gender = 'U'
        self._DOB = None
        self._Citizenship = 'Unknown'
        self._ContrDig = None
        self._Message = 'No validation done'
        self._BornOn = 'Unknown'
        self._CurrDate = datetime.date.today()
        self._DateFormat = "%d/%m/%Y"

        if IDNum <> None:
            self._FirstCheck()

    #Private methods to process internal data
    def _FirstCheck(self):
        
        #Check length, must be 13
        #Make sure ID only digits
        if len(self._ID) == 13 and self._ID.isdigit():
            
            #Set control digit
            self._ContrDig = int(self._ID[-1:])
            
            #Run validation if everything ok
            self._Validate()
        else:
            self._Message = 'Not required length or contains alpha numeric characters'

    def _Validate(self):
        #Run algo on ID
        
        #Change to generator?
        eveNums = int(self._ID[1::2])*2
        oddNums = self._ID[0::2][:-1]

        Total = 0
        CalcDig = 0
        
        #xrange?
        for i in range(0,len(oddNums)):
            Total += int(oddNums[i])
        
        #xrange?
        for i in range(0,len(str(eveNums))):
            Total += int(str(eveNums)[i])


        if Total > 9:
            CalcDig = 10-int(str(Total)[-1:])
        else:
            CalcDig = 10-Total

        if CalcDig == self._ContrDig:
            
            #Set rest of data pending on algo
            self._Valid = True
            self._Message = 'ID Valid'
            self._Citizenship = CITIZ[int(self._ID[10])]
            
            if self._ID[6] > 4:
                self._Gender = 'M'
            else:
                self._Gender = 'F'

        
            #Try building date
            self._BuildDOB(self._ID[0:2],self._ID[2:4],self._ID[4:6])
                
        else:
            self._Message = 'ID seems to be invalid'

    def _BuildDOB(self,Year,Month,Day):

        if int(Year) > (self._CurrDate.year - 2000):
            Year = '19'+Year
        else:
            Year = '20'+Year

        try:
            
            self._DOB = date(int(Year),int(Month),int(Day)) #d.strftime("%d/%m/%Y")
            self._DayBorn(self._DOB.weekday())
            
        except:
            self._Message = 'Could not build DOB'
        

    def _DayBorn(self,Day):
        self._BornOn = WEEKDAYS[Day]
        



    #Public methods to get attributes or all attributes in a data format
    
    def ChangeID(self,IDNum):
        
        #Change ID Number
        #Validate and set data
        #Make sure to reset data see links in TODO
        
        self._ID = IDNum
        self._Valid = False
        self._Gender = 'U'
        self._DOB = None
        self._Citizenship = 'Unknown'
        self._ContrDig = None
        self._Message = 'No validation done'
        self._BornOn = 'Unknown'

        self._FirstCheck()

    def DateFormat(self,dtformat):
        self._DateFormat = dtformat
    
    def DOB(self,dtformat=None):
        
        #ReturnDOB with format if specified
        if dtformat <> None:
            self._DateFormat = dtformat

        if self._DOB <> None:
            return self._DOB.strftime(self._DateFormat)
        else:
            return self._DOB
               
    def Gender(self):
        #Return Gender
        return self._Gender

    def Citizen(self):
        #Return Citizenship
        return self._Citizenship

    def BornOn(self):
        #Return Day born on
        return self._BornOn

    def Valid(self):
        #Return Valid
        return self._Valid
        
    
    def ToList(self):
        #Return List
        return [self._ID,self._Valid,self._Gender,self.DOB(),self._BornOn,self._Citizenship,self._Message]

    def ToDict(self):
        #Return Dictionary
        return {
        "ID":self._ID,
        "Valid":self._Valid,
        "Gender":self._Gender,
        "DOB":self.DOB(),
        "BornOn":self._BornOn,
        "Citizenship":self._Citizenship,
        "Message":self._Message}

    def ToString(self):
        
        #Return string
        return "ID: {}\nValid: {}\nGender: {}\nDOB: {}\nBornOn: {}\nCitizenship: {}\nMessage: {}".format(
        self._ID,self._Valid,self._Gender,self.DOB(),self._BornOn,self._Citizenship,self._Message)
        
    
        
