def get_no_presents_from_true_love(target_n,n=1,pt1=0,pt2=0):
    if target_n==n:
        return n+2*pt1+pt2
    return get_no_presents_from_true_love(target_n,n+1,pt1+n,pt1+pt2)


if __name__ == "__main__":
    ans = []
    for i in range(20):
        ans.append(get_no_presents_from_true_love(i+1))

    print(ans)
