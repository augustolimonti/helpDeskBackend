# Help Desk Backend

This backend is designed to power a basic "help desk" or support ticket management system.

# Table of Contents
 - Features
 - Hosting on AWS EC2
 - SSL Configuration
 - API Endpoints
 - Contributing

# Features
  - Ticket Submission: Users can submit support tickets with their name, email, and a problem description.
  - Admin Panel: Support staff can view tickets, respond to them, and update their status.

# Hosting on AWS EC2

The backend is deployed on an Amazon Web Services (AWS) Elastic Compute Cloud (EC2) instance. Here's a brief overview:

  - Instance Type: The EC2 instance type can be adjusted based on traffic expectations.
  - Security: Security Groups in AWS have been set to ensure only necessary ports are exposed.
  - IP Address: The instance uses a Public IP for easy access.
  - Domain Configuration: While the system currently uses the public IP, it's possible to associate it with a custom domain or subdomain.

# SSL Configuration

For secure communication, I've used a self-signed SSL certificate. Note: In a real production environment, I'd use a certificate from a recognized certificate authority.

# API Endpoints

  - POST /add/: Submit a new ticket.
  - GET /tickets/: Fetch all tickets (primarily for admin usage).
  - DELETE /delete/<int:ticket_id>/ Deletes all tickets (primarily for admin usage).
  - PATCH update_status/<int:ticket_id>/ Updates the ticket status (primarily for admin usage).

# Future Add-Ons I would Consider
As the backend evolves, there are several improvements and new features that can be incorporated to enhance both security and functionality. 
Two honorable mentions are the following:

1. API Encryption:
  - Description: Encrypt all data sent to and from the API to ensure secure data exchange and protection against man-in-the-middle attacks.
  - Implementation: Integrate a system like JWT (JSON Web Tokens) to provide encrypted and signed tokens for API calls.

2. Admin Authentication:
  - Description: Ensure that only authorized personnel can access the admin panel and make administrative changes.
  - Implementation: Implement a robust username/password authentication mechanism, possibly using Django's built-in admin authentication or integrating with frameworks like django-allauth or django-rest-auth.

3. SSL-secured Domain:
 - Point a legitimate domain name to the EC2 instance to ensure users don't encounter warnings or mixed content issues.
 - By doing so, the front end will operate smoothly without hitches related to insecure content.



