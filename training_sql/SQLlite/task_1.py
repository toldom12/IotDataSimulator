import sqlite3
con = sqlite3.connect("data_logs.db")

cursor = con.cursor()

"""
[{
  "device_id": 0,
  "device_status": "Disconnected",
  "battery_status": 50,
  "motion_status": 0,
  "timestamp": 199999
},

"""

pass

def create_base():
    cursor.execute(
        """
        CREATE TABLE sensors_logs (
        DeviceId INTEGER PRIMARY KEY,
        Device_status varchar(255) NOT NULL, 
        Battery_status INTEGER, 
        MotionStatus INTEGER 
        );
        """
    )

    con.commit()
    cursor.close()

def insert_data():
    """
    INSERT INTO sensors_logs
    (DeviceId, Device_status, Battery_status, MotionStatus)
    VALUES (1, "ACTIVE", 87, 0);
    """

    for i in range(40):

        cursor.execute(
            """
            INSERT INTO sensors_logs 
            (DeviceId, Device_status, Battery_status, MotionStatus)
            VALUES (?,?,?,?)
            """, (1 * i,"ACTIVE" if i % 2 == 0 else 'INACTIVE', 87 * i, 1 * i)
        )

    con.commit()

def read_data():
    cursor.execute(
        """
        SELECT DeviceId, Device_status, Battery_status FROM sensors_logs 
        """
    )
    rows = cursor.fetchall()
    print(rows)


def where_table_battery_status():
    cursor.execute(
        """
        SELECT DeviceId, Battery_status 
        FROM sensors_logs
        WHERE Battery_status < 300
        """
    )
    rows = cursor.fetchall()
    print(rows)



def where_txt():
    cursor.execute(
        """
        SELECT DeviceId, Device_status
        FROM sensors_logs
        WHERE Device_status = 'ACTIVE'
        """
    )

    rows = cursor.fetchall()
    print(rows)

def two_conditions():
    cursor.execute("""
    SELECT DeviceId, Device_status,Battery_status 
    FROM sensors_logs
    WHERE Device_status = 'ACTIVE' AND  Battery_status < 300 
    """)
    row = cursor.fetchall()
    print(row)

def avg_data():
    cursor.execute(
        """
        SELECT DeviceId, AVG(Battery_status)
        FROM sensors_logs 
        GROUP BY DeviceID 
        """
    )
    sum = cursor.fetchall()
    print(sum)



if __name__ == '__main__':
    avg_data()


    pass





