from file_organizer import organize_files
from email_sender import send_report
from excel_merger import merge_excels

def main():
    print("Running automation scripts...")
    organize_files()
    merge_excels()
    send_report()
    print("✅ All tasks completed!")

if __name__ == "__main__":
    main()
