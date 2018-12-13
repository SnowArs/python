##___Крылов А.В.____
##
### Задание-1:
### Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
### Первыми элементами ряда считать цифры 1 1

##def fibonacci(n, m):
##    a = b = 1
##    fib = [a, b]
##    if m > 2:
##        i = 2    
##        while i < m:
##            fib.append(a+b)
##            c = b 
##            b = a + b
##            a = c
##            i +=1
##    return(fib[(n):(m+1)])
##
##print(fibonacci(5, 10))

### Задача-2:
### Напишите функцию, сортирующую принимаемый список по возрастанию.
### Для сортировки используйте любой алгоритм (например пузырьковый).
### Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
##
##
##def sort_to_max(origin_list):
##    origin_list1 = []
##    new_order_list = []
##    for f in origin_list:
##        origin_list1.append(f)
##    for f in origin_list:
##        min = origin_list1[0]
##        for i in origin_list1:
##            if min >= i:
##               min = i
##        new_order_list.append(min)
##
##        origin_list1.pop(origin_list1.index(min))
##    print(new_order_list)
##
##sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
##
##
### Задача-3:
### Напишите собственную реализацию стандартной функции filter.
### Разумеется, внутри нельзя использовать саму функцию filter.
##
##def my_filter(mixed_list, filter_word):
##    filtered_list = []
##    for f in mixed_list:
##        if f == filter_word:
##            filtered_list.append(f)
##    return filtered_list
##
##print(my_filter(['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак'], "просо"))
##

##
### Задача-4:
### Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
### Определить, будут ли они вершинами параллелограмма.
##
##
##def vertex_parallelogram(a, b, c, d):
##    Xo = (a[0] + c[0]) / 2  # находим координаты середины 
##    Yo = (a[1] + c[1]) / 2 
##    if (2 * Xo - b[0]) == d[0] and (2 * Yo - b[1]) == d[1]:
##        print ("точки - вершины параллелограмма") 
##    else:
##        print ("точки - какие-то странные ") 
##
##vertex_parallelogram([-3, 11], [12, -4], [1, -7], [-14, 8])
##
##


