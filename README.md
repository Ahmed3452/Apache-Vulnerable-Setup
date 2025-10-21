Vulnerable Web Lab

This project provides a quick lab environment using docker compose to create a vulnerable Apache web server with common security flaws, designed specifically for testing security tools like NIDS/IPS.

Included Services

    Web Server (Apache): Runs on port 8082.

    FTP Server (vsftpd): Runs on port 21.

    SSH Server (OpenSSH): Runs on port 2222.

    Database (MySQL): Runs on port 3306.

Included Vulnerabilities

    Command Injection: via /cgi-bin/test.cgi?ip=...

    Directory Listing: Enabled on the server.

    Weak Passwords: On FTP and SSH services.

    Anonymous FTP Login: Enabled.
