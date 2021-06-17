from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pickle

from Comment import Comment

def get_purpose_from_comment(a):
    a = a.find('p', {'class': 'ddc-comment-content'})
    a = str(a)
    b0 = a.index("<b>")
    b1 = a.index("</b>")
    a = a[b0 + 3:b1]
    a = a.replace('For', 'for')
    a = a.split('for')[1][1:-1]
    return a

def get_user_from_comment(a):
    a = a.find('span', {'class': 'user-name'})
    a = str(a)
    b0 = a.index("\">")
    b1 = a.index("</")
    a = a[b0 + 2:b1]
    return a

def get_content_from_comment(a):
    a = a.find('p', {'class': 'ddc-comment-content'})
    a = str(a)
    b0 = a.index("<span>\"")
    b1 = a.index("\"</span>")
    a = a[b0+7:b1]
    return a

def get_rating_from_content(a):
    a = a.find('div', {'class': 'rating-score'})
    a = str(a)
    b0 = a.index("\">")
    b1 = a.index("</")
    a = a[b0 + 2:b1]
    return float(a)

def get_max_comment_page(drug):
    url = "http://www.drugs.com/comments/{}/?page={}".format(drug, 10000)

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, features="html.parser")

    a = soup.find_all('span', {'aria-current': "page"})[0]
    a = str(a)
    b0 = a.index("\">")
    b1 = a.index("</")
    a = a[b0 + 2:b1]
    return int(a)

data = {}

drugs = ['fluoxetine', 'escitalopram', 'citalopram', 'fluvoxamine', 'paroxetine', 'sertraline', 'vilazodone', 'bupropion', 'tranylcypromine',
'phenelzine', 'duloxetine', 'desvenlafaxine', 'levomilnacipran', 'venlafaxine', 'nefazodone', 'trazodone', 'amitriptyline', 'clomipramine',
'desipramine', 'doxepin', 'imipramine', 'nortriptyline', 'mirtazapine']

for drug in drugs:
    print("Starting scraping for {}".format(drug))
    comments = []

    m = get_max_comment_page(drug)

    i = 1
    while i <= m:
        #print("{}/{}".format(i, m))
        url = "http://www.drugs.com/comments/{}/?page={}".format(drug, i)

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()

        soup = BeautifulSoup(webpage, features="html.parser")

        a = soup.find_all('div', {'class': "ddc-comment"})

        for j in a:
            try:
                user = get_user_from_comment(j)
                purpose = get_purpose_from_comment(j)
                rating = get_rating_from_content(j)
                content = get_content_from_comment(j)

                if user == 'Anonymous':
                    continue
                elif purpose == '':
                    continue

                comments.append(Comment(user, purpose, content, rating))
            except ValueError:
                continue
        i += 1
    comments = set(comments)
    comments = list(comments)
    data[drug] = comments
    print("{} comments for {}".format(len(comments), drug))

with open('./data/comment_data.pkl', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

#print(data)
