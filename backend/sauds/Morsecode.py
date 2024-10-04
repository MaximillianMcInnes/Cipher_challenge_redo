from clipboard import copy
cipher="""-.-- --- ..- / - .... --- ..- --. .... - / - .... .. ... / .-- --- ..- .-.. -.. / -... . / .- / .... .. -. - ..--.. / ... --- .-. .-. -.-- / ..-. --- .-. / .- .-.. .-.. / -.-. .- .--. ..."""
cipher=cipher.replace("\n","")
if cipher=="":
	exit("I think you forgot to put in the morse code...")
cipher = cipher.replace("·",".")
cipher = cipher.replace("_","-")
text=[]
cipher_list = cipher.split(" ")
for i in range(len(cipher_list)):
	match cipher_list[i]:
		case ".-":
			text.append("A")
		case "-...":
			text.append("B")
		case "-.-.":
			text.append("C")
		case "-..":
			text.append("D")
		case ".":
			text.append("E")
		case "..-.":
			text.append("F")
		case "--.":
			text.append("G")
		case "....":
			text.append("H")
		case "..":
			text.append("I")
		case ".---":
			text.append("J")
		case "-.-":
			text.append("K")
		case ".-..":
			text.append("L")
		case "--":
			text.append("M")
		case "-.":
			text.append("N")
		case "---":
			text.append("O")
		case ".--.":
			text.append("P")
		case "--.-":
			text.append("Q")
		case ".-.":
			text.append("R")
		case "...":
			text.append("S")
		case "-":
			text.append("T")
		case "..-":
			text.append("U")
		case "...-":
			text.append("V")
		case ".--":
			text.append("W")
		case "-..-":
			text.append("X")
		case "-.--":
			text.append("Y")
		case "--..":
			text.append("Z")
		case "-----":
			text.append("0")
		case ".----":
			text.append("1")
		case "..---":
			text.append("2")
		case "...--":
			text.append("3")
		case "....-":
			text.append("4")
		case ".....":
			text.append("5")
		case "-....":
			text.append("6")
		case "--...":
			text.append("7")
		case "---..":
			text.append("8")
		case "----.":
			text.append("9")
		case ".-.-.-":
			text.append(".")
		case "--..--":
			text.append(",")
		case "/":
			text.append(" ")
#		case other:
#			text.append("ERROR")
text = "".join(text)
if len(input(f"\033[H\033[JText:\n\n{text}\n\nDo you want this to be copied to your clipboard? enter anything for yes\n\n"))>0:
	copy(text)