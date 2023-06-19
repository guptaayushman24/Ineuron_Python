import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc = f.read()
# First create the soup project
soup = BeautifulSoup(html_doc,'html.parser') # Soup is an special type of object
print(soup.prettify()) # We are displaying the whole data of sample.html file
print(soup.title) # Here we are getting the title of the page
print(soup.title,type(soup.title)) # Here it is showing the title of that soup.title()
print(soup.title.string,type(soup.title.string)) # Will print the title in the string format and type
print(soup.title.string) # Will only print the content of the title
print(soup.div) # Will give the div tag and contain
print(soup.find_all("div")) # Will give all the div of the html file
print(soup.find_all("div")[0])
print(soup.find_all("div")[1])

print(type(soup.find_all("div")[0])) # It is an bs4 element
print(type(soup.find_all("div")[1]))  # It is an bs4 element

for link in soup.find_all("a") : # Here we are getting all the links
    print(link.get("href"))

print(soup.find(id="link3")) # Finding the id in the html page
print(soup.find(id="link3").get("href")) # If we want the link which is present in the id tag
print(soup.find(id="link3").text) # These will give the text which is present inside the link
print(soup.select("div.italic"))
# What will happen if there is more than one italic in the html file
# Then it will give all italic div tag which are present in the html file
print(soup.select("div.italic")) # For class we use "."
print(soup.select("span#italic")) # For class we use "#"
print(soup.span.get("class"))

print(soup.find(id="italic"))
print(soup.find(class_="italic")) # By doing these you will get one
print(soup.find_all(class_="italic")) # By doing these you will get all the class

# How can we get the child of the partuclar tag
# Using the for loop
for child in soup.find(class_="container").children :
    print(child)


# How can we get the parent of the particular container
# Using the for loop
for parent in soup.find(class_="box").parents :
    print(parent) # Here it will print the whole html file becaues the parent of the conrtainer is the body of the html file
    break; # If we use break then we ony get one parent

cont = soup.find(class_="container") # Change the name of the container
cont.name="span"
print(cont)
# Changing the name of the class
cont.name = "span"
cont["class"] = "myclass" # Changing the name of the container class
print(cont)

# Changing the name of the class
cont.name = "span"
cont["class"] = "myclass class2" # We can add more class myclass class2
print(cont)


# We can update tje whole content of the class
cont.name = "span"
cont["class"] = "myclass class2"
cont.string="I am a string"
print(cont)

# How can we add the new tag
ulTag = soup.new_tag("ul")
liTag = soup.new_tag("li")
# Inserting the data inside the liTag
liTag.string = "Home"
# Appending the liTag inside the ulTag
ulTag.append(liTag)

# Creating the new liTag
# liTag = soup.new_tag("li")
# # Inserting the data inside the liTag
# liTag.string = "About"
# # Appending the liTag inside the ulTag
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag)
# # We want to save these in the file
# with open("modified.html","w") as f :
#     f.write(str(soup))

# We want to know that the specific container contains the particular attribute or not
# Why it is giving erroe
# cont = soup.find(id="container")
# print(cont.has_attr("contenteditable"))

# Creating the function
# In tutorial it is running but here it is not
# def has_class_but_not_id(tag) :
#     return tag.has_attr("class") and not tag.has_attr("id")
# has_class_but_not_id()

# result = soup.find_all(has_class_but_not_id("class"))
# print(result)








