# Company-ResT-API

API - company information on AWS

The aim is to provide a public API on AWS that enables a user
Request and save company information (e.g. company Name, Legal Entity
Number of employees, Share Capital ). Here is an example of the data:
Company Name Legal Entity Number of employees Share Capital
BMW              AG            13000             800000
Commerzbank      AG            14000             500000
Example Company  GmbH          300               50000


tasks
Create an API prototype with Python, which has the following functionalities:
• GET request to receive data from the database as json.
• POST request to update or new company information in the database Filing companies. It should also be
possible to enter completely new information (such as
company rating) for a company entry.
Save the data in an AWS database. Which is best for this use Case suitable?
Components that can be used in AWS for this:
- AWS Lambda
- AWS API Gateway
During the presentation there will be a code review and a review of the
Configuration of the AWS services.
Bonus:
• Which services could be used to monitor the architecture (monitoring /
Logging)?
• Integrate user authentication. Keyword "Amazon Cognito"
