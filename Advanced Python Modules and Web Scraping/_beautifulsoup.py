html_doc= '''                    ### This code is from index.html. We are gonna do some mistakes in this code   ###
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>my web page</title>
</head>
<body>

<h1 id="header">
        Python
    </h1>

    <div class="group1">
        <h2>
            Programming
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
     </ul>
    </div>

    <div class="group2">
        <h2>
            Modules
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
</div>

    <div class="group3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <img src="xd.jpg" alt="">
    
    
    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
'''

from bs4 import BeautifulSoup

soup=BeautifulSoup(html_doc,'html.parser')         
result=soup.prettify()              # We did some mistakes in that code. And 'soup.prettify()' will fix it.

print(result)

#printing html parts
result = soup.title
result = soup.head
result = soup.body
result = soup.title.name
result = soup.title.string
result = soup.h1
result = soup.h2
result = soup.h2.name
result = soup.h2.string
result = soup.h1.string   
print(result) 

#find and print h2
result = soup.find_all('h2')
result = soup.find_all('h2')[0]

result = soup.div        #prints first div(group 1)
result = soup.find_all('div')[1]        #prints second div(group2)
result = soup.find_all('div')[1].ul.li   #prints the 'li' inside the 'ul' within the second div

print(result)
#siblings
result = soup.div.findChildren()     # div is parent and h2 and li's are children 

result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

result = soup.find_all('a')         