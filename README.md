# download_ncert_books
download NCERT books using scrapy

## How to use
Initial Setup

```shell
git clone https://github.com/nit-in/download_ncert_books.git
cd download_ncert_books
pip install -r requirements.txt
```

to run the spider 
```shell
scrapy crawl --nolog ncert
```
and follow the prompts

for example if you want to download Class 11th Economics Book
```shell
 scrapy crawl  --nolog ncert                                                                                                                                      ─╯

Enter the class:        11

Select one the subjects:
Enter 1 for Sanskrit
Enter 2 for Accountancy
Enter 3 for Chemistry
Enter 4 for Mathematics
Enter 5 for Economics
Enter 6 for Psychology
Enter 7 for Geography

and so on ...

Enter subject number:   5

Select one the books:
Enter 1 for Indian Economic Development
Enter 2 for Statistics for Economics
Enter 3 for Sankhyiki
Enter 4 for Bhartiya Airthryavstha Ka Vikas 
Enter 5 for Hindustan Ki Moaashi Tarraqqi(Urdu)
Enter 6 for Shumariyaat Bar-e-Mushiyat(Urdu)

Enter book number:      1

Downloading...  Class: Class11  Subject: Economics      Book: Indian_Economic_Development       Chapters: 10


downloading keec1ps.pdf to  /home/user/ncert/Class11/Economics/Indian_Economic_Development/keec1ps.pdf
downloading keec101.pdf to  /home/user/ncert/Class11/Economics/Indian_Economic_Development/keec101.pdf
downloading keec102.pdf to  /home/user/ncert/Class11/Economics/Indian_Economic_Development/keec102.pdf

			OR 

to download multiple books

enter their numbers separated by commas

e.g. 

Select one the books:
Enter 1 for Indian Economic Development
Enter 2 for Statistics for Economics
Enter 3 for Sankhyiki
Enter 4 for Bhartiya Airthryavstha Ka Vikas 
Enter 5 for Hindustan Ki Moaashi Tarraqqi(Urdu)
Enter 6 for Shumariyaat Bar-e-Mushiyat(Urdu)

Enter book number:      1,2

```

if you want to see scrapy spider log
```shell
scrapy shell ncert
```
