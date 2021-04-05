#kata link: https://www.codewars.com/kata/514a024011ea4fb54200004b  
#Instruction : Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

#Code:
def domain_name(url):
    import re
    stripped_url = re.split("[://.]", url)
    if stripped_url.count("https") == 1:
        stripped_url.remove("https")
        
    domain = max(stripped_url, key=len)
    
    return domain
