import csv
from datetime import datetime

def load_recipients(file_path):
    recipients = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipients.append(row)
    return recipients


def load_message_template(template_path):
    with open(template_path, 'r', encoding='utf-8') as file:
        return file.read()


def send_email_simulation(recipient_name, recipient_email, message):
    print(f"--- Simulated email to {recipient_name} ({recipient_email}) ---")
    print(message)
    print("✅ Email sent successfully (simulation)\n")


def main():
    recipients = load_recipients('emails.csv')
    message_template = load_message_template('templates/message.txt')

    for recipient in recipients:
        personalized_message = message_template.format(
            name=recipient['name'],
            date=datetime.now().strftime('%B %d, %Y')
        )
        send_email_simulation(recipient['name'], recipient['email'], personalized_message)


if __name__ == "__main__":
    main()
