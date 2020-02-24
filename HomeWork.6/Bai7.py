import string

def remove_dollar_sign(s):
    newstr = s.replace("$","")
    return newstr

print(remove_dollar_sign(" Huyen$ Kahnh$"))

str = remove_dollar_sign("Huyen $$$$$$Khsngfdsjgr")
print(str)