import requests
import os

import TKinter

from bs4 import BeautifulSoup

URL = "https://gleipniremanga.com/"
page = requests.get(URL)

CDN_URL = "https://cdn.bakihanma.com/file/Zolyvmanga/gleipnir/"

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="ResultsContainer")

job_elements = soup.find_all("ul", class_="su-posts su-posts-list-loop")



print_logs = False

for job_element in job_elements:
    webpage = job_element.find_all("a")

    for el in webpage:
        #get_ = el['href'].strip().split('/')[-2]
        #link = "{}{}".format(URL, get_)
        #print(link)
        ##print(el.text)

        s = el.text.replace(",","").replace(":","").replace(".","-").replace(" ", "-").replace("--","-").lower()
        s = s.replace("gleipnir-","")
        #print(CDN_URL+str)

        current_dir = os.getcwd()
        final_dir = os.path.join(current_dir, s)
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)


        for i in range(100):
            image_string = CDN_URL+s+"/"+str(i)+".jpg"
            if (print_logs == True):
                print(image_string)
            #print(CDN_URL+s+"/"+str(i)+".jpg")
            #print()
            #img_data = requests.get(image_string).content
            #print(final_dir+"/"+str(i)+'.jpg')


            ##

            image_res = requests.get(image_string, stream = True)

            if image_res.status_code == 200:
                with open(final_dir+"/"+str(i)+'.jpg', 'wb') as handler:
                    #handler.write(img_data)
                    handler.write(requests.get(image_string).content)
                if (print_logs == True):
                    print('Image sucessfully Downloaded: ',final_dir+"/"+str(i)+'.jpg')
            else:
                if (print_logs == True):
                    print('Image Couldn\'t be retrieved')
