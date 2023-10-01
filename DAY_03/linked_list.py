'''
Đoạn mã này định nghĩa một lớp Node đại diện cho một nút trong danh sách liên kết. Lớp Node có hai thuộc tính:
data: Dữ liệu được lưu trữ trong nút.
nextNode: Con trỏ đến nút tiếp theo trong danh sách liên kết.
Phương thức init() của lớp Node được sử dụng để khởi tạo một nút mới. 
Phương thức này nhận vào một giá trị dữ liệu và gán giá trị đó cho thuộc tính data của nút.
'''
class Node:
    def __init__(self) :
        self.data = data 
        self.nextNode = None

'''
Đoạn mã này định nghĩa một lớp LinkedList đại diện cho một danh sách liên kết. Lớp LinkedList có hai thuộc tính:
head: Con trỏ đến nút đầu tiên trong danh sách liên kết.
numOfNodes: Số lượng nút trong danh sách liên kết.
Phương thức init() của lớp LinkedList được sử dụng để khởi tạo một danh sách liên kết mới. 
Phương thức này gán giá trị None cho thuộc tính head và giá trị 0 cho thuộc tính numOfNodes.
'''
class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0



    def insert_start(self, data):  #khai báo phương thức insert_start(). Phương thức này nhận vào một giá trị dữ liệu và trả về None
        self.numOfNodes = self.NumofNodes + 1 #tăng số lượng nút trong danh sách liên kết lên 1
        new_node = Node(data)  #tạo một nút mới với dữ liệu được truyền vào
        
        if not self.head: #Nếu danh sách liên kết trống, thì dòng code này gán nút mới cho thuộc tính head của danh sách liên kết
            self.head = new_node
        else: #Nếu danh sách liên kết không trống, thì dòng code này gán nút mới cho thuộc tính nextNode 
            #của nút head hiện tại và cập nhật nút head của danh sách liên kết thành nút mới.
            new_node.nextNode = self.head
            self.head = new_node


    def insert_end(self, data): #khai báo phương thức insert_end(). Phương thức này nhận vào một giá trị dữ liệu và trả về None
        self.numOfNodes = self.numOfNodes+1 #tăng số lượng nút trong danh sách liên kết lên 1
        new_node = Node(data) #tạo một nút mới với dữ liệu được truyền vào

        actual_node = self.head #gán nút đầu tiên của danh sách liên kết cho biến actual_node
        while actual_node.nextNode is not None: #duyệt qua danh sách liên kết cho đến khi tìm thấy nút cuối cùng. Nút cuối cùng là nút có thuộc tính nextNode bằng None
            actual_node = actual_node.nextNode
        actual_node.nextNode = new_node