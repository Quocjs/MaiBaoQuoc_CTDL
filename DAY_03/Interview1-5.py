#Interview 1: Viết thuật toán hàm reverse 1 list cho trước.
def reverse_fc(a):
    c = int(len(a)) #lấy kích thước của chuỗi a
    list1 = list([0] * c) # tạo ra một chuỗi mới bằng kích thước của chuỗi a
    for i in range(c):
        list1[i] = a[c-i-1] # gán phần tử của list1 tương ứng cho các giá trị từ cuối -> đầu của a
    return list1 # trả về chuỗi đã được reversed

mang = [1, 2, 3, 4]
print(reverse_fc(mang))



#Interview 2: Viết thuật toán kiểm tra chữ đầu và chữ cuối của 
def is_palindrome(string):
  """Kiểm tra xem một chuỗi có phải là palindrome hay không.

  Args:
    string: Chuỗi cần kiểm tra.

  Returns:
    True nếu chuỗi là palindrome, False nếu không.
  """

  # Chuẩn hóa chuỗi bằng cách chuyển tất cả các ký tự sang chữ thường và loại bỏ các khoảng trắng.
  normalized_string = string.lower().strip()

  # Kiểm tra xem chuỗi có bằng với chuỗi đảo ngược của nó hay không.
  return normalized_string == normalized_string[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False



# #Interview 3: Viết thuật toán đảo số
# # ý tưởng cho cách viết là ép số -> string -> đảo string -> ép lại về số
def DaoSo(so):
    b = str(so)
    c = "".join(reversed(b))
    return int(c)

a = 1234
print(DaoSo(a))

# Interview 4: Viết thuật toán 
#kiểm tra các kí tự bên trong chuỗi có giống nhau hay không
def is_anagram(str1, str2):
  #Kiểm tra độ dài hai chuỗi có giống nhau không
  if len(str1) != len(str2):
    return False

  count = {}

  for char in str1:
    count[char] = count.get(char, 0) + 1

  for char in str2:
    if char not in count or count[char] <= 0:
      return False
    count[char] -= 1

  return True
a = "deal"
b = "laed"
print(is_anagram(a, b))

#Interview 5: Viết thuật toán 
def find_duplicates(array):
  """Tìm kiếm các phần tử trùng lặp trong một mảng một chiều các số nguyên trong thời gian chạy O(N), nơi các giá trị số nguyên nhỏ hơn độ dài của mảng.

  Args:
    array: Mảng cần tìm kiếm các phần tử trùng lặp.

  Returns:
    Một danh sách chứa các phần tử trùng lặp trong mảng.
  """
def duplicates(arr, n):

	# Tăng các phần tử của mảng lên 1
	for i in range(n):
		arr[i] = arr[i] + 1
		
	# trả về mảng
	res = []
	
	# Biến đếm số lượng
	# Phần tử lớn nhất
	count = 0
	for i in range(n):
	
		# Tìm giá trị trị số
		if(abs(arr[i]) > n):
			index = abs(arr[i])//(n+1)
		else:
			index = abs(arr[i])
			
		# Kiểm tra xem chỉ số có bằng giá trị phần tử lớn nhất không
		if(index == n):
			count += 1
			continue
			
		# Lấy giá trị phần tử tại chỉ mục
		val = arr[index]
		
		# Kiểm tra xem giá trị phần tử là âm, dương
    # hoặc lớn hơn n
		if(val < 0):
			res.append(index-1)
			arr[index] = abs(arr[index]) * (n + 1)
		elif(val>n):
			continue
		else:
			arr[index] = -arr[index]
			
	# Nếu phần tử lớn nhất xuất hiện nhiều lần
	if(count > 1):
		res.append(n - 1)
	if(len(res) == 0):
		res.append(-1)
	else:
		res.sort()
	return res

numRay = [ 1, 2, 3, 1, 5 ]
n = len(numRay)
ans = duplicates(numRay,n)
print(ans)

