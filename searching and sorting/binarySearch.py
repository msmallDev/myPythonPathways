def binary_search(arr, target):
    size = len(arr) - 1
    start = 0
    end = size - 1

    while(start <= end):
        mid = (start + end)// 2

        if (arr[mid] == target):
            return mid # found target
        elif (arr[mid] > target):
            end = mid - 1
        elif (arr[mid] < target):
            start = mid + 1

    return -1



sorted_list = [10, 23, 35, 45, 50, 70, 85]
target = 10

result = binary_search(sorted_list, target)

print(result)