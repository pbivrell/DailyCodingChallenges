# Time: O(n^2)
# Space O(n)
def soln1(array):
    result = [1] * len(array)
    for i,e in enumerate(array):
        for n in range(len(array)):
            if i != n:
                result[n] *= e
    return result

# Credit: https://www.geeksforgeeks.org/a-product-array-puzzle/
# Time: O(n)
# Space: O(n)
def answer(array):
    result = [1] * len(array)
    temp = 1
    # Product of stuff to left of i
    for i,e in enumerate(array):
        result[i] *= temp
        temp *= e
    temp = 1
    # Product of stuff to right of i
    for i, e in reversed(list(enumerate((array)))):
        result[i] *= temp
        temp *= e
    return result

def main():
    tests = { 
        'provided1' : ([1,2,3,4,5], [120,60,40, 30, 24]),
        'provided2' :([3,2,1], [2,3,6]),
        'test1-empty' : ([],[]),
        'test2-one-element' : ([1],[1]),
        'test3-zero' : ([0,1,2,3],[6,0,0,0])
    }
    test(tests, soln1)
    test(tests, answer)

def test(tests, func):
    print("Testing Function [{}]".format(func.__name__))
    for k,v in tests.items():
        res = func(v[0])
        print("Passed" if res == v[1] else "Failed", end=" ")
        print("Test [{}]: Expected {} Recieved {}".format(k, v[1], res))

if __name__ == "__main__":
    main()
