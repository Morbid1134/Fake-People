import random
import os
import datetime

#uncomment to close chrome browser when ran
#os.system("TASKKILL /F /IM chrome.exe")

thisYear = datetime.datetime.now().year

choicefile=open("First.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
FirstName=random.choice(linelist)
import random

choicefile=open("Last.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
LastName=random.choice(linelist)

choicefile=open("data.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
one=random.choice(linelist)
two=random.choice(linelist)
three=random.choice(linelist)

choicefile=open("month.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
Month=random.choice(linelist)

choicefile=open("passwords.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
password=random.choice(linelist)

choicefile=open("gender.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
gender=random.choice(linelist)

choicefile=open("sexuality.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
sexuality=random.choice(linelist)

choicefile=open("photoList.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
photo=random.choice(linelist)

choicefile=open("provider.txt","r")
linelist=[]
for line in choicefile:
    linelist.append(line)
provider=random.choice(linelist)

day = random.randint(1, 28)

year = random.randint(1995, 2002)

age = (thisYear - year)

email = str(("%s%s%s@%s" % (FirstName, LastName, year, provider)).replace("\n", ""))

msg = str("     Name - %s  %s \n\n       DOB - %s  %s, %s \n\n     Characteristics - %s , %s , and %s \n\n    Gender - %s \nSexuality - %s \n\nSelfie - %s" % (FirstName, LastName, Month, day, year, one, two, three, gender, sexuality, photo))
msg1 = msg.replace("\n ", "")

html = str("<html>\n <head>\n <script>\n function myFunction() {\n  var x = document.getElementById('myDIV');\n  if (x.style.display === 'none') {\n    x.style.display = 'block';\n  } else {\n    x.style.display = 'none';\n  }\n}\n</script>\n<style>\n body {\n     background-color: #f9f9fa\n }\n .padding {\n     padding: 3rem !important\n }\n .user-card-full {\n     overflow: hidden\n }\n .card {\n     border-radius: 5px;\n     -webkit-box-shadow: 0 1px 20px 0 rgba(69, 90, 100, 0.08);\n     box-shadow: 0 1px 20px 0 rgba(69, 90, 100, 0.08);\n     border: none;\n     margin-bottom: 30px\n }\n .m-r-0 {\n     margin-right: 0px\n }\n .m-l-0 {\n     margin-left: 0px\n }\n .user-card-full .user-profile {\n     border-radius: 5px 0 0 5px\n }\n .bg-c-lite-green {\n     background: -webkit-gradient(linear, left top, right top, from(#f29263), to(#ee5a6f));\n     background: linear-gradient(to right, #ee5a6f, #f29263)\n }\n .user-profile {\n     padding: 20px 0\n }\n .card-block {\n     padding: 1.25rem\n }\n .m-b-25 {\n     margin-bottom: 25px\n }\n .img-radius {\n     border-radius: 5px\n }\n h6 {\n     font-size: 14px\n }\n .card .card-block p {\n     line-height: 25px\n }\n @media only screen and (min-width: 1400px) {\n     p {\n         font-size: 14px\n     }\n }\n .card-block {\n     padding: 1.25rem\n }\n .b-b-default {\n     border-bottom: 1px solid #e0e0e0\n }\n .m-b-20 {\n     margin-bottom: 20px\n }\n .p-b-5 {\n     padding-bottom: 5px !important\n }\n .card .card-block p {\n     line-height: 25px\n }\n .m-b-10 {\n     margin-bottom: 10px\n }\n .text-muted {\n     color: #919aa3 !important\n }\n .b-b-default {\n     border-bottom: 1px solid #e0e0e0\n }\n .f-w-600 {\n     font-weight: 600\n }\n .m-b-20 {\n     margin-bottom: 20px\n }\n .m-t-40 {\n     margin-top: 20px\n }\n .p-b-5 {\n     padding-bottom: 5px !important\n }\n .m-b-10 {\n     margin-bottom: 10px\n }\n .m-t-40 {\n     margin-top: 20px\n }\n .user-card-full .social-link li {\n     display: inline-block\n }\n .user-card-full .social-link li a {\n     font-size: 20px;\n     margin: 0 10px 0 0;\n     -webkit-transition: all 0.3s ease-in-out;\n     transition: all 0.3s ease-in-out\n }\n </style>\n </head>\n <body onload='myFunction()'>\n <div class='page-content page-container' id='page-content'>\n     <div class='padding'>\n         <div class='row container d-flex justify-content-center'>\n             <div class='col-xl-6 col-md-12'>\n                 <div class='card user-card-full'>\n                     <div class='row m-l-0 m-r-0'>\n                         <div class='col-sm-4 bg-c-lite-green user-profile'>\n                             <div class='card-block text-center text-white'>\n                                 <button onclick='myFunction()'>Show/Hide</button>\n                                 <div id='myDIV' class='m-b-25'> <img src='%sgreatly' class='img-radius' alt='User-Profile-Image'> </div>\n                                 <h6 class='f-w-600'>%sgreatly %sgreatly</h6>\n                             </div>\n                         </div>\n                         <div class='col-sm-8'>\n                             <div class='card-block'>\n                                 <h6 class='m-b-20 p-b-5 b-b-default f-w-600'>Information</h6>\n                                 <div class='row'>\n                                     <div class='col-sm-6'>\n                                         <p class='m-b-10 f-w-600'>Date of Birth - %sgreatly %sgreatly %sgreatly (%sgreatly this Year )</p>\n                                     </div>\n                                     <div class='col-sm-6'>\n                                         <p class='m-b-10 f-w-600'>Gender - %sgreatly</p>\n                                     </div>\n                                     <div class='col-sm-6'>\n                                         <p class='m-b-10 f-w-600'>Sexuality - %sgreatly</p>\n                                     </div>\n                                     <div class='col-sm-6'>\n                                         <p class='m-b-10 f-w-600'>Characteristics - %sgreatly, %sgreatly, and %sgreatly</p>\n                                     </div>\n                                     <div class='col-sm-6'>\n                                         <p class='m-b-10 f-w-600'>Email - %sgreatly - - - - - - - - Password - %sgreatly</p>\n                                     </div>\n                                 </div>\n                                 </div>\n                                 <ul class='social-link list-unstyled m-t-40 m-b-10'>\n                                     <li><a href='#!' data-toggle='tooltip' data-placement='bottom' title='' data-original-title='facebook' data-abc='true'><i class='mdi mdi-facebook feather icon-facebook facebook' aria-hidden='true'></i></a></li>\n                                     <li><a href='#!' data-toggle='tooltip' data-placement='bottom' title='' data-original-title='twitter' data-abc='true'><i class='mdi mdi-twitter feather icon-twitter twitter' aria-hidden='true'></i></a></li>\n                                     <li><a href='#!' data-toggle='tooltip' data-placement='bottom' title='' data-original-title='instagram' data-abc='true'><i class='mdi mdi-instagram feather icon-instagram instagram' aria-hidden='true'></i></a></li>\n                                 </ul>\n                             </div>\n                         </div>\n                     </div>\n                 </div>\n             </div>\n         </div>\n     </div>\n </div>\n </body>\n </html>" % (photo, FirstName, LastName, Month, day, year, age, gender, sexuality, one, two, three, email, password))
htmldone = html.replace("\ngreatly", "")
html = htmldone.replace("greatly", "")

filenameBF = "people\%s_%s.html" % (FirstName, LastName)
filename = filenameBF.replace("\n", "")

with open(filename, 'w') as f:
    f.write(html)
    f.close()

f = open("collectedInfo.txt", "a")

f.write("%s\n\n" % (msg1))
f.close()

name = str(("%s, %s" % (FirstName, LastName)).replace("\n", ""))

outputform = str('dim speechobject\nset speechobject=createobject("sapi.spvoice")\nspeechobject.speak "Introducing... '+name+'"')
output = outputform.replace('\n"', '"')

f = open("index.vbs", "w")
f.write(output)
f.close()

os.startfile("index.vbs")

os.startfile(filename)
















