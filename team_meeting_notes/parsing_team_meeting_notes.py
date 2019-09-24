


# awake
# ___next_week___
# need help

# what people spend most of their time on
# 	most used words overall
# most frequent blockers (keeps me awake)
# 	most freq words only in awake section
# is anyone a bottleneck // is one specific person slowing down others more often // who is the most sought after person? (need help with section) // lazy or knowledgeable
# 	section where do I need help with
# 	parsing where do I need help with


# -------
import operator

text_file_unopened = open("team_meeting_notes.txt", "r")
text_file = text_file_unopened.read().split("\n")
text_file = " ".join(text_file)

# get notes
try:
    list_of_weekly_notes = text_file.split("awake")
except:
    print("impossible, awake is at least once in the file")

list_of_AWAKE_sections = []
list_of_NEXTWEEK_sections = []
list_of_NEEDHELP_sections = []


# check how many notes we get ...:
print("len(list_of_weekly_notes) --> "+str(len(list_of_weekly_notes)))
print()

for note in list_of_weekly_notes:
    try:
        note_split_NEXTWEEK = note.split("___next_week___")
        if len(note_split_NEXTWEEK) > 1:
            awake_section = note_split_NEXTWEEK[0]
            list_of_AWAKE_sections.append(awake_section)
    except:
        continue
    try:
        note_split_NEEDHELP = note_split_NEXTWEEK[1].split("need help")
        if len(note_split_NEEDHELP) > 1:
            next_week_section = note_split_NEEDHELP[0]
            list_of_NEXTWEEK_sections.append(next_week_section)
    except:
        continue
    try:
        if len(note_split_NEEDHELP) > 1:
            need_help_section = note_split_NEEDHELP[1]
            list_of_NEEDHELP_sections.append(need_help_section)
    except:
        continue


# --- inspect: ---
# Q1: most used words in 2nd section:

# what people spend most of their time on
# 	most used words overall // for now in 2nd section

hash_of_words_IN_2ND_SECTION = {}
for words in list_of_NEXTWEEK_sections:
    words_split = words.split(" ")
    for word in words_split:
        try:
            hash_of_words_IN_2ND_SECTION[word] += 1
        except KeyError:
            hash_of_words_IN_2ND_SECTION[word] = 0
            hash_of_words_IN_2ND_SECTION[word] += 1


sortedPredictions = sorted(hash_of_words_IN_2ND_SECTION.items(), key=operator.itemgetter(1), reverse=True)

print("hash_of_words_IN_2ND_SECTION --> ")
for word, num_occ in sortedPredictions:
    print(str(word)+" --> "+str(num_occ))


# most frequent blockers (keeps me awake)
# 	most freq words only in awake section

hash_of_words_IN_2ND_SECTION = {}
for words in list_of_NEXTWEEK_sections:
    words_split = words.split(" ")
    for word in words_split:
        try:
            hash_of_words_IN_2ND_SECTION[word] += 1
        except KeyError:
            hash_of_words_IN_2ND_SECTION[word] = 0
            hash_of_words_IN_2ND_SECTION[word] += 1


sortedPredictions = sorted(hash_of_words_IN_2ND_SECTION.items(), key=operator.itemgetter(1), reverse=True)

print("hash_of_words_IN_2ND_SECTION --> ")
for word, num_occ in sortedPredictions:
    print(str(word)+" --> "+str(num_occ))



# is anyone a bottleneck // is one specific person slowing down others more often // who is the most sought after person? (need help with section) // lazy or knowledgeable
# 	section where do I need help with
# 	parsing where do I need help with