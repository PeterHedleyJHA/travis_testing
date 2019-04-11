def get_no_presents_from_true_love(target_n,n=1,pt1=0,pt2=0):
    if target_n==n:
        return n+2*pt1+pt2
    return get_no_presents_from_true_love(target_n,n+1,pt1+n,pt1+pt2)


def bubble_sort(array):
    start = 0
    finished=False
    while(finished==False):
        finished = True
        for index in range(len(array)-1):
            if(array[index] < array[index+1]):
                temp = array[index]
                array[index] = array[index+1]
                array[index+1] = temp
                finished = False
    return array

if __name__ == "__main__":
    ans = []
    for i in range(20):
        ans.append(get_no_presents_from_true_love(i+1))
    print(ans)

    print(bubble_sort([3,4,5]))
    print(bubble_sort([3,4,5,2,3,3,4,4,3,35,3,4,9,10,11,2,3,2,43]))
