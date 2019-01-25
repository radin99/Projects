from HashMap import Hashmap as HshMap



tst = HshMap()

tst.Put(2,1)
tst.Put(43,2)
tst.Put(84,3)

print(tst.EntrySet())
print(tst.store[2].next.next.key)

print(tst.RemoveItem(84))
print(tst.store[2].next.key)
print(tst.Get(84))










