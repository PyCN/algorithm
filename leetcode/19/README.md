# hduyyg.py

解法：深搜。

def dfs(head, n):

1.  如果返回值不是数字，那么代表需要被删除的就是head.next，此时的返回值是head.next.next，直接head.next=res即可实现删除。

2.  如果返回值是数字，那么就代表head之后的数字总数，如果res + 1 == n，那么代表当前head是需要被删除的，此时返回head.next，如果不是，则返回 res + 1。

    需要特殊处理的是，在情况 1 中，由于已经找答案，此时返回一个不会再得到解的数字——n 即可。

