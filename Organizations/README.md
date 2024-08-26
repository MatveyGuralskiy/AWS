# AWS Organizations
AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization

Consolidated Billing - One Billing to all accounts

Organization Units - To group users AWS

Service Control Policies - Ban or limit some resources for accounts(users) or groups(units)

Isolate Resources for Development, Staging, Production and more

Centralize all Users

Summary sales, AWS Credits for everyone

Reserved Instances from every account

## Types of Accounts:

Root Account - Master Account with VISA/MASTER CARD

Member Account - has 2 types:         
        1. Invited  
        2. Created

Every Project or Environment has different account IAM

* Before you delete/remove an account you should back to him and fill all information and Credit Card

<img src="https://miro.medium.com/v2/resize:fit:1200/1*rHTw2yBfqyRMrFuEfWBQqw.png">

## Service Control Policies (SCP)
It's only to Ban or Limit Resources access/actions

SCP can be attached to different targets:
1. Organizational Account (Member Account)
2. Organization Unit
3. Organization Root

**Maximum** count of Policies it's 5!