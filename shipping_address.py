

def checkstreetnumber(street):
    number_count = 0
    street_number = ""
    for number in street:
        if number.isdecimal():
            number_count += 1
            street_number = street_number + number

    if number_count == 0:
        street_check = False
    elif number_count > 6 :
        print("Street number can not be so long")
    else:
        street_check = True
    
    return street_number,street_check

def checkstreet(street):
    count = 0
    street_address = ""
    for alphabet in street:
        if alphabet.isalpha():
            street_address = street_address + alphabet
            count += 1
 
    if count < 6 :
        street_confirmation = False
    else:
        street_confirmation = True
    
    return street_address,street_confirmation

def checkpincode(pincode_input,check,province):
    count = 0
    postal = ""
    for pin in pincode_input:

        if count == 0:
            if province == "ON":
                if pin.isalpha() and count == 0:
                    
                    count += 1
                    pin = pin.upper()
                    if pin == check[0] or pin == check[1] or pin == check[2] or pin == check[3] or pin == check[4]:
                        pincode = True
                        postal = postal + pin
                    else:
                        pincode = False
                        print("**First letter of pincode is does not match with province name")
                        break

            elif province == "QC":
                if pin.isalpha() and count == 0:
                    count += 1
                    
                    pin = pin.upper()
                    if pin == check[0] or pin == check[1] or pin == check[2]:
                        pincode = True
                        postal = postal + pin
                    else:
                        pincode = False
                        print("**First letter of pincode is does not match with province name")
                        break
                    
            else :
                if pin.isalpha() and count == 0:
                    count += 1
                    
                    pin = pin.upper()
                    if pin == check:
                        pincode = True
                        postal = postal + pin
                    else:
                        pincode = False
                        print("**First letter of pincode is does not match with province name")

        elif count == 1:
            
            if pin.isdecimal():
                pin = pin.upper()
                pincode = True
                count += 1
                postal = postal + pin

        elif count == 2:
            
            if pin.isalpha():
                pin = pin.upper()
                pincode = True
                count += 1
                postal = postal + pin

        elif count == 3:
            
            if pin.isdecimal():
                pin = pin.upper()
                pincode = True
                count += 1
                postal = postal + pin

        elif count == 4:
            
            if pin.isalpha():
                pin = pin.upper()
                pincode = True
                count += 1
                postal = postal + pin
        
        elif count == 5:
            
            if pin.isdecimal():
                pin = pin.upper()
                pincode = True
                count += 1
                postal = postal + pin

        else:
            pincode = False
    print(postal)
    return postal,pincode
            
print("Hello Sir,Thank you for buying product from our website")
print("Can I grab your Shipping address for the product you bought ?")
reply = input("Please reply yes or no : ")

reply = reply.lower()
if reply == "no":
    print("Your order is cancelled")


else :
    
    street_check = False
    comma = False
    city_check = False
    province_check = False
    pincode = False
    while street_check == False or city_check == False or comma == False or province == False or pincode == False:

        if street_check == False:
            street = input("Enter your street number first and then street name followed by name : ")
            street_number,streetnumber_check = checkstreetnumber(street)
            street_address,street_check = checkstreet(street)
            
        if city_check == False or comma == False or province == False or pincode == False:    
            city_count = 0
            city_input = input("Enter your City and Province must be seprated by comma e.g.(Hamilton,ON) : ")
            for word in city_input:
                if word.isalpha():
                    city_check = True
                    city_count += 1
                else:
                    city_check = False
                if word == ",":
                    comma = True
            province = city_input[-2:].upper()
        
            if province in ["ON","AB","BC","MB","NB","NL","NT","NS","NU","PE","QC","SK","YT"]:
                province_check = True

            pincode_input = input("Enter the valid postal code : ")
        
            if province == "AB":
                postal,pincode = checkpincode(pincode_input,"T","AB")

            elif province == "BC":
                postal,pincode = checkpincode(pincode_input,"V","BC")

            elif province == "MB":
                postal,pincode = checkpincode(pincode_input,"R","MB")   

            elif province == "NB":
                postal,pincode = checkpincode(pincode_input,"E","NB")
       
            elif province == "NL":
                postal,pincode = checkpincode(pincode_input,"A","NL")

            elif province == "NT" or province == "NU":
                postal,pincode = checkpincode(pincode_input,"X","NT")

            elif province == "NS":
                postal,pincode = checkpincode(pincode_input,"B","NS")

            elif province == "ON":
                postal,pincode = checkpincode(pincode_input,["K","L","M","N","P"],"ON")

            elif province == "PE":
                postal,pincode = checkpincode(pincode_input,"C","PE")

            elif province == "QC":
                postal,pincode = checkpincode(pincode_input,["G","H","J"],"QC")

            elif province == "SK":
                pincode = checkpincode(pincode_input,"S","SK")

            elif province == "YT":
                postal,pincode = checkpincode(pincode_input,"Y","YT")

            else:
                pincode == False


        if street_check == False:
            print("**You haven't entered appropriate street address")

        if city_check == False:
            print("**You haven't entered the right city name and province name")
        if comma == False:
            print("**You haven't entered comma between city and province")
        if province == False:
            print("**You haven't entered right province name")
        if pincode == False:
            print("**The pincode you entered is wrong")

    if province == "AB" or province == "BC" or province == "MB" or province == "SK":
        cost = "$12"

    elif province == "NB" or province == "NL" or province == "NS" or province == "PE":
        cost = "$15"

    elif province == "NT" or province == "NU" or province == "YK":
        cost = "$20"

    elif province == "ON" or province == "QC":
        cost = "$8"

    print("Your order is shipping to " + street_number +" "+ street_address + ", " \
      + city_input + " - " + postal[:3] + " " + postal[3:] + " will cost " + cost + ".") 
