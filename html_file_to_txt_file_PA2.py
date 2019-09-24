import glob
import sys

from bs4 import BeautifulSoup


# ---------------
if len(sys.argv) >= 2:
    path = sys.argv[1]
else:
    path = '/Users/nicolasg-chausseau/Downloads/movie_html_files/*.html' # not case folded, the original html files to transfor into text.
    # path = 'review_polarity/txt_sentoken/neg/*.txt' # review set
    # path = 'validation_set/*.txt' # validation set
    # path = 'test_set/*.txt' # test set: 'test_set/*.txt'

file_folder = glob.glob(path)
file_folder = sorted(file_folder)

counter_of_files_in_folder = 0
for file in file_folder:

    counter_of_files_in_folder += 1

    print("==================================================================================================================================")
    print("==================================================================================================================================")
    print("==================================== processing file # "+str(counter_of_files_in_folder)+" =======================================")
    print("==================================================================================================================================")
    print("==================================================================================================================================")

    try:
        f = open(file, 'r', encoding='utf-8', errors='ignore')
        text_input = f.read()
        print(text_input)
        f.close()
    except:
        print("error at file number: " + file)


    # get visible text in browser: i.e. just the code:
    try:
        soup = BeautifulSoup(text_input)
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title', 'pre', 'small', 'head', 'a', 'h1', 'h3'])] # 'p ALIGN=CENTER',
        for tag in soup.findAll("p", {'align':'CENTER'}):
            #tag.attrs = None
            tag.decompose() # or extract() ?
        visible_text_from_html = soup.getText()
    except:
        print("error at file number: " + file)

    print(visible_text_from_html)

    filename_only = file.split('/')[-1][0:-5]
    file = open('/Users/nicolasg-chausseau/Downloads/movie_html_files_as_txt/'+filename_only+'.txt', "w+")
    file.write(visible_text_from_html)

    file.close()
