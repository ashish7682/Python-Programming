r"""

\'---->	Single Quote	
\\---->	Backslash	
\n---->	New Line	
\r---->	Carriage Return	
\t---->	Tab	
\b---->	Backspace	
\f---->	Form Feed	
\ooo---->Octal value	
\xhh---->Hex value
"""

#..........1...........

txt="It 's alright"
print(txt)

#..........2...........

txt="This will insert one \\ (backslash)."
print(txt)

#..........3...........

txt="Hello \nWorld"
print(txt)

#..........4............

txt = "Hello\rWorld!"
print(txt)#-------World!----------

#..........5............

txt="Hello\tWorld!"
print(txt)

#..........6............

#This example erases one character (backspace):
txt="Hello\bWorld!"
print(txt)