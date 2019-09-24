import glob
import re
import sys

methods_file = "/Users/nicolasg-chausseau/Downloads/all_Java_methods.txt"
try:
    f = open(methods_file, 'r', encoding='utf-8', errors='ignore')
    text_input = f.read()
    print(text_input)
    f.close()
    #methods_list = text_input.split("\n")
    methods_dict = dict((item,0) for item in text_input.split("\n"))
    for mymethod in methods_dict:
        print(mymethod)
except:
    print("error at file number: " + f)


methods_file = "/Users/nicolasg-chausseau/Downloads/all_Java_classes.txt"
try:
    f = open(methods_file, 'r', encoding='utf-8', errors='ignore')
    text_input = f.read()
    print(text_input)
    f.close()
    #methods_list = text_input.split("\n")
    classes_dict = dict((item,0) for item in text_input.split("\n"))
    for mymethod in methods_dict:
        print(mymethod)
except:
    print("error at file number: " + f)

d4 = dict(methods_dict)
d4.update(classes_dict)



#-----
path = "/Users/nicolasg-chausseau/Documents/Code_To_English_Code_Snippets_For_Queries/*.java"

file_folder = glob.glob(path)
file_folder = sorted(file_folder)

counter_of_files_in_folder = 0
for file in file_folder:

    counter_of_files_in_folder += 1
    string_to_append_to_code_file = ""

    try:
        f = open(file, 'r', encoding='utf-8', errors='ignore')
        text_input = f.read()
        #print(text_input)



        # match all functions in file:
        import re
        #function_regex = r"[\n\r]+[ \t]*(|public|private|protected) [\w]+ nameOfMethod \([)]\) {([\w]+)}"
        all_functions = re.findall(
            r"(/\*\*((?!\*/)[\w\W])*\*/)" \
            r"([\n\r]+[ \t]*(@Override[\s]*))*" \
            r"[\n\r]+[ \t]*" \
            r"(public|private|protected|static|abstract|synchronized|volatile|final|native| )+" \
            r"([\w]+ )" \
            r"([\w\d_]+[ ]*)" \
            r"(\([\w\d_, ]*\))" \
            r"[\s]*({[\w\W]*?})"
            , text_input)

        #print(all_functions)
        print()





        # match body of method to API elements: ..... #lines = all_functions[0][8].split("\n")
        for function in all_functions:
            print("################################function docstring:#####################################")
            print(function[0])
            print("################################function code:#####################################")
            print(function[8])
            lines = function[8].split("\n")
            for line in lines:
                if line.strip().startswith("//"):
                    continue
                if "//" in line:
                    line = line.split("//")[0]
                #print (line)
                #line.split()
                line_split = re.split('[\W+\(\) =]+', line)
                for word in line_split:
                    print(word)
                    word = word.strip()
                    if(word is not '' and word in d4):
                        #string_to_append_to_code_file += word + str("\n") # writes the actual word
                        string_to_append_to_code_file += line + str(" // ") + word + str("\n") # writes the line containing the word matched
                        #f.write(string_to_append_to_code_file)

            f.close()

            print("################################recognized API elements and its line of code:#####################################")
            print(string_to_append_to_code_file)

            f_output = open("/Users/nicolasg-chausseau/Downloads/OUTPUT_FILE_MATCHED_API_ELEMENTS.txt", 'a', encoding='utf-8', errors='ignore')
            f_output.write("---------------------API ELEMENTS RECOGNIZED: ------------------------\n")
            f_output.write(string_to_append_to_code_file)
            f_output.close()
            #sys.exit()



    except:
        print("error at file number: " + f)


# TODO: handle cases where the path is actually spelled out (poften it's static methods): "Logger.getLogger" or "TextInputFormatter.class.getName()"
# TODO: disambiguate API elements --> try to infer the full path of each API element from the imports.