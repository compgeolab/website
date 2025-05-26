- Create a github profile
- https://github.com/BenjMy/website_grwater/ 

**News folder** --> New Tab in the website 
- Index files --> don't need to touch them
- files in Markdown --> content of the website

https://www.markdownguide.org/basic-syntax/

## Example: I want to add a news
1. Open the github
2. Open the news folder
3. Add file --> create new file
4. Give a name to the file: ICA_jornada_Maria.md (for instance)
5. Use the template below: copy/paste 
6. Fill the text
7. Press commit changes 






## To upload pictures


{{ macros.figure(src="../images/news/NAMEOFMYPICTURE.jpg", alt="", caption="") }}



## Template

---
title: ""
date: 2023-04-26
---

{% import "macros.html" as macros %}

## Abstract

**This line below allow you to insert the image**
{{ macros.figure(src="../images/news/NAMEOFMYPICTURE.jpg", alt="", caption="") }}
