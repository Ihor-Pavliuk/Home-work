# Декілька способів, можно ще модулі підв'язати, але це буде окремий файл
#Hello world, again!
print ('Hello world, again!')
#Hello world, again!
text_1 = 'Hello world' 
text_2 = 'again'
print (text_1, text_2, sep=', ', end='!\n')
#Hello world, again!
print ('{0}, {1}' .format(text_1, text_2), end='!\n')
#Hello world, again!
print (f"{text_1}, {text_2}!\n\n")


print ("""#########\n#\t#\n#\t#\n#\t#\n#########\n""")
print ("""#\t#\n#\t#\n#########\n#\t#\n#\t#\n""")
#або так
print ("""#########
#\t#
#\t#
#\t#
#########\n""")
print ('''#\t#
#\t#
#########
#\t#
#\t#''')