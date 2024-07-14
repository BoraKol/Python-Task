def flattenList(xss):
    result = []
    for xs in xss:
        if isinstance(xs, list):
            result.extend(flattenList(xs))
        else:
            result.append(xs)
    return result

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print("Çözüm yapılması istenen 1.sorudaki list:" , input_list)
print("1.Sorunun Çözümü:" , flattenList(input_list))

def reverse(lst):
    reversed_lst = lst[::-1]

    for i in range(len(reversed_lst)):
        if isinstance(reversed_lst[i], list):
            reversed_lst[i] = reverse(reversed_lst[i])

    return reversed_lst

inputList = [[1, 2], [3, 4], [5, 6, 7]]
print("Çözüm yapılması istenen 2.sorudaki list:" , inputList)
reversed_lst = reverse(inputList)
print("2.Sorunun Çözümü:",reversed_lst)
