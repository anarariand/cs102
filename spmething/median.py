def get_median(array):
    array.sort()
    if len(array) % 2:
        return(array[len(array) // 2])
    else:
        return(array[len(array) // 2] / 2 + (array[len(array) // 2] - 1) / 2)
 
if __name__ == '__main__':
    print(get_median([6,9,4,3,2,-52]))
