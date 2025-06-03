import scrapy
from scrapy_playwright.page import PageMethod
import re
import subprocess
from pathlib import Path
import requests


url = 'https://ncert.nic.in/textbook.php/'
common_url = "https://ncert.nic.in/textbook/pdf/"
ext = ".pdf"
ncert_folder = "~/ncert"
ncert_folder_path = Path(ncert_folder).expanduser()
cwd = Path.cwd()
dflname = "dwnlnk"
txtext = ".txt"

class NcertSpider(scrapy.Spider):
    name = "ncert"
    allowed_domains = ["ncert.nic.in"]



    def start_requests(self):
        self.tclass = int(input("\nEnter the class:\t"))
        yield scrapy.Request(
            url="https://ncert.nic.in/textbook.php/textbook.php",
            meta={
                "playwright": True,
                "playwright_include_page": True,

                "playwright_page_methods": [
                    # You can execute custom JS or click buttons etc.
                    PageMethod(
                        "evaluate",
                        "document.getElementsByName('tclass')[0].value="+str(self.tclass)+";change();"
                    ),

                 ]
            },
            dont_filter = True

        )

    def parse(self, response, **kwargs):
        page: Page = response.meta["playwright_page"]
        self.tsubjects = response.xpath("//select[contains(@name,'tsubject')]/option/text()").getall()
        print(f"\nSelect one the subjects:")
        for i in range(1,len(self.tsubjects)):
            print(f"Enter {i} for {self.tsubjects[i]}")
        self.tsubject = int(input(f"\nEnter subject number:\t"))
        try:
            yield scrapy.Request(
                url=response.url,
                callback=self.parse_book,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page": page,
                    "playwright_page_methods": [
                        # You can execute custom JS or click buttons etc.
                        PageMethod(
                            "evaluate",
                            "document.getElementsByName('tclass')[0].value="+ str(self.tclass) +";change();change1(document.getElementsByName('tsubject')[0].selectedIndex=" + str(self.tsubject) + ");"
                        ),

                     ]
                },
                dont_filter = True

            )
        except IndexError:
            print(f"\nEnter correct subject number.\n")

    def parse_book(self, response):
        page: Page = response.meta["playwright_page"]
        op = response.xpath("//select/option[contains(@value,'tbook')]")
        print(f"\nSelect one the books:")
        for j in range(0,len(op)):
            tbook_name = op[j].xpath("text()").get()
            print(f"Enter {j+1} for {tbook_name}")


        book_prompt = input(f"\nEnter book number:\t")
        book_list = self.to_list([str(book_prompt)])
        for select_book in book_list:
            try:
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
            except IndexError:
                print(f"\nEnter correct book number.\n")



    def download_books(self,theclass,subject,book_name,book_code,chapters):
        class_path = Path(ncert_folder_path, theclass)
        subject_path = Path(class_path, subject)
        book_path = Path(subject_path, book_name)
        if not book_path.exists():
            book_path.mkdir(parents=True)

        pdf_links = []
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
                pdf_links.append(str(pdf_link))
                print(f"Adding {str(pdf_link)} to list")
            else:
                print(f"Already downloaded {pdf_name} to ",f"{str(pdf_path)}")

            dtfname = str(dflname) + str(txtext)
            dtxtfile = Path(cwd, dtfname)

            with open(str(dtxtfile), "w") as lfile:
                for pl in pdf_links:
                    lfile.write(f"{str(pl)}\n")

        self.start_download(dtxtfile, book_path)

    def start_download(self, dlfile, book_path):
        program = "aria2c"
        arg1 = "-x16"
        arg2 = "-s16"
        arg3 = "-j16"
        arg4 = "-d"
        arg5 = "-i"
        print(f"Downloading files to ",f"{str(book_path)}")
        subprocess.run([program, arg1, arg2, arg3, arg4, str(book_path), arg5, str(dlfile)], stderr=subprocess.STDOUT)

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

