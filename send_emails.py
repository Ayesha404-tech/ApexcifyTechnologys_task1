#!/usr/bin/env python3
import smtplib
import threading
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import argparse

# Dry run flag for testing (set to False for actual sending)
DRY_RUN = False

# Sender credentials (Gmail with App Password)
SENDER_EMAIL = "ayeshashabbir053@gmail.com"
SENDER_PASSWORD = "rerf qyer qens vcas"  # Gmail App Password

# List of 50+ predefined recipient emails for scalability testing
RECIPIENTS = [
    "recipient3@example.com",
    "recipient3@example.com",
    "recipient3@example.com",
    "recipient4@example.com",
    "recipient5@example.com",
    "recipient6@example.com",
    "recipient7@example.com",
    "recipient8@example.com",
    "recipient9@example.com",
    "recipient10@example.com",
    "recipient11@example.com",
    "recipient12@example.com",
    "recipient13@example.com",
    "recipient14@example.com",
    "recipient15@example.com",
    "recipient16@example.com",
    "recipient17@example.com",
    "recipient18@example.com",
    "recipient19@example.com",
    "recipient20@example.com",
    # Add more recipients as needed (100+ supported)
]

# Email content
EMAIL_SUBJECT = "Automated Notification - Apexcify Technologies"
EMAIL_BODY = """Dear Recipient,

We are reaching out to you with important information from Apexcify Technologies.

This is an automated message sent to multiple recipients simultaneously. Our email automation system allows us to send personalized or bulk messages efficiently to a large audience.

Key Features of Our Email System:
• Send to multiple recipients in one go
• Reliable delivery with error handling
• Professional email formatting
• Timestamp tracking

If you have any questions or would like to unsubscribe, please reply to this email.

Best regards,
Apexcify Technologies Team
"""

# STATISTICS AND TRACKING
class EmailStats:
    """Track email sending statistics"""
    def __init__(self):
        self.total = 0
        self.successful = 0
        self.failed = 0
        self.failed_list = []
        self.lock = threading.Lock()
        self.start_time = None
        self.end_time = None
    
    def increment_successful(self):
        with self.lock:
            self.successful += 1
    
    def increment_failed(self, email, reason):
        with self.lock:
            self.failed += 1
            self.failed_list.append({"email": email, "reason": reason})
    
    def get_duration(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0

stats = EmailStats()

# EMAIL SENDING FUNCTIONS
def send_email_to_recipient(recipient_email, subject, body, sender_email, sender_password):
    """
    Send email to a single recipient

    Args:
        recipient_email (str): Recipient's email address
        subject (str): Email subject
        body (str): Email body content
        sender_email (str): Sender's email address
        sender_password (str): Sender's email password or app password

    Returns:
        bool: True if successful, False otherwise
    """
    if DRY_RUN:
        # Simulate sending for testing
        time.sleep(0.1)  # Simulate network delay
        return True  # Always succeed in dry run for full testing

    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg['Date'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')

        # Attach body
        msg.attach(MIMEText(body, 'plain'))

        # Send email via Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure connection
        server.login(sender_email, sender_password)

        # Send message
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        return True

    except smtplib.SMTPAuthenticationError:
        return False, "Authentication failed - check email/password"
    except smtplib.SMTPException as e:
        return False, f"SMTP error: {str(e)}"
    except Exception as e:
        return False, str(e)

def send_email_threaded(recipient_email, subject, body, sender_email, sender_password):
    """
    Send email in a separate thread
    
    Args:
        recipient_email (str): Recipient's email address
        subject (str): Email subject
        body (str): Email body
        sender_email (str): Sender's email
        sender_password (str): Sender's password
    """
    result = send_email_to_recipient(recipient_email, subject, body, sender_email, sender_password)
    
    if result is True:
        stats.increment_successful()
        print(f" Email sent successfully to: {recipient_email}")
    else:
        stats.increment_failed(recipient_email, result[1] if isinstance(result, tuple) else "Unknown error")
        print(f" Failed to send to {recipient_email}: {result[1] if isinstance(result, tuple) else result}")

def send_bulk_emails(recipients_list, subject, body, sender_email, sender_password, max_threads=10):
    """
    Send bulk emails to multiple recipients using threading
    
    Args:
        recipients_list (list): List of recipient email addresses
        subject (str): Email subject
        body (str): Email body
        sender_email (str): Sender's email
        sender_password (str): Sender's password
        max_threads (int): Maximum number of concurrent threads (default: 10)
    """
    stats.total = len(recipients_list)
    stats.start_time = time.time()
    
    print("=" * 70)
    print("📧 EMAIL AUTOMATION SYSTEM - BULK SENDER")
    print("=" * 70)
    print(f"Total Recipients: {stats.total}")
    print(f"Subject: {subject}")
    print(f"Max Concurrent Threads: {max_threads}")
    print("=" * 70)
    print()
    
    threads = []
    
    # Create and start threads
    for recipient in recipients_list:
        # Wait if we have max threads running
        while threading.active_count() > max_threads + 1:
            time.sleep(0.1)
        
        # Create thread for each recipient
        thread = threading.Thread(
            target=send_email_threaded,
            args=(recipient, subject, body, sender_email, sender_password)
        )
        thread.daemon = True
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    stats.end_time = time.time()
    
    # Print summary
    print_summary()

def send_sequential_emails(recipients_list, subject, body, sender_email, sender_password):
    """
    Send emails sequentially (one after another)
    Slower but more stable for large lists
    
    Args:
        recipients_list (list): List of recipient email addresses
        subject (str): Email subject
        body (str): Email body
        sender_email (str): Sender's email
        sender_password (str): Sender's password
    """
    stats.total = len(recipients_list)
    stats.start_time = time.time()
    
    print("=" * 70)
    print(" EMAIL AUTOMATION SYSTEM - SEQUENTIAL SENDER")
    print("=" * 70)
    print(f"Total Recipients: {stats.total}")
    print(f"Subject: {subject}")
    print("Sending emails sequentially...")
    print("=" * 70)
    print()
    
    for i, recipient in enumerate(recipients_list, 1):
        print(f"[{i}/{stats.total}] Sending to {recipient}...", end=" ")
        
        result = send_email_to_recipient(recipient, subject, body, sender_email, sender_password)
        
        if result is True:
            stats.increment_successful()
            print("")
        else:
            stats.increment_failed(recipient, result[1] if isinstance(result, tuple) else "Unknown error")
            print(f" ({result[1] if isinstance(result, tuple) else result})")
        
        # Small delay between emails to avoid rate limiting
        time.sleep(0.5)
    
    stats.end_time = time.time()
    print_summary()

def print_summary():
    """Print sending statistics and summary"""
    print()
    print("=" * 70)
    print(" SENDING SUMMARY")
    print("=" * 70)
    print(f"Total Recipients:    {stats.total}")
    print(f"Successful:          {stats.successful} ")
    print(f"Failed:              {stats.failed} ")
    print(f"Success Rate:        {(stats.successful/stats.total*100):.1f}%" if stats.total > 0 else "N/A")
    print(f"Duration:            {stats.get_duration():.2f} seconds")
    print("=" * 70)
    
    if stats.failed_list:
        print("\n  FAILED EMAILS:")
        for item in stats.failed_list:
            print(f"  • {item['email']}: {item['reason']}")
    
    print()


# MAIN EXECUTION
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Email Automation System")
    parser.add_argument('--mode', choices=['bulk', 'sequential'], default='bulk',
                        help='Sending mode: bulk (threaded) or sequential')
    parser.add_argument('--threads', type=int, default=10,
                        help='Max concurrent threads for bulk mode (default: 10)')

    args = parser.parse_args()

    print("\n Starting Email Automation System...\n")

    if args.mode == 'bulk':
        print(f"Mode: Bulk (Threaded) - Max Threads: {args.threads}")
        send_bulk_emails(
            recipients_list=RECIPIENTS,
            subject=EMAIL_SUBJECT,
            body=EMAIL_BODY,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            max_threads=args.threads
        )
    else:
        print("Mode: Sequential")
        send_sequential_emails(
            recipients_list=RECIPIENTS,
            subject=EMAIL_SUBJECT,
            body=EMAIL_BODY,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD
        )

    print("\n Email automation process completed!")
