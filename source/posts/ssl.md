Date: 2012-06-13
Title: Installing Free SSL certificate with StartSSL and Webfaction
Slug: ssl
Category: Blog
Tags: ssl, webfaction

For my next big project it will be mandatory to use a SSL certificate for the
web application. I have never dealt with SSL before, so I am going to take
some notes here. Let's see how it goes...

I decided to give [StartSSL](https://www.startssl.com/) a trie because when I
asked around it got recommended several times for offering a good free
certificate. Their website looks exceptionally ugly but since it is free, I am
not going to compain here.

After chosing the free option I had to provide my name, address, phone number
and email. I got an activation link via email immediately. Adter using the
activation link I was told that my details will be checked within the next 24
hours. Twenty minutes later I got another activation link and was told to
generate a private certificate for my browser which I would need to
authenticate myself against StartSSL.

I was asked to backup that certificate to an external medium, so I'm going to
store it in an encrypted folder in my Dropbox account. There is a description
on [how to export your client certificate](https://www.startssl.com/?app=25#4).

After some searching I found the _Control panel_ link on the StartSSL website.
It presented me with a field where I can enter the domain name that I want to
use. I entered my domain name and needed to provide an email address where
they would send a verification link to. I got several options like
postmaster@mydomain.com but thankfully I also got the option of my own email
address which I used when creating my StartSSL account.

Next I was presented with a form to generate my private key. Unfortunately my
passphrase contained spaces which resulted in an error, so I had to start the
process over again. Clicking back crashed the website. A few clicks later I
found a way to start the process again by clicking at the _Certificates Wizard_
tab and chosing the web certificate.

This time I chose a valid password. I needed to copy my private key into a file
ssl.key and run the command "openssl rsa -in ssl.key -out ssl.key", however I
do not understand what this command does.

After this step I had to provide at least one subdomain, so I chose _www_.

The next step started processing the certificate and I had to stare at a
loading animation for quite some time. After 3 minutes or so I got unpatient
and clicked at the _Continue_ button again which, after a few more seconds, led
me to the next page. I was instructed to copy and save the certificate into a
file _ssl.cert_. This chunk of text was significantly longer than the private
key so maybe there is a good reason why the computation took so long.

I also had to download the intermediate and root certificates which came in the
form of .pem files.

It seeed as if the process was done now, so I headed over to the [SSL docs at
Webfaction](https://docs.webfaction.com/user-guide/websites.html#secure-sites-https).

The docs just say "_To enable your security certificate, please upload the
certificate and key files to your home directory and open a support ticket to
request activation._", so I used _scp_ to copy the .pem, .crt and .key files
into the home folder of my Webfaction server.

I opened a support request in my Webfaction account and asked for activation
of the certificate. In the meantime I created another website in the control
panel that uses HTTPS and maps the same apps as the non-HTTPS version.

Just a few minutes after opening the support ticket I got a friendly response
from the Webfaction support telling me that everything worked fine and indeed,
I can now access my website via HTTPS.

Wow. That was easy! I'm going to use SSL for all my sites from now on.
