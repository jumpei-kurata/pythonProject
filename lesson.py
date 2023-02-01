num = 1
name = 'Mike'
no = '1'

print(num)
print(type(num))

print(type(no))
no = int(no)
print(no)
print(type(no))

print('Hi', 'Mike')
print('Hi\nMike')
print(r'C:\name\name')
print('Hi' * 4 + 'Mike')

word = 'python'
print(word[0])
print(word[-1])
print(word[0:3])
print(word[3:])
# word[0] = 'j' + word[1:]
word = 'j' + word[1:]
print(word)
print(len(word))

s = 'a is {}'.format('jumpei')
print(s)
# python3.6よりformatではなく、f-stringsが使えるようになった。こっちのが処理早いっぽいので、これを使うとよいかも。
name1 = 'jumpei'
family = 'kurata'
print(f'My name is {name1} {family}')

l = [1, 20, 342, 34, 5]
print(l)
print(type(l))
a = ['a', 'b', 'c']
ll = [l, a]
print(ll)
print(ll[0][1])
x = [1, 3, 35, 35214351, 1]
y = [8, 8, 777, 9]
print(x.extend(y))

# 整数とかは値渡しだけど、listとかは参照渡し（アドレスを渡す）

t = (1, 2, 3, 4, 5, 6, 7)
print(type(t))

# タプルには付け加えたりできない→使いどころは書き換えてはいけないものをタプルにいれる。

d = {'x': 10, 'y': 20}
print(type(d))
print(d)
print(d.keys())
print(d.values())
# 辞書型はmapみたいなもん、keyがわかれば、valueを検索できる。また、リストとかより辞書の方が、検索が早い。

# 集合型
aa = {1, 2, 4, 5, 6, 6, 7, 8, 9, 10}
print(aa)
print(type(aa))
print(aa.add(134))
# help(set)

x = 10
if x > 0:
    print('zero')
elif x == 0:
    print('000000000000000')
else:
    print('else')

if x in y:
    print('in')

if 100 not in y:
    print('not in')

is_ok = True

if not is_ok:
    print('hello')
else:
    print('False')

is_empty = None
print(type(is_empty))

if is_empty is not None:
    print('None!!')

count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1
else:
    print('done')

count1 = 0
while count1 <= 5:
    print(count1)
    count1 += 1
else:
    print('done')


# while True:
#     worddd = input('Enter:')
#     num = int(worddd)
#     if num == 100:
#         break
#     print('next')

for s in 'abcde':
    print(s)

for i in range(2, 15, 2):
    print(i)

for _ in range(5):
    print('hello')

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)


d = {'x': 100, 'y':200}
print(d.items())
for k, v in d.items():
    print(k, ':', v)


def say_something():
    print('hi')
say_something()
print(type(say_something))
f = say_something
f()
print(f)

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

menu(entree='beef', dessert='ice', drink='beer')