# Address Entry

#contact information
contact_info = {
    "Full_name": "Jane Smith",
    "address": "123 Sam st",
    "city": "Charlotte",
    "state": "NC",
    "zip": "12345"
}


print(f"""\
{contact_info["Full_name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}
""")

Full_name = { "first name":"Jane", 
             "last name": "Smith"}
Full_name.update({"honorific": "Ms."})            

print(str,
{contact_info['Full_name']},
{contact_info['address']},
{contact_info['city']},{contact_info['state']},{contact_info["zip"]})