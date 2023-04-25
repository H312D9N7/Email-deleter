# **Email Deleter**

This is a Python file that uses IMAP to grab emails and delete them.
I made this because I was getting tired of all the emails cluttering my inbox
that I did not need anymore.

## *How to use*

The variables *username* and *password* are your email login credentials.
Imap must connect to the incoming messages server use link in code to
find supported servers. Next select your search function and fill out your parameters. There is an optional loop in the deletion loop that prints to the console the subjects of the emails that are being marked for deletion, if the program is running slow for you than you can remove it and the deleter will still work.