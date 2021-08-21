# download_ncert_books
download NCERT books using scrapy

[![NCERT_CLASS_1](https://github.com/nit-in/download_ncert_books/actions/workflows/class_1.yml/badge.svg?branch=class_1)](https://github.com/nit-in/download_ncert_books/releases/tag/class_1)
[![NCERT_CLASS_2](https://github.com/nit-in/download_ncert_books/actions/workflows/class_2.yml/badge.svg?branch=class_2)](https://github.com/nit-in/download_ncert_books/releases/tag/class_2)
[![NCERT_CLASS_3](https://github.com/nit-in/download_ncert_books/actions/workflows/class_3.yml/badge.svg?branch=class_3)](https://github.com/nit-in/download_ncert_books/releases/tag/class_3)
[![NCERT_CLASS_4](https://github.com/nit-in/download_ncert_books/actions/workflows/class_4.yml/badge.svg?branch=class_4)](https://github.com/nit-in/download_ncert_books/releases/tag/class_4)
[![NCERT_CLASS_5](https://github.com/nit-in/download_ncert_books/actions/workflows/class_5.yml/badge.svg?branch=class_5)](https://github.com/nit-in/download_ncert_books/releases/tag/class_5)
[![NCERT_CLASS_6](https://github.com/nit-in/download_ncert_books/actions/workflows/class_6.yml/badge.svg?branch=class_6)](https://github.com/nit-in/download_ncert_books/releases/tag/class_6)
[![NCERT_CLASS_7](https://github.com/nit-in/download_ncert_books/actions/workflows/class_7.yml/badge.svg?branch=class_7)](https://github.com/nit-in/download_ncert_books/releases/tag/class_7)
[![NCERT_CLASS_8](https://github.com/nit-in/download_ncert_books/actions/workflows/class_8.yml/badge.svg?branch=class_8)](https://github.com/nit-in/download_ncert_books/releases/tag/class_8)
[![NCERT_CLASS_9](https://github.com/nit-in/download_ncert_books/actions/workflows/class_9.yml/badge.svg?branch=class_9)](https://github.com/nit-in/download_ncert_books/releases/tag/class_9)
[![NCERT_CLASS_10](https://github.com/nit-in/download_ncert_books/actions/workflows/class_10.yml/badge.svg?branch=class_10)](https://github.com/nit-in/download_ncert_books/releases/tag/class_10)
[![NCERT_CLASS_11](https://github.com/nit-in/download_ncert_books/actions/workflows/class_11.yml/badge.svg?branch=class_11)](https://github.com/nit-in/download_ncert_books/releases/tag/class_11)
[![NCERT_CLASS_12](https://github.com/nit-in/download_ncert_books/actions/workflows/class_12.yml/badge.svg?branch=class_12)](https://github.com/nit-in/download_ncert_books/releases/tag/class_12)


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
