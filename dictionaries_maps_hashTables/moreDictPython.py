#come back to this, needs more explanation
'''
import collections
d = collections.OrderedDict(one=1, two=2, three=3)

print(d)

d["onehundred"] = 100
print(d)

print(d.keys())
'''
##############

from collections import defaultdict
dd = defaultdict(list)

# so we just accessed a missing key called list so it created the missing key
#initialized missing key using default factory

dd["dogs"].append("Rufus")
dd["dogs"].append("Kathrin")
dd["dogs"].append("Mr Sniffles")

print(dd["dogs"])
