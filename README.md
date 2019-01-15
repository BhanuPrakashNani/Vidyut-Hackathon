[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Amrita Mailroom Portal(AMP)

### Issues
The current mail room system in our college has few issues:
* There is lot of crowd as the students and staff come frequently to check of their package has arrived not being aware of the time of delivery.
* Lot of paperwork. The package arrival logs are noted down in a register which is time consuming and there are chances that the register paper might get torn or something related.
* Sometimes students miss out their names while checking the register. As a result, their packages get returned.
* Storage. The way of storage of packages is inefficient as it takes a long time for the mailman to search for the name on the package. 
* COD(Cash on delivery). Presently there isn't good facility for COD. Postman usually rings up the recipient and there are high chances that the student would miss the calls.

### Our innovative solutions
* Manage crowd: We came up with an idea of making a portal with three types of users: Admin, mailman and the recipients. The admin has access to everything. The mailman is a person who has access to add the packages which would contain details of recipients, service and tracking id. Recipients can view a public dashboard as well as a personlised one where they can see their delivered items.
* Paperwork: By creating this portal, we are reducing lot of paperwork and saving everything into database.
* Notification: Thus a student wil never miss his package as he can see his dashboard for the packages that have arrived in the mailroom.
* Storage: We have thought of an idea to tokenize the packages. So that it would be easier for the mailman to search for the package. This while filling the details of arrived package, the mailman wil assign a token(a number) to the package.
COD: A section for the recipients to apply for COD, where they would have to enter the name, tracking id, roll number and the amount. After application of COD, the mailman will get a notification regarding this and will have an option to tick if the payment is done. After successful payment, both will recieve a confirmation email to avoid confusions.


### Milestones:
* Image processing to extract information of invoice.
* Integration with AUMS.
* Integrating with gmail to send comfirmation mails on delivery and COD.

### Technologies used:
*Django framework
*python scripts for OCR
*HTML
*CSS.
