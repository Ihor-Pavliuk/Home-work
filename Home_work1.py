# Декілька способів, можно ще модулі підв'язати, але це буде окремий файл
print ('Hello world')
text_1 = 'Hello world' 
text_2 = 'again'
print (text_1, text_2, sep=',', end='!\n')
print ('{0},{1}' .format(text_1, text_2), end='!\n')
print (f"{text_1}, {text_2}!\n\n")

s = '#' # це не правильно написаний код, тому що сторонній особі нічого не зрозуміло, просто було цікаво чи можно це зробити в одній строці 
print (f"{s}{s}{s}{s}{s}{s}{s}{s}{s}\n{s}\t{s}\n{s}\t{s}\n{s}\t{s}\n{s}{s}{s}{s}{s}{s}{s}{s}{s}\n\n{s}\t{s}\n{s}\t{s}\n{s}{s}{s}{s}{s}{s}{s}{s}{s}\n{s}\t{s}\n{s}\t{s}\n")
# ось домашка
print (f"{s}{s}{s}{s}{s}{s}{s}{s}{s}\n{s}\t{s}\n{s}\t{s}\n{s}\t{s}\n{s}{s}{s}{s}{s}{s}{s}{s}{s}\n")
print (f"{s}\t{s}\n{s}\t{s}\n{s}{s}{s}{s}{s}{s}{s}{s}{s}\n{s}\t{s}\n{s}\t{s}\n")
# перше виконання моє, цього завдання:
print('#','#','#','#','#','#','#','#','#', end='\n') 
print('#','#', sep='\t\t', end='\n')
print('#','#', sep='\t\t', end='\n')
print('#','#', sep='\t\t', end='\n')
print('#','#','#','#','#','#','#','#','#', end='\n\n\n')
print('#','#', sep='\t\t', end='\n')
print('#','#', sep='\t\t', end='\n')
print('#','#','#','#','#','#','#','#','#', end='\n')
print('#','#', sep='\t\t', end='\n')
print('#','#', sep='\t\t', end='\n')