'''

What you'll do:
  Replacing the old domain name (abc.edu) with a new domain name (xyz.edu).
  Storing all domain names, including the updated ones, in a new file user_emails2.csv

'''


import csv
import re

def main():
    def contains_domain(address, domain):
      domain_pattern = r'[\w\.-]+@'+domain+'$'
      if re.match(domain_pattern, address):
        return True
      return False

    def replace_domain(address, old_domain, new_domain):
      old_domain_pattern = r'' + old_domain + '$'
      address = re.sub(old_domain_pattern, new_domain, address)
      return address

    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    #data_dir = '/home/<username>/data/'
    data_dir = ''
    csv_file_location = data_dir + 'user_emails2.csv'
    report_file =  data_dir + 'updated_user_emails.csv'

    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]

    for email_address in user_email_list:
        if contains_domain(email_address, old_domain):
            old_domain_email_list.append(email_address)
            replaced_email = replace_domain(email_address, old_domain, new_domain)
            new_domain_email_list.append(replaced_email)

    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
          for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
            if user[email_index] == ' ' + old_domain:
              user[email_index] = ' ' + new_domain
    f.close()

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()

main()