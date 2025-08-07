letter = '''  Dear <|Name|>, 
You are selected! 
<|Date|> '''
#chaining
print(letter.replace("<|Name|>","Isha").replace("<|Date|" , "2024-03-10"))