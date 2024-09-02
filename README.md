# Equity Deployment Automation


Download the releases from github and place it inside the build folder


### Pre requisites 
1. Create two folders at the project root by the names build and release

### Steps to Run
2. Inside the bash terminal

    `source entrypoint && main`


### TODO

- [x] Download the Jira dump and test cases files 
- [ ] Push files to s3 
	- [ ] Release files 
	- [ ] Test cases and JIRA Dump 

- [ ] Download the deployment doc 

- [ ] Make changes to the deployment doc 
	- [ ] Mentions of the tickets table
	- [ ] Changes to the version
	- [ ] Changes to the path
	- [ ] Changes to the steps 
	- [ ] Changes to the rollback
- [ ] Send a mail