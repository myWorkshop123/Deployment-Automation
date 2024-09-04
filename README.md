# Equity Deployment Automation

Download the releases from github and place it inside the build folder

### Pre requisites

1. Create two folders at the project root by the names build and release

### Steps to Run

2. Inside the bash terminal

   `source entrypoint && main`

### TODO

- [x] Download the files from Google Drive

  - [x] Test Cases
  - [x] JIRA Dump
  - [x] Deployment Doc

- [x] Push files to s3

  - [x] Release files
  - [x] Test cases and JIRA Dump
  - [x] Deployment Doc

- [ ] Make changes to the deployment doc

  - [ ] Mentions of the tickets table
  - [ ] Changes to the version
  - [ ] Changes to the path
  - [ ] Changes to the steps
  - [ ] Changes to the rollback

- [ ] Send a mail using outlook api

  - [x] Write function to trigger outlook mail
  - [ ] Prepare mail body
    - [ ] Mention S3 URI Links of Test Cases , Jira Dump and Build Folders

### DOCS

[TODO](https://docs.google.com/document/d/1t1WGxcrz6IO44S0I_R4W11g7n8WmIjHz1OGQTxWQtE8/edit)
