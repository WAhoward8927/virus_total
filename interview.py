from typing import List


def Solution(A: List[int]):
    maxbeans = 0
    beans = [len(A) + 1]
    ibean = 0
    counter = 0

    if len(A) > 0:
        for i in range(len(A)):
            counter = 1
            head = i
            tail = A[i]
            if head is not tail:
                if head not in beans or head == 0:
                    ibean += 1
                    beans[ibean] = head
                    beans[ibean] = tail
                    while head is not tail:
                        tail = A[tail]
                        beans[ibean+1] = tail
                        counter += 1
            if counter > maxbeans:
                maxbeans = counter
    return maxbeans


if __name__ == '__main__':
    print(Solution([5, 4, 0, 3, 1, 6, 2]))

