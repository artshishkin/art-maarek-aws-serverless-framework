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

#####  10. Deploying our First Function

1.  List commands
    -  `serverless --help`
    -  `sls --help` - shortcut
2.  Create 
    -  `sls create --template aws-python --path hello-world-python`
3.  Runtime version
    -  `runtime: python3.8`
4.  Deploy
    -  `sls deploy --verbose`

#####  11. Running the function from the CLI

-  `sls invoke -f hello -l`

#####  12. Updating the function from the CLI

1.  Redeploy entire stack
    -  `sls deploy --verbose`
    -  too long
2.  Deploy only function
    -  `sls deploy function -f hello`

#####  13. Fetching the function logs from the CLI

-  `sls logs -f hello -t`
    - `-t` - tail



