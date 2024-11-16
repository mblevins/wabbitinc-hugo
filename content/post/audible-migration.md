---
title: 'Kobo Migration'
date: Sat, 02 Nov 2024 12:00:00 +0000
draft: true
tags: ['Howoto']
---

Downloaded kindle for windows from https://filehippo.com/download_kindle-for-pc/2.4.70904/ . Note this has to be a pre 2.5 version, as that version will add additional DRM to downloaded books.

Downloaded all kindle books. This was manual, did 10 at a time. 

Downloaded https://www.epubor.com/, paid the $29 license fee. Set the output path to /users/user/ultimate. Added all the kindle books from "Documents/My Kindle Content" and converted to epub. Note: some of the books were in mobi and not converted.

Downloaded Calibre. Set the library directory to d:/Calibre. Added all the converted books from /users/user/ultimate. 

Ran job "download metadata", setting:

Source=amazon.com, google, open library
Metadata fields=authors, comments, pub date, publisher, rating, series, tags, title
Do not swap author names 
Do prefer fewer tags


