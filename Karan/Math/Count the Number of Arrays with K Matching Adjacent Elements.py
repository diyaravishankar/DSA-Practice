MOD=10**9+7
class Solution:
 def countGoodArrays(self,n,m,k):
  fact=[1]*(n)
  invfact=[1]*(n)
  for i in range(1,n):
   fact[i]=fact[i-1]*i%MOD
  invfact[-1]=pow(fact[-1],MOD-2,MOD)
  for i in range(n-2,-1,-1):
   invfact[i]=invfact[i+1]*(i+1)%MOD
  def comb(a,b):
   if b<0 or b>a:return 0
   return fact[a]*invfact[b]%MOD*invfact[a-b]%MOD
  return comb(n-1,k)*m*pow(m-1,n-1-k,MOD)%MOD