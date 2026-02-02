import shutil
import datetime
source="C:/Users/chari/Downloads/cherry.txt"
backup=f"C:/Users/chari/Downloads/data_backup_{datetime.date.today()}.txt"
shutil.copy(source, backup )
print(f"Backup of {source} created at {backup} on {datetime.datetime.now()}")