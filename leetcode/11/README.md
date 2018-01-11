# hduyyg.py

解法：双指针。

初始时：

~~~py
L = 0

R = len(height) - 1

ans = min(height[L]，height[R]) * (R - L)
~~~

那么下一个比当前值更大的区间怎么获得呢？

假设height[L]更小，那么指针 L 就向右移动到第一个 `height[newL] > height[L]`的地方，此时区间`[newL,R]`就是下一个有可能的区间。

其他情况以此类推。