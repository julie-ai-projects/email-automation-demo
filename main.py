from file_organizer import organize_files
from excel_merger import merge_excels
from email_sender import send_email

if __name__ == "__main__":
    print("⚙️ Starting automation tasks...\n")

    organize_files()
    merge_excels()
    send_email()

    print("\n🎉 All tasks completed successfully!")

