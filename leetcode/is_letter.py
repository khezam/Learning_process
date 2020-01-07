# This function checks if character is a letter
def is_letter(char):
	if ord(char) >= 97 and ord(char) <= 122 or ord(char) >= 65 and ord(char) <= 90:
		return True
	return False

# 012m_o!!M2
# This fuction filters out the letter
def convert_string(str):
	i = 0
	new_str  = ""
	while i <= len(str) - 1:
		if is_letter(str[i]):
			new_str += str[i].lower()
		i += 1
	return new_str
	
# This function checks if the pramater is a palindrom
def check_palidrom(str):
	stringValue = convert_string(str)
	i = 0
	lenOfStringValue = len(stringValue) - 1
	while i < lenOfStringValue:
		if stringValue[i] != stringValue[lenOfStringValue]:
			return False
		i +=1
		lenOfStringValue -=1
	return True
print(check_palidrom("012m_o!!M2"))
