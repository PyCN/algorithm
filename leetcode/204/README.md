# hduyyg.py

解法：用一个prime数组记录小于 n 的所有素数。然后枚举prime中 <= sqrt(x) 的数，若其中不存在 x 的因数，则x为素数。