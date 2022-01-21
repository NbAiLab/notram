# Downloaded from https://repo.progsbase.com - Code Developed Using progsbase.

from math import *
def IsValidNorwegianPersonalIdentificationNumber(fnummer):

  errorMessage = CreateStringReference("")

  if len(fnummer) == 11.0:
    failures = CreateNumberReference(0.0)

    d1 = CharToNumberWithCheck(fnummer[int(0.0)], failures)
    d2 = CharToNumberWithCheck(fnummer[int(1.0)], failures)
    d3 = CharToNumberWithCheck(fnummer[int(2.0)], failures)
    d4 = CharToNumberWithCheck(fnummer[int(3.0)], failures)
    d5 = CharToNumberWithCheck(fnummer[int(4.0)], failures)
    d6 = CharToNumberWithCheck(fnummer[int(5.0)], failures)
    d7 = CharToNumberWithCheck(fnummer[int(6.0)], failures)
    d8 = CharToNumberWithCheck(fnummer[int(7.0)], failures)
    d9 = CharToNumberWithCheck(fnummer[int(8.0)], failures)
    d10 = CharToNumberWithCheck(fnummer[int(9.0)], failures)
    d11 = CharToNumberWithCheck(fnummer[int(10.0)], failures)

    if failures.numberValue == 0.0:
      aDatetimeDate = GetDateFromNorwegianPersonalIdentificationNumber(fnummer, failures)

      if datetimeIsValidDate(aDatetimeDate, errorMessage):
        if failures.numberValue == 0.0:
          k1 = d1*3.0 + d2*7.0 + d3*6.0 + d4*1.0 + d5*8.0 + d6*9.0 + d7*4.0 + d8*5.0 + d9*2.0
          k1 = k1 % 11.0
          if k1 != 0.0:
            k1 = 11.0 - k1
          if k1 == 10.0:
            failures.numberValue = failures.numberValue + 1.0

          k2 = d1*5.0 + d2*4.0 + d3*3.0 + d4*2.0 + d5*7.0 + d6*6.0 + d7*5.0 + d8*4.0 + d9*3.0 + k1*2.0
          k2 = k2 % 11.0
          if k2 != 0.0:
            k2 = 11.0 - k2
          if k2 == 10.0:
            failures.numberValue = failures.numberValue + 1.0

          if k1 == d10 and k2 == d11 and failures.numberValue == 0.0:
            gyldig = True
          else:
            gyldig = False
        else:
          gyldig = False
      else:
        gyldig = False
    else:
      gyldig = False
  else:
    gyldig = False

  return gyldig

def GetDateFromNorwegianPersonalIdentificationNumber(fnummer, failures):

  aDatetimeDate = datetimeDate()

  d1 = CharToNumberWithCheck(fnummer[int(0.0)], failures)
  d2 = CharToNumberWithCheck(fnummer[int(1.0)], failures)
  d3 = CharToNumberWithCheck(fnummer[int(2.0)], failures)
  d4 = CharToNumberWithCheck(fnummer[int(3.0)], failures)
  d5 = CharToNumberWithCheck(fnummer[int(4.0)], failures)
  d6 = CharToNumberWithCheck(fnummer[int(5.0)], failures)
  d7 = CharToNumberWithCheck(fnummer[int(6.0)], failures)
  d8 = CharToNumberWithCheck(fnummer[int(7.0)], failures)
  d9 = CharToNumberWithCheck(fnummer[int(8.0)], failures)

  if failures.numberValue == 0.0:
    # Individnummer
    individnummer = d7*100.0 + d8*10.0 + d9

    # Make date
    day = d1*10.0 + d2
    month = d3*10.0 + d4
    year = d5*10.0 + d6

    if individnummer >= 0.0 and individnummer <= 499.0:
      year = year + 1900.0
    elif individnummer >= 500.0 and individnummer <= 749.0 and year >= 54.0 and year <= 99.0:
      year = year + 1800.0
    elif individnummer >= 900.0 and individnummer <= 999.0 and year >= 40.0 and year <= 99.0:
      year = year + 1900.0
    elif individnummer >= 500.0 and individnummer <= 999.0 and year >= 0.0 and year <= 39.0:
      year = year + 1900.0
    else:
      failures.numberValue = failures.numberValue + 1.0

    aDatetimeDate.year = year
    aDatetimeDate.month = month
    aDatetimeDate.day = day

  return aDatetimeDate

def CharToNumberWithCheck(c, failures):

  if charIsNumber(c):
    val = nGetNumberFromNumberCharacterForBase(c, 10.0)
  else:
    val = 0.0
    failures.numberValue = failures.numberValue + 1.0

  return val

def test1():
  failures = CreateNumberReference(0.0)

  AssertTrue(IsValidNorwegianPersonalIdentificationNumber("10061270707"), failures)

  return failures.numberValue

def test():
  failures = 0.0

  failures = failures + test1()

  return failures

class BooleanArrayReference:
  booleanArray = None

class BooleanReference:
  booleanValue = None

class CharacterReference:
  characterValue = None

class NumberArrayReference:
  numberArray = None

class NumberReference:
  numberValue = None

class StringArrayReference:
  stringArray = None

class StringReference:
  string = None

def CreateBooleanReference(value):
  ref = BooleanReference()
  ref.booleanValue = value

  return ref

def CreateBooleanArrayReference(value):
  ref = BooleanArrayReference()
  ref.booleanArray = value

  return ref

def CreateBooleanArrayReferenceLengthValue(length, value):
  ref = BooleanArrayReference()
  ref.booleanArray =  [None]*int(length)

  i = 0.0
  while i < length:
    ref.booleanArray[int(i)] = value
    i = i + 1.0
  

  return ref

def FreeBooleanArrayReference(booleanArrayReference):
  booleanArrayReference.booleanArray = None
  booleanArrayReference = None

def CreateCharacterReference(value):
  ref = CharacterReference()
  ref.characterValue = value

  return ref

def CreateNumberReference(value):
  ref = NumberReference()
  ref.numberValue = value

  return ref

def CreateNumberArrayReference(value):
  ref = NumberArrayReference()
  ref.numberArray = value

  return ref

def CreateNumberArrayReferenceLengthValue(length, value):
  ref = NumberArrayReference()
  ref.numberArray =  [None]*int(length)

  i = 0.0
  while i < length:
    ref.numberArray[int(i)] = value
    i = i + 1.0
  

  return ref

def FreeNumberArrayReference(numberArrayReference):
  numberArrayReference.numberArray = None
  numberArrayReference = None

def CreateStringReference(value):
  ref = StringReference()
  ref.string = value

  return ref

def CreateStringReferenceLengthValue(length, value):
  ref = StringReference()
  ref.string =  [None]*int(length)

  i = 0.0
  while i < length:
    ref.string[int(i)] = value
    i = i + 1.0
  

  return ref

def FreeStringReference(stringReference):
  stringReference.string = None
  stringReference = None

def CreateStringArrayReference(strings):
  ref = StringArrayReference()
  ref.stringArray = strings

  return ref

def CreateStringArrayReferenceLengthValue(length, value):
  ref = StringArrayReference()
  ref.stringArray =  [None]*int(length)

  i = 0.0
  while i < length:
    ref.stringArray[int(i)] = CreateStringReference(value)
    i = i + 1.0
  

  return ref

def FreeStringArrayReference(stringArrayReference):
  i = 0.0
  while i < len(stringArrayReference.stringArray):
    stringArrayReference.stringArray[int(i)] = None
    i = i + 1.0
  
  stringArrayReference.stringArray = None
  stringArrayReference = None

def nCreateStringDecimalFromNumber(decimal):
  stringReference = StringReference()

  # This will succeed because base = 10.
  nCreateStringFromNumberWithCheck(decimal, 10.0, stringReference)

  return stringReference.string

def nCreateStringFromNumberWithCheck(decimal, base, stringReference):
  if decimal == 0.0:
    stringReference.string = "0"
    success = True
  else:
    characterReference = CharacterReference()
    if IsInteger(base):
      success = True
      string =  [None]*int(0.0)
      maximumDigits = nGetMaximumDigitsForBase(base)
      digitPosition = nGetFirstDigitPosition(decimal, base)
      decimal = round(decimal*base**(maximumDigits - digitPosition - 1.0))
      hasPrintedPoint = False
      if digitPosition < 0.0:
        string = AppendCharacter(string, '0')
        string = AppendCharacter(string, '.')
        hasPrintedPoint = True
        i = 0.0
        while i <  -digitPosition - 1.0:
          string = AppendCharacter(string, '0')
          i = i + 1.0
        
      i = 0.0
      while i < maximumDigits and success:
        d = floor(decimal/base**(maximumDigits - i - 1.0))
        if  not hasPrintedPoint  and digitPosition - i + 1.0 == 0.0:
          if decimal != 0.0:
            string = AppendCharacter(string, '.')
          hasPrintedPoint = True
        if decimal == 0.0 and hasPrintedPoint:
          pass
        else:
          success = nGetSingleDigitCharacterFromNumberWithCheck(d, base, characterReference)
          if success:
            c = characterReference.characterValue
            string = AppendCharacter(string, c)
        if success:
          decimal = decimal - d*base**(maximumDigits - i - 1.0)
        i = i + 1.0
      
      if success:
        i = 0.0
        while i < digitPosition - maximumDigits + 1.0:
          string = AppendCharacter(string, '0')
          i = i + 1.0
        
        stringReference.string = string
    else:
      success = False

  # Done
  return success

def nGetMaximumDigitsForBase(base):
  t = 10.0**15.0
  return floor(log10(t)/log10(base))

def nGetFirstDigitPosition(decimal, base):
  power = ceil(log10(decimal)/log10(base))

  t = decimal*base**( -power)
  if t < base and t >= 1.0:
    pass
  elif t >= base:
    power = power + 1.0
  elif t < 1.0:
    power = power - 1.0

  return power

def nGetSingleDigitCharacterFromNumberWithCheck(c, base, characterReference):
  numberTable = nGetDigitCharacterTable()

  if c < base or c < len(numberTable):
    success = True
    characterReference.characterValue = numberTable[int(c)]
  else:
    success = False

  return success

def nGetDigitCharacterTable():
  numberTable =  [None]*int(36.0)

  numberTable[int(0.0)] = '0'
  numberTable[int(1.0)] = '1'
  numberTable[int(2.0)] = '2'
  numberTable[int(3.0)] = '3'
  numberTable[int(4.0)] = '4'
  numberTable[int(5.0)] = '5'
  numberTable[int(6.0)] = '6'
  numberTable[int(7.0)] = '7'
  numberTable[int(8.0)] = '8'
  numberTable[int(9.0)] = '9'
  numberTable[int(10.0)] = 'A'
  numberTable[int(11.0)] = 'B'
  numberTable[int(12.0)] = 'C'
  numberTable[int(13.0)] = 'D'
  numberTable[int(14.0)] = 'E'
  numberTable[int(15.0)] = 'F'
  numberTable[int(16.0)] = 'G'
  numberTable[int(17.0)] = 'H'
  numberTable[int(18.0)] = 'I'
  numberTable[int(19.0)] = 'J'
  numberTable[int(20.0)] = 'K'
  numberTable[int(21.0)] = 'L'
  numberTable[int(22.0)] = 'M'
  numberTable[int(23.0)] = 'N'
  numberTable[int(24.0)] = 'O'
  numberTable[int(25.0)] = 'P'
  numberTable[int(26.0)] = 'Q'
  numberTable[int(27.0)] = 'R'
  numberTable[int(28.0)] = 'S'
  numberTable[int(29.0)] = 'T'
  numberTable[int(30.0)] = 'U'
  numberTable[int(31.0)] = 'V'
  numberTable[int(32.0)] = 'W'
  numberTable[int(33.0)] = 'X'
  numberTable[int(34.0)] = 'Y'
  numberTable[int(35.0)] = 'Z'

  return numberTable

def nCreateNumberFromDecimalStringWithCheck(string, decimalReference, errorMessage):
  return nCreateNumberFromStringWithCheck(string, 10.0, decimalReference, errorMessage)

def nCreateNumberFromDecimalString(string):
  doubleReference = CreateNumberReference(0.0)
  stringReference = CreateStringReference("")
  nCreateNumberFromStringWithCheck(string, 10.0, doubleReference, stringReference)
  number = doubleReference.numberValue

  doubleReference = None
  stringReference = None

  return number

def nCreateNumberFromStringWithCheck(string, base, decimalReference, errorMessage):
  success = True
  i = 0.0
  isPositive = True
  beforeDecimalPoint = 0.0
  afterDecimalPoint = 0.0
  n = 0.0
  validCharacters = 0.0

  if base >= 2.0 and base <= 36.0:
    j = 0.0
    while j < len(string):
      c = string[int(j)]
      if nCharacterIsNumberCharacterInBase(c, base) or c == '.' or c == '-':
        validCharacters = validCharacters + 1.0
      j = j + 1.0
    
    if validCharacters == len(string):
      if len(string) > 0.0:
        c = string[int(i)]
        if c == '-':
          isPositive = False
          i = i + 1.0
        if i < len(string):
          c = string[int(i)]
          if nCharacterIsNumberCharacterInBase(c, base):
            while nCharacterIsNumberCharacterInBase(c, base) and (i < len(string)):
              beforeDecimalPoint = beforeDecimalPoint + 1.0
              i = i + 1.0
              if i < len(string):
                c = string[int(i)]
            
            if i < len(string):
              c = string[int(i)]
              if c == '.':
                i = i + 1.0
                if i < len(string):
                  c = string[int(i)]
                  while nCharacterIsNumberCharacterInBase(c, base) and (i < len(string)):
                    afterDecimalPoint = afterDecimalPoint + 1.0
                    i = i + 1.0
                    if i < len(string):
                      c = string[int(i)]
                  
                else:
                  success = False
                  errorMessage.string = "Number must have digits after the decimal point."
          else:
            success = False
            errorMessage.string = "Number must start with digits (for negative numbers, after the negative sign)."
        if success != False:
          if isPositive:
            i = 0.0
          else:
            i = 1.0
          j = 0.0
          while j < beforeDecimalPoint:
            c = string[int(i)]
            i = i + 1.0
            d = nGetNumberFromNumberCharacterForBase(c, base)
            n = n + d*base**(beforeDecimalPoint - j - 1.0)
            j = j + 1.0
          
          if afterDecimalPoint > 0.0:
            i = i + 1.0
            j = 0.0
            while j < afterDecimalPoint:
              c = string[int(i)]
              i = i + 1.0
              d = nGetNumberFromNumberCharacterForBase(c, base)
              n = n + d*base**(0.0 - j - 1.0)
              j = j + 1.0
            
          if  not isPositive :
            n =  -n
          decimalReference.numberValue = n
          success = True
      else:
        success = False
        errorMessage.string = "String has no content."
    else:
      success = False
      errorMessage.string = "String contains invalid character."
  else:
    success = False
    errorMessage.string = "Base must be from 2 to 36."

  return success

def nGetNumberFromNumberCharacterForBase(c, base):
  numberTable = nGetDigitCharacterTable()
  position = 0.0

  i = 0.0
  while i < base:
    if numberTable[int(i)] == c:
      position = i
    i = i + 1.0
  

  return position

def nCharacterIsNumberCharacterInBase(c, base):
  numberTable = nGetDigitCharacterTable()
  found = False

  i = 0.0
  while i < base:
    if numberTable[int(i)] == c:
      found = True
    i = i + 1.0
  

  return found

def nStringToNumberArray(str):
  numberArrayReference = NumberArrayReference()
  stringReference = StringReference()

  nStringToNumberArrayWithCheck(str, numberArrayReference, stringReference)

  numbers = numberArrayReference.numberArray

  numberArrayReference = None
  stringReference = None

  return numbers

def nStringToNumberArrayWithCheck(str, numberArrayReference, errorMessage):
  numberStrings = SplitByString(str, ",")

  numbers =  [None]*int(len(numberStrings))
  success = True
  numberReference = NumberReference()

  i = 0.0
  while i < len(numberStrings):
    numberString = numberStrings[int(i)].string
    trimmedNumberString = Trim(numberString)
    success = nCreateNumberFromDecimalStringWithCheck(trimmedNumberString, numberReference, errorMessage)
    numbers[int(i)] = numberReference.numberValue
    FreeStringReference(numberStrings[int(i)])
    trimmedNumberString = None
    i = i + 1.0
  

  numberStrings = None
  numberReference = None

  numberArrayReference.numberArray = numbers

  return success

class datetimeDate:
  year = None
  month = None
  day = None

class datetimeDateReference:
  date = None

class datetimeDateTimeTimezone:
  dateTime = None
  timezoneOffsetSeconds = None

class datetimeDateTimeTimezoneReference:
  dateTimeTimezone = None

class datetimeDateTime:
  date = None
  hours = None
  minutes = None
  seconds = None

class datetimeDateTimeReference:
  dateTime = None

def datetimeCreateDate(year, month, day):
  date = datetimeDate()

  date.year = year
  date.month = month
  date.day = day

  return date

def datetimeIsLeapYearWithCheck(year, isLeapYearReference, errorMessage):
  if year >= 1752.0:
    success = True
    itIsLeapYear = datetimeIsLeapYear(year)
  else:
    success = False
    itIsLeapYear = False
    errorMessage.string = "Gregorian calendar was not in general use."

  isLeapYearReference.booleanValue = itIsLeapYear
  return success

def datetimeIsLeapYear(year):
  if DivisibleBy(year, 4.0):
    if DivisibleBy(year, 100.0):
      if DivisibleBy(year, 400.0):
        itIsLeapYear = True
      else:
        itIsLeapYear = False
    else:
      itIsLeapYear = True
  else:
    itIsLeapYear = False

  return itIsLeapYear

def datetimeDayToDateWithCheck(dayNr, dateReference, errorMessage):
  if dayNr >=  -79623.0:
    date = datetimeDate()
    remainder = NumberReference()
    remainder.numberValue = dayNr + 79623.0
    date.year = datetimeGetYearFromDayNr(remainder.numberValue, remainder)
    date.month = datetimeGetMonthFromDayNr(remainder.numberValue, date.year, remainder)
    date.day = 1.0 + remainder.numberValue
    dateReference.date = date
    success = True
  else:
    success = False
    errorMessage.string = "Gregorian calendar was not in general use before 1752."

  return success

def datetimeGetMonthFromDayNrWithCheck(dayNr, year, monthReference, remainderReference, errorMessage):
  if dayNr >=  -79623.0:
    month = datetimeGetMonthFromDayNr(dayNr, year, remainderReference)
    monthReference.numberValue = month
    success = True
  else:
    success = False
    errorMessage.string = "Gregorian calendar not in general use before 1752."

  return success

def datetimeGetMonthFromDayNr(dayNr, year, remainderReference):
  daysInMonth = datetimeGetDaysInMonth(year)
  done = False
  month = 1.0

  while  not done :
    if dayNr > daysInMonth[int(month)]:
      dayNr = dayNr - daysInMonth[int(month)]
      month = month + 1.0
    else:
      done = True
  
  remainderReference.numberValue = dayNr

  return month

def datetimeGetYearFromDayNrWithCheck(dayNr, yearReference, remainder, errorMessage):
  if dayNr >= 0.0:
    success = True
    year = datetimeGetYearFromDayNr(dayNr, remainder)
    yearReference.numberValue = year
  else:
    success = False
    errorMessage.string = "Day number must be 0 or higher. 0 is 1752-01-01."

  return success

def datetimeGetYearFromDayNr(dayNr, remainder):
  done = False
  year = 1752.0

  while  not done :
    if datetimeIsLeapYear(year):
      nrOfDays = 366.0
    else:
      nrOfDays = 365.0
    if dayNr >= nrOfDays:
      dayNr = dayNr - nrOfDays
      year = year + 1.0
    else:
      done = True
  
  remainder.numberValue = dayNr

  return year

def datetimeDaysBetweenDates(A, B):
  daysA = datetimeDateToDays(A)
  daysB = datetimeDateToDays(B)

  daysBetween = daysB - daysA

  return daysBetween

def datetimeGetDaysInMonthWithCheck(year, daysInMonthReference, errorMessage):
  date = datetimeCreateDate(year, 1.0, 1.0)

  success = datetimeIsValidDate(date, errorMessage)
  if success:
    daysInMonth = datetimeGetDaysInMonth(year)
    daysInMonthReference.numberArray = daysInMonth

  return success

def datetimeGetDaysInMonth(year):
  daysInMonth =  [None]*int(1.0 + 12.0)

  daysInMonth[int(0.0)] = 0.0
  daysInMonth[int(1.0)] = 31.0

  if datetimeIsLeapYear(year):
    daysInMonth[int(2.0)] = 29.0
  else:
    daysInMonth[int(2.0)] = 28.0
  daysInMonth[int(3.0)] = 31.0
  daysInMonth[int(4.0)] = 30.0
  daysInMonth[int(5.0)] = 31.0
  daysInMonth[int(6.0)] = 30.0
  daysInMonth[int(7.0)] = 31.0
  daysInMonth[int(8.0)] = 31.0
  daysInMonth[int(9.0)] = 30.0
  daysInMonth[int(10.0)] = 31.0
  daysInMonth[int(11.0)] = 30.0
  daysInMonth[int(12.0)] = 31.0

  return daysInMonth

def datetimeDateToDaysWithCheck(date, dayNumberReferenceReference, errorMessage):
  success = datetimeIsValidDate(date, errorMessage)
  if success:
    days = datetimeDateToDays(date)
    dayNumberReferenceReference.numberValue = days

  return success

def datetimeDateToDays(date):
  days =  -79623.0

  days = days + datetimeDaysInYears(date.year)
  days = days + datetimeDaysInMonths(date.month, date.year)
  days = days + date.day - 1.0

  return days

def datetimeDateToWeekdayNumberWithCheck(date, weekDayNumberReference, errorMessage):
  success = datetimeIsValidDate(date, errorMessage)
  if success:
    weekDay = datetimeDateToWeekdayNumber(date)
    weekDayNumberReference.numberValue = weekDay

  return success

def datetimeDateToWeekdayNumber(date):
  days = datetimeDateToDays(date)

  days = days + 79623.0
  days = days + 5.0

  weekDay = days % 7.0 + 1.0

  return weekDay

def datetimeDaysInMonthsWithCheck(month, year, daysInMonthsReference, errorMessage):
  date = datetimeCreateDate(year, month, 1.0)

  success = datetimeIsValidDate(date, errorMessage)
  if success:
    days = datetimeDaysInMonths(month, year)
    daysInMonthsReference.numberValue = days

  return success

def datetimeDaysInMonths(month, year):
  daysInMonth = datetimeGetDaysInMonth(year)

  days = 0.0
  i = 1.0
  while i < month:
    days = days + daysInMonth[int(i)]
    i = i + 1.0
  

  return days

def datetimeDaysInYearsWithCheck(years, daysReference, errorMessage):
  date = datetimeCreateDate(years, 1.0, 1.0)

  success = datetimeIsValidDate(date, errorMessage)
  if success:
    days = datetimeDaysInYears(years)
    daysReference.numberValue = days

  return success

def datetimeDaysInYears(years):
  days = 0.0
  i = 1752.0
  while i < years:
    if datetimeIsLeapYear(i):
      nrOfDays = 366.0
    else:
      nrOfDays = 365.0
    days = days + nrOfDays
    i = i + 1.0
  

  return days

def datetimeIsValidDate(date, errorMessage):
  if date.year >= 1752.0:
    if date.month >= 1.0 and date.month <= 12.0:
      daysInMonth = datetimeGetDaysInMonth(date.year)
      daysInThisMonth = daysInMonth[int(date.month)]
      if date.day >= 1.0 and date.day <= daysInThisMonth:
        valid = True
      else:
        valid = False
        errorMessage.string = "The month does not have the given day number."
    else:
      valid = False
      errorMessage.string = "Month must be between 1 and 12, inclusive."
  else:
    valid = False
    errorMessage.string = "Gregorian calendar was not in general use before 1752."

  return valid

def datetimeCreateDateTimeTimezone(year, month, day, hours, minutes, seconds, timezoneOffsetSeconds):
  dateTimeTimezone = datetimeDateTimeTimezone()

  dateTimeTimezone.dateTime = datetimeCreateDateTime(year, month, day, hours, minutes, seconds)
  dateTimeTimezone.timezoneOffsetSeconds = timezoneOffsetSeconds

  return dateTimeTimezone

def datetimeCreateDateTimeTimezoneInHoursAndMinutes(year, month, day, hours, minutes, seconds, timezoneOffsetHours, timezoneOffsetMinutes):
  dateTimeTimezone = datetimeDateTimeTimezone()

  dateTimeTimezone.dateTime = datetimeCreateDateTime(year, month, day, hours, minutes, seconds)
  dateTimeTimezone.timezoneOffsetSeconds = datetimeGetSecondsFromHours(timezoneOffsetHours) + datetimeGetSecondsFromMinutes(timezoneOffsetMinutes)

  return dateTimeTimezone

def datetimeGetDateFromDateTimeTimeZone(dateTimeTimezone, dateTimeReference, errorMessage):
  dateTime = dateTimeTimezone.dateTime

  return datetimeAddSecondsToDateTime(dateTime,  -dateTimeTimezone.timezoneOffsetSeconds, dateTimeReference, errorMessage)

def datetimeCreateDateTimeTimezoneFromDateTimeAndTimeZoneInSeconds(dateTime, timezoneOffsetSeconds, dateTimeTimezoneReference, errorMessage):
  adjustedDateTimeReference = datetimeDateTimeReference()
  dateTimeTimezone = datetimeDateTimeTimezone()

  success = datetimeAddSecondsToDateTime(dateTime, timezoneOffsetSeconds, adjustedDateTimeReference, errorMessage)

  if success:
    dateTimeTimezone.dateTime = adjustedDateTimeReference.dateTime
    dateTimeTimezone.timezoneOffsetSeconds = timezoneOffsetSeconds
    dateTimeTimezoneReference.dateTimeTimezone = dateTimeTimezone

  return success

def datetimeCreateDateTimeTimezoneFromDateTimeAndTimeZoneInHoursAndMinutes(dateTime, timezoneOffsetHours, timezoneOffsetMinutes, dateTimeTimezoneReference, errorMessage):
  return datetimeCreateDateTimeTimezoneFromDateTimeAndTimeZoneInSeconds(dateTime, datetimeGetSecondsFromHours(timezoneOffsetHours) + datetimeGetSecondsFromMinutes(timezoneOffsetMinutes), dateTimeTimezoneReference, errorMessage)

def datetimeCreateDateTime(year, month, day, hours, minutes, seconds):
  dateTime = datetimeDateTime()

  dateTime.date = datetimeCreateDate(year, month, day)
  dateTime.hours = hours
  dateTime.minutes = minutes
  dateTime.seconds = seconds

  return dateTime

def datetimeGetDateTimeFromSeconds(seconds, dateTimeReference, errorMessage):
  secondsInMinute = 60.0
  secondsInHour = 60.0*secondsInMinute
  secondsInDay = 24.0*secondsInHour
  days = floor(seconds/secondsInDay)
  remainder = seconds - days*secondsInDay
  dateReference = datetimeDateReference()

  success = datetimeDayToDateWithCheck(days, dateReference, errorMessage)
  if success:
    date = dateReference.date
    dateTime = datetimeDateTime()
    dateTime.date = date
    dateTime.hours = floor(remainder/secondsInHour)
    remainder = remainder - dateTime.hours*secondsInHour
    dateTime.minutes = floor(remainder/secondsInMinute)
    remainder = remainder - dateTime.minutes*secondsInMinute
    dateTime.seconds = remainder
    dateTimeReference.dateTime = dateTime

  return success

def datetimeGetSecondsFromDateTime(dateTime):
  seconds = 0.0
  dayNumberReferenceReference = NumberReference()
  errorMessage = StringReference()

  success = datetimeDateToDaysWithCheck(dateTime.date, dayNumberReferenceReference, errorMessage)
  if success:
    days = dayNumberReferenceReference.numberValue
    secondsInMinute = 60.0
    secondsInHour = 60.0*secondsInMinute
    secondsInDay = 24.0*secondsInHour
    seconds = seconds + secondsInDay*days
    seconds = seconds + secondsInHour*dateTime.hours
    seconds = seconds + secondsInMinute*dateTime.minutes
    seconds = seconds + dateTime.seconds

  return seconds

def datetimeGetSecondsFromMinutes(minutes):
  return minutes*60.0

def datetimeGetSecondsFromHours(hours):
  return datetimeGetSecondsFromMinutes(hours*60.0)

def datetimeGetSecondsFromDays(days):
  return datetimeGetSecondsFromHours(days*24.0)

def datetimeGetSecondsFromWeeks(weeks):
  return datetimeGetSecondsFromDays(weeks*7.0)

def datetimeGetMinutesFromSeconds(seconds):
  return seconds/60.0

def datetimeGetHoursFromSeconds(seconds):
  return datetimeGetMinutesFromSeconds(seconds)/60.0

def datetimeGetDaysFromSeconds(seconds):
  return datetimeGetHoursFromSeconds(seconds)/24.0

def datetimeGetWeeksFromSeconds(seconds):
  return datetimeGetDaysFromSeconds(seconds)/7.0

def datetimeGetDateFromDateTime(dateTime):
  return dateTime.date

def datetimeAddSecondsToDateTime(dateTime, seconds, dateTimeReference, errorMessage):
  secondsInDateTime = datetimeGetSecondsFromDateTime(dateTime)
  secondsInDateTime = secondsInDateTime + seconds

  return datetimeGetDateTimeFromSeconds(secondsInDateTime, dateTimeReference, errorMessage)

def datetimeAddMinutesToDateTime(dateTime, minutes, dateTimeReference, errorMessage):
  return datetimeAddSecondsToDateTime(dateTime, datetimeGetSecondsFromMinutes(minutes), dateTimeReference, errorMessage)

def datetimeAddHoursToDateTime(dateTime, minutes, dateTimeReference, errorMessage):
  return datetimeAddSecondsToDateTime(dateTime, datetimeGetSecondsFromHours(minutes), dateTimeReference, errorMessage)

def datetimeAddDaysToDateTime(dateTime, days, dateTimeReference, errorMessage):
  return datetimeAddSecondsToDateTime(dateTime, datetimeGetSecondsFromDays(days), dateTimeReference, errorMessage)

def datetimeAddWeeksToDateTime(dateTime, weeks, dateTimeReference, errorMessage):
  return datetimeAddSecondsToDateTime(dateTime, datetimeGetSecondsFromWeeks(weeks), dateTimeReference, errorMessage)

def AssertFalse(b, failures):
  if b:
    failures.numberValue = failures.numberValue + 1.0

def AssertTrue(b, failures):
  if  not b :
    failures.numberValue = failures.numberValue + 1.0

def AssertEquals(a, b, failures):
  if a != b:
    failures.numberValue = failures.numberValue + 1.0

def AssertBooleansEqual(a, b, failures):
  if a != b:
    failures.numberValue = failures.numberValue + 1.0

def AssertCharactersEqual(a, b, failures):
  if a != b:
    failures.numberValue = failures.numberValue + 1.0

def AssertStringEquals(a, b, failures):
  if  not StringsEqual(a, b) :
    failures.numberValue = failures.numberValue + 1.0

def AssertNumberArraysEqual(a, b, failures):
  if len(a) == len(b):
    i = 0.0
    while i < len(a):
      AssertEquals(a[int(i)], b[int(i)], failures)
      i = i + 1.0
    
  else:
    failures.numberValue = failures.numberValue + 1.0

def AssertBooleanArraysEqual(a, b, failures):
  if len(a) == len(b):
    i = 0.0
    while i < len(a):
      AssertBooleansEqual(a[int(i)], b[int(i)], failures)
      i = i + 1.0
    
  else:
    failures.numberValue = failures.numberValue + 1.0

def AssertStringArraysEqual(a, b, failures):
  if len(a) == len(b):
    i = 0.0
    while i < len(a):
      AssertStringEquals(a[int(i)].string, b[int(i)].string, failures)
      i = i + 1.0
    
  else:
    failures.numberValue = failures.numberValue + 1.0

def StringToNumberArray(string):
  array =  [None]*int(len(string))

  i = 0.0
  while i < len(string):
    array[int(i)] = ord(string[int(i)])
    i = i + 1.0
  
  return array

def NumberArrayToString(array):
  string =  [None]*int(len(array))

  i = 0.0
  while i < len(array):
    string[int(i)] = unichr(int(array[int(i)]))
    i = i + 1.0
  
  return string

def NumberArraysEqual(a, b):
  equal = True
  if len(a) == len(b):
    i = 0.0
    while i < len(a) and equal:
      if a[int(i)] != b[int(i)]:
        equal = False
      i = i + 1.0
    
  else:
    equal = False

  return equal

def BooleanArraysEqual(a, b):
  equal = True
  if len(a) == len(b):
    i = 0.0
    while i < len(a) and equal:
      if a[int(i)] != b[int(i)]:
        equal = False
      i = i + 1.0
    
  else:
    equal = False

  return equal

def StringsEqual(a, b):
  equal = True
  if len(a) == len(b):
    i = 0.0
    while i < len(a) and equal:
      if a[int(i)] != b[int(i)]:
        equal = False
      i = i + 1.0
    
  else:
    equal = False

  return equal

def FillNumberArray(a, value):
  i = 0.0
  while i < len(a):
    a[int(i)] = value
    i = i + 1.0
  

def FillString(a, value):
  i = 0.0
  while i < len(a):
    a[int(i)] = value
    i = i + 1.0
  

def FillBooleanArray(a, value):
  i = 0.0
  while i < len(a):
    a[int(i)] = value
    i = i + 1.0
  

def FillNumberArrayInterval(a, value, fromx, to):
  if fromx >= 0.0 and fromx < len(a) and to >= 0.0 and to < len(a):
    i = fromx
    while i < to:
      a[int(i)] = value
      i = i + 1.0
    
    success = True
  else:
    success = False

  return success

def FillBooleanArrayInterval(a, value, fromx, to):
  if fromx >= 0.0 and fromx < len(a) and to >= 0.0 and to < len(a):
    i = max(fromx,0.0)
    while i < min(to,len(a)):
      a[int(i)] = value
      i = i + 1.0
    
    success = True
  else:
    success = False

  return success

def FillStringInterval(a, value, fromx, to):
  if fromx >= 0.0 and fromx < len(a) and to >= 0.0 and to < len(a):
    i = max(fromx,0.0)
    while i < min(to,len(a)):
      a[int(i)] = value
      i = i + 1.0
    
    success = True
  else:
    success = False

  return success

def CopyNumberArray(a):
  n =  [None]*int(len(a))

  i = 0.0
  while i < len(a):
    n[int(i)] = a[int(i)]
    i = i + 1.0
  

  return n

def CopyBooleanArray(a):
  n =  [None]*int(len(a))

  i = 0.0
  while i < len(a):
    n[int(i)] = a[int(i)]
    i = i + 1.0
  

  return n

def CopyString(a):
  n =  [None]*int(len(a))

  i = 0.0
  while i < len(a):
    n[int(i)] = a[int(i)]
    i = i + 1.0
  

  return n

def CopyNumberArrayRange(a, fromx, to, copyReference):
  if fromx >= 0.0 and fromx < len(a) and to >= 0.0 and to < len(a) and fromx <= to:
    length = to - fromx
    n =  [None]*int(length)
    i = 0.0
    while i < length:
      n[int(i)] = a[int(fromx + i)]
      i = i + 1.0
    
    copyReference.numberArray = n
    success = True
  else:
    success = False

  return success

def CopyBooleanArrayRange(a, fromx, to, copyReference):
  if fromx >= 0.0 and fromx < len(a) and to >= 0.0 and to < len(a) and fromx <= to:
    length = to - fromx
    n =  [None]*int(length)
    i = 0.0
    while i < length:
      n[int(i)] = a[int(fromx + i)]
      i = i + 1.0
    
    copyReference.booleanArray = n
    success = True
  else:
    success = False

  return success

def CopyStringRange(a, fromx, to, copyReference):
  if fromx >= 0.0 and fromx < len(a) and to >= 0.0 and to < len(a) and fromx <= to:
    length = to - fromx
    n =  [None]*int(length)
    i = 0.0
    while i < length:
      n[int(i)] = a[int(fromx + i)]
      i = i + 1.0
    
    copyReference.string = n
    success = True
  else:
    success = False

  return success

def IsLastElement(length, index):
  return index + 1.0 == length

def CreateNumberArray(length, value):
  array =  [None]*int(length)
  FillNumberArray(array, value)

  return array

def CreateBooleanArray(length, value):
  array =  [None]*int(length)
  FillBooleanArray(array, value)

  return array

def CreateString(length, value):
  array =  [None]*int(length)
  FillString(array, value)

  return array

def SubstringWithCheck(string, fromx, to, stringReference):
  if fromx < len(string) and to < len(string) and fromx <= to and fromx >= 0.0 and to >= 0.0:
    stringReference.string = Substring(string, fromx, to)
    success = True
  else:
    success = False

  return success

def Substring(string, fromx, to):
  n =  [None]*int(max(to - fromx,0.0))

  i = fromx
  while i < to:
    n[int(i - fromx)] = string[int(i)]
    i = i + 1.0
  

  return n

def AppendString(string, s):
  newString = ConcatenateString(string, s)

  string = None

  return newString

def ConcatenateString(string, s):
  newString =  [None]*int(len(string) + len(s))

  i = 0.0
  while i < len(string):
    newString[int(i)] = string[int(i)]
    i = i + 1.0
  

  i = 0.0
  while i < len(s):
    newString[int(len(string) + i)] = s[int(i)]
    i = i + 1.0
  

  return newString

def AppendCharacter(string, c):
  newString = ConcatenateCharacter(string, c)

  string = None

  return newString

def ConcatenateCharacter(string, c):
  newString =  [None]*int(len(string) + 1.0)

  i = 0.0
  while i < len(string):
    newString[int(i)] = string[int(i)]
    i = i + 1.0
  

  newString[int(len(string))] = c

  return newString

def SplitByCharacter(toSplit, splitBy):
  stringToSplitBy =  [None]*int(1.0)
  stringToSplitBy[int(0.0)] = splitBy

  split = SplitByString(toSplit, stringToSplitBy)

  stringToSplitBy = None

  return split

def IndexOfCharacter(string, character, indexReference):
  found = False
  i = 0.0
  while i < len(string) and  not found :
    if string[int(i)] == character:
      found = True
      indexReference.numberValue = i
    i = i + 1.0
  

  return found

def SubstringEqualsWithCheck(string, fromx, substring, equalsReference):
  if fromx < len(string):
    success = True
    equalsReference.booleanValue = SubstringEquals(string, fromx, substring)
  else:
    success = False

  return success

def SubstringEquals(string, fromx, substring):
  equal = True
  i = 0.0
  while i < len(substring) and equal:
    if string[int(fromx + i)] != substring[int(i)]:
      equal = False
    i = i + 1.0
  

  return equal

def IndexOfString(string, substring, indexReference):
  found = False
  i = 0.0
  while i < len(string) - len(substring) + 1.0 and  not found :
    if SubstringEquals(string, i, substring):
      found = True
      indexReference.numberValue = i
    i = i + 1.0
  

  return found

def ContainsCharacter(string, character):
  return IndexOfCharacter(string, character, NumberReference())

def ContainsString(string, substring):
  return IndexOfString(string, substring, NumberReference())

def ToUpperCase(string):
  i = 0.0
  while i < len(string):
    string[int(i)] = charToUpperCase(string[int(i)])
    i = i + 1.0
  

def ToLowerCase(string):
  i = 0.0
  while i < len(string):
    string[int(i)] = charToLowerCase(string[int(i)])
    i = i + 1.0
  

def EqualsIgnoreCase(a, b):
  if len(a) == len(b):
    equal = True
    i = 0.0
    while i < len(a) and equal:
      if charToLowerCase(a[int(i)]) != charToLowerCase(b[int(i)]):
        equal = False
      i = i + 1.0
    
  else:
    equal = False

  return equal

def ReplacesString(string, toReplace, replaceWith):
  equalsReference = BooleanReference()
  result =  [None]*int(0.0)

  i = 0.0
  while i < len(string):
    success = SubstringEqualsWithCheck(string, i, toReplace, equalsReference)
    if success:
      success = equalsReference.booleanValue
    if success and len(toReplace) > 0.0:
      result = ConcatenateString(result, replaceWith)
      i = i + len(toReplace)
    else:
      result = ConcatenateCharacter(result, string[int(i)])
      i = i + 1.0
  

  return result

def ReplaceCharacter(string, toReplace, replaceWith):
  result =  [None]*int(0.0)

  i = 0.0
  while i < len(string):
    if string[int(i)] == toReplace:
      result = ConcatenateCharacter(result, replaceWith)
    else:
      result = ConcatenateCharacter(result, string[int(i)])
    i = i + 1.0
  

  return result

def Trim(string):
  lastWhitespaceLocationStart =  -1.0
  firstNonWhitespaceFound = False
  i = 0.0
  while i < len(string) and  not firstNonWhitespaceFound :
    if charIsWhiteSpace(string[int(i)]):
      lastWhitespaceLocationStart = i
    else:
      firstNonWhitespaceFound = True
    i = i + 1.0
  

  # Find whitepaces at the end.
  lastWhitespaceLocationEnd = len(string)
  firstNonWhitespaceFound = False
  i = len(string) - 1.0
  while i >= 0.0 and  not firstNonWhitespaceFound :
    if charIsWhiteSpace(string[int(i)]):
      lastWhitespaceLocationEnd = i
    else:
      firstNonWhitespaceFound = True
    i = i - 1.0
  

  if lastWhitespaceLocationStart < lastWhitespaceLocationEnd:
    result = Substring(string, lastWhitespaceLocationStart + 1.0, lastWhitespaceLocationEnd)
  else:
    result =  [None]*int(0.0)

  return result

def StartsWith(string, start):
  startsWithString = False
  if len(string) >= len(start):
    startsWithString = SubstringEquals(string, 0.0, start)

  return startsWithString

def EndsWith(string, end):
  endsWithString = False
  if len(string) >= len(end):
    endsWithString = SubstringEquals(string, len(string) - len(end), end)

  return endsWithString

def SplitByString(toSplit, splitBy):
  split =  [None]*int(0.0)

  next =  [None]*int(0.0)
  i = 0.0
  while i < len(toSplit):
    c = toSplit[int(i)]
    if SubstringEquals(toSplit, i, splitBy):
      if len(split) != 0.0 or i != 0.0:
        n = StringReference()
        n.string = next
        split = AddString(split, n)
        next =  [None]*int(0.0)
        i = i + len(splitBy)
    else:
      next = AppendCharacter(next, c)
      i = i + 1.0
  

  if len(next) > 0.0:
    n = StringReference()
    n.string = next
    split = AddString(split, n)

  return split

def Negate(x):
  return  -x

def Positive(x):
  return  +x

def Factorial(x):
  f = 1.0

  i = 2.0
  while i <= x:
    f = f*i
    i = i + 1.0
  

  return f

def Round(x):
  return floor(x + 0.5)

def BankersRound(x):
  if Absolute(x - Truncate(x)) == 0.5:
    if  not DivisibleBy(Round(x), 2.0) :
      r = Round(x) - 1.0
    else:
      r = Round(x)
  else:
    r = Round(x)

  return r

def Ceil(x):
  return ceil(x)

def Floor(x):
  return floor(x)

def Truncate(x):
  if x >= 0.0:
    t = floor(x)
  else:
    t = ceil(x)

  return t

def Absolute(x):
  return fabs(x)

def Logarithm(x):
  return log10(x)

def NaturalLogarithm(x):
  return log(x)

def Sin(x):
  return sin(x)

def Cos(x):
  return cos(x)

def Tan(x):
  return tan(x)

def Asin(x):
  return asin(x)

def Acos(x):
  return acos(x)

def Atan(x):
  return atan(x)

def Atan2(y, x):
  a = 0.0

  if x > 0.0:
    a = Atan(y/x)
  elif x < 0.0 and y >= 0.0:
    a = Atan(y/x) + pi
  elif x < 0.0 and y < 0.0:
    a = Atan(y/x) - pi
  elif x == 0.0 and y > 0.0:
    a = pi/2.0
  elif x == 0.0 and y < 0.0:
    a =  -pi/2.0

  return a

def Squareroot(x):
  return sqrt(x)

def Exp(x):
  return exp(x)

def DivisibleBy(a, b):
  return ((a % b) == 0.0)

def Combinations(n, k):
  return Factorial(n)/(Factorial(n - k)*Factorial(k))

def EpsilonCompareApproximateDigits(a, b, digits):
  if a < 0.0 and b < 0.0 or a > 0.0 and b > 0.0:
    if a < 0.0 and b < 0.0:
      a =  -a
      b =  -b
    ad = log10(a)
    bd = log10(b)
    d = max(ad,bd)
    epsilon = 10.0**(d - digits)
    ret = fabs(a - b) > epsilon
  else:
    ret = False

  return ret

def EpsilonCompare(a, b, epsilon):
  return fabs(a - b) < epsilon

def GreatestCommonDivisor(a, b):
  while b != 0.0:
    t = b
    b = a % b
    a = t
  

  return a

def IsInteger(a):
  return (a - floor(a)) == 0.0

def GreatestCommonDivisorWithCheck(a, b, gcdReference):
  if IsInteger(a) and IsInteger(b):
    gcd = GreatestCommonDivisor(a, b)
    gcdReference.numberValue = gcd
    success = True
  else:
    success = False

  return success

def LeastCommonMultiple(a, b):
  if a > 0.0 and b > 0.0:
    lcm = fabs(a*b)/GreatestCommonDivisor(a, b)
  else:
    lcm = 0.0

  return lcm

def Sign(a):
  if a > 0.0:
    s = 1.0
  elif a < 0.0:
    s =  -1.0
  else:
    s = 0.0

  return s

def Max(a, b):
  return max(a,b)

def Min(a, b):
  return min(a,b)

def Power(a, b):
  return a**b

def AddNumber(list, a):
  newlist =  [None]*int(len(list) + 1.0)
  i = 0.0
  while i < len(list):
    newlist[int(i)] = list[int(i)]
    i = i + 1.0
  
  newlist[int(len(list))] = a
		
  list = None
		
  return newlist

def AddNumberRef(list, i):
  list.numberArray = AddNumber(list.numberArray, i)

def RemoveNumber(list, n):
  newlist =  [None]*int(len(list) - 1.0)

  i = 0.0
  while i < len(list):
    if i < n:
      newlist[int(i)] = list[int(i)]
    if i > n:
      newlist[int(i - 1.0)] = list[int(i)]
    i = i + 1.0
  
		
  list = None
		
  return newlist

def GetNumberRef(list, i):
  return list.numberArray[int(i)]

def RemoveNumberRef(list, i):
  list.numberArray = RemoveNumber(list.numberArray, i)

def AddString(list, a):
  newlist =  [None]*int(len(list) + 1.0)

  i = 0.0
  while i < len(list):
    newlist[int(i)] = list[int(i)]
    i = i + 1.0
  
  newlist[int(len(list))] = a
		
  list = None
		
  return newlist

def AddStringRef(list, i):
  list.stringArray = AddString(list.stringArray, i)

def RemoveString(list, n):
  newlist =  [None]*int(len(list) - 1.0)

  i = 0.0
  while i < len(list):
    if i < n:
      newlist[int(i)] = list[int(i)]
    if i > n:
      newlist[int(i - 1.0)] = list[int(i)]
    i = i + 1.0
  
		
  list = None
		
  return newlist

def GetStringRef(list, i):
  return list.stringArray[int(i)]

def RemoveStringRef(list, i):
  list.stringArray = RemoveString(list.stringArray, i)

def AddBoolean(list, a):
  newlist =  [None]*int(len(list) + 1.0)
  i = 0.0
  while i < len(list):
    newlist[int(i)] = list[int(i)]
    i = i + 1.0
  
  newlist[int(len(list))] = a
		
  list = None
		
  return newlist

def AddBooleanRef(list, i):
  list.booleanArray = AddBoolean(list.booleanArray, i)

def RemoveBoolean(list, n):
  newlist =  [None]*int(len(list) - 1.0)

  i = 0.0
  while i < len(list):
    if i < n:
      newlist[int(i)] = list[int(i)]
    if i > n:
      newlist[int(i - 1.0)] = list[int(i)]
    i = i + 1.0
  
		
  list = None
		
  return newlist

def GetBooleanRef(list, i):
  return list.booleanArray[int(i)]

def RemoveDecimalRef(list, i):
  list.booleanArray = RemoveBoolean(list.booleanArray, i)

def AddCharacter(list, a):
  newlist =  [None]*int(len(list) + 1.0)
  i = 0.0
  while i < len(list):
    newlist[int(i)] = list[int(i)]
    i = i + 1.0
  
  newlist[int(len(list))] = a
		
  list = None
		
  return newlist

def AddCharacterRef(list, i):
  list.string = AddCharacter(list.string, i)

def RemoveCharacter(list, n):
  newlist =  [None]*int(len(list) - 1.0)

  i = 0.0
  while i < len(list):
    if i < n:
      newlist[int(i)] = list[int(i)]
    if i > n:
      newlist[int(i - 1.0)] = list[int(i)]
    i = i + 1.0
  

  list = None

  return newlist

def GetCharacterRef(list, i):
  return list.string[int(i)]

def RemoveCharacterRef(list, i):
  list.string = RemoveCharacter(list.string, i)

def charToLowerCase(character):
  toReturn = character
  if character == 'A':
    toReturn = 'a'
  elif character == 'B':
    toReturn = 'b'
  elif character == 'C':
    toReturn = 'c'
  elif character == 'D':
    toReturn = 'd'
  elif character == 'E':
    toReturn = 'e'
  elif character == 'F':
    toReturn = 'f'
  elif character == 'G':
    toReturn = 'g'
  elif character == 'H':
    toReturn = 'h'
  elif character == 'I':
    toReturn = 'i'
  elif character == 'J':
    toReturn = 'j'
  elif character == 'K':
    toReturn = 'k'
  elif character == 'L':
    toReturn = 'l'
  elif character == 'M':
    toReturn = 'm'
  elif character == 'N':
    toReturn = 'n'
  elif character == 'O':
    toReturn = 'o'
  elif character == 'P':
    toReturn = 'p'
  elif character == 'Q':
    toReturn = 'q'
  elif character == 'R':
    toReturn = 'r'
  elif character == 'S':
    toReturn = 's'
  elif character == 'T':
    toReturn = 't'
  elif character == 'U':
    toReturn = 'u'
  elif character == 'V':
    toReturn = 'v'
  elif character == 'W':
    toReturn = 'w'
  elif character == 'X':
    toReturn = 'x'
  elif character == 'Y':
    toReturn = 'y'
  elif character == 'Z':
    toReturn = 'z'

  return toReturn

def charToUpperCase(character):
  toReturn = character
  if character == 'a':
    toReturn = 'A'
  elif character == 'b':
    toReturn = 'B'
  elif character == 'c':
    toReturn = 'C'
  elif character == 'd':
    toReturn = 'D'
  elif character == 'e':
    toReturn = 'E'
  elif character == 'f':
    toReturn = 'F'
  elif character == 'g':
    toReturn = 'G'
  elif character == 'h':
    toReturn = 'H'
  elif character == 'i':
    toReturn = 'I'
  elif character == 'j':
    toReturn = 'J'
  elif character == 'k':
    toReturn = 'K'
  elif character == 'l':
    toReturn = 'L'
  elif character == 'm':
    toReturn = 'M'
  elif character == 'n':
    toReturn = 'N'
  elif character == 'o':
    toReturn = 'O'
  elif character == 'p':
    toReturn = 'P'
  elif character == 'q':
    toReturn = 'Q'
  elif character == 'r':
    toReturn = 'R'
  elif character == 's':
    toReturn = 'S'
  elif character == 't':
    toReturn = 'T'
  elif character == 'u':
    toReturn = 'U'
  elif character == 'v':
    toReturn = 'V'
  elif character == 'w':
    toReturn = 'W'
  elif character == 'x':
    toReturn = 'X'
  elif character == 'y':
    toReturn = 'Y'
  elif character == 'z':
    toReturn = 'Z'

  return toReturn

def charIsUpperCase(character):
  isUpper = False
  if character == 'A':
    isUpper = True
  elif character == 'B':
    isUpper = True
  elif character == 'C':
    isUpper = True
  elif character == 'D':
    isUpper = True
  elif character == 'E':
    isUpper = True
  elif character == 'F':
    isUpper = True
  elif character == 'G':
    isUpper = True
  elif character == 'H':
    isUpper = True
  elif character == 'I':
    isUpper = True
  elif character == 'J':
    isUpper = True
  elif character == 'K':
    isUpper = True
  elif character == 'L':
    isUpper = True
  elif character == 'M':
    isUpper = True
  elif character == 'N':
    isUpper = True
  elif character == 'O':
    isUpper = True
  elif character == 'P':
    isUpper = True
  elif character == 'Q':
    isUpper = True
  elif character == 'R':
    isUpper = True
  elif character == 'S':
    isUpper = True
  elif character == 'T':
    isUpper = True
  elif character == 'U':
    isUpper = True
  elif character == 'V':
    isUpper = True
  elif character == 'W':
    isUpper = True
  elif character == 'X':
    isUpper = True
  elif character == 'Y':
    isUpper = True
  elif character == 'Z':
    isUpper = True

  return isUpper

def charIsLowerCase(character):
  isLower = False
  if character == 'a':
    isLower = True
  elif character == 'b':
    isLower = True
  elif character == 'c':
    isLower = True
  elif character == 'd':
    isLower = True
  elif character == 'e':
    isLower = True
  elif character == 'f':
    isLower = True
  elif character == 'g':
    isLower = True
  elif character == 'h':
    isLower = True
  elif character == 'i':
    isLower = True
  elif character == 'j':
    isLower = True
  elif character == 'k':
    isLower = True
  elif character == 'l':
    isLower = True
  elif character == 'm':
    isLower = True
  elif character == 'n':
    isLower = True
  elif character == 'o':
    isLower = True
  elif character == 'p':
    isLower = True
  elif character == 'q':
    isLower = True
  elif character == 'r':
    isLower = True
  elif character == 's':
    isLower = True
  elif character == 't':
    isLower = True
  elif character == 'u':
    isLower = True
  elif character == 'v':
    isLower = True
  elif character == 'w':
    isLower = True
  elif character == 'x':
    isLower = True
  elif character == 'y':
    isLower = True
  elif character == 'z':
    isLower = True

  return isLower

def charIsLetter(character):
  return charIsUpperCase(character) or charIsLowerCase(character)

def charIsNumber(character):
  isNumber = False
  if character == '0':
    isNumber = True
  elif character == '1':
    isNumber = True
  elif character == '2':
    isNumber = True
  elif character == '3':
    isNumber = True
  elif character == '4':
    isNumber = True
  elif character == '5':
    isNumber = True
  elif character == '6':
    isNumber = True
  elif character == '7':
    isNumber = True
  elif character == '8':
    isNumber = True
  elif character == '9':
    isNumber = True

  return isNumber

def charIsWhiteSpace(character):
  isWhiteSpace = False
  if character == ' ':
    isWhiteSpace = True
  elif character == '\t':
    isWhiteSpace = True
  elif character == '\n':
    isWhiteSpace = True
  elif character == '\r':
    isWhiteSpace = True

  return isWhiteSpace

def charIsSymbol(character):
  isSymbol = False
  if character == '!':
    isSymbol = True
  elif character == '\"':
    isSymbol = True
  elif character == '#':
    isSymbol = True
  elif character == '$':
    isSymbol = True
  elif character == '%':
    isSymbol = True
  elif character == '&':
    isSymbol = True
  elif character == '\'':
    isSymbol = True
  elif character == '(':
    isSymbol = True
  elif character == ')':
    isSymbol = True
  elif character == '*':
    isSymbol = True
  elif character == '+':
    isSymbol = True
  elif character == ',':
    isSymbol = True
  elif character == '-':
    isSymbol = True
  elif character == '.':
    isSymbol = True
  elif character == '/':
    isSymbol = True
  elif character == ':':
    isSymbol = True
  elif character == ';':
    isSymbol = True
  elif character == '<':
    isSymbol = True
  elif character == '=':
    isSymbol = True
  elif character == '>':
    isSymbol = True
  elif character == '?':
    isSymbol = True
  elif character == '@':
    isSymbol = True
  elif character == '[':
    isSymbol = True
  elif character == '\\':
    isSymbol = True
  elif character == ']':
    isSymbol = True
  elif character == '^':
    isSymbol = True
  elif character == '_':
    isSymbol = True
  elif character == '`':
    isSymbol = True
  elif character == '{':
    isSymbol = True
  elif character == '|':
    isSymbol = True
  elif character == '}':
    isSymbol = True
  elif character == '~':
    isSymbol = True

  return isSymbol


