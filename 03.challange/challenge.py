# number = input("Please input a positive integer: ")

# product_of_numbers = 1
# sum_of_numbers = 0
# num_list = []
# reversed_num = ""
# even = 0
# odd = 0


# for num in number:
# 	sum_of_numbers += int(num)
# 	product_of_numbers *= int(num)
# 	num_list.append(int(num))
# 	reversed_num = num + reversed_num
# 	if int(num) % 2 == 0 :
# 		even+=1
# 	else:
# 		odd+=1
	

	
	

# print("Sum of digits: ",sum_of_numbers)
# print("Product of digits: ",product_of_numbers)
# print("Reverse: ", int(reversed_num))
# print("Palindrome",True if number == reversed_num else False)
# print("Largest Digit: ",max(num_list))
# print("Smallest Digit: ",min(num_list))
# print("Even Digits: ",even)
# print("Odd Digits: ",odd)


num = 255
sum_of_num = 0

while num > 0:
    sum_of_num += num%10

    num //= 10
print(sum_of_num)
