Feature: Install Mysql and nginx

#	Scenario: Setup and Install Mysql
#		Given I have a running ubuntu docker container
#		When I run my config scripts
#		Then It should succeed
#		And mysql should be running on port 3306
	
	Scenario: have nginx up and running
		Given We have a docker container running
		When I run the scripts
		Then nginx should be installed
		And nginx should be running on port 80
