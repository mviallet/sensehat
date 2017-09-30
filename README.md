# sensehat
An IoT application based on the Raspberry Pi with a sense HAT

# Database

To create the database:

sqlite3 sensehat.db
BEGIN;
CREATE TABLE pth (today DATE, timeofday TIME, temperature NUMERIC, pressure NUMERIC, humidity NUMERIC, location TEXT, device TEXT);
COMMIT;
.quit

# Main program
python3 Main.py will read the HAT sensors and write values to the database. Run this periodically, e.g., using Cron tables (see "crontab-example").

