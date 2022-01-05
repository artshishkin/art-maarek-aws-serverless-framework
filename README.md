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

#####  14. Removing the function

-  `sls remove`

####  Section 5: AWS Lambda & Serverless - In Depth

#####  16. Create AWS Lambda function using any runtime

-  `sls create --help` - list
-  `sls create --template aws-nodejs --path sls-nodejs-example`
-  `sls create --template aws-java-maven --path sls-java-example`

#####  18. JSON to YAML Practice Exercise!

- [json2yaml](https://www.json2yaml.com/)

#####  19. Functions timeout and memory

-  [custom serverless framework json schema](https://raw.githubusercontent.com/softprops/serverless-yml-schema/master/serverless-schema.json)
-  `sls invoke -f hello-short-timeout -l`
-  `sls invoke -f hello-long-timeout -l`

#####  20. IAM Permissions for Lambda Functions

1.  Deploy stack
    -  `sls deploy --verbose`
2.  Invoke function    
    -  `sls invoke -f hello-iam-example -l`
    -  **got an error**   
    -  `{`
    -  `  "errorMessage": "An error occurred (AccessDeniedException) when calling the ListFunctions operation: User: arn:aws:sts::392971033516:assumed-role/sls-python-iam-dev-eu-north-1-lamb`
    -  `  daRole/sls-python-iam-dev-hello-iam-example is not authorized to perform: lambda:ListFunctions on resource: * because no identity-based policy allows the lambda:ListFunctions action",`
    -  `  "errorType": "ClientError",`
    -  `  "stackTrace": [`
    -  `  "  File \"/var/task/handler.py\", line 6, in hello\n    response = client.list_functions()\n",`
    -  `  "  File \"/var/runtime/botocore/client.py\", line 386, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n",`
    -  `  "  File \"/var/runtime/botocore/client.py\", line 705, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"`
    -  `]`
    -  `}`
3.  Add IAM Permissions to ListFunctions
4.  Invoke -> OK

#####  22. VPC for Lambda Functions

-  VPC console
    -  VPCs -> 1
    -  Subnets -> 3 (for example choose 2)
-  Security Groups
    -  create security group
    -  Name: `my-lambda-sg`
    -  Description: `Test Security Group`
    -  Create
-  GroupId: `sg-0b46b252a446a15e4`
-  Deploy: `sls deploy --verbose`
-  View VPC in Lambda Configuration
    -  Lambda Console -> Configuration -> VPC
    -  Match: VPC, Subnets, Security groups
-  View Lambda Role
    -  Attached policy: AWSLambdaVPCAccessExecutionRole

####  Section 6: Real World Example 1 - S3 Thumbnails

#####  26. Implementation of Thumbnail Service

-  `serverless plugin install -n serverless-python-requirements`

