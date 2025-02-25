from collections import defaultdict, OrderedDict
class AllOne:
 def __init__(self):
  self.key_count={}
  self.count_keys=defaultdict(OrderedDict)
  self.min_count=float('inf')
  self.max_count=0
 def inc(self,key):
  count=self.key_count.get(key,0)
  self.key_count[key]=count+1
  if count in self.count_keys and key in self.count_keys[count]:
   del self.count_keys[count][key]
   if not self.count_keys[count]:
    del self.count_keys[count]
  self.count_keys[count+1][key]=None
  self.max_count=max(self.max_count,count+1)
  if self.min_count==count and count not in self.count_keys:
   self.min_count=count+1
  else:
   self.min_count=min(self.min_count,count+1)
 def dec(self,key):
  if key not in self.key_count:
   return
  count=self.key_count[key]
  if count==1:
   del self.key_count[key]
   if key in self.count_keys[1]:
    del self.count_keys[1][key]
    if not self.count_keys[1]:
     del self.count_keys[1]
   self.min_count=min(self.key_count.values(),default=float('inf'))
  else:
   self.key_count[key]=count-1
   if key in self.count_keys[count]:
    del self.count_keys[count][key]
    if not self.count_keys[count]:
     del self.count_keys[count]
   self.count_keys[count-1][key]=None
   self.min_count=min(self.min_count,count-1)
  if count==self.max_count and count not in self.count_keys:
   self.max_count=max(self.count_keys.keys(),default=0)
 def getMaxKey(self):
  return next(iter(self.count_keys[self.max_count]),"")
 def getMinKey(self):
  return next(iter(self.count_keys[self.min_count]),"")