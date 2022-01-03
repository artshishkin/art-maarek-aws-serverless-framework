# art-maarek-aws-serverless-framework
AWS Lambda and the Serverless Framework - Hands On Learning!  - Tutorial from Stephane Maarek (Udemy)

####  Section 4: AWS Lambda & Serverless - Getting Started

#####  9. Installing Serverless

[Serverless Framework](https://www.serverless.com/)
1.  Install Serverless
    -  `npm install -g serverless`
2.  Create User for Serverless Framework
    -  IAM Console -> Users -> Add
        -  User name: `serverless-admin`
        -  Select AWS credential type: `Access key - Programmatic access`
        -  Attach existing policies directly: `AdministratorAccess`
        -  Create User
        -  Download .csv
3.  Configure credentials
    -  `serverless config credentials --provider aws --key XXX --secret YYY --profile serverless-admin`
