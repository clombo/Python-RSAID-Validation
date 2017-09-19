from IDVal import IDValid


#Test ID
TestID = IDValid()
print TestID.ToString()

print '\n'
print 'Changing ID'
print '\n'

TestID.ChangeID('8001015009087')
print TestID.ToString()

print '\n'
print 'Changing date format'
print '\n'

TestID.DateFormat("%Y-%m-%d")
print TestID.ToString()

print '\n'
print 'Get date only in different format'
print '\n'

print TestID.DOB("%d/%m/%y")
print '\n'

print TestID.ToString()

print '\n'
print 'Change to invalid ID'
print '\n'

TestID.ChangeID('8001015009088')
print TestID.ToString()

print '\n'
print 'Creating new object with IDNum parameter set to ID number'
print '\n'

TestID2 = IDValid(IDNum='8001015009087')
print TestID2.ToString()
