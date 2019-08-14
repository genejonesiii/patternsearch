import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#Place all the code from the previous steps here
s=len(lorem_ipsum)
countalpha=0
countdigit=0
for ch in lorem_ipsum:
    if ch.isalpha():
        countalpha=countalpha + 1
        if not ():
            countdigit=countdigit + 1
countalpha=s - countalpha
countdigit=s - countdigit
print (countalpha)
number=0
s=len(lorem_ipsum)
r=0
r1=0
occurrance_sit_amet=re.findall(r"sit-amet", lorem_ipsum)
for occurrance_sit_amet in occurrance_sit_amet:
    r=r+1
occurrance_sit_amet1=re.findall(r"sit:amet", lorem_ipsum)
for occurrance_sit_amet1 in occurrance_sit_amet1:
    r1=r1+1
occurrance_sit_amet=r+r1
print(occurrance_sit_amet)
replace_results=re.sub(r"sit-amet","sit amet", lorem_ipsum) and (r"sit:amet", "sit amet", lorem_ipsum)
occurrance_sit_amet=len(replace_results)
print (occurrance_sit_amet)
    

