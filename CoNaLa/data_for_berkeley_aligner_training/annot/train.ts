sum(d * 10 ** i for i, d in enumerate(x[::-1]))
r = int(''.join(map(str, x)))
datetime.strptime('2010-11-13 10:33:54.227806', '%y-%m-%d %h:%m:%s.%f')
[(i, sum(j) / len(j)) for i, j in list(d.items())]
zip([1, 2], [3, 4])
['hello{0}'.format(i) for i in a]
re.sub('(?<!\\s)((\\s+)(?:\\s+\\2))(?:\\s+\\2)+(?!\\s)', '\\1', s)
df.div(df.sum(axis=1), axis=0)
map(lambda t: (t[1], t[0]), mylist)
[(t[1], t[0]) for t in mylist]
driver.find_element_by_xpath("//p[@id, 'one']/following-sibling::p")
re.findall('\\[[^\\]]*\\]|\\([^\\)]*\\)|"[^"]*"|\\s+', strs)
print(list(itertools.combinations({1, 2, 3, 4}, 3)))
df[['hour', 'weekday', 'weeknum']] = df.apply(lambdafunc, axis=1)
soup.find_all('a', string='elsie')
my_datetime.strftime('%b %d, %y')
int(''.join(c for c in s if c.isdigit()))
dic['test'].update({'class': {'section': 5}})
dict(map(int, x.split(':')) for x in s.split(','))
driver.find_element_by_xpath("//div[@id='a']//a[@class='click']")
np.where((vals == (0, 1)).all(axis=1))
somemodel.objects.filter(id=id).delete()
dict([['two', 2], ['one', 1]])
dict(zip(l[::2], l[1::2]))
gravity = 9.8
re.findall('(([0-9]+)([a-z]))', '20m10000n80m')
re.findall('([0-9]+|[a-z])', '20m10000n80m')
re.findall('([0-9]+)([a-z])', '20m10000n80m')
re.compile('\\w+').findall('hello world, my name is...james the 2nd!')
datetime.datetime.strptime('03:55', '%h:%m').time()
requests.get('https://www.reporo.com/', verify=false)
a[a != 0]
new_dict = {k: v for k, v in zip(keys, values)}
dict((k, v) for k, v in zip(keys, values))
dict([(k, v) for k, v in zip(keys, values)])
m = re.search('\\[(\\w+)\\]', s)
s.setsockopt(sol_socket, so_reuseaddr, 1)
list3 = [(a + b) for a, b in zip(list1, list2)]
[ord(c) for c in s.decode('hex')]
print(sorted(student_tuples, key=lambda t: (-t[2], t[0])))
[y for x in range(3) for y in [x, x]]
txt = open('file.txt').read()
mylist[:] = [(x / myint) for x in mylist]
"""name: {0[person.name]}""".format({'person.name': 'joe'})
df.replace(' ', '_', regex=true)
datetime.datetime.combine(my_date, datetime.time.min)
tst2 = str(tst)
time.ctime(os.path.getmtime(file))
time.ctime(os.path.getctime(file))
t = os.path.getmtime(filename)
os.path.getmtime(path)
print(('last modified: %s' % time.ctime(os.path.getmtime(file))))
print(('created: %s' % time.ctime(os.path.getctime(file))))
return os.path.getctime(path_to_file)
os.system('taskkill /f /im firefox.exe')
return (x.group(0) for x in re.finditer("[a-za-z']+", string))
""", """.join(['%.2f'] * len(x))
print(re.match('(\\d+(\\.\\d+)?)', '3434.35353').group(1))
df['name'].str.replace('\\(.*\\)', '')
result = [x for x in list_a if x[0] in list_b]
print([''.join(a) for a in combinations(['hel', 'lo', 'bye'], 2)])
[x for x in li if 'ar' in x[2]]
unsorted_list.sort(key=lambda x: x[3])
logging.info('test')
fig.add_subplot(1, 1, 1)
sorted(list(x.items()), key=operator.itemgetter(1))
sorted(dict1, key=dict1.get)
sorted(d, key=d.get, reverse=true)
sorted(list(d.items()), key=(lambda x: x[1]))
np.einsum('ijk,ikl->ijl', a, b)
print('i have: {0.price}'.format(card))
f.write('# data for class a\n')
a = a[-1:] + a[:-1]
datetimevariable.strftime('%y-%m-%d')
mixed.replace('\r\n', '\n').replace('\r', '\n')
os.path.expanduser('~user')
t = [l[i] for i in idx]
words = open('myfile').read().split()
[[sum([x[1] for x in i])] for i in data]
[sum([x[1] for x in i]) for i in data]
article.objects.annotate(like_count=count('likes')).order_by('-like_count')
today = datetime.datetime.utcnow().date()
[(a * b) for a, b in zip(lista, listb)]
re.findall('(?::|;|=)(?:-)?(?:\\)|\\(|d|p)', s)
re.match('[:;][)(](?![)(])', str)
json_string = json.dumps([ob.__dict__ for ob in list_name])
listofzeros = [0] * n
stringnamehere.decode('utf-8', 'ignore')
re.findall('((?:a|b|c)d)', 'bde')
dic.setdefault(key, []).append(value)
a[np.argmin(a[:, (1)])]
a.update(b)
[{k: v for k, v in d.items() if k != 'mykey1'} for d in mylist]
[dict((k, v) for k, v in d.items() if k != 'mykey1') for d in mylist]
numpy.random.random((3, 3))
df['c'] = df['a'] + df['b']
[value for key, value in list(programs.items()) if 'new york' in key.lower()]
sys.path.append('/path/to/main_folder')
re.findall('\\d+(?=[^[]+$)', s)
pickle.load(open('afile', 'rb'))
driver.find_element_by_xpath('xpath').click()
ex.groupby(level='a').agg(lambda x: x.index.get_level_values(1).nunique())
pd.concat(map(pd.dataframe, iter(d.values())), keys=list(d.keys())).stack().unstack(0)
sum(1 for i, j in zip(a, b) if i != j)
d = {(a.lower(), b): v for (a, b), v in list(d.items())}
list_.sort(key=lambda x: [x[0], len(x[1]), x[1]])
s.strip()
s = s.lstrip()
s = s.rstrip()
s = s.strip(' \t\n\r')
print(re.sub('[\\s+]', '', s))
task.objects.exclude(prerequisites__status__in=['a', 'p', 'f'])
root.configure(background='black')
numpy.array([(key, val) for key, val in result.items()], dtype)
pd.concat([df_1, df_2.sort_values('y')])
re.sub('(.*)</div>', '\\1</bad>', s)
print(max(d, key=lambda x: (d[x]['salary'], d[x]['bonus'])))
book.objects.filter(author__id=1).filter(author__id=2)
re.compile('xyz', re.ignorecase).split('fooxyzbar')
[sum(map(int, s)) for s in example.split()]
[i for i in y if y[i] == 1]
c.decode('unicode_escape')
pd.melt(x, id_vars=['farm', 'fruit'], var_name='year', value_name='value')
default_data['item3'] = 3
default_data.update({'item3': 3, })
default_data.update({'item4': 4, 'item5': 5, })
l[:3] + l[-3:]
df = df.reset_index(drop=true)
[a[x].append(b[x]) for x in range(3)]
os.path.realpath(path)
set(l[0].f.items()).issubset(set(a3.f.items()))
zip(*np.where(a == 1))
np.where(a == 1)
df.columns = df.columns.get_level_values(0)
x = scipy.matrix([1, 2, 3]).transpose()
text = re.sub('(\\bget\\b)', '\\1@', text)
np.array([np.arange(3), np.arange(2, -1, -1), np.ones((3,))]).min(axis=0)
df['new_col'] = list(range(1, len(df) + 1))
os.environ['debussy'] = '1'
print(os.environ['debussy'])
os.environ['debussy'] = '1' 
b.update(d)
df['b']
ebar = plt.errorbar(x, y, yerr=err, ecolor='y')
results += [each for each in os.listdir(folder) if each.endswith('.c')]
print('\xc2\xa3'.decode('utf8') + '1')
re.sub('(?<=[a-z])([a-z])', '-\\1', s).lower()
os.system('ulimit -s unlimited; some_executable')
"""{0:.3g}""".format(num)
numpy.append(a, a[0])
df.ix[:, (df.loc[0] == 38.15)].columns
df2['revenue'] = df2.cet.map(df1.set_index('date')['revenue'])
json_data = json.loads(json_string)
math.cos(math.radians(1))
sum(isinstance(x, int) for x in a)
'used\u200b'.replace('\u200b', '*')
threading.thread(target=sudsmove).start()
sum(i * i for i in l)
sum(map(lambda x: x * x, l))
d = dict(((key, value) for (key, value) in iterable))
d = {key: value for (key, value) in iterable}
d = {k: v for (k, v) in iterable}
df.round({'alabama_exp': 2, 'credit_exp': 3})
p.setopt(pycurl.writefunction, lambda x: none)
print(random.choice(words))
max(d, key=lambda x: d[x]['count'])
[(int(x) if x else 0) for x in data.split(',')]
""",""".join(x or '0' for x in s.split(','))
re.compile('$^')
re.compile('.\\a|.\\a*|.\\a+')
re.compile('a^')
df.columns[df.max() > 0]
yourdatetime.date() == datetime.today().date()
print('\x1b[1m' + 'hello')
re.sub('.{20}(.mkv)', '\\1', 'unique12345678901234567890.mkv')
['a', 'c', 'b', 'obj']
""" """.join(mystring.split())
print('{:.100f}'.format(2.345e-67))
('key1' in dict)
('a' in d)
('c' in d)
if ('key1' in dict):     pass
if (key in d):     pass
blog.objects.filter(pk__in=[1, 4, 7])
f = open('test/test.pdf', 'rb')
format(12345678.46, ',').replace(',', ' ').replace('.', ',')
pd.merge(frame_1, frame_2, left_on='county_id', right_on='countyid')
np.isnan(a).sum() / np.prod(a.shape)
sorted(iter(citypopulation.items()), key=lambda k_v: k_v[1][2], reverse=true)
sorted(list(u.items()), key=lambda v: v[1])
sorted(list(d.items()), key=lambda k_v: k_v[1], reverse=true)
sorted(list(d.items()), key=lambda k_v: k_v[1])
f = open(os.path.join(__location__, 'bundled-resource.jpg'))
f = open('words.txt', 'ru')
{k: (float(d2[k]) / d1[k]) for k in d2}
{k: (d2[k] / d1[k]) for k in list(d1.keys()) & d2}
dict((k, float(d2[k]) / d1[k]) for k in d2)
df.to_csv(filename, date_format='%y%m%d')
my_dict.pop('key', none)
b = np.where(np.isnan(a), 0, a)
subprocess.call('start command -flags arguments', shell=true)
subprocess.call('command -flags arguments &', shell=true)
f = urllib.request.urlopen(url, urllib.parse.unquote(urllib.parse.urlencode(params)))
"""    xyz     """.rstrip()
urllib.parse.quote(s.encode('utf-8'))
urllib.parse.quote_plus('a b')
np.array(map(int, '100110'))
print(np.array(list(mystr), dtype=int))
img = cv2.imread('messi5.jpg', 0)
lst.sort(key=lambda x: x[2], reverse=true)
indices = [i for i, x in enumerate(my_list) if x == 'whatever']
subprocess.call('grep -r passed *.log | sort -u | wc -l', shell=true)
len(my_text) - len(my_text.rstrip('?'))
df[df.columns[1:]].replace('[\\$,]', '', regex=true).astype(float)
df1.merge(df2, how='left', on='word')
print(''.join(''.join(i) for i in zip(a2, a1)) + a[-1] if len(a) % 2 else '')
root.attributes('-topmost', true)
root.lift()
hex(int(''.join([str(int(b)) for b in walls]), 2))
hex(sum(b << i for i, b in enumerate(reversed(walls))))
print(('total score for', name, 'is', score))
print('total score for {} is {}'.format(name, score))
print('total score for %s is %s  ' % (name, score))
print(('total score for', name, 'is', score)) 
url('^$', templateview.as_view(template_name='your_template.html'))
df[df['a'].isin([3, 6])]
instance.__class__.__name__
system('/path/to/my/venv/bin/python myscript.py')
employees.objects.values_list('eng_name', flat=true)
re.findall('\\d|\\d,\\d\\)', '6,7)')
input('press enter to continue...')
"""abc""".encode('hex')
db.doc.update({'_id': b['_id']}, {'$set': {'geoloccountry': mygeoloccountry}})
re.sub('l+', 'l', 'lollll')
rows = soup.findall('tr')[4::5]
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
pd.concat([goog, aapl], keys=['goog', 'aapl'], axis=1)
return httpresponse(json.dumps(response_data), content_type='application/json')
mystring.decode('string_escape')
hashlib.md5(open('filename.exe', 'rb').read()).hexdigest()
[k for k, v in d.items() if v == desired_value]
{k for d in lod for k in list(d.keys())}
set([i for s in [list(d.keys()) for d in lod] for i in s])
[i for s in [list(d.keys()) for d in lod] for i in s]
keys, values = zip(*list(d.items()))
int(decimal(s))
int(s.split('.')[0])
numpy.in1d(b, a).all()
numpy.array([(x in a) for x in b])
networkx.draw_networkx_labels(g, pos, labels)
y = [row[:] for row in x]
x = numpy.loadtxt('somefile.csv', delimiter=',')
matching = [s for s in some_list if 'abc' in s]
df.to_csv('mydf.tsv', sep='\t')
random.sample(list(range(100)), 10)
s.rsplit(',', 1)
all(isinstance(x, int) for x in lst)
all(isinstance(x, int) for x in lst) 
line.strip()
driver.execute_script('window.scrollto(0, y)')
driver.execute_script('window.scrollto(0, document.body.scrollheight);')
datetime.datetime.combine(dateobject, datetime.time())
print(any(x in a for x in b))
scipy.misc.imsave('outfile.jpg', image_array)
item = re.sub(' ?\\([^)]+\\)', '', item)
item = re.sub(' ?\\(\\w+\\)', '', item)
item = re.sub(' \\(\\w+\\)', '', item)
len(set(list1).intersection(list2)) > 0
i = int(s, 16)
int('0xff', 16)
int('ffff', 16)
ast.literal_eval('0xdeadbeef')
int('deadbeef', 16)
os.system('screencapture screen.png')
driver.set_window_size(1400, 1000)
unicodedata.normalize('nfkd', 'm\xfasica').encode('ascii', 'ignore')
pandas.concat([df1, df2]).drop_duplicates().reset_index(drop=true)
a = numpy.fromfile('filename', dtype=numpy.float32)
subprocess.call('mv /home/somedir/subdir/* somedir/', shell=true)
subprocess.call('mv /home/somedir/subdir/* somedir/', shell=true) 
print('\u25b2'.encode('utf-8'))
difflib.sequencematcher(none, file1.read(), file2.read())
dict((k, int(v)) for k, v in (e.split(' - ') for e in s.split(',')))
all(i in (1, 2, 3, 4, 5) for i in (1, 6))
df['date'].map(lambda t: t.date()).unique()
"""{:>7s}""".format(mystring)
open('componentreport-dji.xls', 'rb').read(200)
df.sort_values(['b', 'c'], ascending=[true, false], inplace=true)
df.sort_values(['a', 'b'], ascending=[true, false])
df1.sort(['a', 'b'], ascending=[true, false], inplace=true)
df.sort(['a', 'b'], ascending=[true, false])
redirect('home.views.index')
[x for x in a if x not in [2, 3, 7]]
out = ''.join(c for c in asking if c not in ('!', '.', ':'))
soup.find('meta', {'name': 'city'})['content']
urllib.parse.unquote('%0a')
urllib.parse.unquote(url).decode('utf8')
del lst[:]
del lst1[:]
lst[:] = []
alist[:] = []
s.reset_index(0).reset_index(drop=true)
elems[0].gettext().encode('utf-8')
[(y - x) for x, y in zip(l, l[1:])]
print(re.search('\\blog_addr\\s+(\\s+)', line).group(1))
globals().update(importlib.import_module('some.package').__dict__)
"""""".join(['a', 'b', 'c', 'd'])
url.split('&')
od = collections.ordereddict(sorted(d.items()))
ordereddict(sorted(list(d.items()), key=(lambda t: t[0])))
response = requests.put(url, data=json.dumps(data), headers=headers)
re.sub('[\\w_]+', '', s)
[(x + y) for x in l2 for y in l1]
dict([x.split('=') for x in s.split()])
my_list.pop(2)
s = s.replace('m', '')
newstr = oldstr.replace('m', '')
sum(x * y for x, y in zip(a, b))
list(x * y for x, y in list(zip(a, b)))
sum(i * j for i, j in zip(a, b))
sum(x * y for x, y in list(zip(a, b)))
f.write(open('xxx.mp4', 'rb').read())
new_list = [(x + 1) for x in my_list]
[x for x in j if x >= 5]
plt.plot(list(range(10)), '--bo')
plt.plot(list(range(10)), linestyle='--', marker='o', color='b')
[i.split('\t', 1)[0] for i in l]
mylist = [i.split('\t')[0] for i in mylist]
sum(your_list)
forkedpdb().set_trace()
result = {k: d2.get(v) for k, v in list(d1.items())}
datetime.datetime.now() + datetime.timedelta(days=1, hours=3)
[int(s[i:i + 3], 2) for i in range(0, len(s), 3)]
dict((v, k) for k, v in my_dict.items())
print(sorted(l, key=lambda x: int(x.split('.')[2])))
any(d['name'] == 'test' for d in label)
a[:] = [x for x in a if x != [1, 1]]
[x for x in a if x != [1, 1]]
b = {a[i]: a[i + 1] for i in range(0, len(a), 2)}
len(set(a)) == len(a)
print(hashlib.md5(open(full_path, 'rb').read()).hexdigest())
sorted(list(data.items()), key=lambda x: x[1][0])
"""""".join(x.upper() if random.randint(0, 1) else x for x in s)
os.system('grepdb="echo 123"; /bin/bash -c "$grepdb"')
os.system('/bin/bash -c "echo hello world"')
getattr(test, a_string)
image.open('pathtofile').show()
"""didn't""".replace("'", '')
files.sort(key=file_number)
sentence.replace(' ', '')
pattern = re.compile('\\s+') sentence = re.sub(pattern, '', sentence)
sentence.strip()
sentence = re.sub('\\s+', '', sentence, flags=re.unicode)
sentence = ''.join(sentence.split())
sum(my_counter.values())
np.sqrt(((a - b) ** 2).sum(-1))
levels = [{}, {}, {}]
weekly = [sum(visitors[x:x + 7]) for x in range(0, len(daily), 7)]
del d[key]
{i: a[i] for i in a if (i != 0)}
lol.pop('hello')
del r[key]
np.linalg.solve(np.dot(a.t, a), np.dot(a.t, b))
pd.concat([df.drop('b', axis=1), pd.dataframe(df['b'].tolist())], axis=1)
for i in range(0, 10, 2):     pass
for i in mylist[::2]:     pass
[{'content': x['content'].lower()} for x in messages]
""" """.join(my_list)
re.sub('(http://\\s+|\\s*[^\\w\\s]\\s*)', '', a)
str(n) == str(n)[::-1]
ftp.storbinary('stor myfile.txt', open('myfile.txt', 'rb'))
re.sub('.*i', 'i', stri)
int('1,000,000'.replace(',', ''))
pd.merge(df1, df2, left_index=true, right_index=true, how='outer')
pandas.concat([df1, df2], axis=1)
all(dict.values())
df.c_contofficeid.str.replace('^12(?=.{4}$)', '')
l[::(-1)]
reversed(array)
l.reverse()
list(reversed(array))
[tup[0] for tup in a]
newcontents = contents.replace('a', 'e').replace('s', '3')
json.dumps([dict(list(row.items())) for row in rs])
config_file = os.path.expanduser('~/foo.ini')
request.params.getall('c')
np.corrcoef(x)
print(max(1, 2, 3))
self.request.get('var_name')
a['x'].apply(lambda x, y: x + y, args=(100,))
user.objects.order_by('-pet__age')[:10]
time.sleep(5)
time.sleep(60)
sleep(0.1)
time.sleep(60) 
time.sleep(0.1)
[x for x in my_list if not any(c.isdigit() for c in x)]
df['state'].apply(lambda x: x[len(x) / 2 - 1:len(x) / 2 + 1])
plt.grid(true)
sorted(lst, key=lambda x: (-1 * c[x], lst.index(x)))
[max(len(str(x)) for x in line) for line in zip(*foo)]
df.country.value_counts().reset_index(name='sum of accidents')
data.set_index('date').diff()
a.update([3, 4])
a[1::2] = -1
df.groupby('group')['value'].rank(ascending=false)
datetime.strptime('tue, 22 nov 2011 06:00:00 gmt', '%a, %d %b %y %h:%m:%s %z')
struct.pack('<i', 1633837924)
list.append('foo')
list.insert(0, 'foo')
theset = set(k.lower() for k in thedict)
"""{s:{c}^{n}}""".format(s='dog', n=5, c='x')
isinstance(s, str)
isinstance(s, str) 
dict(pair for d in l for pair in list(d.items()))
{k: v for d in l for k, v in list(d.items())}
df.sort_values(['peak', 'weeks'], ascending=[true, false], inplace=true)
df.sort(['peak', 'weeks'], ascending=[true, false], inplace=true)
eval("print('hello')")
[{'a': 1, 'c': 4, 'b': 2, 'd': 4}, {'a': 1, 'c': 4, 'b': 1, 'd': 5}]
[{'a': 1, 'c': 4, 'b': 2, 'd': 4}, {'a': 1, 'c': 4, 'b': 1, 'd': 5}] 
list(itertools.product(*a))
df.groupby(['country', 'item_code'])[['y1961', 'y1962', 'y1963']].sum()
done = [(el, x) for el in [a, b, c, d]]
x = x[numpy.logical_not(numpy.isnan(x))]
os.path.join(*x.split(os.path.sep)[2:])
line = line.replace(';', ':')
subprocess.call('tar c my_dir | md5sum', shell=true)
"""437c2123""".decode('hex')
[k for k, v in user._fields.items() if v.required]
df = df.ix[:, 0:2]
x = map(int, x.split())
x = [int(i) for i in x.split()]
driver.find_element_by_css_selector("input[onclick*='1 bedroom deluxe']")
re.sub('[^a-za-z0-9-_*.]', '', my_string)
webbrowser.open('file:///my_pdf.pdf')
result = result.replace('\\', '')
result.replace('\\', '')
df.replace('-', 'nan')
datetime.datetime.now().date()
datetime.datetime.now().date() 
[elem.tag for elem in a.iter()]
[elem.tag for elem in a.iter() if elem is not a]
"""2.7.0_bf4fda703454""".split('_')
sorted(lst, key=lambda x: x['language'] != 'en')
all(value == 0 for value in list(your_dict.values()))
df.pivot_table('y', rows='x', cols='x2')
try:     dosomething() except:     pass
try:     dosomething() except exception:     pass
m.sum(axis=0).sum(axis=0)
time.mktime(dt.timetuple()) + dt.microsecond / 1000000.0
df[(x <= df['columnx']) & (df['columnx'] <= y)]
sorted(l, key=itemgetter(2))
l.sort(key=(lambda x: x[2]))
sorted(l, key=(lambda x: x[2]))
sorted_list = sorted(list_to_sort, key=itemgetter(2, 0, 1))
np.argwhere(np.all(arr == [[0, 3], [3, 0]], axis=(1, 2)))
data.loc[:, (list(itertools.product(['one', 'two'], ['a', 'c'])))]
data.loc[:, ([('one', 'a'), ('one', 'c'), ('two', 'a'), ('two', 'c')])]
hashtags = re.findall('#(\\w+)', str1, re.unicode)
os.rename(src, dst)
print(etree.tostring(some_tag.find('strong')))
json.dumps({str(k): v for k, v in data.items()})
soup = beautifulsoup(response.read().decode('utf-8'))
os.remove(filename)
min([x for x in num_list if x > 2])
df['prod_type'] = 'responsive'
sorted(lst, key=lambda x: (x < 0, x))
six_months = (date.today() + relativedelta(months=(+ 6)))
(date(2010, 12, 31) + relativedelta(months=(+ 1)))
(date(2010, 12, 31) + relativedelta(months=(+ 2)))
print((datetime.date.today() + datetime.timedelta(((6 * 365) / 12))).isoformat())
sorted(list(things.keys()), key=lambda x: things[x]['weight'], reverse=true)
a[np.arange(len(a)) != 3]
[x for x in lst if fn(x) != 0]
df.set_index('month')
arr = [line.split(',') for line in open('./urls-eu.csv')]
[i for i in range(100) if i > 10 if i < 20]
"""""".join([c for c in strs if c.isdigit()])
re.split('\\t+', yas.rstrip('\t'))
(a.t * b).t
'test string\n'.rstrip()
'test string \n\n'.rstrip('\n')
s.strip() 
s.rstrip()
s.lstrip()
'mac eol\r'.rstrip('\r\n')
'windows eol\r\n'.rstrip('\r\n')
'unix eol\n'.rstrip('\r\n')
'hello\n\n\n'.rstrip('\n')
re.findall('.{,16}\\b', text)
[[x[i][j] for j in range(len(x[i]))] for i in range(len(x))]
'\xd0\xbc\xd0\xb0\xd1\x80\xd0\xba\xd0\xb0'.encode('latin-1')
df.groupby((df.a == 'b').shift(1).fillna(0).cumsum())
urllib.request.urlretrieve('http://search.twitter.com/search.json?q=hi', 'hi.json')
numpy.where((x == 0))[0]
sys.stdout.flush()
str(i)
a.__str__()
str(a)
l.sort(key=operator.itemgetter(1))
print(str(count) + '    ' + str(conv))
df.fillna(method='ffill', inplace=true)
text.config(state=disabled)
sum(map(ord, string))
list(itertools.product(*arrays))
'{:,}'.format(value)
locale.setlocale(locale.lc_all, 'en_us') locale.format('%d', 1255000, grouping=true)
df[df.col1.isin(['men', 'rocks', 'mountains'])]
[x[1] for x in l]
'\u0440\u0430\u0437 \u0434\u0432\u0430 \u0442\u0440\u0438'.split()
mymodel.objects.extra(select={'length': 'length(name)'}).order_by('length')
min(dicts, key=lambda x: (abs(1.77672955975 - x['ratio']), -x['pixels']))
m[~m.mask]
re.findall('\\b[a-z]', formula)
matrix = [([0] * 5) for i in range(5)]
np.vstack(np.meshgrid(x_p, y_p, z_p)).reshape(3, -1).t
arr[arr != 0].min()
browser.find_elements_by_xpath("//*[@type='submit']/@value").text
browser.find_elements_by_xpath("//*[@type='submit']").get_attribute('value')
with open('example.yaml', 'r') as stream:     try:         print((yaml.load(stream)))     except yaml.yamlerror as exc:         print(exc)
with open('example.yaml') as stream:     try:         print((yaml.load(stream)))     except yaml.yamlerror as exc:         print(exc)
pd.dataframe(df.columns[np.argsort(df.values)], df.index, np.unique(df.values))
datetime.datetime.today().strftime('%y-%m-%d')
urllib.parse.quote_plus('string_of_characters_like_these:$#@=?%^q^$')
print(' '.join(sorted(d, key=lambda k: len(d[k]), reverse=true)))
map(list, zip(*[(1, 2), (3, 4), (5, 6)]))
map(list, zip(*[(1, 2), (3, 4), (5, 6)])) 
zip(*[(1, 2), (3, 4), (5, 6)])
[(x, y) for x, y in zip(mylist, mylist[1:]) if y == 9]
driver.get('http://www.google.com.br')
b = a.decode('utf8')[::-1].encode('utf8')
dparser.parse('monkey 2010-07-32 love banana', fuzzy=true)
dparser.parse('monkey 20/01/1980 love banana', fuzzy=true)
dparser.parse('monkey 10/01/1980 love banana', fuzzy=true)
dict(map(lambda s: s.split(':'), ['a:1', 'b:2', 'c:3', 'd:4']))
re.search('[a-za-z]', the_string)
dataframe({'count': df1.groupby(['name', 'city']).size()}).reset_index()
re.sub('[^0-9]', '', 'sdkjh987978asd098as0980a98sd')
[y for y in a if y not in b]
df.groupby('id').head(4)
zip(*l)
dict(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd']))
dict(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd'])) 
request.url
somestring.replace('\\r', '')
simplejson.dumps(dict([('%d,%d' % k, v) for k, v in list(d.items())]))
datetime.strptime('jun 1 2005  1:33pm', '%b %d %y %i:%m%p')
parser.parse('aug 28 1999 12:00am')
os.path.split(os.path.abspath(existgdbpath))
os.path.dirname(os.path.abspath(existgdbpath))
requests.post('http://httpbin.org/post', json={'test': 'cheers'})
a = [x for x in a if x['link'] not in b]
{{request.args.get('a')}}
list(range(11, 17))
data_df['grade'] = data_df['grade'].astype(float).astype(int)
max(alkaline_earth_values, key=lambda x: x[1])
your_string.strip('0')
list(permutations(list(range(9)), 2))
re.compile('^(.+)(?:\\n|\\r\\n?)((?:(?:\\n|\\r\\n?).+)+)', re.multiline)
re.compile('^(.+)\\n((?:\\n.+)+)', re.multiline)
call(['path/to/python', 'test2.py', 'neededargumetgohere'])
a.sort(key=operator.itemgetter(2, 3))
final_choices = ((another_choice,) + my_choices)
final_choices = ((another_choice,) + my_choices) 
os.getcwd()
os.path.realpath(__file__)
os.path.dirname(path)
os.path.realpath(path) 
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
full_path = os.path.realpath(__file__)
arr[arr[:, (2)].argsort()]
numpy.sort(arr, axis=0)
re.split('[ .]', 'a b.c')
shutil.copy('file.txt', 'file2.txt')
print(''.join(choice(ascii_uppercase) for i in range(12)))
[''.join(seq) for seq in zip(lst, lst[1:])]
data.rename(columns={'gdp': 'log(gdp)'}, inplace=true)
print(soup.get_text())
sorted(li, key=operator.itemgetter(1), reverse=true)
data['sex'].replace([0, 1], ['female', 'male'], inplace=true)
re.split('\\w+', 'words, words, words.')
re.match('(.*?[.?!](?:\\s+.*?[.?!]){0,1})', phrase).group(1)
print([a for a, b in re.findall('((\\w)\\2*)', s)])
print(' '.join(ordereddict.fromkeys(s)))
print(' '.join(set(s)))
[x for x in file.namelist() if x.endswith('/')]
input_string.count('hello')
print('.'.join([item[0] for item in data]))
fh1.seek(2)
print(zip(my_list[0::2], my_list[1::2]))
my_new_list = zip(my_list[0::2], my_list[1::2])
sys.setdefaultencoding('utf8')
datetime.datetime.now().strftime('%y-%m-%d %h:%m:%s')
print(re.findall('[\\u0600-\\u06ff]+', my_string))
df.groupby(df.index.map(lambda t: t.minute))
dict['apple']['american']
df2.dropna(subset=['three', 'four', 'five'], how='all')
a.insert(0, k)
a = a[:n] + k + a[n:]
np.flatnonzero(x).mean()
df['just_date'] = df['dates'].dt.date
[x for x in a if x not in b]
[''.join(x) for x in a]
list(map(''.join, a))
re.split('\n\\s*\n', s)
from functools import reduce reduce(lambda x, y: 10 * x + y, [1, 2, 3, 4, 5])
"""{0:,.2f}""".format(24322.34)
my_function(**data)
sum((1 for line in open('myfile.txt')))
def bufcount(filename):     f = open(filename)     lines = 0     buf_size = (1024 * 1024)     read_f = f.read     buf = read_f(buf_size)     while buf:         lines += buf.count('\n')         buf = read_f(buf_size)     return lines
print(round(1123.456789, -1))
[x for y, x in sorted(zip(y, x))]
[x for y, x in sorted(zip(y, x))] 
datetime.date(2010, 6, 16).isocalendar()[1]
df.iloc[:, (np.r_[1:10, (15), (17), 50:100])]
df.groupby('dummy').agg({'returns': [np.mean, np.sum]})
s.lower()
s.decode('utf-8').lower()
ftp.retrbinary('retr %s' % filename, file.write)
urlfetch.fetch(url, deadline=10 * 60)
print(my_string[0:100])
legend(numpoints=1)
dict((x, set(y) & set(d1.get(x, ()))) for x, y in d2.items())
numpy.loadtxt(open('test.csv', 'rb'), delimiter=',', skiprows=1)
sample.objects.filter(date__range=['2011-01-01', '2011-01-31'])
sample.objects.filter(date__year='2011', date__month='01')
d['dict3'] = {'spam': 5, 'ham': 6}
numpy.apply_along_axis(numpy.linalg.norm, 1, a)
dict((k, v) for d in dicts for k, v in list(d.items()))
print('your string'.decode('string_escape'))
sum([true, true, false, false, false, true])
fig.set_size_inches(w, h, forward=true)
'hello there %(5)s' % {'5': 'you'}
map(int, example_string.split(','))
[int(s) for s in example_string.split(',')]
x = [i[0] for i in x]
y = map(operator.itemgetter(0), x)
y = [i[0] for i in x]
results = [item['value'] for item in test_data]
datetime.datetime.now().isoformat()
datetime.datetime.utcnow().isoformat()
df.apply(' '.join, axis=0)
pd.dataframe(df.values - df2.values, columns=df.columns)
print(open('myfile.txt', 'u').read())
print(line.decode('utf-16-le').split())
file = io.open('data.txt', 'r', encoding='utf-16-le')
s1 = pd.merge(df1, df2, how='inner', on=['user_id'])
foo.decode('utf8').encode('utf8')
a.shape
n.shape(a)
n.shape(a) 
a.shape 
[i for i, v in enumerate(l) if v[0] == 53]
struct.unpack('<l', 'y\xcc\xa6\xbb')[0]
arr[[0, 1, 1], [1, 0, 2]]
list(powerset('abcd'))
s in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
urllib.parse.quote('http://spam.com/go/')
plt.savefig('test.svg')
len(myarray)
sys.path.insert(0, './path/to/your/modules/')
ax.xaxis.set_ticks_position('top')
cursor.execute('insert or replace into master.table1 select * from table1')
re.match('[a-za-z][\\w-]*\\z', 'a\n')
re.match('[a-za-z][\\w-]*$', '!a_b')
int('deadbeef', 16) 
int('a', 16)
int('0xa', 16)
int(s, 16)
int(hexstring, 16)
print('value is "' + str(value) + '"')
print('value is "{}"'.format(value))
{{tags | join(' ')}}
help('modules')
[[[x[0]] for x in listd[i]] for i in range(len(listd))]
sorted(s, key=str.upper)
sorted(sorted(s), key=str.upper)
sorted(s, key=str.lower)
pd.merge(df1, df2, on=['a', 'b', 'c', 'd'], how='inner')
dict((v, k) for k, v in map.items())
s.decode('unicode_escape')
[int(i) for i in str_list]
map(int, ['1', '2', '3'])
list(map(int, ['1', '2', '3']))
soup.find_all('a', href=re.compile('http://www\\.iwashere\\.com/'))
soup.find_all('a', href=re.compile('^(?!(?:[a-za-z][a-za-z0-9+.-]*:|//))'))
subprocess.call(['java', '-jar', 'blender.jar'])
cursor.execute('insert into table (`column1`) values (%s)', (value,))
if url.endswith('.com'):     url = url[:(-4)]
url = re.sub('\\.com$', '', url)
print(url.replace('.com', ''))
if (not text.endswith(suffix)):     return text return text[:(len(text) - len(suffix))]
print(', ,'.join([str(i[0]) for i in mytuple]))
max(min(my_value, max_value), min_value)
re.findall('\\w+|[^\\w\\s]', text, re.unicode)
result = db.engine.execute('<sql here>')
sys.exit(0)
"""""".join(c for c in my_string if c.isdigit())
re.split(' +', str1)
re.findall('\\s+', str1)
getattr(getattr(myobject, 'id', none), 'number', none)
{i: (i * 2) for i in range(10)}
dict((i, i * 2) for i in range(10))
plt.cla()
total = sum(float(item) for item in s.split(','))
bin(ord('p'))
print(my_string.split(', ', 1)[1])
print(data['places'][0]['post code'])
word = re.sub('([aeiou]):(([aeiou][^aeiou]*){3})$', '\\1\\2', word)
json.loads('{"foo": 42, "bar": "baz"}')['bar']
data = json.loads(array)
data = json.loads(array) 
re.findall('#(\\w+)', 'http://example.org/#comments')
any(e in lestring for e in lelist)
df.plot(x='col_name_1', y='col_name_2', style='o')
parsed_html = beautifulsoup(html) print(parsed_html.body.find('div', attrs={'class': 'container', }).text)
page = urllib.request.urlopen('http://www.google.com/') soup = beautifulsoup(page)
plt.figure(figsize=(3, 4))
s.translate(none, string.punctuation)
base64.urlsafe_b64decode(uenc.encode('ascii'))
len(dict_test) + sum(len(v) for v in dict_test.values())
hex(d).split('x')[1]
list(str(123))
[int(x) for x in str(num)]
br.select_form(nr=0)
json.load(codecs.open('sample.json', 'r', 'utf-8-sig'))
json.loads(open('sample.json').read().decode('utf-8-sig'))
server = smtplib.smtp('smtp.gmail.com', 587)
int('{:08b}'.format(n)[::-1], 2)
df.set_index(['d'], append=true)
for (key, value) in d.items():     pass
for (key, value) in list(d.items()):     pass
for (letter, number) in list(d.items()):     pass
for (k, v) in list(d.items()):     pass
list(d.items())
list(d.items()) 
for (k, v) in list(d.items()):     pass 
for (letter, number) in list(d.items()):     pass 
for (letter, number) in list(d.items()):     pass  
session.query(task).filter(task.time_spent > timedelta(hours=3)).all()
os.system('msbuild project.sln /p:configuration=debug')
max(list(mycount.keys()), key=int)
os.system('source .bashrc; shopt -s expand_aliases; nuke -x scriptpath')
my_function.__name__
my_function.__name__ 
np.all(a == a[(0), :], axis=0)
sorted(a, key=lambda x: (sum(x[1:3]), x[0]))
sorted(a, key=lambda x: (sum(x[1:3]), x[0]), reverse=true)
sorted(lst, key=lambda x: (sum(x[1:]), x[0]))
sorted(lst, key=lambda x: (sum(x[1:]), x[0]), reverse=true)
response.headers['www-authenticate'] = 'basic realm="test"'
del request.session['mykey']
datetime.datetime.strptime('24052010', '%d%m%y').date()
re.sub('[^\\x00-\\x7f]+', ' ', text)
numpy.array([[1, 2], [3, 4]])
mylist = [i for i in range(10)]
[m[0] for m in re.compile('((.+?)\\2+)').findall('44442(2)2(2)44')]
[i[0] for i in re.findall('((\\d)(?:[()]*\\2*[()]*)*)', s)]
fig.subplots_adjust(wspace=0, hspace=0)
x[::-1]
json.dumps({'apple': 'cat', 'banana': 'dog', 'pear': 'fish'})
csvwriter.writerow(row)
{{(item.date | date): 'y m d'}}
re.split('(?<=[\\.\\?!]) ', text)
re.compile('\xe2\x80\x93')
variable = []
intarray = array('i')
[sublist[::-1] for sublist in to_reverse[::-1]]
re.sub('[^0-9a-za-z]+', '*', 'h^&ell`.,|o w]{+orld')
"""""".join(['i ', '<', '3s u ', '&', ' you luvz me'])
logging.disable(logging.critical)
cursor.execute('insert into index(url) values(%s)', (url,))
df['datestr'] = df['dateobj'].dt.strftime('%d%m%y')
s.split('@')[0]
df.query('index < @start_remove or index > @end_remove')
df.loc[(df.index < start_remove) | (df.index > end_remove)]
df.isnull().sum()
df.reset_index(inplace=true)
[x['value'] for x in list_of_dicts]
[d['value'] for d in l]
[d['value'] for d in l if 'value' in d]
np.array([[1, 2, 3], [4, 5, 6]]).tolist()
ast.literal_eval('(1,2,3,4)')
datalist.sort(key=lambda x: x[1])
list(map(list, set(map(lambda i: tuple(i), testdata))))
[list(i) for i in set(tuple(i) for i in testdata)]
return user.groups.filter(name='member').exists()
return user.groups.filter(name__in=['group1', 'group2']).exists()
logging.getlogger().setlevel(logging.debug)
"""""".join(str(i) for i in (34.2424, -64.2344, 76.3534, 45.2344))
"""""".join([s[x:x + 2][::-1] for x in range(0, len(s), 2)])
plt.savefig('graph.png', dpi=1000)
my_list = [[x for x in sublist if x not in to_del] for sublist in my_list]
[item for item in a if 1 in item]
[item for item in a if item[0] == 1]
{p.id: {'id': p.id, 'position': ind} for ind, p in enumerate(p_list)}
[dict(y) for y in set(tuple(x.items()) for x in d)]
exec(compile(open('file.py').read(), 'file.py', 'exec'))
rows = session.query(congress).count()
subprocess.call(['test.sh', str(domid)])
dfs = pd.read_excel(file_name, sheetname=none)
struct.unpack('d', binascii.unhexlify('4081637ef7d0424a'))
a[tuple(b)]
map(list, permutations([2, 3, 4]))
sorted(unsorted_list, key=presorted_list.index)
datetime.datetime.now() - datetime.timedelta(days=1)
d = pd.dataframe(0, index=np.arange(len(data)), columns=feature_list)
x.find('world')
x.find('aloha')
'sdfasdf'.index('cc')
'sdfasdf'.index('df')
str.find('a')
str.find('g')
str.find('s', 11)
str.find('s', 15)
str.find('s', 16)
str.find('s', 11, 14)
sorted(d, key=lambda x: datetime.datetime.strptime(x, '%m-%y'))
re.split('\\.\\s', text)
re.split('\\.\\s', re.sub('\\.\\s*$', '', text))
"""foobar"""[:4]
s.rfind('&')
s[:s.rfind('&')]
driver.find_element_by_xpath("//option[@value='" + state + "']").click()
with open('test.txt', 'a') as myfile:     myfile.write('appended text')
with open('foo', 'a') as f:     f.write('cool beans...')
with open('test1', 'ab') as f:     pass
open('test', 'a+b').write('koko')
print([i for i in re.split('([\\d.]+|\\w+)', 'x+13.5*10x-4e1') if i])
re.findall('[\u4e00-\u9fff]+', ipath)
s.split('s')
subprocess.popen(['rm', '-r', 'some.file'])
dict((d['name'], d) for d in listofdict)
datetime.datetime.now().strftime('%y-%m-%d %h:%m')
time.strftime('%y-%m-%d %h:%m')
re.findall('[bcdfghjklmnpqrstvwxyz]+', 'concertation', re.ignorecase)
[i for i, e in enumerate(a) if e != 0]
map(int, re.findall('\\d+', string1))
os.path.dirname(sys.executable)
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top()
ax.xaxis.set_ticks_position('top') 
datetime.strptime('2015/01/01 12:12am', '%y/%m/%d %i:%m%p')
img = image.open('picture.jpg') img.show()
img = image.open('picture.jpg') img.show
sys.exit(0) 
sys.exit('aa! errors!')
sys.exit()
[max(abs(x) for x in arr[i:i + 4]) for i in range(0, len(arr), 4)]
os.chdir('c:\\users\\uname\\desktop\\python')
os.chdir(path)
no_integers = [x for x in mylist if not isinstance(x, int)]
tree.xpath(".//a[text()='example']")[0].tag
""", """.join([(str(k) + ' ' + str(v)) for k, v in list(a.items())])
print(set(re.sub('[\x00-\x7f]', '', '\xa3\u20ac\xa3\u20ac')))
print(re.sub('[\x00-\x7f]', '', '\xa3100 is worth more than \u20ac100'))
ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
print(t.decode('unicode_escape'))
print(str.encode('cp1252').decode('utf-8').encode('cp1252').decode('utf-8'))
zip(list_a, list_b)
list(zip(a, b))
df.set_index('id').to_dict()
df.set_index('id')['value'].to_dict()
sorted(list(mydict.items()), key=lambda a: map(int, a[0].split('.')))
re.sub('\\([^)]*\\)', '', filename)
"""a b""".replace(' ', '').isalpha()
[(x + y) for x, y in zip(first, second)]
sorted(list(a_dict.items()), key=lambda item: item[1][1])
re.compile('[^a-za-z0-9-]+')
sorted(list(range(len(a))), key=lambda i: a[i])[-2:]
zip(*sorted(enumerate(a), key=operator.itemgetter(1)))[0][-2:]
sorted(list(range(len(a))), key=lambda i: a[i], reverse=true)[:2]
list(x.keys()).index('c')
print('{0:+d}'.format(score))
[k for k, g in itertools.groupby([1, 2, 2, 3, 2, 2, 4])]
"""0,1,2""".split(',')
[int(x) for x in '0,1,2'.split(',')]
dict([('a', 1), ('b', 2), ('c', 3)])
np.savetxt('test.txt', x)
direct_output = subprocess.check_output('ls', shell=true)
df[df.columns - ['t1_v6']]
((25 < a) & (a < 100)).sum()
date.today().strftime('%a')
re.search('\\bis\\b', your_string)
{{car.date_of_manufacture | datetime}}
{{car.date_of_manufacture.strftime('%y-%m-%d')}}
[item for sublist in l for item in sublist]
list(itertools.chain(*list2d))
list(itertools.chain.from_iterable(list2d))
ord('a')
re.sub('(?m)^[^\\s\\n]+', '', '  a\n b\n c\nd  e')
re.sub('(?m)^\\s+', '', 'a\n b\n c')
a, b, c = [1, 2, 3]
[list(v) for k, v in itertools.groupby(mylist, key=lambda x: x[:5])]
line = re.sub('\\(+as .*?\\) ', '', line)
print(line.rstrip('\n'))
df.index.values.tolist()
if (not a):     pass
if (not seq):     pass
if (len(li) == 0):     pass
[i for i, v in enumerate(a) if v > 4]
sorted(yourdata, reverse=true)
sorted(yourdata, key=lambda d: d.get('key', {}).get('subkey'), reverse=true)
yourdata.sort(key=lambda e: e['key']['subkey'], reverse=true)
df.round()
gca().get_lines()[n].get_xydata()
a[:, -2:]
request.get.get('username', '')
pprint(dict(list(o.items())))
url('^$', include('sms.urls')),
url('^', include('sms.urls')),
max_item = max(a_list, key=operator.itemgetter(1))
max(a_list, key=operator.itemgetter(1))
s.resample('3m', how='sum')
[a[i] for i in (1, 2, 5)]
[line for line in open('textfile') if 'apple' in line]
datetime.datetime.strptime(s, '%y-%m-%dt%h:%m:%sz')
pandas.read_csv(filename, sep='\t', lineterminator='\r')
'longlongteststringtest'.replace('test', '?', 1)
archive.write(pdffile, os.path.basename(pdffile))
dict(x[1:] for x in reversed(mylistoftuples))
[(x1 - x2) for x1, x2 in zip(list1, list2)]
string[0].isdigit()
strg.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
print(os.path.dirname(os.path.realpath(__file__)))
re.split('(?<=\\?|!|\\.)\\s{0,2}(?=[a-z]|$)', text)
plt.scatter(*zip(*li))
tuple(zip(*t))
df.groupby(np.arange(len(df.columns)) // 3, axis=1).mean()
"""""".join(chr(i) for i in l)
sum(x == chosen_value for x in list(d.values()))
sum(1 for x in list(d.values()) if some_condition(x))
struct.unpack('f', struct.pack('f', 0.00582811585976))
timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
df.sort('m')
a = sorted(a, key=lambda x: x.modified, reverse=true)
print(bool(a))
df = df.rename(index={last: 'a'})
km.fit(x.reshape(-1, 1))
sorted(words, key=lambda x: 'a' + x if x.startswith('s') else 'b' + x)
webbrowser.open('http://somesite.com/adminpanel/index.php')
dict((k, v) for k, v in parent_dict.items() if 2 < k < 4)
dict((k, v) for k, v in parent_dict.items() if k > 2 and k < 4)
[list(x) for x in zip(*sorted(zip(list1, list2), key=lambda pair: pair[0]))]
sum(((i > 5) for i in j))
len([1 for i in j if (i > 5)])
j = np.array(j) sum((j > i))
[(x + tuple(y)) for x, y in zip(zip(a, b), c)]
os.chmod(path, stat.s_irusr | stat.s_irgrp | stat.s_iroth)
parser.add_argument('file', nargs='*')
z = [(i == j) for i, j in zip(x, y)]
[(x[i] == y[i]) for i in range(len(x))]
[int(s) for s in re.findall('\\b\\d+\\b', "he33llo 42 i'm a 32 string 30")]
df2 = pd.dataframe(index=df1.index)
struct.unpack('h', ps[0:2])
print('\n'.join('  '.join(map(str, row)) for row in t))
df.sort_values(by='date')
driver.find_element_by_name('<check_box_name>').is_selected()
driver.find_element_by_id('<check_box_id>').is_selected()
[(a if a else 2) for a in [0, 1, 0, 3]]
'm\\n{ampersand}m\\n{apostrophe}s'.encode().decode('unicode-escape')
'm\\n{ampersand}m\\n{apostrophe}s'.decode('unicode-escape')
chr(int('fd9b', 16)).encode('utf-8')
print('0x%x' % value)
cleaned = [x for x in your_list if x]
slice(*[(int(i.strip()) if i else none) for i in string_slice.split(':')])
soup.find_all(['a', 'div'])
print(func.__name__)
"""""".join('{}{}'.format(key, val) for key, val in sorted(adict.items()))
"""""".join('{}{}'.format(key, val) for key, val in list(adict.items()))
new_list = old_list[:]
new_list = list(old_list)
new_list = copy.copy(old_list)
new_list = copy.deepcopy(old_list)
[i for i in old_list]
plt.legend(frameon=false)
"""\\ud83d\\ude4f""".encode('utf-16', 'surrogatepass').decode('utf-16')
globals()['myfunction']()
urllib.request.urlopen('http://www.stackoverflow.com').getcode()
conn = httplib.httpconnection('www.python.org') conn.request('head', '/') r1 = conn.getresponse() print(r1.status, r1.reason)
r = requests.head(url) return (r.status_code == 200)
print(urllib.request.urlopen('http://www.stackoverflow.com').getcode())
driver.find_element_by_css_selector("a[href^='javascript']").click()
df.to_pickle(file_name)
df.groupby(by=df.columns, axis=1).mean()
bar.sort(key=lambda x: (x.attrb1, x.attrb2), reverse=true)
alpha = img.split()[-1]
[len(x) for x in s.split()]
soup.findall('div', style='width=300px;')
cursor.execute(sql, list(mydict.values()))
df.to_csv('result.csv', index=false, sep=' ')
globals().update(vars(args))
re.findall('\\[(.*?)\\]', mystring)
print('%.2f kg = %.2f lb = %.2f gal = %.2f l' % (var1, var2, var3, var4))
d = dict((k, v) for k, v in d.items() if v > 0)
d = {k: v for k, v in list(d.items()) if v > 0}
pd.to_datetime(pd.series(date_stngs))
df.iloc[2, 0]
matplotlib.rcparams.update({'font.size': 22})
pd.dataframe(list(d.items()), columns=['date', 'datevalue'])
pd.dataframe(df.values * df2.values, columns=df.columns, index=df.index)
re.findall('\\d+\\.\\d+', 'current level: 13.4 db.')
re.findall('[-+]?\\d*\\.\\d+|\\d+', 'current level: -13.2 db or 14.2 or 3')
zip(it, it, it)
df['x'].str.lower()
jsobj['a']['b']['e'].append({'f': var6, 'g': var7, 'h': var8})
"""""".join(lst)
sum(v for v in list(d.values()) if v > 0)
app.run(debug=true)
df.drop(df.index[[1, 3]], inplace=true)
df.apply(lambda x: x.fillna(x.mean()), axis=0)
[o.my_attr for o in my_list]
time.strftime('%m/%d/%y', time.gmtime(os.path.getmtime(file)))
all(item in list(superset.items()) for item in list(subset.items()))
[str(wi) for wi in wordids]
df2 = df.reset_index()
dt.strftime('%m/%d/%y')
print('total cost is: ${:,.2f}'.format(totalamount))
df.groupby(np.arange(len(df.columns)) // 2 + 1, axis=1).sum().add_prefix('s')
randomlist = [random.random() for _ in range(10)]
print(soup.find('a', href=re.compile('.*follow\\?page.*')))
sys.stdout.flush() 
country, capital = random.choice(list(d.items()))
list('word to split')
[w for w in open('file.txt') if not re.search('[aeiou]{2}', w)]
pat = re.compile('^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$')
exec(compile(open('filename.py').read(), 'filename.py', 'exec'))
session.query(tag).distinct(tag.name).group_by(tag.name).count()
df = df.dropna(axis=1, how='all')
all(x.count(1) == 3 for x in l)
[x[0] for x in l1 if any(x[0] == y[0] for y in l2)]
tex.delete('1.0', end)
datetime.datetime.fromtimestamp(mynumber).strftime('%y-%m-%d %h:%m:%s')
system('python myscript.py')
your_list.sort(key=operator.attrgetter('anniversary_score'))
your_list.sort(key=lambda x: x.anniversary_score)
print(type(tf.session().run(tf.constant([1, 2, 3]))))
list(itertools.chain(*a))
count.setdefault('a', 0)
df.groupby(['cluster']).mean()
min(mylist, key=lambda x: abs(x - mynumber))
any(x in string for x in search)
print(pattern.search(url).group(1))
(s.factorize()[0] + 1).astype('float')
c = [(a - b) for a, b in zip(a, b)]
datetime.datetime.strptime('2011, 4, 0', '%y, %u, %w')
map(int, ['1', '-1', '1'])
datetime.datetime.strptime('16sep2012', '%d%b%y')
book.objects.filter(pk=pk).update(**d)
book.objects.create(**d)
print('{0:.2f}'.format(your_number))
random.randint(100000000000, 999999999999)
int(''.join(str(random.randint(0, 9)) for _ in range(12)))
"""""".join(str(random.randint(0, 9)) for _ in range(12))
'%0.12d' % random.randint(0, 999999999999)
numpy.delete(a, index)
sorted(trial_list, key=lambda x: trial_dict[x])
sys.stdin.read(1)
print(re.findall(pattern, x))
k = soup.find(text=re.compile('my keywords')).parent.text
df.apply(lambda x: x.tolist(), axis=1)
b = np.reshape(a, (-1, 2))
app.run(host='192.168.0.58', port=9000, debug=false)
print('\xc5\xc4\xd6'.encode('utf8'))
[x[0] for x in g]
re.findall('-(?!aa-|bb-)([^-]+)', string)
re.findall('-(?!aa|bb)([^-]+)', string)
{k: v for k, v in list(hand.items()) if v}
dict((k, v) for k, v in hand.items() if v)
sorted(l, key=operator.itemgetter('resulttype'))
s.sort(key=operator.attrgetter('resulttype'))
somelist.sort(key=lambda x: x.resulttype)
df1.merge(df2, on='name').merge(df3, on='name')
decimal.decimal(random.randrange(10000)) / 100
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
f = [] for (dirpath, dirnames, filenames) in walk(mypath):     f.extend(filenames)     break
print(glob.glob('/home/adam/*.txt'))
os.listdir('somedirectory')
cur.executemany('insert into table values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', tup)
print([key for key in d if d[key] == 1])
print([key for key, value in d.items() if value == 1])
print([key for key, value in list(d.items()) if value == 1])
strs = ['' for x in range(size)]
with open(input_filename, 'r') as f:     html_text = markdown(f.read(), output_format='html4') pdfkit.from_string(html_text, output_filename)
[dict(t) for t in set([tuple(d.items()) for d in l])]
time_zone = 'europe/istanbul'
dates_dict.setdefault(key, []).append(date)
article.objects.values('pub_date').annotate(article_count=count('title'))
canvas.delete('all')
s = pd.series(['a', 'b', 'a1r', 'b2', 'aabb4'])
datetime.datetime.strptime('2007-03-04t21:08:12', '%y-%m-%dt%h:%m:%s')
a.sort(key=lambda x: b.index(x[0]))
a.sort(key=lambda x_y: b.index(x_y[0]))
plt.savefig('filename.png')
plt.savefig('filename.png', dpi=300)
p1.communicate()[0]
output = subprocess.popen(['mycmd', 'myarg'], stdout=pipe).communicate()[0]
soup.body.findall(text='python')
soup.body.findall(text='python jobs')
sorted(list(d.items()), key=lambda name_num: (name_num[0].rsplit(none, 1)[0], name_num[1]))
set([1, 2, 3]) ^ set([3, 4, 5])
request.post.getlist('pass_id')
list(dict((x['id'], x) for x in l).values())
df.groupby(df.columns, axis=1).sum()
dict(zip(list(range(1, 5)), list(range(7, 11))))
numpy.where(mask)
if (string1.lower() == string2.lower()):     print('the strings are the same (case insensitive)') else:     print('the strings are not the same (case insensitive)')
if (string1.lower() == string2.lower()):     pass
(string1.lower() == string2.lower())
(first.lower() == second.lower())
(first.upper() == second.upper())
os.system("awk '{print $10, $11}' test.txt > test2.txt")
del my_list[2:6]
int(s.encode('hex'), 16)
re.findall('taa(?:[atgc]{3})+?taa', seq)
sorted(s, key=float)
hex(65)
a.append(b).reset_index(drop=true)
pd.concat([a, b], ignore_index=true)
[(i, j) for i in range(1, 3) for j in range(1, 5)]
sorted(iter(mydict.items()), key=itemgetter(1), reverse=true)
pd.date_range('1/1/2014', periods=12, freq='bm')
requests.get('https://kennethreitz.com', verify=false)
df.ix[:-1]
if ('blah' not in somestring):     pass
if (needle in haystack):     pass
string.find('substring')
if (s.find('is') == (-1)):     print("no 'is' here!") else:     print("found 'is' in the string.")
pd.concat([df.head(1), df.tail(1)])
mymodel.objects.extra(where=['char_length(text) > 254'])
mymodel.objects.filter(text__regex='^.{254}.*')
sum(df.apply(lambda x: sum(x.isnull().values), axis=1) > 0)
sorted(enumerate(a), key=lambda x: x[1])
canvas.create_text(x, y, font=('purisa', 12), text=k)
[y['baz'] for x in foos for y in x['bar']]
df = pd.read_csv('comma.csv', quotechar="'")
df['a'] = df['a'].str.replace('in.', ' in. ')
[i for i in range(len(a)) if a[i] > 2]
('myvar' in locals())
('myvar' in globals())
hasattr(obj, 'attr_name')
if ('myvar' in locals()):     pass
if ('myvar' in globals()):     pass
lambda x, y: x + y
sum(1 for i in it)
[(x, lst2[i]) for i, x in enumerate(lst)]
[(i, j) for i, j in zip(lst, lst2)]
[(lst[i], lst2[i]) for i in range(len(lst))]
struct.unpack('bbb', rgbstr.decode('hex'))
(3 not in [2, 3, 4])
((2, 3) not in [(2, 3), (5, 6), (9, 1)])
((2, 3) not in [(2, 7), (7, 3), 'hi'])
(3 not in [4, 5, 6])
[value for pair in zip(a, b[::-1]) for value in pair]
b = np.delete(a, -1, 1)
dbb.commit()
pd.merge(a, b, on=['a', 'b'], how='outer')
setstylesheet('qpushbutton {background-color: #a3c1da; color: red;}')
sum(l) / float(len(l))
[(k, v) for k, v in d.items() if 'light' in k]
k = hashlib.md5('thecakeisalie').hexdigest()
os.path.basename(os.path.normpath('/foldera/folderb/folderc/folderd/'))
birthdays.sort(key=lambda d: (d.month, d.day))
[[td.findnext(text=true) for td in tr.findall('td')] for tr in rows]
"""boat.txt.txt""".replace('.txt', '')
list(df.index)
df.index
"""""".join(list(ordereddict.fromkeys('aaabcabccd').keys()))
list(set('aaabcabccd'))
"""""".join(set('aaabcabccd'))
df.loc[(df.loc[:, (df.dtypes != object)] != 0).any(1)]
br.form.add_file(open(filename), 'text/plain', filename)
all(word in d for word in ['somekey', 'someotherkey', 'somekeyggg'])
subprocess.check_output(['espeak', text], stderr=subprocess.stdout)
df.fillna(method='ffill', inplace=true) 
print(np.linspace(1, 3, num=4, endpoint=false))
print(np.linspace(1, 3, num=5))
kdll.createsymboliclinkw('d:\\testdirlink', 'd:\\testdir', 1)
slice = [arr[i][0:2] for i in range(0, 2)]
upload_url = blobstore.create_upload_url('/upload', gs_bucket_name='my_bucket')
os.chdir(os.path.dirname(__file__))
func(*args)
df['ab'].str.split(' ', 1, expand=true)
df['a'], df['b'] = df['ab'].str.split(' ', 1).str
print(sorted(xs, key=len))
xs.sort(lambda x, y: cmp(len(x), len(y)))
xs.sort(key=lambda s: len(s))
ts.plot(marker='.')
lst = list(itertools.product([0, 1], repeat=n))
lst = map(list, itertools.product([0, 1], repeat=n))
bin = [0, 1] [(x, y, z) for x in bin for y in bin for z in bin]
lst = list(itertools.product([0, 1], repeat=3))
df['col'] = 'str' + df['col'].astype(str)
dict((name, eval(name)) for name in ['some', 'list', 'of', 'vars'])
plt.colorbar(im, ax=ax)
[a for c in cards for b in c for a in b]
sorted(d, key=d.get)
print(len([x for x in lst if x is not none]))
{{json.key1}}
mynewlist = list(myset)
set(['a', 'b', 'c', 'd'])
figure(figsize=(11.69, 8.27))
url.rsplit('/', 1)
url.rsplit('/', 1)[-1]
x_file = open(os.path.join(direct, '5_1.txt'), 'r')
list('5+6')
np.concatenate(input_list).ravel().tolist()
print([y for x in list(dict.items()) for y in x])
[y for x in list(dict.items()) for y in x]
mymodel.objects.order_by('?').first()
os.chdir('chapter3')
os.chdir('c:\\users\\username\\desktop\\headfirstpython\\chapter3')
os.chdir('.\\chapter3')
dict((key, sum(d[key] for d in dictlist)) for key in dictlist[0])
df.sort(['c1', 'c2'], ascending=[true, true])
floats = [float(x) for x in s.split()]
floats = map(float, s.split())
plt.xticks([1, 2, 3, 4, 5])
for line in fileinput.input():     pass
for line in sys.stdin:     pass
'one' in list(d.values())
'one' in iter(d.values())
super(instructor, self).__init__(name, year)
dict(zip(x, y))
sorted(a, key=lambda i: list(i.values())[0], reverse=true)
sorted(a, key=dict.values, reverse=true)
df.groupby(level=0).agg(['sum', 'count', 'std'])
a.setdefault('somekey', []).append('bob')
sum(item['gold'] for item in example_list)
sum([item['gold'] for item in example_list])
sum(item['gold'] for item in mylist)
f.write('text to write\n')
file.write('my string\n')
df.reset_index().groupby('a')['index'].apply(np.array)
fn = os.path.join(os.path.dirname(__file__), 'my_file')
e = next(iter(s))
os.system('dir c:\\')
self.treeview.connect('size-allocate', self.treeview_changed)
3 in [1, 2, 3]
datetime.datetime.strptime('10/05/2012', '%d/%m/%y').strftime('%y-%m-%d')
s = s.replace('\\', '\\\\')
print(proc.communicate()[0])
pd.concat([pd.dataframe(l) for l in my_list], axis=1).t
df.loc[:, ((df != 0).any(axis=0))]
sorted(a, key=lambda x: x[1])
[x.strip() for x in s.split(',')]
items = [item for item in container if item.attribute == value]
open('filename', 'w').write('\n'.join('%s %s' % x for x in mylist))
pattern = re.compile('(?:review: )?(http://url.com/(\\d+))\\s?', re.ignorecase)
str = open('very_important.txt', 'r').read()
df.groupby(['a', 'b'])['c'].unique()
with open(fname) as f:     content = f.readlines()
with open('filename') as f:     lines = f.readlines()
lines = [line.rstrip('\n') for line in open('filename')]
with open('file.txt', 'r') as ins:     array = []     for line in ins:         array.append(line)
df['col'] = pd.to_datetime(df['col'])
[k for d in list(foo.values()) for k in d]
print('hello, {0}, how do you do?'.format(input('enter name here: ')))
df = pd.read_csv('filename.txt', sep=';', names=['region name'])
df['a'] = df['a'].apply(lambda x: x + 1)
platform.system()
a = sorted(a, key=lambda x: float(x))
re.search('name (.*)', s)
db.collection.find({}, {'_id': false})
[row[1] for row in a]
[row[0] for row in a]
sorted(['10', '3', '2'], key=int)
os.path.commonprefix(['/the/dir/', os.path.realpath(filename)]) == '/the/dir/'
any(substring in string for substring in substring_list)
df = pandas.dataframe(data, columns=['r_number', 'c_number', 'avg', 'std'])
re.sub('^((?:(?!cat).)*cat(?:(?!cat).)*)cat', '\\1bull', s)
re.sub('^((.*?cat.*?){1})cat', '\\1bull', s)
sorted(the_list, key=lambda k: int(k.split('_')[1]))
sorted(the_list, key=lambda x: int(x.split('_')[1]))
[list(g) for _, g in itertools.groupby(test, lambda x: x.split('_')[0])]
[list(g) for _, g in itertools.groupby(test, lambda x: x.partition('_')[0])]
driver.get('http://www.google.com')
(datetime.datetime.utcnow() - datetime.timedelta(hours=11)).year
counter([1, 2, 2, 2, 3]) - counter([1, 2])
re.sub('<[^>]*>', '', mystring)
data.encode('hex')
user.objects.filter(userprofile__level__gte=0)
soup.findall(id=re.compile('para$'))
soup.select('div[id^="value_xxx_c_1_f_8_a_"]')
cleaned_list = [x for x in some_list if x is not thing]
var = input('please enter something: ')
foo.append(4)
foo.append([8, 7])
x.insert(2, 77)
plt.savefig('test.png', bbox_inches='tight')
(listone + listtwo)
for item in itertools.chain(listone, listtwo):     pass
males = df[(df[gender] == 'male') & (df[year] == 2014)]
print('\\')
df.replace('-', np.nan)
df = df.drop('column_name', 1)
df.drop(df.columns[[0, 1, 3]], axis=1)
df.drop('column_name', axis=1, inplace=true)
parser = argparse.argumentparser(allow_abbrev=false)
feature3 = [d.get('feature3') for d in df.dic]
df.loc[gb.groups['foo'], ('a', 'b')]
print('[%s, %s, %s]' % (1, 2, 3))
print('[{0}, {1}, {2}]'.format(1, 2, 3))
[v for k, v in list(my_dict.items()) if 'date' in k]
"""{0.month}/{0.day}/{0.year}""".format(my_date)
df.drop(('col1', 'a'), axis=1)
df.drop('a', level=1, axis=1)
{_key: _value(_key) for _key in _container}
browser.find_element_by_class_name('section-select-all').click()
dict((k, d.get(k, '') + d1.get(k, '')) for k in keys)
hash(pformat(a)) == hash(pformat(b))
list(map(tuple, [['tom', 'cat'], ['jerry', 'mouse'], ['spark', 'dog']]))
df.groupby(['stock', 'same1', 'same2'], as_index=false)['positions'].sum()
df.groupby(['stock', 'same1', 'same2'])['positions'].sum().reset_index()
s.upper()
dict(item.split('=') for item in s.split(';'))
br.addheaders = [('cookie', 'cookiename=cookie value')]
df['value'] = df['value'].str[0]
df['value'] = df['value'].str.get(0)
df['value'] = df['value'].str.strip('[]')
""", """.join(['{}_{}'.format(k, v) for k, v in d.items()])
sum(sum(x) for x in lists)
any(np.equal(a, [1, 2]).all(1))
len(set(mylist)) == 1
[map(int, x.split('\t')) for x in s.rstrip().split('\r\n')]
t = sorted(list(a.items()), key=lambda x: x[1])
if ('blabla' in open('example.txt').read()):     pass
f = open('example.txt') s = mmap.mmap(f.fileno(), 0, access=mmap.access_read) if (s.find('blabla') != (-1)):     pass
datafile = file('example.txt') found = false for line in datafile:     if (blabla in line):         return true return false
string2.replace('', string1)[len(string1):-len(string1)]
list(itertools.combinations([1, 2, 3, 4, 5, 6], 2))
"""x = {}""".format(x.decode('utf8')).encode('utf8')
isinstance(x, int)
(type(x) == int)
winsound.playsound('sound.wav', winsound.snd_filename)
[next(it) for _ in range(n)]
list(itertools.islice(it, 0, n, 1))
set(a).intersection(b)
[i for i, j in zip(a, b) if i == j]
print(''.join(map(str, data)))
re.match('\\$[0-9]+[^\\$]*$', '$1 off delicious $5 ham.')
importlib.import_module('.c', 'a.b')
importlib.import_module('a.b.c')
a = np.array(a)
soup.find_all('div', class_=re.compile('comment-'))
[[] for _ in range(n)]
dict((k, globals()[k]) for k in ('foo', 'bar'))
mymodel.objects.order_by('?')[:2]
"""hello {user[name]}""".format(**{'user': {'name': 'markus'}})
list_dict = {t[0]: t for t in tuple_list}
randint(0, 9)
random.randint(a, b)
print((random.randint(0, 9)))
"""""".join(reversed([a[i:i + 2] for i in range(0, len(a), 2)]))
pd.pivot_table(df, index=df.index.date, columns=df.index.time, values='close')
any(item[2] == 0 for item in items)
[x for x in items if x[2] == 0]
sorted(list(dic.items()), key=lambda x: x[1]['fisher'], reverse=true)
plt.yscale('log', nonposy='clip')
map(int, re.findall('\\d+', s))
os.listdir('/home/username/www/')
os.listdir('path')
pd.concat([distancesdf, datesdf.dates], axis=1)
[x[0] for x in a]
[i[0] for i in a]
re.sub('(?<=[a-z])\\r?\\n', ' ', textblock)
gzip.open('file.gz', 'rt', encoding='utf-8')
set(['a', 'b']).issubset(['b', 'a', 'foo', 'bar'])
all(x in ['b', 'a', 'foo', 'bar'] for x in ['a', 'b'])
line.translate(none, '!@#$')
line = re.sub('[!@#$]', '', line)
string.replace('1', '')
a = a.replace(char, '')
a = a.replace(char, '') 
line = line.translate(string.maketrans('', ''), '!@#$')
pd.concat([df, pd.get_dummies(df, '', '').astype(int)], axis=1)[order]
[3, 4, 1, 2]
globals()['something'] = 'bob'
re.sub('([a-z](?=[a-z])|[a-z](?=[a-z][a-z]))', '\\1 ', text)
print('ex\xe1mple'.upper())
[l.split('\\')[-1] for l in list_dirs]
dict(zip(keys, values))
formatter = logging.formatter('%(asctime)s;%(levelname)s;%(message)s')
new_string = re.sub('"(\\d+),(\\d+)"', '\\1.\\2', original_string)
subprocess.call('test.sh otherfunc')
subprocess.popen(['bash', '-c', '. foo.sh; go'])
""" """.join(foo.split())
list('{0:0b}'.format(8))
[int(x) for x in list('{0:0b}'.format(8))]
[int(x) for x in bin(8)[2:]]
dict(zip(my_list, map(my_dictionary.get, my_list)))
numpy.dstack(numpy.meshgrid(x, y)).reshape(-1, 2)
driver.implicitly_wait(60)
driver.switch_to_frame('framename')
time.strftime('{%y-%m-%d %h:%m:%s}')
sorted(['14:10:01', '03:12:08'])
re.findall('(?:\\w+(?:\\s+\\w+)*,\\s)+(?:\\w+(?:\\s\\w+)*)', x)
df1.groupby(['key', 'year']).size().reset_index()
sorted(list(dictionary.items()), key=operator.itemgetter(1))
sorted(iter(d.items()), key=lambda x: x[1])
sorted(list(dictionary.items()), key=lambda x: x[1])
np.split(a, [-1])
df.pivot(index='order', columns='sample')
df[(df['a'] > 1) | (df['b'] < -1)]
[list(a) for a in zip([1, 2, 3], [4, 5, 6], [7, 8, 9])]
print(df.loc[df['a'] == 'foo'])
df.loc[df['column_name'] != some_value]
df.loc[~df['column_name'].isin(some_values)]
df.loc[df['column_name'] == some_value]
print(df.loc[df['b'].isin(['one', 'three'])])
"""""".join(map(lambda x: x * 7, 'map'))
os.rmdir()
shutil.rmtree(path, ignore_errors=false, onerror=none)
os.removedirs(name)
df.loc[len(df)] = ['8/19/2014', 'jun', 'fly', '98765']
glob.glob('*')
glob.glob('[!hello]*.txt')
glob.glob('hello*.txt')
eval('20<30')
new_list = [x[:] for x in old_list]
"""{:.50f}""".format(float(a[0] / a[1]))
df.to_sparse(0)
print([obj.attr for obj in my_list_of_objs])
sum(1 if d['success'] else 0 for d in s)
sum(d['success'] for d in s)
imp.find_module('os')[1]
(bool(a) != bool(b))
((a and (not b)) or ((not a) and b))
(bool(a) ^ bool(b))
xor(bool(a), bool(b))
return (bool(str1) ^ bool(str2))
my_list.sort(key=operator.itemgetter('name'))
re.split('\\s*,\\s*|\\s*;\\s*', 'a , b; cdf')
[t.strip() for s in string.split(',') for t in s.split(';')]
f = lambda x, y: x + y
instancelist = [myclass() for i in range(29)]
{f[i + 1]: [f[i], f[i + 2]] for i in range(0, len(f), 3)}
struct.unpack('>q', s)[0]
pd.concat([students, pd.dataframe(marks)], axis=1)
alist.sort(key=lambda x: x.foo)
soup.select('div[id$=_answer]')
linsolve(matrix(([1, 1, 1, 1], [1, 1, 2, 3])), (x, y, z))
{k: bigdict[k] for k in list(bigdict.keys()) & {'l', 'm', 'n'}}
dict((k, bigdict[k]) for k in ('l', 'm', 'n'))
{k: bigdict.get(k, none) for k in ('l', 'm', 'n')}
{k: bigdict[k] for k in ('l', 'm', 'n')}
driver.page_source
data[:, ([1, 9])]
re.sub('\\[.*?\\]', '', 'abcd[e]yth[ac]ytwec')
root.geometry('500x500')
re.findall('\\b(?:b+a)+b+\\b', mystring)
str_list = [tuple('{0:.8e}'.format(flt) for flt in sublist) for sublist in lst]
str_list = [['{0:.8e}'.format(flt) for flt in sublist] for sublist in lst]
t = tuple(x[0] for x in s)
datetime.datetime.now().strftime('%a')
ord('a') 
ord('\u3042')
ord()
json.load(u)
yourdf.drop(['columnheading1', 'columnheading2'], axis=1, inplace=true)
[s.strip() for s in input().split(',')]
[int(d) for d in str(bin(x))[2:]]
max(len(word) for word in i)
len(max(i, key=len))
os.system(my_cmd)
mylist.sort(key=lambda x: x.lower())
mylist.sort(key=str.lower)
mylist.sort()
list.sort()
df.set_index(['company', 'date'], inplace=true)
getattr(your_obj, x)
s.split(' ', 1)[1]
workbook = xlsxwriter.workbook('app/smth1/smth2/expenses01.xlsx')
workbook = xlsxwriter.workbook('c:/users/steven/documents/demo.xlsx')
pyplot.legend(loc=2, fontsize='x-small')
plot.legend(loc=2, prop={'size': 6})
[l[i:i + n] for i in range(0, len(l), n)]
[l[i:i + n] for i in range(0, len(l), n)] 
df['a'].str.contains('-')
re.sub("[^\\w' ]", '', "doesn't this mean it -technically- works?")
print(re.findall('\\d+', '\n'.join(re.findall('\xab([\\s\\s]*?)\xbb', text))))
monthly_mean.reset_index().plot(x='index', y='a')
subprocess.check_output('echo "foo"', shell=true)
[x.encode('utf8') for x in employeelist]
pandas.concat([df['foo'].dropna(), df['bar'].dropna()]).reindex_like(df)
list(range(9))
"""""".join(chr(i) for i in myintegers)
super(executive, self).__init__(*args)
[item for item in my_sequence if item != 'item']
random.choice(foo)
set(['a', 'b']).issubset(['a', 'b', 'c'])
set(['a', 'b']).issubset(set(l))
p = popen(['grep', 'f'], stdout=pipe, stdin=pipe, stderr=stdout) grep_stdout = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n')[0]
p = subprocess.popen(['grep', 'f'], stdout=subprocess.pipe, stdin=subprocess.pipe) p.stdin.write('one\ntwo\nthree\nfour\nfive\nsix\n') p.communicate()[0] p.stdin.close()
[list(t) for t in zip(*list_of_tuples)]
zip(*list_of_tuples)
pd.merge(y, x, on='k')[['a', 'b', 'y']]
[item.strip() for item in my_string.split(',')]
print((obj.__dict__))
dir()
dir() 
window.set_position(gtk.windowposition.center)
plt.rc('font', **{'size': '30'})
df.isnull().values.any()
some_func(*params)
urllib.parse.unquote(h.path.encode('utf-8')).decode('utf-8')
(trace_df['ratio'] > 0).mean()
emaillist = '\n'.join(item[0] for item in queryresult)
[item[0] for item in queryresult]
emaillist = '\n'.join([item[0] for item in queryresult])
print(('focus object class:', window2.focus_get().__class__))
a = [0] * 10000
print(' '.join(sorted(set(words), key=words.index)))
random.sample(range(1, 50), 6)
random.sample(range(1, 50), 6) 
{k.lower(): v.lower() for k, v in list({'my key': 'my value'}.items())}
dict((k.lower(), v) for k, v in {'my key': 'my value'}.items())
dict((k.lower(), v.lower()) for k, v in {'my key': 'my value'}.items())
[sorted(item) for item in data]
names = list(map(lambda x: x[0], cursor.description))
os.path.abspath(__file__)
sorted(matrix, key=itemgetter(1))
[index for index, letter in enumerate(word) if letter == 'e']
print(str(x).decode('raw_unicode_escape'))
re.findall('\\w', 'abcdefg')
os.path.isfile(fname)
my_file = path('/path/to/file') if my_file.is_file():     pass
os.path.exists(file_path)
print(os.path.isfile('/etc/password.txt'))
print(os.path.isfile('/etc'))
print(os.path.exists('/does/not/exist'))
print(os.path.isfile('/does/not/exist'))
print(os.path.exists('/etc'))
print(os.path.exists('/etc/password.txt'))
"""a;bcd,ef g""".replace(';', ' ').replace(',', ' ').split()
list(i for i in range(3))
writer.writeheader()
[(a, b, c) for a, (b, c) in l]
"""0x{0:08x}""".format(3652458)
[(v, k) for k, v in list(d.items())]
[(v, k) for k, v in d.items()]
[(v, k) for k, v in a.items()]
[(k, v) for k, v in a.items()]
[int(x, 16) for x in ['bb', 'a7', 'f6', '9e']]
[int(x, 16) for x in l]
var1, var2 = input('enter two numbers here: ').split()
test.objects.filter(actions__contains=[{'fixed_key_1': 'foo2'}])
itertools.product(list(range(2)), repeat=4)
(datetime.now() - timedelta(1)).strftime('%y-%m-%d')
np.dot([1, 0, 0, 1, 0, 0], [[0, 1], [1, 1], [1, 0], [1, 0], [1, 1], [0, 1]])
df['date'] = pd.to_datetime(df['date'], format='%d%b%y')
sys.path.insert(0, '/path/to/application/app/folder') import file
x.reset_index().merge(y, how='left', on='state', sort=false).sort('index')
json.loads(request.post.get('mydata', '{}'))
list(zip(*((iter([1, 2, 3, 4, 5, 6, 7, 8, 9]),) * 3)))
list(grouper(2, [1, 2, 3, 4, 5, 6, 7]))
[input[i:i + n] for i in range(0, len(input), n)]
keys.sort(key=lambda x: map(int, x.split('.')))
keys.sort(key=lambda x: [int(y) for y in x.split('.')])
img.transpose(2, 0, 1).reshape(3, -1)
df['brandname'].replace(['abc', 'ab'], 'a')
df['brandname'] = df['brandname'].replace(['abc', 'ab'], 'a')
df.sub(df.mean(axis=1), axis=0)
"""""".join([i for i in s if i.isalpha()])
l = (int(x) for x in s.split())
"""42 0""".split()
map(int, '42 0'.split())
[i for i, elem in enumerate(bool_list, 1) if elem]
data.groupby(data['date'].map(lambda x: x.year))
np.in1d(b, a).nonzero()[0]
time.strftime('%l:%m%p %z on %b %d, %y')
ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)
"""""".join(['x', 'x', 'x'])
x[(np.arange(x.shape[0]) != 1), :, :]
print(item['name'])
result = sys.stdin.read()
"""""".join(soup.findall(text=true))
data[data['value'] == true]
"""""".join(set(foo))
sorted(profile.objects.all(), key=lambda p: p.reputation)
df.values.flatten()
users.sort(key=lambda x: order.index(x['id']))
users.sort(key=lambda x: order.index(x['id'])) 
r = requests.get('<my_uri>', headers={'authorization': 'tok:<my_token>'})
print('"hello,\\nworld!"'.decode('string_escape'))
re.findall('a*?bc*?', 'aabcc', re.dotall)
a.shape[1]
d.apply(lambda row: min([row['a'], row['b']]) - row['c'], axis=1)
"""abcdabcva""".count('ab')
[d['key'] for d in l if 'key' in d]
[d['key'] for d in l]
[d['key'] for d in l] 
l1.sort(key=lambda x: int(x[0]))
sorted([[1, 'mike'], [1, 'bob']])
"""abc""".translate(maketrans('abcabc', 'defdef'))
"""<br/>""".join([('%s:: %s' % (key, value)) for key, value in list(d.items())])
self.writer.writerow([str(s).encode('utf-8') for s in row])
os.system('cls')
os.system('clear')
os.system('tcsh your_own_script')
os.system("zsh -c 'echo $0'")
[dict(d, count=n) for d, n in zip(l1, l2)]
[sum(x) for x in zip(*l)]
map(sum, zip(*l))
np.count_nonzero(~np.isnan(data))
map(list, zip(*main_list))
request.post.get('title', '')
"""test.mp3""".endswith(('.mp3', '.avi'))
re.findall('\\[[^\\]]*\\]|"[^"]*"|\\s+', s)
data.apply(lambda x: sorted(x, 3))
os.chdir('c:/users/name/desktop')
re.findall('\\$([^$]*)\\$', string)
re.findall('\\$(.*?)\\$', '$sin (x)$ is an function of x')
datetime.datetime.strptime(str_date, '%m/%d/%y').date().isoformat()
a[[0, 1], [0, 1]]
a[np.arange(3), (0, 1, 0)]
[k for k, v in dicta.items() if v.count('duck') > 1]
[[2, 3, 4], [2, 3, 4], [2, 3, 4]]
print(arr[1, 1])
quadmesh.set_clim(vmin=0, vmax=15)
my_data = genfromtxt('my_file.csv', delimiter=',')
df = pd.read_csv('myfile.csv', sep=',', header=none)
np.genfromtxt('myfile.csv', delimiter=',')
np.genfromtxt('myfile.csv', delimiter=',', dtype=none)
my_string.splitlines()[0]
my_string.split('\n', 1)[0]
df.values.tolist()
re.sub('\\*\\*+', '*', text)
re.sub('\\*+', '*', text)
dict((k, v * dict2[k]) for k, v in list(dict1.items()) if k in dict2)
return ''.join(random.choice(string.lowercase) for i in range(length))
sum(len(x) for x in list(food_colors.values()))
sum(len(v) for v in food_colors.values())
all(a_list)
"""""".join(c for c in text if c not in 'aeiouaeiou')
[(x / y) for x, y in zip(a, b)]
re.findall('abc(de)fg(123)', 'abcdefg123 and again abcdefg123')
df.groupby('type').apply(lambda x: np.mean(np.log2(x['v'])))
[key for key, value in list(my_dict.items()) if set(value).intersection(lst)]
[key for item in lst for key, value in list(my_dict.items()) if item in value]
c = [[(i + j) for i, j in zip(e, b)] for e in a]
os.path.commonprefix(['/usr/var', '/usr/var2/log'])
print(os.path.relpath('/usr/var/log/', '/usr/var'))
grouped.filter(lambda x: len(x) > 1)
sorted(list(mydict.items()), key=lambda e: e[1][2])
"""hello {name}, how are you {name}, welcome {name}""".format(name='john')
df.reindex(['z', 'c', 'a'])
any(isinstance(el, list) for el in input_list)
len(items)
len([1, 2, 3])
items.__len__()
len()
len(s)
df.sort(axis=1, ascending=false)
df.sort(df.columns, axis=1, ascending=false)
df.groupby(['col5', 'col2']).size().groupby(level=1).max()
'x' in ['x', 'd', 'a', 's', 'd', 's']
mydict.pop('key', none)
del mydict[key]
try:     del mydict[key] except keyerror:     pass try:     del mydict[key] except keyerror:     pass
parser.add_argument('input', nargs='+')
pyplot.plot(x, y, color='#112233')
re.sub('<[^<]+?>', '', text)
a[np.in1d(a, b)]
"""jvm.args= -dappdynamics.com=true, -dsomeotherparam=false,""".split('=', 1)
print('[%s]' % ', '.join('%.3f' % val for val in list))
print('[' + ', '.join('%5.3f' % v for v in l) + ']')
print([('%5.3f' % val) for val in l])
os.chdir('..')
print(text.encode('windows-1252'))
struct.unpack('d', struct.pack('q', int(s2, 0)))[0]
float(int('-0b1110', 0))
struct.unpack('d', b8)[0]
df.colour.value_counts().plot(kind='bar')
df.groupby('colour').size().plot(kind='bar')
line.strip().split(' ')
df.groupby(lambda idx: 0).agg(['mean', 'std'])
sorted(list(tag_weight.items()), key=lambda x: int(x[1]), reverse=true)
int(math.ceil(x)) - 1
if (not mystring):     pass
if (not some_string):     pass
if (not my_string):     pass
if some_string:     pass
it = iter(sorted(d.items()))
for (key, value) in sorted(d.items()):     pass
return sorted(dict.items())
return iter(sorted(dict.items()))
for (k, v) in sorted(foo.items()):     pass
for k in sorted(foo.keys()):     pass
last = len(s) - s[::-1].index(x) - 1
str1 = ''.join(list1)
' '.join((str(x) for x in l))
str1 = ''.join((str(e) for e in list1))
makeitastring = ''.join(map(str, l))
[x for x in l if x is not none]
random.choice([1, 2, 3])
x = [[none for _ in range(5)] for _ in range(6)]
a[(np.random.choice(a.shape[0], 2, replace=false)), :]
a[(np.random.randint(a.shape[0], size=2)), :]
df.groupby(df.index).sum()
root.findall('{http://www.w3.org/2002/07/owl#}class')
"""""".join(random.choice(string.lowercase) for x in range(x))
sys.path.append('/path/to/2014_07_13_test')
int(round(x))
h = int(round(h))
round(32.268907563, 3)
round(value, significantdigit)
round(1.0005, 3)
round(2.0005, 3)
round(3.0005, 3)
round(4.0005, 3)
round(8.005, 2)
round(7.005, 2)
round(6.005, 2)
round(1.005, 2)
df['cat1'].fillna(df['cat2'])
logging.info('date=%s', date)
logging.info('date={}'.format(date))
{k: int(v) for k, v in d.items()}
map(sum, zip(*lists))
s.decode('hex')
binascii.a2b_hex(s)
connection.send('http/1.0 200 established\r\n\r\n')
connection.send('http/1.0 200 ok\r\n\r\n')
df['x']['c'] = 10
np.sqrt(np.square(df).sum(axis=1))
sorted(set(my_list))
max(enumerate(a), key=lambda x: x[1])[0]
[d['name'] for d in thisismylist]
[(d['name'], d['age']) for d in thisismylist]
model.objects.all().order_by('?')[0]
os.system('script2.py 1')
re.findall('\\w+(?:-\\w+)+', text)
parser.add_argument('--conf', nargs=2, action='append')
random.sample(list(range(1, 16)), 3)
strings.sort(key=lambda str: re.sub('.*%(.).*', '\\1', str))
strings.sort(key=lambda str: re.sub('.*%', '', str))
listy = [[] for i in range(3)]
a = np.array(sorted(a, key=tuple))
[(x + y) for x in '12345' for y in 'ab']
' hello '.strip()
mystring.strip()
' hello '.strip() 
' hello'.strip()
'bob has a cat'.strip()
'          hello        '.strip()
str.strip()
mystring.strip('\n')
mystring.lstrip('\n\r')
mystring.rstrip('\n\t')
'  hello\n'.strip(' ')
sorted(unsorted, key=lambda element: (element[1], element[2]))
print(content.decode('utf8'))
np.ma.array(np.tile(arr, 2).reshape(2, 3), mask=~cond).argmax(axis=1)
pd.to_datetime(df.id.str[1:-3])
df = pd.read_csv('my.csv', dtype={'my_column': np.float64}, na_values=['n/a'])
df = pd.read_csv('my.csv', na_values=['n/a'])
list(itertools.product(*a)) 
re.sub('[^a-z]', '', s)
datetime.strptime('2011221', '%y%w%w')
codecs.open('myfile', 'r', 'iso-8859-1').read()
[f(x) for x in list]
re.findall('(?<!\\d)\\d{5}(?!\\d)', s)
[item for item in a if sum(item) > 10]
cents_int = int(round(float(dollars.strip('$')) * 100))
"""""".join(dropwhile(lambda x: x in bad_chars, example_line[::-1]))[::-1]
l = []
l = list()
list()
[]
sys.exit(0)  
s[:4] + '-' + s[4:]
[[] for i in range(3)]
a = [[] for i in range(3)]
requests.get(url, headers={'referer': my_referer})
pylab.ylim([0, 1000])
pd.get_dummies(s.apply(pd.series).stack()).sum(level=0)
max(abs(x - y) for x, y in zip(values[1:], values[:-1]))
y = str(int(x, 16))
a.isdigit()
isdigit()
b.isdigit()
pd.read_csv(stringio(s), sep=',', comment='#')
df['date'] = df['date'].apply(lambda x: int(str(x)[-4:]))
sum(list_of_nums)
max(lst, key=lambda x: x['score'])
soup.findall(attrs={'name': 'description'})
str({'a': 1, 'b': 'as df'}).replace(': ', ':').replace(', ', ',')
'{' + ','.join('{0!r}:{1!r}'.format(*x) for x in list(dct.items())) + '}'
"""""".join(parts[1:])
""",+""".join(c.rsplit('+', 1))
a[np.all(a != 0, axis=1)]
""" """.join(re.split('[^a-za-z]*', 'your string'))
re.split('[^a-za-z]*', 'your string')
results_union = set().union(*results_list)
return list(set(itertools.chain(*result_list)))
np.any(np.in1d(a1, a2))
return ''.join(ch for ch in s if unicodedata.category(ch)[0] != 'c')
all(i < j for i, j in zip(a, b))
driver.find_element_by_css_selector('.button.c_button.s_button').click()
driver.find_element_by_css_selector('.button .c_button .s_button').click()
os.system('taskkill /im make.exe')
print(select([my_table, func.current_date()]).execute())
re.sub('([a-z])\\1+', '\\1', 'ffffffbbbbbbbqqq')
re.sub('(?<!\\w)([a-z])\\.', '\\1', s)
split_list = [the_list[i:i + n] for i in range(0, len(the_list), n)]
re.sub('\\b(this|string)\\b', '<markup>\\1</markup>', 'this is my string')
pandas.set_option('display.max_columns', 7)
pandas.set_option('display.max_columns', none)
df.ix[df.a == 0, 'b'] = np.nan
driver.find_element_by_xpath("//li/label/input[contains(..,'polishpottery')]")
mylist.sort(key=operator.itemgetter('weight', 'factor'))
mylist.sort(key=lambda d: (d['weight'], d['factor']))
{x[1]: x for x in lol}
sorted(d, key=lambda k: d[k][1])
int(round(123, -2))
fd = os.open('x', os.o_wronly | os.o_creat | os.o_excl)
new_list = [x.split()[-1] for x in original_list]
'hello world'[::(-1)]
s[::(-1)]
''.join(reversed('foo'))
''.join(reversed(string))
'foo'[::(-1)]
a_string[::(-1)]
def reversed_string(a_string):     return a_string[::(-1)]
''.join(reversed(s))
""",""".join(str(i) for i in range(100) if i % 4 in (1, 2))
dict([(e[0], int(e[1])) for e in lst])
sorted(list_of_tuples, key=lambda tup: tup[::-1])
sorted(list_of_tuples, key=lambda tup: tup[1])
numpy.concatenate([a, b])
for item in thelist:     thefile.write(('%s\n' % item))
for item in thelist:     pass
pickle.dump(itemlist, outfile)
outfile.write('\n'.join(itemlist))
session.query(user).filter_by(id=123).update({'name': 'bob marley'})
r = requests.post('http://wikipedia.org', cookies=cookie)
sys.path.insert(0, 'libs')
datetime.datetime.now()
datetime.datetime.now().time()
strftime('%y-%m-%d %h:%m:%s', gmtime())
str(datetime.now())
datetime.datetime.time(datetime.datetime.now())
ord('\xff')
df.groupby(['pplnum', 'roomnum']).cumcount() + 1
datetime.utcnow()
a[-1:] + a[:-1]
df.set_index(['year', 'month', 'item']).unstack(level=-1)
df.pivot_table(values='value', index=['year', 'month'], columns='item')
print('\n\x1b[4m' + '3' + '\x1b[0m' + '\n2')
li1.sort(key=lambda x: not x.startswith('b.'))
range(10, 0, -1)
name[0].firstchild.nodevalue
thread.start_new_thread(myfunction, ('mystringhere', 1))
thread.start_new_thread(myfunction, ('mystringhere', 1)) 
a.index(max(a))
re.sub('\\.(?=[^ .])', '. ', para)
[i.split() for i in re.findall('\\[([^\\[\\]]+)\\]', a)]
[d for d in a if d['name'] == 'pluto']
[d for d in a if d['name'] == 'pluto'] 
list(d.values())
re.sub(' +', ' ', s)
os.chmod('my_script.sh', 484)
df.to_csv('c:\\data\\t.csv', index=false)
re.sub('\\w*\\d\\w*', '', words).strip()
dogtail.rawinput.click(100, 100)
datetime.strptime('2009/05/13 19:19:30 -0400', '%y/%m/%d %h:%m:%s %z')
re.search('\\bis\\b', string).start()
re.search('is', string).start()
tuple(map(int, input().split(',')))
tuple(int(x.strip()) for x in input().split(','))
str.decode('utf-8').replace('\u2022', '*').encode('utf-8')
str.decode('utf-8').replace('\u2022', '*')
np.zeros((3, 3)).ravel()
import platform platform.system()
import platform platform.release()
print(os.name)
[x for x in my_list if not x.startswith('#')]
"""day old bread, 50% sale {0}""".format('today')
min(list, key=lambda x: float('inf') if math.isnan(x[1]) else x[1])
a = [(sum(x) / len(x)) for x in zip(*a)]
logging.info('log message', extra={'app_name': 'myapp'})
df.applymap(lambda x: isinstance(x, (int, float)))
sorted(l, key=lambda x: int(re.search('\\d+', x).group(0)))
self.root.destroy()
df.iloc[:, ([2, 5, 6, 7, 8])].mean(axis=1)
df[df.index.map(lambda x: x[1].endswith('0630'))]
db.session.delete(page)
"""""".join(chr(ord(c)) for c in 'andr\xc3\xa9')
"""""".join(chr(ord(c)) for c in 'andr\xc3\xa9').decode('utf8')
for (dirname, dirnames, filenames) in os.walk('.'):     for subdirname in dirnames:         print(os.path.join(dirname, subdirname))     for filename in filenames:         pass
os.listdir(path)
os.rename(dir, dir + '!')
"""-""".join(a + b for a, b in zip(s[::2], s[1::2]))
print('%.3f' % 3.1415)
data[0]['f'] = var
print(a_module.__file__)
print(os.getcwd())
path = os.path.abspath(amodule.__file__)
self.mylist.extend([0] * (4 - len(self.mylist)))
df[~df.index.duplicated()]
foo(*i)
[('%.2d' % i) for i in range(16)]
sorted(iter(mydict.items()), key=lambda tup: sum(tup[1]), reverse=true)[:3]
heapq.nlargest(3, iter(mydict.items()), key=lambda tup: sum(tup[1]))
['a', 'b'].index('b')
plt.setp(legend.get_title(), fontsize='xx-small')
int('  23  ')
[x[1] for x in elements]
np.diag(np.rot90(array))
list(chain.from_iterable(a))
re.sub('\\s{2,}', '|', line.strip())
print(('%.2f' % a))
print(('{0:.2f}'.format(a)))
print(('{0:.2f}'.format(round(a, 2))))
print(('%.2f' % round(a, 2)))
('%.2f' % 13.9499999)
('%.2f' % 3.14159)
float('{0:.2f}'.format(13.95))
'{0:.2f}'.format(13.95)
dataframe.from_csv('c:/~/trainsetrel3.txt', sep='\t')
dateutil.parser.parse('2013/09/11 00:17 +0900')
cur.mogrify('select * from table where column in %s;', ((1, 2, 3),))
sum([sum(x) for x in [[1, 2, 3, 4], [2, 4, 5, 6]]])
next(iter(dict.values()))
next(iter(list(dict.values())))
df.groupby(['month', 'fruit']).sum().unstack(level=0)
sorted(mylist, key=lambda x: order.index(x[1]))
sorted(persons, key=lambda x: x['passport']['birth_info']['date'])
urlparse.urldefrag('http://www.address.com/something#something')
urllib.request.urlretrieve('http://example.com/file.ext', '/path/to/dir/filename.ext')
list(set(frozenset(item) for item in l))
[set(item) for item in set(frozenset(item) for item in l)]
p.terminate()
del mylist[:]
ctypes.windll.user32.messageboxw(0, 'error', 'error', 0)
str_list = list([_f for _f in str_list if _f])
re.sub('[\\ \\n]{2,}', '', yourstring)
re.sub('\\.[^.]+$', '', s)
a[np.all(np.any(a - b[:, (none)], axis=2), axis=0)]
a.to_csv('test.csv', cols=['sum'])
exec(compile(open('test2.py').read(), 'test2.py', 'exec'))
subprocess.call('test1.py', shell=true)
sorted(zipped, key=lambda x: x[1])
zipped.sort(key=lambda t: t[1])
sorted(list(y.items()), key=lambda x: (x[1], x[0]), reverse=true)
soup.find_all('div', class_='crblock ')
[element for i, element in enumerate(centroids) if i not in index]
list(set(lista) & set(listb))
testfile = urllib.request.urlopener() testfile.retrieve('http://randomsite.com/file.gz', 'file.gz')
urllib.request.urlretrieve('http://randomsite.com/file.gz', 'file.gz')
file_name = wget.download(file_url)
ax.set_yticklabels(['\xe9', '\xe3', '\xe2'])
list(itertools.product(list(range(-x, y)), repeat=dim))
print(s.encode('unicode_escape'))
'hello %s' % ', '.join(my_args)
re.split('(ddd)', 'aaa bbb ccc ddd eee fff', 1)
re.split('(d(d)d)', 'aaa bbb ccc ddd eee fff', 1)
pd.dataframe(d)
"""this is a string""".split()
"""this     is a     string""".split()
my_series.apply(your_function, args=(2, 3, 4), extra_kw=1)
woduplicates = list(set(lseperatedorblist))
sum([(i * j) for i, j in list(itertools.combinations(l, 2))])
re.compile('{}-\\d*'.format(user))
[float(i) for i in lst]
from functools import reduce reduce(lambda x, y: x * y, [1, 2, 3, 4, 5, 6])
writer.writerow(a)
writer.writerows(a)
"""{} %s {}""".format('foo', 'bar')
example = [x.replace('\r\n', '') for x in example]
[i.partition('\t')[-1] for i in l if '\t' in i]
re.search('test(.*)print', teststr, re.dotall)
next = driver.find_element_by_css_selector('li.next>a')
os.stat('c:\\python27\\lib\\genericpath.py').st_size
imtag = re.match('<img.*?>', line).group(0)
os.rename('joe blow', 'blow, joe')
re.findall('(?=(\\w\\w))', 'hello')
bin(173)
int('01010101111', 2)
int('010101', 2)
int('0b0010101010', 2)
bin(21)
int('11111111', 2)
re.sub('$\\d+\\w+|\\b\\d+\\b|\\w+\\d+$', '', s)
re.sub('\\b\\d+\\b', '', s)
s = re.sub('^\\d+\\s|\\s\\d+\\s|\\s\\d+$', ' ', s)
s.split(':', 1)[1]
print(s.split(','))
mystring.split(',')
re.sub('\\((\\w+)\\)', '\\1', s)
webbrowser.open_new(url)
webbrowser.open('http://example.com')
self.pushbutton.setstylesheet('background-color: red')
[x(y) for x, y in zip(functions, values)]
wx.textctrl(self, -1, size=(300, -1))
imshow(imagearray, cmap='greys_r')
df.fillna(0)
df.topandas().to_csv('mycsv.csv')
df.write.csv('mycsv.csv')
sum(x[1] for x in structure)
df.groupby('stname')['county_pop'].agg(lambda x: x.nlargest(3).sum())
datetime.strptime('21/11/06 16:30', '%d/%m/%y %h:%m')
os.path.dirname(os.path.abspath(__file__))
re.sub('(.)', '\\1\\1', text.read(), 0, re.s)
"""""".join(('a', 'b', 'c', 'd', 'g', 'x', 'r', 'e'))
os.path.dirname(os.path.abspath(__file__)) 
"""{0:.{1}%}""".format(value, digits)
self.request.url
random_choice = random.choice(choices)
length = sum(len(s) for s in strings)
s = sorted(s, key=lambda x: (x[1], x[2]))
s.sort(key=operator.itemgetter(1, 2))
con.commit()
[k for k in lst if 'ab' in k]
output = ''.join(item[0].upper() for item in input.split())
custompk._meta.pk.name
len(s.split())
np.einsum('ji,i->j', a, b)
sys.version
sys.version_info
print('\\num{{{0:.2g}}}'.format(1000000000.0))
x = [[] for i in range(3)]
{{my_variable | forceescape | linebreaks}}
zip(*[(1, 4), (2, 5), (3, 6)])
[list(group) for key, group in itertools.groupby(data, operator.itemgetter(1))]
list('hello')
df['a_perc'] = df['a'] / df['sum']
os.walk(directory)
[x[0] for x in os.walk(directory)]
{i: 'updated' for i, j in list(d.items()) if j != 'none'}
dict((k, 'updated') for k, v in d.items() if v is none)
dict((k, 'updated') for k, v in d.items() if v != 'none')
df.groupby(key_columns).size()
result = [sum(b) for b in a]
any(d['site'] == 'superuser' for d in data)
nodes = [[node() for j in range(cols)] for i in range(rows)]
print(os.path.splitext('/home/user/somefile.txt')[0] + '.jpg')
pygame.display.set_mode((0, 0), pygame.fullscreen)
ax.set_title('$%s \\times 10^{%s}$' % ('3.5', '+20'))
print(os.path.getmtime('/tmp'))
today.strftime('%b')
today.strftime('%b') 
[j for i in x for j in i]
print(list(itertools.chain.from_iterable(a)))
datetime.datetime.strptime('january 11, 2010', '%b %d, %y').strftime('%a')
datetime.datetime.strptime('january 11, 2010', '%b %d, %y').strftime('%a') 
a.remove('b')
a.remove(c)
a.remove(6)
a.remove(6) 
if (c in a):     a.remove(c)
try:     a.remove(c) except valueerror:     pass
re.findall('(?=(a.*?a))', 'a 1 a 2 a 3 a 4 a')
np.einsum('ij,kj->jik', x, x)
some_list[(-1)]
some_list[(-2)]
some_list[(- n)]
alist[(-1)]
astr[(-1)]
print([u for v in [[i, i] for i in range(5)] for u in v])
[0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
[(i // 2) for i in range(10)]
s[s.find('\n') + 1:s.rfind('\n')]
{(x ** 2) for x in range(100)}
zip(*[[1, 2], [3, 4], [5, 6]])
zip(*[[1, 2], [3, 4], [5, 6]]) 
requests.get('https://www.mysite.com/', auth=('username', 'pwd'))
x[2:]
x[:2]
x[:(-2)]
x[(-2):]
x[2:(-2)]
some_string[::(-1)]
'h-e-l-l-o- -w-o-r-l-d'[::2]
s = s[beginning:(beginning + length)]
sys.exit() 
quit()
sys.exit('some error message')
data['city'].encode('ascii', 'ignore')
psutil.cpu_percent() psutil.virtual_memory()
pid = os.getpid() py = psutil.process(pid) memoryuse = (py.memory_info()[0] / (2.0 ** 30))
print((psutil.cpu_percent())) print((psutil.virtual_memory()))
pd.read_csv('d:/temp/tt.csv', names=list('abcdef'))
df.stack().groupby(level=0).first()
"""{0} {1}""".format(10, 20)
"""{1} {ham} {0} {foo} {1}""".format(10, 20, foo='bar', ham='spam')
changed_list = [(int(f) if f.isdigit() else f) for f in original_list]
dict(zip(keys, zip(*data)))
apple.decode('iso-8859-1').encode('utf8')
df.to_csv('filename.csv', header=false)
print('{0}:<15}}{1}:<15}}{2}:<8}}'.format('1', '2', '3'))
max(ld, key=lambda d: d['size'])
"""{0}\\w{{2}}b{1}\\w{{2}}quarter""".format('b', 'a')
user = models.foreignkey('user', unique=true)
re.compile('^([^a]*)aa([^a]|aa)*$')
b = np.concatenate((a, a), axis=0)
sorted(l, key=lambda x: x.replace('0', 'z'))
ax.set_yscale('log')
os.environ['home']
os.environ['home'] 
print(os.environ)
os.environ
print(os.environ.get('key_that_might_exist'))
print(os.getenv('key_that_might_exist', default_value))
print(os.environ.get('home', '/home/username/'))
print(dict([s.split('=') for s in my_list]))
min(enumerate(a), key=lambda x: abs(x[1] - 11.5))
e = root.xpath('.//a[contains(text(),"text a")]')
e = root.xpath('.//a[starts-with(text(),"text a")]')
e = root.xpath('.//a[text()="text a"]')
c = [b[i] for i in index]
np.dot(a[:, (none)], b[(none), :])
np.outer(a, b)
subprocess.call(['./abc.py', arg1, arg2])
df[['value']].fillna(df.groupby('group').transform('mean'))
re.sub('(.)(?=.)', '\\1-', s)
re.sub('(?<=.)(?=.)', '-', str)
i, j = np.where(a == value)
print(collections.counter(s).most_common(1)[0])
float(re.findall('(?:^|_)' + par + '(\\d+\\.\\d*)', dir)[0])
re.findall('[^a]', 'abcd')
print([item for item in dir(adfix) if not item.startswith('__')])
[x[0] for x in rows]
res_list = [x[0] for x in rows]
pd.concat([x] * 5, ignore_index=true)
pd.concat([x] * 5)
sorted_list_of_keyvalues = sorted(list(ips_data.items()), key=item[1]['data_two'])
pd.read_json(elevations)
numpy.random.choice(numpy.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])
df.loc[df['value'].idxmax()]
re.findall('^(.+?)((.+)\\3+)$', '42344343434')[0][:-1]
np.fromstring('\x00\x00\x80?\x00\x00\x00@\x00\x00@@\x00\x00\x80@', dtype='<f4')
np.fromstring('\x00\x00\x80?\x00\x00\x00@\x00\x00@@\x00\x00\x80@', dtype='>f4')
cursor.execute('insert into table values (?, ?, ?)', (var1, var2, var3))
cursor.execute('insert into table values (%s, %s, %s)', (var1, var2, var3))
cursor.execute('insert into table values (%s, %s, %s)', (var1, var2, var3)) 
df['stats'].str[1:-1].str.split(',', expand=true).astype(float)
df['stats'].str[1:-1].str.split(',').apply(pd.series).astype(float)
df['stats'].apply(pd.series)
p.wait()
s.encode('utf8')
datetime.datetime.strptime('01-jan-1995', '%d-%b-%y')
copyfile(src, dst)
shutil.copy2('/dir/file.ext', '/new/dir/newname.ext')
shutil.copy2('/dir/file.ext', '/new/dir')
print(', '.join(str(x) for x in list_of_ints))
df[['a', 'b']].multiply(df['c'], axis='index')
hex(ord('a'))
sum(j ** i for i, j in enumerate(l, 1))
""" """.join(s.split())
s = s.replace(',', '')
frame.resample('1h').agg({'radiation': np.sum, 'tamb': np.mean})
root.destroy()
df = pd.dataframe.from_dict({k: v for k, v in list(nvalues.items()) if k != 'y3'})
first_name = request.args.get('firstname')
first_name = request.form.get('firstname')
[s[:5] for s in buckets]
the_list.sort(key=lambda item: (-len(item), item))
df = df.set_index(['trx_date'])
list(accumulate(list(range(10))))
datetime.datetime.strptime('2013-1-25', '%y-%m-%d').strftime('%m/%d/%y')
datetime.datetime.strptime('2013-1-25', '%y-%m-%d').strftime('%-m/%d/%y')
df2 = df.ix[:, (~df.columns.str.endswith('prefix'))]
new_list = my_list[-10:]
my_list[-10:]
np.array(x._data).reshape(x.size[::-1]).t
df.groupby(level=0, as_index=false).nth(0)
numpy.concatenate(list, axis=0)
"""\\xc3\\x85あ""".encode('utf-8').decode('unicode_escape')
"""\\xc3\\x85あ""".encode('utf-8')
[j for i in zip(a, b) for j in i]
[j for i in zip(a, b) for j in i] 
print([s.replace('8', '') for s in lst])
""",""".join('hello')
content.objects.all().order_by('?')[:100]
a[np.arange(a.shape[0])[:, (none)], b]
df.pivot_table(index='saleid', columns='upc', aggfunc='size', fill_value=0)
re.findall('([a-z]*)', 'f233op')
re.findall('([a-z])*', 'f233op')
re.split('_for_', 'happy_hats_for_cats')
re.split('_(?:for|or|and)_', 'sad_pandas_and_happy_cats_for_people')
[re.split('_(?:f?or|and)_', s) for s in l]
[dict(zip(k, x)) for x in v]
sorted(lst, reverse=true)
order_array.sort(order=['year', 'month', 'day'])
df.sort(['year', 'month', 'day'])
return my_list == list(range(my_list[0], my_list[-1] + 1))
df.groupby('id').agg(lambda x: x.tolist())
'x\xc3\xbcy\xc3\x9f'.encode('raw_unicode_escape').decode('utf-8')
float(a)
try:     return int(s) except valueerror:     return float(s)
if hasattr(a, 'property'):     pass
if hasattr(a, 'property'):     pass 
getattr(a, 'property', 'default value')
np.delete(a, list(range(0, a.shape[1], 8)), axis=1)
datetime.datetime.fromtimestamp(ms / 1000.0)
np.einsum('...j,...j->...', vf, vf)
r = requests.get(url)
r = requests.get(url, params=payload)
r = requests.post(url, data=payload)
post_response = requests.post(url='http://httpbin.org/post', json=post_data)
{{(mylist | slice): '3:8'}}
df1 = pd.read_hdf('/home/.../data.h5', 'firstset')
max(test_string.rfind(i) for i in '([{')
print('here is your checkmark: ' + '\u2713')
print('\u0420\u043e\u0441\u0441\u0438\u044f')
print('{0}'.format('5'.zfill(2)))
sorted(set(itertools.chain.from_iterable(sequences)))
df['a'].values.tolist()
df['a'].tolist()
replace('"', '\\"')
print(all(word[0].isupper() for word in words))
mydict = {key: val for key, val in list(mydict.items()) if val != 42}
{key: val for key, val in list(mydict.items()) if val != 42}
return len(s.encode('utf-8'))
os.kill(process.pid, signal.sigkill)
df[pd.isnull(df).any(axis=1)]
url.split('&')[-1].replace('=', '') + '.html'
parser.parsefile(open('sample.xml', 'rb'))
sys.exit()  
setattr(self, attr, group)
urllib.parse.unquote(urllib.parse.unquote(some_string))
urllib.parse.unquote(urllib.parse.unquote('fireshot3%2b%25282%2529.png'))
app.config['security_register_url'] = '/create_account'
output = open('/home/user/test/wsservice/data.pkl', 'wb')
del a[(-1)]
a.pop(1)
a.pop()
a.pop(index)
del a[index]
ax.set_xlabel('temperature (\u2103)')
ax.set_xlabel('temperature ($^\\circ$c)')
[''.join(l) for l in list_of_lists]
pd.concat(g for _, g in df.groupby('id') if len(g) > 1)
x = numpy.delete(x, 2, axis=1)
x = numpy.delete(x, 0, axis=0)
pd.concat((df1, df2), axis=1).mean(axis=1)
np.mean(np.array([old_set, new_set]), axis=0)
scatter(x, y, s=500, color='green', marker='h')
result = [item for word in words for item in word.split(',')]
datetime.datetime.strptime('2012-05-29t19:30:03.283z', '%y-%m-%dt%h:%m:%s.%fz')
sum(item['one'] for item in list(tadas.values()))
a = open('pdf_reference.pdf', 'rb').read().encode('base64')
a.rstrip().split('\n')
a.split('\n')[:-1]
return httpresponse(status=204)
(7 in a)
('a' in a)
sorted(results, key=itemgetter('year'))
print(browser.current_url)
re.split('; |, ', str)
"""\\u003cp\\u003e""".decode('unicode-escape')
time.mktime(datetime.datetime.strptime(s, '%d/%m/%y').timetuple())
int(datetime.datetime.strptime('01/12/2011', '%d/%m/%y').strftime('%s'))
request.headers['your-header-name']
df.groupby('user')['x'].filter(lambda x: x.sum() == 0)
df.loc[df.groupby('user')['x'].transform(sum) == 0]
df.groupby('user')['x'].transform(sum) == 0
driver.find_elements_by_xpath("//*[contains(text(), 'my button')]")
df.set_index(['name', 'destination'])
print(re.sub('(\\w)\\1+', '\\1', a))
os.system('start "$file"')
unicodedata.normalize('nfkd', title).encode('ascii', 'ignore')
a.encode('ascii', 'ignore')
files = [f for f in os.listdir('.') if re.match('[0-9]+.*\\.jpg', f)]
np.zeros((6, 9, 20)) + np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])[(none), :, (none)]
np.zeros((6, 9, 20)) + np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape((1, 9, 1))
os.system('start excel.exe <path/to/file>')
print(max(x, key=sum))
sum(len(y) for y in x if len(y) > 1)
re.sub('(\\d+)', '"\\1"', 'this is number 1 and this is number 22')
numpy.dot(numpy.dot(a, m), a)
entry.objects.filter(name='name', title='title').exists()
sorted(l, key=lambda x: (-int(x[1]), x[0]))
request.meta['http_host']
re.findall("api\\('(.*?)'", "api('randomkey123xyz987', 'key', 'text')")
subprocess.call(['/usr/bin/perl', './uireplace.pl', var])
print('\n'.join(str(p) for p in mylist))
mydic.update({i: o['name']})
list(stru.decode('utf-8'))
u = s.decode('utf-8-sig')
entry.objects.filter(~q(id=3))
getattr(__builtins__, 'range')
subprocess.call(['shutdown', '/r', '/t', '900'])
subprocess.call(['shutdown', '/s'])
subprocess.call(['shutdown', '/a '])
subprocess.call(['shutdown', '/l '])
subprocess.call(['shutdown', '/r'])
open('filename', 'w').close()
open('file.txt', 'w').close()
df.to_dict('index')
df.to_dict('records')
df.groupby(pd.timegrouper(freq='m'))
[(c / t) for c, t in zip(conversions, trials)]
sorted(data, key=data.get)
sorted(data.values())
sorted(list(data.items()), key=lambda x: x[1])
sorted(list(data.items()), key=lambda x: x[1]) 
now = datetime.datetime.now().strftime('%h:%m:%s')
"""foo bar bar bar""".replace('bar', 'xxx', 1).find('bar')
set(['stackoverflow', 'google']).issubset(sites)
stuff.replace(' and ', '/')
np.savez(tmp, *[getarray[0], getarray[1], getarray[8]])
t = datetime.datetime.now() (t - datetime.timedelta(hours=1, minutes=10))
(t - datetime.timedelta(hours=1, minutes=10))
dt = datetime.datetime.combine(datetime.date.today(), t)
dt -= datetime.timedelta(hours=5)
print(data.encode('hex'))
print(' '.join([str(ord(a)) for a in data]))
[x for x in l if x[1] == 1]
a.fromlist([int(val) for val in stdin.read().split()])
print(re.sub('[_%^$]', '\\\\\\g<0>', line))
doc.xpath("//a[starts-with(text(),'some text')]")
zip(*a)
[map(int, sublist) for sublist in lst]
[[int(x) for x in sublist] for sublist in lst]
np.where(np.in1d(a, b))[0]
[{'key1': a, 'key2': b} for a, b in zip(d['key1'], d['key2'])]
map(dict, zip(*[[(k, v) for v in value] for k, value in list(d.items())]))
calendar.monthrange(2002, 1)
calendar.monthrange(2008, 2)
calendar.monthrange(2100, 2)
calendar.monthrange(year, month)[1]
monthrange(2012, 2)
(datetime.date(2000, 2, 1) - datetime.timedelta(days=1))
from subprocess import call
os.system('some_command with args')
os.system('some_command < input_file | another_command > output_file')
stream = os.popen('some_command with args')
print(subprocess.popen('echo hello world', shell=true, stdout=subprocess.pipe).stdout.read())
print(os.popen('echo hello world').read())
return_code = subprocess.call('echo hello world', shell=true)
p = subprocess.popen('ls', shell=true, stdout=subprocess.pipe, stderr=subprocess.stdout) for line in p.stdout.readlines():     print(line, end=' ') retval = p.wait()
call(['ls', '-l'])
print(urllib.parse.unquote(url).decode('utf8'))
url = urllib.parse.unquote(url).decode('utf8')
"""""".join(filter(str.isdigit, '12454v'))
df['season'].str.split('-').str[0].astype(int)
my_list.sort(key=lambda x: x[1])
[m.start() for m in re.finditer('(?=tt)', 'ttt')]
[m.start() for m in re.finditer('test', 'test test test test')]
re.findall('\\s+|\\s+', s)
rdata.set_index(['race_date', 'track_code', 'race_number'])
for (root, subfolders, files) in os.walk(rootdir):     pass
list.sort(key=lambda item: item['date'], reverse=true)
"""{:.5}""".format('aaabbbccc')
struct.unpack('11b', s)
[i for i, j in enumerate(['foo', 'bar', 'baz']) if j == 'foo']
print(list(itertools.product([1, 2, 3], [4, 5, 6])))
itertools.permutations([1, 2, 3])
return re.sub('\\p{p}+', '', text)
raise valueerror('a very specific bad thing happened')
raise exception('i know python!')
raise exception('i know python!') 
raise valueerror('represents a hidden bug, do not catch this')
raise exception('this is the exception you expect to handle')
raise valueerror('a very specific bad thing happened') 
raise runtimeerror('specific message')
raise assertionerror("unexpected value of 'distance'!", distance)
driver.find_element_by_id('foo').clear()
driver.find_element_by_id('foo').clear() 
socket.inet_ntoa(struct.pack('!l', 2130706433))
df = df[['x', 'y', 'a', 'b']]
super(childclass, self).__init__(*args, **kwargs)
sum(d.values())
sum(d.values()) 
json.dumps(your_data, ensure_ascii=false)
values = np.array([i for i in range(100)], dtype=np.float64)
sorted(list_of_dct, key=lambda x: order.index(list(x.values())[0]))
return s[0].upper() + s[1:]
"""""".join([1, 2, 3, 4])
line = line.decode('utf-8', 'ignore').encode('utf-8')
os.system(command)
c.execute('select * from foo where bar = %s and baz = %s', (param1, param2))
dateobj = datetime.datetime.strptime(datestr, '%y-%m-%d').date()