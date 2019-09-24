
from bs4 import BeautifulSoup
from urllib.request import urlopen


visible_text_from_html = ""

for i in range(1, 28):

    #file = 'https://docs.oracle.com/javase/9/docs/api/index-files/index-'+str(i)+'.html'
    #file = 'https://docs.oracle.com/javase/9/docs/api/index-files/index-1.html'
    file = 'https://docs.oracle.com/javase/9/docs/api/index-files/index-16.html'


    # from urllib.request import urlopen
    # from bs4 import BeautifulSoup
    # websitecode = urlopen("https://docs.oracle.com/javase/9/docs/api/index-files/index-16.html").read()
    # soup=BeautifulSoup(websitecode, "html.parser")
    # links=soup.findAll("a")
    # print(links)

    try:
        #f = open(file, 'r', encoding='utf-8', errors='ignore')
        #text_input = f.read()
        f = urlopen("https://docs.oracle.com/javase/9/docs/api/index-files/index-"+str(i)+".html")
        # f = urlopen("https://docs.oracle.com/javase/9/docs/api/index-files/index-16.html")
        text_input = f.read()
        print(text_input)
        #f.close()
    except:
        print("error at file number: " + file)


    # get visible text in browser: i.e. just the code:
    try:
        soup = BeautifulSoup(text_input, "html.parser")
        # [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title', 'pre', 'small', 'head', 'a', 'h1', 'h3'])] # 'p ALIGN=CENTER',
        # for tag in soup.findAll("p", {'align':'CENTER'}):
        #     #tag.attrs = None
        #     tag.decompose() # or extract() ?
        # visible_text_from_html = soup.getText()
        for memberNameLink in soup.findAll("span", {'class':'memberNameLink'}):
            print(memberNameLink.getText())
            print()
            visible_text_from_html += memberNameLink.getText() + "\n"

    except:
        print("error at file number: " + file)

    print(visible_text_from_html)


print("visible_text_from_html ==> " + str(visible_text_from_html))
filename_output = 'filename_output'
file = open('/Users/nicolasg-chausseau/Downloads/'+filename_output+'.txt', "w+")
file.write(visible_text_from_html)
file.close()
