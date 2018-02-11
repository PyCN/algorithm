# hduyyg.py

解法：dp。

首先，dp方程为：

~~~ python
f[i] = max(f[i - 1], f[j - 1] + prices[i] - prices[j])
~~~

两种情况：

1. 第 i 天不处理：f[i - 1]
2. 第 i 天卖出，枚举一下买入的时间 j ： f[j - 1] + prices[i] - prices[j]

上诉方程复杂度是o(n^2)，现在做一下变形：

~~~ python
f[i] = max(f[i - 1], prices[i] + max(f[j - 1] - prices[j]))
~~~

那么，我们现在只需要在枚举 i 的过程中，动态维护一下max(f[ i - 1] - prices[i])，就可以达到o(n)的复杂度。