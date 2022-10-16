# -*- coding: utf-8 -*-

print ()

# strings
# "..." or '...'
# ordered and indexable (by number)
# immutable
strg = "amy bob cathy dan erica"
print (strg, len(strg), strg[4])
#strg[4] = 'B'

print ()

# lists
# [...]
# ordered and indexable (by number)
# mutable
lst = ['amy', 'bob', 'cathy', 'dan', 'erica']
print (lst, len(lst), lst[4])
lst[1] = 'Bob'
print (lst)
lst.append('fey')
print (lst)
del lst[1]
print (lst)

print ()

# tuples
# (...)
# ordered and indexable (by number)
# immutable
tup = ('amy', 'bob', 'cathy', 'dan', 'erica')
print (tup, len(tup), tup[4])
#tup[2] = 'Bob'

print ()

# ranges 
# range(start, end, step)
# ordered and indexable (by number)
rng = range(0, 10, 2)
print (rng, list(rng), len(rng), rng[4])

print ()

# sets
# {...}
# unordered and not indexable
# mutable
# deduped
st = {'amy', 'bob', 'bob', 'cathy', 'dan', 'erica'}
print (st, len(st))
#print (st[4])
st.add('fey')
print (st)
st.remove('bob')
print (st)

print ()

# dictionaries
# {k:v}
# unordered and indexable (by key)
# key unique and immutable, value mutable
dd = {'amy':10, 'bob':30, 'cathy':40, 'dan':50, 'erica':60}
print (dd, len(dd), dd['dan'])
dd['bob'] = 3
print (dd)
dd['fey'] = 60
print (dd)
del dd['amy']
print (dd)
