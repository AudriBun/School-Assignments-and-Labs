class arr(object):
    def __init__(self, i_size): # Constructor
        self._a = [None]*i_size
        self.item_count = 0
        self.is_sorted = False # Check if array is sorted

    def insert(self, data, index): # Insert at specified index
        try:
            self._a[index] = data
            self.item_count += 1
            if self.is_sorted == True:
                self.is_sorted = False
        except:
            print("insertion error")

    def delete(self, index): # Delete at specified index
        self._a[index] = 0
        self.item_count -= 1
        if self.is_sorted == True:
            self.is_sorted = False

    def sort(self): # Sort array
        self._a.sort()
        self.is_sorted = True

    def print_contents(self): # Print contents
        print("-----")
        for i in self._a:
            print(i)
    
menu = True

arr_size = input("Declare array size: ")
arr_size = int(arr_size)
temp_arr = arr(arr_size)

while menu == True:
    
    print("-----")
    print("insert")
    print("delete")
    print("sort")
    print("display")
    print("exit")
    print("-----")
    choice = input("Select Option: ")

    if choice == "insert":
        print("-----")
        item = input("input data: ")
        item = int(item)
        print("-----")
        index = input("input index: ")
        index = int(index)
        print("-----")
        temp_arr.insert(item, index)
    elif choice == "delete":
        print("-----")
        index = input("input index: ")
        index = int(index)
        print("-----")
        temp_arr.delete(index)
    elif choice == "sort":
        try:
            temp_arr.sort()
            print("-----")
            print("array sorted")
        except:
            print("sorting error")
        print("-----")
    elif choice == "display":
        temp_arr.print_contents()
    elif choice == "exit":
        menu = False
        break
    else:
        print("invalid selection")



    

