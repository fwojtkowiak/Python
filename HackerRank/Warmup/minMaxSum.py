def miniMaxSum(arr):
    a=[sum(arr[x] for x in range(len(arr)) if x!=i) for i in range(5)]
    print(min(a),max(a))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
