import scrapy
from scrapy_selenium import SeleniumRequest
import re
import subprocess
from pathlib import Path
import requests
"""
https://ncert.nic.in/textbook/pdf/keac103.pdf ----> example pdf link format
https://ncert.nic.in/textbook/pdf/ is common part
next 5 chars (keac1) define book and next 2 numbers (03) define chapter number
also to download index page scheme is adding 2 chars (ps) instead of chapters number
"""


"""
clone the repo and run the spider

scrapy crawl --nolog ncert

follow the prompts

to download multiple books

enter their no separated by comma

e.g. 

Select one the books:
Enter 1 for Indian Economic Development
Enter 2 for Statistics for Economics
Enter 3 for Sankhyiki
Enter 4 for Bhartiya Airthryavstha Ka Vikas 
Enter 5 for Hindustan Ki Moaashi Tarraqqi(Urdu)
Enter 6 for Shumariyaat Bar-e-Mushiyat(Urdu)

Enter book number:      1,2


"""

url = 'https://ncert.nic.in/textbook.php/'
common_url = "https://ncert.nic.in/textbook/pdf/"
ext = ".pdf"
ncert_folder = "~/ncert"
ncert_folder_path = Path(ncert_folder).expanduser()
cwd = Path.cwd()
chromedriver = "selenium/chromedriver"
chromedriver_path = Path(cwd,chromedriver).expanduser()

class NcertSpider(scrapy.Spider):
	name = 'ncert'
	allowed_domains = ['ncert.nic.in']
	custom_settings = {
		'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
		'SELENIUM_DRIVER_EXECUTABLE_PATH' : str(chromedriver_path)
	}

	def start_requests(self):
		self.tclass = int(input("\nEnter the class:\t"))
		yield SeleniumRequest(url=url, callback=self.parse_result,script=f"document.test.tclass.value={self.tclass};change()")

	def parse_result(self, response):
		self.tsubjects = response.xpath("//select[contains(@name,'tsubject')]/option/text()").getall()
		print(f"\nSelect one the subjects:")
		for i in range(1,len(self.tsubjects)):
			print(f"Enter {i} for {self.tsubjects[i]}")
		self.tsubject = int(input(f"\nEnter subject number:\t"))
		yield SeleniumRequest(url=url, callback=self.parse_book,script=f"document.test.tclass.value={self.tclass};change();change1({self.tsubject});")

	def parse_book(self, response):
		op = response.xpath("//select/option[contains(@value,'textbook.php')]")
		print(f"\nSelect one the books:")
		for j in range(0,len(op)):
			tbook_name = op[j].xpath("text()").get()
			print(f"Enter {j+1} for {tbook_name}")


		book_prompt = input(f"\nEnter book number:\t")
		book_list = self.to_list([str(book_prompt)])
		for select_book in book_list:
			thebook_name = op[select_book-1].xpath("text()").get()
			thebook_name = thebook_name.replace(" ","_")
			tbook_link = op[select_book-1].xpath("@value").get()
			tbook_pre = tbook_link.split("=",1)[0].split("?",1)[1]
			tbook_chapters = tbook_link.split("=",1)[1].split("-",1)[1]

			theclass = str("Class") + str(self.tclass)
			thesubject = self.tsubjects[self.tsubject]
			thesubject = thesubject.replace(" ","_")
			print(f"\nDownloading...",f"Class: {theclass}",f"Subject: {thesubject}",f"Book: {thebook_name}",f"Chapters: {tbook_chapters}",sep="\t",end="\n\n\n")
			self.download_books(theclass, thesubject,thebook_name, tbook_pre, tbook_chapters)

	def download_books(self,theclass,subject,book_name,book_code,chapters):
		class_path = Path(ncert_folder_path, theclass)
		subject_path = Path(class_path, subject)
		book_path = Path(subject_path, book_name)
		if not book_path.exists():
			book_path.mkdir(parents=True)

		chap = int(chapters) + 1
		for k in range(0,chap):
			if k == 0:
				chapter_no = "ps"
			elif k < 10 :
				chapter_no = str(0) + str(k)
			else:
				chapter_no = str(k)

			pdf_name =  str(book_code) + str(chapter_no) + str(ext)
			pdf_path = Path(book_path, pdf_name)

			pdf_link = str(common_url) + str(pdf_name)
			pdf_size = requests.head(pdf_link).headers["Content-Length"]

			if not self.check_file(pdf_path,pdf_size):
				program = "wget"
				arg1 = "--show-progress"
				arg2 = "--server-response"
				arg3 = "--continue"
				arg4 = "-O"
				print(f"Downloading {pdf_name} to ",f"{str(pdf_path)}")
				subprocess.run([program, arg1, arg2, arg3, str(pdf_link), arg4, str(pdf_path)], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
			else:
				print(f"Already downloaded {pdf_name} to ",f"{str(pdf_path)}")


	def check_file(self,pdf_path,pdf_size):
		if pdf_path.exists() and int(pdf_path.stat().st_size) == int(pdf_size):
			return True
		else:
			return False

	def to_list(self,obj_list):
		rl = []
		for obj in obj_list:
			for lobj in obj.split(","):
				rl.append(int(lobj))
		return rl
