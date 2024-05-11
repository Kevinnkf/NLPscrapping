String_v1 = "I am exploring NLP"

#extract a particular char 
print(String_v1[0])

#extract "exploring" using range in string
print(String_v1[5:14])

#replace exploring with learning
String_v2 = String_v1.replace("exploring", "learning")
print(String_v2)

#concat two string
s1 = "nlp"
s2 = "machine learning"
s3 = s1 + s2

print (s3)

#searching for a substring in a string