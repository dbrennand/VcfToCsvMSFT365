# VcfToCsv
A Python 3.8 script to convert a contact file in .vcf format to CSV.

## Context

I wrote this script as I couldn't believe Microsoft 365 does not allow contacts to be imported from a .vcf file and only allows imports from a CSV file.

**This script was written quickly.**

For my use case, I only required first and last names, phone number and email. However, you could easily add additional columns to this script.

This script uses CSV file headers from the example CSV file located [here](https://support.office.com/en-gb/article/create-or-edit-csv-files-to-import-into-outlook-4518d70d-8fe9-46ad-94fa-1494247193c7).

# Dependencies
* Written in Python 3.8.

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
black = "*"

[packages]
vobject = "*"
fire = "*"
requests = "*"

[requires]
python_version = "3.8"

[pipenv]
allow_prereleases = true

```

## Example Usage
```python
python main.py convert /path/to/mycontacts.vcf
```

## Authors -- Contributors

* **Dextroz** - *Author* - [Dextroz](https://github.com/Dextroz)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) for details.
