# fb-group-scraper

1. Install library using `pip install -r requirements.txt`
2. Install extension "Get cookies.txt LOCALLY" in Chrome or Firefox.
3. Open [https://mbasic.facebook.com/](https://mbasic.facebook.com/), use the extension to download the cookies to local.
4. Open your download folder, copy the file to this repo and change the "cookie" parameter in "scraper_csv.py" to the newly downloaded cookie file name.
5. Change the group id to your desired group id
6. If you want to start from fresh, delete "next_page.txt" and all "messages_*.csv" in folder "data". This ensures the data start from scratch. Else, if you want to continue from the previous scraping progress, don't delete the files, and adjust the `page_start` variable in the code.
7. Change the number of page in `python scraper_csv.py` if required.
8. Run `python scraper_csv.py`
9. After finished, run `bash data/merge.bash`
10. You can check the result in `data/merged.csv`