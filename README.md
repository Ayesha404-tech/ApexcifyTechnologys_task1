# Email Automation System 📧

A powerful and flexible email automation system that allows you to send bulk emails to multiple recipients simultaneously with professional error handling and statistics tracking.

## ✨ Features

### Core Features
- ✅ **Bulk Email Sending**: Send emails to 20+ recipients at once (scalable to 100+)
- ✅ **Multiple Sending Methods**: 
  - **Threaded**: Fast parallel sending (recommended for 50+ recipients)
  - **Sequential**: Stable sending one at a time
- ✅ **Error Handling**: Comprehensive error handling with detailed failure reports
- ✅ **Statistics Tracking**: Real-time success/failure metrics and duration tracking
- ✅ **Professional Formatting**: HTML-ready email with timestamps and proper headers
- ✅ **Thread Management**: Configurable concurrent threads to prevent rate limiting
- ✅ **Email Validation**: Checks for authentication and SMTP errors

### Advanced Features
- 🔒 **Secure Connection**: Uses TLS encryption for Gmail SMTP
- 📊 **Detailed Reporting**: Shows success rate, failed emails with reasons
- ⚡ **Rate Limiting**: Built-in delays to avoid Gmail rate limits
- 🎯 **Flexible Configuration**: Easy to modify sender, subject, and body
- 🔄 **Retry-Ready**: Can be extended with retry logic for failed emails

## 📋 Prerequisites

- **Python 3.6+**
- **Gmail Account** with App Password enabled
- **Required Libraries**: All use Python built-in modules (smtplib, email, threading)

## 🚀 Setup Instructions

### 1. Gmail Setup (Important!)

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Navigate to **Security** (left sidebar)
3. Enable **2-Step Verification** if not already enabled
4. Go to **App Passwords** (appears after 2FA is enabled)
5. Select "Mail" and "Windows Computer"
6. Copy the generated 16-character password
7. Update `SENDER_PASSWORD` in the script with this password

### 2. Configuration

Edit `send_emails.py` and update these variables:

```python
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"  # 16-char password from step 1

RECIPIENTS = [
    "recipient1@example.com",
    "recipient2@example.com",
    # ... add up to 100+ emails
]

EMAIL_SUBJECT = "Your Subject Here"
EMAIL_BODY = """Your email content here"""
```

## 💻 Usage

### Run the Script

```bash
python send_emails.py
```

### Choose Sending Method

When prompted, select:
- **Option 1**: Bulk (Threaded) - Faster for 50+ recipients
- **Option 2**: Sequential - More stable for smaller lists

### For Bulk Method
```
Select sending method:
1. Bulk (Threaded) - Faster, up to 100+ recipients
2. Sequential - Slower but more stable

Enter choice (1 or 2): 1
Enter max concurrent threads (default 10): 15
```

## 📊 Output Example

```
======================================================================
📧 EMAIL AUTOMATION SYSTEM - BULK SENDER
======================================================================
Total Recipients: 20
Subject: Automated Notification - Apexcify Technologies
Max Concurrent Threads: 10
======================================================================

✅ Email sent successfully to: recipient1@example.com
✅ Email sent successfully to: recipient2@example.com
✅ Email sent successfully to: recipient3@example.com
...

======================================================================
📊 SENDING SUMMARY
======================================================================
Total Recipients:    20
Successful:          20 ✅
Failed:              0 ❌
Success Rate:        100.0%
Duration:            12.45 seconds
======================================================================
```

## 🎯 Supported Recipients

- **Default**: 20 predefined recipients
- **Scalable**: Add up to 100+ recipients
- **Flexible**: Can be extended to use CSV files or databases

## 🔧 Customization

### Add More Recipients

```python
RECIPIENTS = [
    "email1@domain.com",
    "email2@domain.com",
    "email3@domain.com",
    # ... add as many as needed
]
```

### Modify Email Content

```python
EMAIL_SUBJECT = "Custom Subject"
EMAIL_BODY = """
Custom email body with:
- Multiple paragraphs
- Formatting
- Call to action
"""
```

### Adjust Thread Count

For threaded sending:
- 5-10 threads: Safe, less likely to trigger Gmail limits
- 15-20 threads: Medium speed, some rate limit risk
- 30+ threads: Fast but may get throttled by Gmail

## 📈 Performance

| Recipients | Method | Approx Time |
|-----------|--------|------------|
| 20 | Sequential | ~10s |
| 20 | Bulk (10 threads) | ~3s |
| 100 | Sequential | ~50s |
| 100 | Bulk (15 threads) | ~10s |

## ⚠️ Common Issues & Solutions

### Issue: "Authentication failed"
**Solution**: 
- Use Gmail App Password, not regular password
- Enable 2-Step Verification
- Verify credentials in script

### Issue: "SMTP error: Too many connections"
**Solution**:
- Reduce max_threads (use 5-10)
- Use Sequential method
- Gmail limits: ~100 emails/minute for new accounts

### Issue: "Port 587 connection timeout"
**Solution**:
- Check internet connection
- Verify firewall not blocking port 587
- SMTP server: smtp.gmail.com:587

## 🔐 Security Best Practices

- ✅ Never use your real Gmail password
- ✅ Always use App Password for scripts
- ✅ Enable 2-Step Verification
- ✅ Don't commit credentials to GitHub
- ✅ Use .env files for sensitive data
- ✅ Monitor account for suspicious activity

## 📝 Task Compliance

✅ **TASK 1: Email Automation System**
- ✅ Same paragraph sent to multiple recipients
- ✅ Support for 20+ predefined emails
- ✅ Can handle 100+ recipients simultaneously
- ✅ Threaded approach for parallel sending
- ✅ Error handling and statistics
- ✅ Professional implementation

## 🆘 Support

For issues:
1. Verify Gmail App Password setup
2. Check 2-Step Verification enabled
3. Test with 1-2 recipients first
4. Check internet connection
5. Review error messages in output

## 📄 License

This project is part of Apexcify Technologies portfolio.

## 👤 Author

Created by **Ayesha404-tech** - https://github.com/Ayesha404-tech
**Last Updated**: November 18, 2024  
"# ApexcifyTechnologys_task1" 
