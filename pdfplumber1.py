# import pdfplumber
# import os
# path = "../DATA/Carhire/Carhire/AVIS/E129344375T_20221006_278191836.pdf"
# with pdfplumber.open(path) as pdf:
#     first_page = pdf.pages[0]
#     result = first_page.extract_text()
#     print (result)

# if "avis" in result:
#     for row in result.split('\n'):
#         if row.startswith('Invoice Date'):
#             date = row.split()[-1]
#             print(date)
#             break
    

import pdfplumber
import os

path = "..\DATA\Carhire\Carhire\AVIS\E591917222T_20221007_278253039.pdf"
all_text = ""
summ = 0
with pdfplumber.open(path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        # print(repr(text))
        summ += len(text)
        all_text += text #make one long string for all pages of the pdf

#Tip : repr to print the text as it is with '\n'

# print(len(all_text))
# print(summ)
#write to a text document 
with open("../Output/output_avis-5.txt", "w") as f:
    f.write(all_text)


if "avis" in all_text:
    #agency account number 
    account_no = 269994521
    print(account_no)
    #car provider
    car_provider = "ZI C"
    print(car_provider)
    #Printing invoice number
    for row in all_text.split('\n'): 
        if row.startswith('Invoice No.'):
            Inv  = row.split()[-1]
            print(Inv)
            # break
    #invoice date
    # for row in all_text.split('\n'):
        if row.startswith('Invoice Date'):
            date = row.split()[-1]
            print(date)
            break   
    #Travel date
    for row in all_text.split('\n'):
        if row.startswith('Check-out date'):
            Rdate = row.split()[3]
            print(Rdate)
            break  
    #Reservation number
    for row in all_text.split('\n'):
        if "Reservation No" in row:
            Rno = row.split()[-1]
            print(Rno)
    #passanger name
    for row in all_text.split('\n'):
        if row.startswith('Rented by'):
            rentedby= row.split (':',1)[1].split('Total')[0].strip()
            print(rentedby)

    # Gross amount
    gross ="null"
    print(gross)
    # Vat %
    for row in all_text.split('\n'):
        if row.startswith('VAT Charge on Taxable'):
            vat = row.split("@",1)[1].split()[0]
            print(vat)
    # comm
    for row in all_text.split('\n'):
        if "Commission @" in row:
            com = row.split('@')[1].split(' ')[0]
            print(com)
            break  
    # nett amount
    for row in all_text.split('\n'):
        if row.startswith('This Invoice is due for payment by'):
            nett = row.split()[-1]
            print(nett)
            break
    # currency
    currency = "GBP"
    print(currency)
    # payment type 
    P_type = "Agency"
    print(P_type)
    # destination
    for row in all_text.split('\n'):
        if row.startswith('Start location'):
            dest = row.split(':')[1].split('Check-out')[0].strip()
            print(dest)
            break  

        