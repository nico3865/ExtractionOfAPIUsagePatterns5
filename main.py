# UPDATED PIPELINE: (API usage pattern recognition is very similar to letter recognition, or idea recognition, within surrounding noise.)
#     download from search --> scrape? in python?
#         yeah
#     build the perplexity / TF-IDF filter FOR THIS MINI QUERY-SPECIFIC-CORPUS: keep only API elements & count their occurrences for each.
#         get a file with all Android API elements
#         get the same for the Java API
#         ------
#         parse: build buckets for each code snippets:
#             with all recognized API elements.
#             COLLISIONS: we probably don't care, because the patterns will be recognized anyway.
#                 we could mark the potential collisions -- but ultimately it serves no purpose.
#         count: at the same time, keep a count of each type of APi element for the next step ("appearance above chance")
#         ---------
#         it's ok if we throw away too much.
#         because when we recover the slice for that particular "terse API usage pattern",
#               we will recover anything that was discarded, if it's really necessary for it.
#         so better to keep only what's for sure'
#             and then later get everything that matters wtih the slice.
#     above chance or not? does the API element appear above chance? then keep it.
#         use some API element stats over a big corpus: how often they appear per line.
#         get freq of each API element in the query results
#         compare: is it above chance?
#         normally there should be a group that's way, way way above chance.
#         if it's way above chance, than keep it.
#         at the end of this step I'll have only significant API elements.
#     get the freq itemsets: the API USAGE PATTERNS:
#         run FP-growth for itemset size = 10
#         run FP-growth for itemset size = 9
#         run FP-growth for itemset size = 8
#         ....
#         run FP-growth for itemset size = 1
#         sort by frequency regardless of the size of itemset.
#         keep the top 5.
#     get AST slice for each in top 5:
#         recover the AST for those freq itemsets in the top 5.




from bs4 import BeautifulSoup
import urllib.request # urllib2 # https://docs.python.org/3.5/howto/urllib2.html
import re
from github import Github

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import time
import os.path

desired_OS_output_folder_for_code_snippets = "/Users/nicolasg-chausseau/Documents/Code_To_English_Code_Snippets_For_Queries"



# # functions:
# def tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True
#
#
# def text_from_html(body):
#     soup = BeautifulSoup(body, 'html.parser')
#     texts = soup.findAll(text=True)
#     visible_texts = filter(tag_visible, texts)
#     return u" ".join(t.strip() for t in visible_texts)



# # download from search --> scrape? in python?
# # https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
# # html_page = urllib.request.urlopen("https://github.com/search?l=Java&q=read+text+file&type=Repositories")
# # curl https://api.github.com/search/code?q=addClass+in:file+language:js+repo:jquery/jquery
# html_page = urllib.request.urlopen("https://api.github.com/search/code?q=addClass+in:file+language:js+repo:jquery/jquery")
# print(html_page)
#
# soup = BeautifulSoup(html_page, "html.parser")
# # soup = BeautifulSoup(html_page)
#
# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#     print(link.get('href'))


# # https://github.com/PyGithub/PyGithub
# # using username and password
# g = Github("user", "password")
# # Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)

g = Github("nico3865", "supercoolcodingwithppl352")
results = g.search_code("read text file language:Java", sort='indexed', order='asc')

from pprint import pprint
pprint(results)
for result in results:
    print("------- new result: -------")
    print(result)
    print(result.download_url)

    cleaned_filename = result.download_url.replace(":", "-")
    cleaned_filename = cleaned_filename.replace("/", ":")
    result_download_url_filename_friendly = desired_OS_output_folder_for_code_snippets + "/" + cleaned_filename
    # truncate it to match mac osx's max length file name: 255 characters
    if len(result_download_url_filename_friendly) > 255:
        result_download_url_filename_friendly = result_download_url_filename_friendly[:140] + "~~~~~" + result_download_url_filename_friendly[-100:]

    # skip files that already have been written by previous runs:
    if os.path.isfile(result_download_url_filename_friendly):
        continue

    html_page = urllib.request.urlopen(result.download_url)
    print(html_page)

    # html = urllib.request.urlopen(result.download_url).read()
    # html = "<html><body>some code</body></html>"
    # visible_text_from_html = text_from_html(html) # doesn't work for non ascii characters # non-ascii friendly way
    # html = urllib.request.urlopen('https://raw.githubusercontent.com/DSC-SPIDAL/twister2/dfe20b01f557e5c328b60aa346cf2e55ee81b00b/twister2/data/src/main/java/edu/iu/dsc/tws/data/api/formatters/TextInputFormatter.java')
    # html = urllib.request.urlopen(result.download_url) # works too, strangely

    # prepend github url for this code:
    visible_text_from_html = "// GitHub url for this code is: " + result.download_url + "\r\n\r\n\r\n"

    # get visible text in browser: i.e. just the code:
    soup = BeautifulSoup(html_page)
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text_from_html += soup.getText()

    print(visible_text_from_html)

    file = open(result_download_url_filename_friendly, "w+")
    file.write(visible_text_from_html)

    file.close()

    # so as not to trigger GitHub's "abuse mechanism":
    time.sleep(20)









