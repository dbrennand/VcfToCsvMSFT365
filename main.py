import vobject
import csv
import requests
import fire


def main(file_path: str):
    """
    A Python 3.8 script to convert a contact file in .vcf format to CSV.
    :param file_path: The path to the .vcf file.
    """
    # Load contacts.
    vcf_data = load_vcf(file_path=file_path)
    csv_headers = download_csv_headers()
    # Create CSV file.
    with open("contacts.csv", "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=csv_headers, delimiter=",")
        csv_writer.writeheader()
        # Init counter.
        count = 0
        while True:
            # Get the next contact.
            contact = next(vcf_data, None)
            # If contact is None, break out of the while loop. No contacts left.
            if contact is None:
                break
            # There is a contact, process it.
            else:
                # Obtain the full name. 
                full_name = contact.fn.value.strip().split(" ")
                # Obtain first name from full name list.
                first_name = full_name[0]
                try:
                    # Attempt to obtain last name from full name list.
                    last_name = full_name[1]
                # Catch if no last name is provided for the contact.
                except IndexError:
                    print("No last name provided for this contact.")
                    # Set to empty string.
                    last_name = ""
                try:
                # Attempt to obtain the email for the contact.
                    email = [email.value for email in contact.contents["email"]][0]
                # Catch if no email is provided for the contact.
                except KeyError:
                    print("No email provided for this contact.")
                    email = ""
                # Obtain phone number.
                phone_number = [tel.value for tel in contact.contents["tel"]][0]
                print(
                    f"Creating CSV row contact first name: {first_name} last name: {last_name} mobile phone: {phone_number} email address: {email}"
                )
                # Add to CSV file.
                csv_writer.writerow(
                    {
                        "First Name": first_name,
                        "Last Name": last_name,
                        "Mobile Phone": phone_number,
                        "E-mail Address": email,
                    }
                )
                count += 1
    print(f"---\n{count} contacts processed.")


def download_csv_headers():
    """
    Download the example CSV file and extract the headers.
    :rtype csv_headers: The example CSV headers.
    """
    example_csv_file = "https://download.microsoft.com/download/5/B/2/5B2108F8-112B-4913-A761-38AFF2FD8598/Sample%20CSV%20file%20for%20importing%20contacts.csv"
    resp = requests.get(example_csv_file)
    with open("example.csv", "wb") as example_csv:
        example_csv.write(resp.content)
    with open("example.csv") as example_csv:
        csv_reader = csv.reader(example_csv, delimiter=",")
        csv_headers = next(csv_reader)
        return csv_headers


def load_vcf(file_path: str):
    """
    Load the contents of the .vcf file.
    :param file_path: The file path to load contacts from.
    :rtype: Generator object.
    """
    # Load .vcf file.
    with open(file_path) as vcf_file:
        vcf_data = vobject.readComponents(vcf_file.read())
    return vcf_data


if __name__ == "__main__":
    __version__ = "0.0.1"
    fire.Fire({"convert": main})
