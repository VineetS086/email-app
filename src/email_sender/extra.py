data = {
    '2019':{
        'BCS':89,
        'BEC':109,
        'BME':53,
        'BCE':61,
        'BEE':38,
        'BAR':24,
        'IES':36,
    },
    
    '2018':{
        'BCS':90,
        'BEC':71,
        'BME':55,
        'BCE':63,
        'BEE':37,
        'BAR':24,
        'IES':30,
    },

    '2017':{
        'BCS':59,
        'BEC':65,
        'BME':34,
        'BAR':30,
        'IES':44,
    }

}

import re

def all_mails_in_branch(year, branch):
    mail_domain = '@smvdu.ac.in'
    students = data[year][branch]
    students_email = [year[2:]+branch.lower()+'0'*(3-len(str(i)))+str(i)+mail_domain for i in range(1,students+1)]
    print(len(students_email))
    return(students_email)


def email_format(email_keywords):
    added_emails = []
    for email_keyword in email_keywords:
        try:
            year    = email_keyword[1:5]
            branch  = email_keyword[6:-1]
            added_emails.extend(all_mails_in_branch(year, branch.upper()))
        except:
            pass

    return(added_emails)

def process(email_str):
    email_str = email_str.replace(",", " ")
    email_list = email_str.split()
    email_keywords = re.findall(r'\[\d{4}-\w{3}\]', email_str)

    email_list = [email for email in email_list if email not in email_keywords]

    print(email_keywords)
    print(email_list)
    email_list.extend(email_format(email_keywords))
    return(email_list)

#[2019-CSE]

'''email_str = '19bcs086@smvdu.ac.in vineet@gmail.com , [2019-BCS] [2018-BME] ,[2019-BCS]'
process(email_str)'''

#all_mails_in_branch('2019','BEC')