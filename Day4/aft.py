# #regular expressions
import re
# text="python is powerful"
# result=re.match("python",text)
# if result:
#     print("Match found:",result.group())
# result1=re.search("powerful",text)
# if result1:
#     print("Match found:",result1.group())


# text="my number is 1234567890 and 9876543210"
# number=re.findall("\d{10}",text)
# print(number)

# for match in re.finditer("\d{10}",text):
#     print("Match found at index:",match.start(),"to",match.end())

text="my phone number is 1234567890"
masked=re.sub(R'\d','*',text)
print(masked)


#log file(security monitoring,VM log scanning,window server event log parsing)
#username password validator(8 u l digit spcl character using regex)

