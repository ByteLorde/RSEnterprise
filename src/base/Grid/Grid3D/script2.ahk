GenerateInfo(byRef FirstName, byref LastName, byRef BirthDay, byRef BirthYear , byRef Email) ;------------------
{
FirstName := RandomName(51, 101)
LastName := RandomName( 4,8 )
Random, BirthDay, 1, 28
Random, BirthYear, 1975, 1999
BirthYearEdit := BirthYear - 1900
Email = %FirstName%%LastName%%BirthYearEdit%
Return
} 
