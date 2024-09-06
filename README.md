# Equity Deployment Automation

Download the releases from github and place it inside the build folder

### Pre requisites

1. Create two folders at the project root by the names build and release

### Steps to Run

2. Inside the bash terminal

   `source entrypoint && initiate_build`

### TODO

- [x] Create build from packages

  - [x] Make version changes to the package files

- [x] Download the files from Google Drive

  - [x] Test Cases
  - [x] JIRA Dump
  - [x] Deployment Doc

- [x] Push files to s3

  - [x] Release files
  - [x] Test cases and JIRA Dump
  - [x] Deployment Doc

- [x] Make changes to the deployment doc

- [x] Send a mail using outlook api

  - [x] Write function to trigger outlook mail
  - [x] Prepare mail body
    - [x] Mention S3 URI Links of Test Cases , Jira Dump and Build Folders

- [x] Happy Path Testing

- [x] Handle edge cases

  - [x] Case where UI Build is not sent

### DOCS

[TODO](https://docs.google.com/document/d/1t1WGxcrz6IO44S0I_R4W11g7n8WmIjHz1OGQTxWQtE8/edit)
