import random

# Define the dimensions of the array
rows, cols = 50, 20

# Create a 3x4 array filled with random integers between 1 and 100
products = [[random.randint(1, 500) for _ in range(cols)] for _ in range(rows)]
PRODUCT_LOW = 100

def Product_Quat(storage_unit):
    for i in range(0, len(storage_unit)):
        print(f'{products[i][storage_unit]}')
def low_stock():
    for i in range(0, len(products)):
        for j in range(0, len(products[i])):
            if products[i][j] <= PRODUCT_LOW:
                print(f'Product at ({i}, {j}): {products[i][j]} is low.')
                
def max_stroage():
    for i in range(0, len(products)):
        max_stroage = 0
        for j in range(0, len(products[i])):
            if products[i][j] >= max_stroage:
                max_stroage = products[i][j]
        print(f"the maximum number of product {products} {i} is {max_stroage}")
            
            
def averge_stock():
    total = 0
    for i in range(0, len(products)):
        total = 0
        for j in range(0, len(products[i])):
            total += products[i][j]
        print(f"the total number of product [i] is {total}")
        
    
def move_stock():
    source_row = int(input("Enter the source row:"))
    source_col = int(input("Enter the source column:"))
    destination_row = int(input("Enter the destination row:"))
    destination_col = int(input("Enter the destination column:"))
    quanity = int(input("Enter quanity to move"))
    products[source_row][source_col] =  (products[source_row][source_col] - quanity)
    products[destination_row][destination_col] =  (products[destination_row][destination_col] + quanity)

def main():
    storage_unit = input("Enter the storage unit to see product quantilities:")
    Product_Quat(storage_unit)
    low_stock()
    max_stroage()

if __name__ == '__main__':
    main()


