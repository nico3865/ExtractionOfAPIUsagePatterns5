os.kill(os.getpid(), signal.sigusr1)
bytes.fromhex('4a4b4c').decode('utf-8')
all(x == mylist[0] for x in mylist)
print('%*s : %*s' % (20, 'python', 20, 'very good'))
d.decode('cp1251').encode('utf8')
res = {k: v for k, v in list(kwargs.items()) if v is not none}
res = dict((k, v) for k, v in kwargs.items() if v is not none)
subprocess.check_output('ps -ef | grep something | wc -l', shell=true)
"""""".join(['a', 'b', 'c'])
pd.series(list(set(s1).intersection(set(s2))))
client.send('http/1.0 200 ok\r\n')
then = datetime.datetime.strptime(when, '%y-%m-%d').date()
inputstring.split('\n')
' a \n b \r\n c '.split('\n')
""":""".join(str(x) for x in b)
entry.objects.filter()[:1].get()
a.sum(axis=1)
warnings.simplefilter('always')
print(' '.join(map(str, l)))
subprocess.call(['python.exe', 'hello.py', 'htmlfilename.htm'])
time.strptime('30/03/09 16:31:32.123', '%d/%m/%y %h:%m:%s.%f')
my_float = float(my_string.replace(',', ''))
float('123,456.908'.replace(',', ''))
sys.path.append('/path/to/whatever')
re.split('(\\w+)', 'words, words, words.')
file = open('output.txt', 'a')
urllib.request.urlretrieve('http://www.example.com/songs/mp3.mp3', 'mp3.mp3')
u = urllib.request.urlopen(url) f = open(file_name, 'wb') meta = u.info() file_size = int(meta.getheaders('content-length')[0]) print(('downloading: %s bytes: %s' % (file_name, file_size))) file_size_dl = 0 block_sz = 8192 while true:     buffer = u.read(block_sz)     if (not buffer):         break     file_size_dl += len(buffer)     f.write(buffer)     status = ('%10d  [%3.2f%%]' % (file_size_dl, ((file_size_dl * 100.0) / file_size)))     status = (status + (chr(8) * (len(status) + 1)))     print(status, end=' ') f.close()
response = urllib.request.urlopen('http://www.example.com/') html = response.read()
r = requests.get(url)
response = requests.get(url, stream=true) with open('10mb', 'wb') as handle:     for data in tqdm(response.iter_content()):         handle.write(data)
parser.add_argument('--version', action='version', version='%(prog)s 2.0')
{i: d[i] for i in d if i != 'c'}
pd.merge(split_df, csv_df, on=['key'], suffixes=('_left', '_right'))
s.split(' ', 4)
input('enter your input:')
app.run(debug=true)
pickle.dump(mylist, open('save.txt', 'wb'))
scipy.tensordot(p, t, axes=[1, 1]).swapaxes(0, 1)
numpy.zeros((3, 3, 3))
""" """.join(content.split(' ')[:-1])
x = np.asarray(x).reshape(1, -1)[(0), :]
sum(sum(i) if isinstance(i, list) else i for i in l)
struct.unpack('!f', '470fc614'.decode('hex'))[0]
my_dict.update((x, y * 2) for x, y in list(my_dict.items()))
subprocess.call('sleep.sh', shell=true)
""",""".join(l)
mylist = ','.join(map(str, mylist))
list(reversed(list(range(10))))
print('lamp, bag, mirror'.replace('bag,', ''))
""".""".join(s.split('.')[::-1])
datetime.datetime.fromtimestamp(s).strftime('%y-%m-%d %h:%m:%s.%f')
time.strftime('%y-%m-%d %h:%m:%s', time.gmtime(1236472051807 / 1000.0))
(datetime.datetime.now() - datetime.timedelta(days=7)).date()
print(sum(row[column] for row in data))
[sum(row[i] for row in array) for i in range(len(array[0]))]
base64.b64encode(bytes('your string', 'utf-8'))
dict((k, [d[k] for d in dicts]) for k in dicts[0])
{k: [d[k] for d in dicts] for k in dicts[0]}
request.args['myparam']
[k for k, v in list(counter(mylist).items()) if v > 1]
sys.path.insert(1, os.path.join(os.path.dirname(__file__), 'apps'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'subdir'))
db.execute("insert into present values('test2', ?, 10)", (none,))
[image for menuitem in list_of_menuitems for image in menuitem]
a.extend(b)
a.extend(list(b))
np.savetxt('c:\\data\\np.txt', df.values, fmt='%d')
df.to_csv('c:\\data\\pandas.txt', header=none, index=none, sep=' ', mode='a')
print(x.rpartition('-')[0])
print(x.rsplit('-', 1)[0])
ftp.storlines('stor ' + filename, open(filename, 'r'))
browser.execute_script("document.getelementbyid('xyz').value+='1'")
np.maximum([2, 3, 4], [1, 5, 2])
print(l[3:] + l[:3])
for fn in os.listdir('.'):     if os.path.isfile(fn):         pass
for (root, dirs, filenames) in os.walk(source):     for f in filenames:         pass
[int(1000 * random.random()) for i in range(10000)]
datetime.datetime.now().strftime('%h:%m:%s.%f')
db.gqlquery('select * from schedule where station = $1', foo.key())
df.b.str.contains('^f')
print('\n'.join('\t'.join(str(col) for col in row) for row in tab))
df.set_index(list('bc')).drop(tuples, errors='ignore').reset_index()
"""({:d} goals, ${:d})""".format(self.goals, self.penalties)
"""({} goals, ${})""".format(self.goals, self.penalties)
"""({0.goals} goals, ${0.penalties})""".format(self)
[int(''.join(str(d) for d in x)) for x in l]
[''.join(str(d) for d in x) for x in l]
l = [int(''.join([str(y) for y in x])) for x in l]
myfile.write('\n'.join(lines))
[x for x in ['aat', 'xac', 'ant', 'tta'] if 'x' not in x and 'n' not in x]
text = re.sub('\\b(\\w+)( \\1\\b)+', '\\1', text)
df.astype(bool).sum(axis=1)
re.search('(?<!distillr)\\\\acrotray\\.exe', 'c:\\somedir\\acrotray.exe')
"""qh qd jc kd js""".split()
print(re.search('>.*<', line).group(0))
open(filename, 'w').close()
datetime.datetime.strptime(string_date, '%y-%m-%d %h:%m:%s.%f')
[index for index, item in enumerate(thelist) if item[0] == '332']
re.sub('[^\\sa-za-z0-9]', '', text).lower().strip()
re.sub('(?!\\s)[\\w_]', '', text).lower().strip()
plt.plot(x, y, label='h\u2082o')
plt.plot(x, y, label='$h_2o$')
[x for x in mylist if len(x) == 3]
lst = [object() for _ in range(100)]
lst = [object() for i in range(100)]
self.driver.find_element_by_css_selector('.someclass a').get_attribute('href')
df1.merge(df2, on='date_time')
'first string is: %s, second one is: %s' % (str1, 'geo.tif')
[x.strip() for x in '2.matches $$text$$ string'.split('$$text$$')]
if (not os.path.exists(directory)):     os.makedirs(directory)
try:     os.makedirs(path) except oserror:     if (not os.path.isdir(path)):         raise
distutils.dir_util.mkpath(path)
try:     os.makedirs(path) except oserror as exception:     if (exception.errno != errno.eexist):         raise
re.sub('\\bh3\\b', 'h1', text)
re.sub('\\d', '', 'aas30dsa20')
"""""".join([x for x in 'aas30dsa20' if x.isdigit()])
print(soup.find('name').string)
records = dict((record['_id'], record) for record in cursor)
np.concatenate((a, b))
np.vstack((a, b))
os.stat(filepath).st_size
l.count('a')
counter(l)
[[x, l.count(x)] for x in set(l)]
dict(((x, l.count(x)) for x in set(l)))
l.count('b')
shutil.copy(srcfile, dstdir)
max(k for k, v in x.items() if v != 0)
(k for k, v in x.items() if v != 0)
max(k for k, v in x.items() if v != 0) 
file.seek(0)
df['c'] = np.where(df['a'].isnull, df['b'], df['a'])
del d['ele']
mymodel.objects.update(timestamp=f('timestamp') + timedelta(days=36524.25))
['it'] + ['was'] + ['annoying']
str(int(x) + 1).zfill(len(x))
all(df.index[:-1] <= df.index[1:])
list(t)
tuple(l)
level1 = map(list, level1)
pprint.pprint(dataobject, logfile)
df.loc[df['boolcol']]
df.iloc[np.flatnonzero(df['boolcol'])]
df[df['boolcol'] == true].index.tolist()
df[df['boolcol']].index.tolist()
os.chdir(owd)
c.execute("insert into test values (?, 'bar')", (testfield,))
"""\\x89\\n""".decode('string_escape')
raw_string.decode('string_escape')
raw_byte_string.decode('unicode_escape')
[m.group(0) for m in re.finditer('(\\d)\\1*', s)]
plt.scatter(np.random.randn(100), np.random.randn(100), facecolors='none')
plt.plot(np.random.randn(100), np.random.randn(100), 'o', mfc='none')
soup.find('div', id='main-content').decompose()
df[df['ids'].str.contains('ball')]
df.reset_index(level=0, inplace=true)
df['index1'] = df.index
df.reset_index(level=['tick', 'obs'])
[x[::-1] for x in b]
np.array([zip(x, y) for x, y in zip(a, b)])
np.array(zip(a.ravel(), b.ravel()), dtype='i4,i4').reshape(a.shape)
""",""".join([str(i) for i in list_of_ints])
requests.post(url, data=data, headers=headers_dict, auth=(username, password))
'abcd}def}'.rfind('}')
print([item for item in [1, 2, 3]])
[(x['x'], x['y']) for x in d]
print(os.path.splitext(os.path.basename('hemanth.txt'))[0])
dict(x[i:i + 2] for i in range(0, len(x), 2))
values = sum([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], [])
df = df[(df['closing_price'] >= 99) & (df['closing_price'] <= 101)]
df.replace({'\n': '<br>'}, regex=true)
df.replace({'\n': '<br>'}, regex=true) 
[(x + y) for x, y in zip(word, word[1:])]
list(map(lambda x, y: x + y, word[:-1], word[1:]))
print(re.findall('(https?://[^\\s]+)', mystring))
print(re.search('(?p<url>https?://[^\\s]+)', mystring).group('url'))
re.sub('[^a-za-z0-9]+', '', mystring)
pd.date_range('2016-01-01', freq='wom-2fri', periods=13)
matrix = [[a, b], [c, d], [e, f]]
mystring.replace(' ', '_')
os.path.abspath('mydir/myfile.txt')
""" """.join(my_string.split())
os.path.splitext(filename)[0]
[sum(l[:i]) for i, _ in enumerate(l)]
"""docs/src/scripts/temp""".replace('/', '/\x00/').split('\x00')
np.random.shuffle(np.transpose(r))
df['d'] = df['b']
list(data['a']['b'].values())[0]['maindata'][0]['info']
all(predicate(x) for x in string)
os.statvfs('/').f_files - os.statvfs('/').f_ffree
cursor.fetchone()[0]
user_list = [int(number) for number in user_input.split(',')]
[int(s) for s in user.split(',')]
sorted(list, key=lambda x: (x[0], -x[1]))
ut.sort(key=cmpfun, reverse=true)
ut.sort(key=lambda x: x.count, reverse=true)
ut.sort(key=lambda x: x.count, reverse=true) 
driver.find_element_by_partial_link_text('send').click()
driver.findelement(by.linktext('send inmail')).click()
driver.find_element_by_link_text('send inmail').click()
'me' + str(i)
df.sort_values(['system_num', 'dis'])
open('outfile', 'w').write('#test firstline\n' + open('infile').read())
l.sort(key=lambda t: len(t[1]), reverse=true)
re.findall('\\b(\\w+)d\\b', s)
bool(re.search('ba[rzd]', 'foobarrrr'))
list(set(t))
list(set(source_list))
list(ordereddict.fromkeys('abracadabra'))
numpy.array(a).reshape(-1).tolist()
numpy.array(a)[0].tolist()
print(soup.find(text='address:').findnext('td').contents[0])
""" """.join([('%d@%d' % t) for t in l])
""" """.join([('%d@%d' % (t[0], t[1])) for t in l])
driver.execute_script('return document.documentelement.outerhtml;')
[i for i in teststr if re.search('\\d+[xx]', i)]
df['a'][(df['b'] > 50) & (df['c'] == 900)]
sorted(o.items())
sorted(d)
sorted(d.items())
int('1')
int()
t2 = [map(int, x) for x in t1]
subprocess.call(['./test.sh'])
subprocess.call(['notepad'])
[val for pair in zip(l1, l2) for val in pair]
encoded = base64.b64encode('data to be encoded')
encoded = 'data to be encoded'.encode('ascii')
lol = list(csv.reader(open('text.txt', 'rb'), delimiter='\t'))
getattr(my_object, my_str)
print(dict(zip(ld[0], zip(*[list(d.values()) for d in ld]))))
sum([pair[0] for pair in list_of_pairs])
d = ast.literal_eval("{'code1':1,'code2':1}")
[word for word in mystring.split() if word.startswith('$')]
text = re.sub('^https?:\\/\\/.*[\\r\\n]*', '', text, flags=re.multiline)
np.where(np.in1d(a, [1, 3, 4]).reshape(a.shape), a, 0)
np.mean(a, axis=1)
subprocess.call(['/usr/bin/rscript', '--vanilla', '/pathto/myrscript.r'])
subprocess.call('/usr/bin/rscript --vanilla /pathto/myrscript.r', shell=true)
writer.writeheader()
df.fillna(df.mean(axis=1), axis=1)
time.strftime('%y-%m-%d %h:%m:%s', time.localtime(1347517370))
super(derived, cls).do(a)
a[np.where((a[:, (0)] == 0) * (a[:, (1)] == 1))]
re.split(' +', 'hello world sample text')
len(max(words, key=len))
result[0]['from_user']
[line.split() for line in open('file.txt')]
res = dict((v, k) for k, v in a.items())
new_file = open('path/to/file_name.ext', 'w')
df.groupby(['col1', 'col2'])['col3'].nunique().reset_index()
any(key.startswith('emp$$') for key in dict1)
[value for key, value in list(dict1.items()) if key.startswith('emp$$')]
pd.dataframe({'email': sf.index, 'list': sf.values})
print('\t'.join(map(str, list)))
print('\xd0\xbf\xd1\x80\xd0\xb8'.encode('raw_unicode_escape'))
'sopet\xc3\xb3n'.encode('latin-1').decode('utf-8')
image = image.resize((x, y), image.antialias)
re.findall('n(?<=[^n]n)n+(?=[^n])(?i)', s)
print('{0:.0f}%'.format(1.0 / 3 * 100))
mylist.sort(key=lambda x: x['title'])
l.sort(key=lambda x: x['title'])
l.sort(key=lambda x: (x['title'], x['title_url'], x['id']))
heapq.nlargest(10, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
soup.find_all('span', {'class': 'stargryb sp'})
df.to_sql('test', engine, schema='a_schema')
brackets = re.sub('[^(){}[\\]]', '', s)
list(dict((x[0], x) for x in l).values())
[line.rstrip('\n') for line in file]
[i for (i, x) in enumerate(testlist) if (x == 1)]
[i for (i, x) in enumerate(testlist) if (x == 1)] 
for i in [i for (i, x) in enumerate(testlist) if (x == 1)]:     pass
for i in (i for (i, x) in enumerate(testlist) if (x == 1)):     pass
gen = (i for (i, x) in enumerate(testlist) if (x == 1)) for i in gen:     pass
print(testlist.index(element))
try:     print(testlist.index(element)) except valueerror:     pass
max(lis, key=lambda item: item[1])[0]
max(lis, key=itemgetter(1))[0]
time.sleep(1)
""", """.join('(' + ', '.join(i) + ')' for i in l)
b = models.charfield(max_length=7, default='0000000', editable=false)
sorted(list5, lambda x: (degree(x), x))
sorted(list5, key=lambda vertex: (degree(vertex), vertex))
(n for n in [1, 2, 3, 5])
newlist = [v for i, v in enumerate(oldlist) if i not in removelist]
f = open('yourfile.txt', 'w')
getattr(obj, 'attr')
from functools import reduce reduce(lambda a, b: a + b, (('aa',), ('bb',), ('cc',)))
map(lambda a: a[0], (('aa',), ('bb',), ('cc',)))
df['range'].replace(',', '-', inplace=true)
zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4)])
zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4)]) 
result = ([a for (a, b) in original], [b for (a, b) in original])
result = ((a for (a, b) in original), (b for (a, b) in original))
zip(*[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e',)])
map(none, *[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e',)])
json.dumps(decimal('3.9'))
d['mynewkey'] = 'mynewvalue'
data.update({'a': 1, })
data.update(dict(a=1))
data.update(a=1)
max([max(i) for i in matrix])
answer = str(round(answer, 2))
ip = re.findall('[0-9]+(?:\\.[0-9]+){3}', s)
df.groupby('a').filter(lambda x: len(x) > 1)
[x for x in myfile.splitlines() if x != '']
lst = map(int, open('filename.txt').readlines())
plt.colorbar(mappable=mappable, cax=ax3)
counter(' '.join(df['text']).split()).most_common(100)
re.findall('(.+?):(.+?)\\b ?', text)
list(itertools.combinations((1, 2, 3), 2))
datetime.now(pytz.utc)
list2 = [x for x in list1 if x != []]
list2 = [x for x in list1 if x]
return httpresponse(data, mimetype='application/json')
re.findall('(.*?)\\[.*?\\]', example_str)
re.findall('(.*?)(?:\\[.*?\\]|$)', example_str)
re.findall('\\(.+?\\)|\\w', '(zyx)bc')
re.findall('\\((.*?)\\)|(\\w)', '(zyx)bc')
re.findall('\\(.*?\\)|\\w', '(zyx)bc')
elements = ['%{0}%'.format(element) for element in elements]
subprocess.popen(['background-process', 'arguments'])
[mydict[x] for x in mykeys]
dict([('name', 'joe'), ('age', 22)])
data.reshape(-1, j).mean(axis=1).reshape(data.shape[0], -1)
print(s.encode('unicode-escape').replace('"', '\\"'))
re.split('(\\w+)', s)
df.plot(kind='barh', stacked=true)
{i[1]: i[0] for i in list(mydictionary.items())}
[i for i, j in enumerate(mylist) if 'how' in j.lower() or 'what' in j.lower()]
isinstance(obj, str)
isinstance(o, str)
(type(o) is str)
isinstance(o, str) 
isinstance(obj_to_test, str)
list2.extend(list1)
list1.extend(mylog)
c.extend(a)
for line in mylog:     list1.append(line)
b.append((a[0][0], a[0][2]))
app.config['secret_key'] = 'your_secret_string'
pd.dataframe(out.tolist(), columns=['out-1', 'out-2'], index=out.index)
[x for x in range(len(stocks_list)) if stocks_list[x] == 'msft']
ax.set_xticklabels(labels, rotation=45)
re.sub('[^\\w]', ' ', s)
os.path.basename(os.path.dirname(os.path.realpath(__file__)))
print(re.findall("'\\\\[0-7]{1,3}'", str))
re.split('[ ](?=[a-z]+\\b)', input)
re.split('[ ](?=[a-z])', input)
r = requests.post(url, files=files, headers=headers, data=data)
open('filename', 'wb').write(bytes_)
[dct[k] for k in lst]
x.set_index('name').index.get_duplicates()
round(1.923328437452, 3)
sorted(li, key=lambda x: datetime.strptime(x[1], '%d/%m/%y'), reverse=true)
ax.set_rlabel_position(135)
os.path.isabs(my_path)
len(list(yourdict.keys()))
len(set(open(yourdictfile).read().split()))
df.groupby('id').first()
pd.concat([df[0].apply(pd.series), df[1]], axis=1)
re.findall('src="js/([^"]*\\bjquery\\b[^"]*)"', data)
sum(int(float(item)) for item in [_f for _f in ['', '3.4', '', '', '1.0'] if _f])
subprocess.popen(['c:\\program files\\vmware\\vmware server\\vmware-cmd.bat'])
q.put((-n, n))
df['group'].plot(kind='bar', color=['r', 'g', 'b', 'r', 'g', 'b', 'r'])
re.findall('([a-fa-f\\d]{32})', data)
len(my_list)
len(l)
len(s)
len(my_tuple)
len(my_string)
"""\\a""".decode('string_escape')
"""obama""".replace('a', '%temp%').replace('b', 'a').replace('%temp%', 'b')
shutil.rmtree('/folder_name')
data['weekday'] = data['my_dt'].apply(lambda x: x.weekday())
sorted(x, key=x.get, reverse=true)
sorted(list(x.items()), key=lambda pair: pair[1], reverse=true)
np.vstack((a, b)) 
print(concatenate((a, b), axis=0))
print(concatenate((a, b), axis=1))
c = np.r_[(a[none, :], b[none, :])]
np.array((a, b))
print(socket.getaddrinfo('google.com', 80))
df.xs('sat', level='day', drop_level=false)
return httpresponse('unauthorized', status=401)
flask(__name__, template_folder='wherever')
session.execute('insert into t1 (select * from t2)')
c2.sort(key=lambda row: row[2])
c2.sort(key=lambda row: (row[2], row[1], row[0]))
c2.sort(key=lambda row: (row[2], row[1]))
matplotlib.rc('font', **{'sans-serif': 'arial', 'family': 'sans-serif'})
df['date'].apply(lambda x: x.toordinal())
element.get_attribute('innerhtml')
df.index.get_loc('bob')
os.system('gnome-terminal -e \'bash -c "sudo apt-get update; exec bash"\'')
my_dict.update({'third_key': 1})
my_list = []
my_list.append(12)
mylist.insert(0, 'wuggah')
"""\\xf3\\xbe\\x80\\x80""".replace('\\x', '').decode('hex')
df[df.columns[-1]]
df.loc[df['letters'] == 'c', 'letters'].values[0]
np.column_stack(([1, 2, 3], [4, 5, 6]))
type(i)
type(v)
type(v) 
type(v)  
type(v)   
print(type(variable_name))
next(itertools.islice(range(10), 5, 5 + 1))
print('"{}"'.format(word))
""" """.join(list)
y = [[] for n in range(2)]
data = [line.strip() for line in open('c:/name/mydocuments/numbers', 'r')]
"""""".join([char for char in 'it is icy' if char != 'i'])
re.sub('i', '', 'it is icy')
"""it is icy""".replace('i', '')
"""""".join([char for char in 'it is icy' if char != 'i']) 
df.dropna(subset=[1])
[x for x in mylist if x.n == 30]
nums = [int(x) for x in intstringlist]
map(int, eval(input('enter the unfriendly numbers: ')))
sys.stdout.write('.')
int(round(2.51 * 100))
os.chdir('/mydir') for file in glob.glob('*.txt'):     pass
for file in os.listdir('/mydir'):     if file.endswith('.txt'):         pass
for (root, dirs, files) in os.walk('/mydir'):     for file in files:         if file.endswith('.txt'):             pass
df.plot(legend=false)
for i in range(256):     for j in range(256):         ip = ('192.168.%d.%d' % (i, j))         print(ip)
for (i, j) in product(list(range(256)), list(range(256))):     pass
generator = iter_iprange('192.168.1.1', '192.168.255.255', step=1)
sum(1 << i for i, b in enumerate(x) if b)
target.write('%r\n%r\n%r\n' % (line1, line2, line3))
[y for x in data for y in (x if isinstance(x, list) else [x])]
print('foo\nbar'.encode('string_escape'))
"""""".join(s.rsplit(',', 1))
(x[1:] + x[:-1]) / 2
x[:-1] + (x[1:] - x[:-1]) / 2
arr = numpy.fromiter(codecs.open('new.txt', encoding='utf-8'), dtype='<u2')
l = sorted(l, key=itemgetter('time'), reverse=true)
l = sorted(l, key=lambda a: a['time'], reverse=true)
df.loc[df[0].str.contains('(hel|just)')]
re.search('\\[(.*)\\]', your_string).group(1)
[d.strftime('%y%m%d') for d in pandas.date_range('20130226', '20130302')]
"""the big brown fox is brown""".count('brown')
json.loads(request.body)
urllib.request.urlretrieve(url, file_name)
text.split()
text.split(',')
line.split()
[re.sub('(?<!\\d)\\.(?!\\d)', ' ', i) for i in s]
sorted(list_of_strings, key=lambda s: s.split(',')[1])
subprocess.check_call('vasp | tee tee_output', shell=true)
[element for element in lst if isinstance(element, int)]
[element for element in lst if not isinstance(element, str)]
newlist = sorted(list_to_be_sorted, key=lambda k: k['name'])
newlist = sorted(l, key=itemgetter('name'), reverse=true)
list_of_dicts.sort(key=operator.itemgetter('name'))
list_of_dicts.sort(key=operator.itemgetter('age'))
df.groupby('prots').sum().sort('scores', ascending=false)
""",""".join(trans['category'])
"""""".join(['a', 'b', 'c', 'd'])
json.load(urllib.request.urlopen('url'))
[x for x in sents if not x.startswith('@$\t') and not x.startswith('#')]
entry.objects.filter(pub_date__contains='08:00')
list.sort(key=lambda item: (item['points'], item['time']))
(t - datetime.datetime(1970, 1, 1)).total_seconds()
re.sub('(\\_a)?\\.([^\\.]*)$', '_suff.\\2', 'long.file.name.jpg')
import imp imp.reload(module)
struct.unpack('h', struct.pack('h', number))
numlist = [float(x) for x in numlist]
df.to_csv(filename, index=false)
json_data = json.loads(unescaped)
[chr(i) for i in range(127)]
newfile.write(struct.pack('5b', *newfilebytes))
re.sub('^[a-z0-9]*(?![a-z])', '', string)
list(dict.keys())[-1]
print('hi there', file=f)
f = open('myfile', 'w') f.write('hi there\n') f.close()
with open('somefile.txt', 'a') as the_file:     the_file.write('hello\n')
s.encode('iso-8859-15')
authorizedemail.objects.filter(group=group).order_by('-added')[0]
re.findall('test([0-9.]*[0-9]+)', text)
re.findall('test([\\d.]*\\d+)', text)
os.system('powershell.exe', 'script.ps1')
b.sort(key=lambda x: x[1][2])
list(cf.get_range().get_keys())
datetime.datetime.now()
next(i for i, x in enumerate(lst) if not isinstance(x, bool) and x == 1)
a[:] = [(x - 13) for x in a]
random.choice(os.listdir('c:\\'))
max(x.min(), x.max(), key=abs)
re.findall('"(http.*?)"', s, re.multiline | re.dotall)
re.findall('http://[^t][^s"]+\\.html', document)
mystring.replace(' ', '! !').split('!')
open(path, 'r')
[[sum(item) for item in zip(*items)] for items in zip(*data)]
a[:, (np.newaxis)]
