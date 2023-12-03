# # py -m smtpd -c DebuggingServer -n localhost:1025

# import smtplib, ssl

# port = 465
# smtp_server = "smtp.gmail.com"
# sender_email = "vrdhnr@gmail.com"
# receiver_email = "vrdhnr@gmail.com"
# password = "scfvdekkakvkyela"
# password =  "vrdavrxcmpelmclz"
# message = """\
# Subject: Tst Mail\

# cc: sexymeidk@gmail.com

# This is a test mail."""

# with smtplib.SMTP_SSL(smtp_server, port, context=ssl.create_default_context()) as server:
#     server.login(sender_email, password)
#     print(server.rcpt(receiver_email)[1].decode(errors="ignore"))
#     # server.sendmail(sender_email, receiver_email, message)

# print("End of program.")

import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "vrdhnr@gmail.com"
receiver_email = "vrdhnr@gmail.com"
password = "vrdavrxcmpelmclz"
message = """\
Subject: Tst Mail\

cc: sexymeidk@gmail.com

This is a test mail."""

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=ssl.create_default_context()) as server:
        server.login(sender_email, password)
        
        # Send the MAIL command first
        server.sendmail(sender_email, receiver_email, "MAIL FROM:<{}>".format(sender_email))
        
        # Send the RCPT command
        server.sendmail(sender_email, receiver_email, "RCPT TO:<{}>".format(receiver_email))
        
        # Send the actual email content
        server.sendmail(sender_email, receiver_email, message)
        
    print("Email sent successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

print("End of program.")
