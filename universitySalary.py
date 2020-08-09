# Sahithi Mankala
#import necessary libraries for project including regex and urllib
import re
import urllib.request

def name_to_url(name):
    '''converts the name argument given into the correctly formatted name for the url'''
    holder = name.replace('.', '')
    holder = holder.lower()
    if ',' in holder:
        comma_index = holder.index(',')
        holder = holder[comma_index:] + " " + holder[:comma_index]
        holder = holder.replace(',', '')
    if holder[0] == " ":
        holder = holder[1:]
    holder = holder.replace(' ', '-')

    return holder

def report(name):
    ''' based on the given name, the function returns the salary, rank, year hired, and job title for that person from the appropriate url '''
    #declare and initializa variables for salary,rank,job, and year hired
    rank_f =0
    job_f = None
    comp_f =0
    years_f =0
    #takes in name given and converts into url to find person's profile
    name = name_to_url(name)
    url_base = 'http://cs1110.cs.virginia.edu/files/uva2018/'
    url = url_base + name
    #regex expressions for each field
    job_re = r'Job title:([^<]*)'

    comp_re = r'<h2 class="pay" id="paytotal">([^<]*)</h2>'

    rank_re = r'<tr><td>University of Virginia rank</td><td>([^of]*) of 8,582<!--not null --></td></tr>'

    years_re = r'<tr><td>Hire date</td><td>[0-9]*/[0-9]*/([0-9]*)</td></tr>'
    #try except to try to open and read the url page and exit if an error occurs
    try:
        fstream = urllib.request.urlopen(url)
        page_text = fstream.read().decode()
    except urllib.error.URLError:
        return job_f, comp_f, rank_f, years_f

    #compiles the regex expressions
    job_finder = re.compile(job_re)
    comp_finder = re.compile(comp_re)
    rank_finder = re.compile(rank_re)
    years_finder = re.compile(years_re)
    #reads through the html page looking for the Hire Date match using finditer function and converts number into an int
    for match in years_finder.finditer(page_text):
        years_f = match.group(1)
        years_f = int(years_f)
    # reads through the html page looking for the salary amount match using finditer function
    # removes extra commas and converts number into a float
    for match in comp_finder.finditer(page_text):
        comp_f = match.group(1)
        comp_f = comp_f[1:]
        if ',' in comp_f:
            comp_f = comp_f.replace(',','')
        comp_f = float(comp_f)
    # reads through the html page looking for the Job Description match using finditer function and removes extra characters
    for match in job_finder.finditer(page_text):
        job_f = match.group(1)
        job_f = job_f[1:]
        if '&amp;' in job_f:
            job_f = job_f.replace('&amp;', '&')
        if ';' in job_f:
            job_f = job_f.replace(';', "")
        if '&#39' in job_f:
            job_f = job_f.replace('&#39', "'")


    # rank is calculated based off of an individual's salary
    # reads through the html page looking for the Rank match using finditer function and removes any commas
    for match in rank_finder.finditer(page_text):
        rank_f = match.group(1)
        if ',' in rank_f:
            rank_f = rank_f.replace(',','')


    #retuens job, salary, rank, and Hire year for desired individual
    return job_f, comp_f, rank_f, years_f



