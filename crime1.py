import mysql.connector 
import time
from datetime import date


global conn,cursor
conn = mysql.connector.connect(host='localhost',database='crime',user='root',password='1234')
cursor = conn.cursor()

def clear():
  for _ in range(5):
     print()
def display_records():
    cursor.execute('select * from crime_record;')
    records = cursor.fetchall()
    for row in records:
        print(row)

def login():
    while True:
        clear()
        uname = input('Enter your id :')
        upass = input('Enter your Password :')
       cursor.execute('select * from login where name="{}" and pwd ="{}"'.format(uname,upass))
        cursor.fetchall()
        rows = cursor.rowcount
        if rows!=1:
            print('Invalid Login details..... Try again')
        else:
            print('You are eligible for operating this system............')
            print('\n\n\n')
            print('Press any key to continue...............')
            break
def add_crime_type():
    clear()
    offence_name = input('Enter offence Name : ')
    ipc_section =  input('Enter IPC section applied for this offence : ')
    comment = input('Enter Any other information : ')  
    sql = 'insert into crime_type(offence_name,ipc_section,comment) values("{}","{}","{}");'.format(offence_name,ipc_section,comment)
    cursor.execute(sql)
    conn.commit()
    print('\n\n New Offence Type added....')
    wait= input('\n\n\nPress any key to continue............' )
def add_record():
    clear()
    Id=int(input("FIR number"))
    crime_date = input('Enter Crime Date (yyyy/mm/dd) : ')
    
    offence_id = input('Enter Offence_id : ')
    compaint_by = input('Enter Name of complainee : ')
    address  = input('Enter Complainee Address :')
    phone  = input('Enter Complainee Phone No :')
    status  = input('Enter current status :')
    update_date = date.today()
    sql = 'insert into crime_record(Id,c_date,offence_type,compaint_by,address,phone_no,status,update_date) values \
            ({},"{}",{},"{}","{}","{}","{}","{}");'.format(Id,crime_date, offence_id,compaint_by,address,phone,status,update_date) 
    cursor.execute(sql)
    conn.commit()
    print('\n\n New Crime Record added....')

    cursor.execute('select max(id) from crime_record;')
    no = cursor.fetchone()
    print(' Your complaint  No is : {} \n\n\n'.format(no[0]))
    wait = input('\n\n\nPress any key to continue............')
def modify_crime_type_record():
    
    clear()
    print(' M O D I F Y    C R I M E  T Y P E  S C R E E N ')
    print('1.  Offence Name \n')
    print('2.  IPC Section \n')
    print('3.  Comment  \n')
    choice = int(input('Enter your choice :'))
    field=''
    if choice==1:
        field='offence_name'
    if choice==2:
        field='ipc_section'
    if choice==3:
        field='comment'

    crime_id = input('Enter Crime Type ID :')
    value = input('Enter new values :')
    sql = 'update crime_type set '+ field +' = "' + value +'" where id ='+ crime_id +';'
    cursor.execute(sql)
    conn.commit()
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')


def modify_record():
    clear()
    print(' M O D I F Y    C R I M E  R E C O R D  S C R E E N ')
    print('1.  Crime date \n')
    print('2.  Offence Type  \n')
    print('3.  Complaint By  \n')
    print('4.  Address  \n')
    print('5.  Phone No  \n')
    print('6.  Status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'c_date'
    if choice ==2:
        field = 'offence_type'
    if choice == 3:
        field = 'compaint_by'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'phone_no'
    if choice == 6:
        field = 'status'
    
    print('\n\n\n')
    crime_id = input('Enter Crime Record ID  :')
    value = input('Enter new values :')
    sql = 'update crime_record set ' + field + \
        ' = "' + value + '" where id =' + crime_id + ';'
    cursor.execute(sql)
    conn.commit()
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')
def search_menu():
    clear()
    print(' S E A R C H    C R I M E  R E C O R D  S C R E E N ')
    print('1.  Crime date \n')
    print('2.  Offence Type  \n')
    print('3.  Complaint By  \n')
    print('4.  Address  \n')
    print('5.  Phone No  \n')
    print('6.  Status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'c_date'
    if choice == 2:
        field = 'offence_type'
    if choice == 3:
        field = 'compaint_by'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'phone_no'
    if choice == 6:
        field = 'status'
    value = input('Enter value to search :')
    if choice == 2:
        sql = 'select cr.id,c_date,offence_name,compaint_by,address,phone_no,status,update_date \
          from crime_record cr, crime_type ct where cr.offence_type = ct.id \
          AND ' + field + '= ' + value + ';'
    else:
        sql = 'select cr.id,c_date,offence_name,compaint_by,address,phone_no,status,update_date \
          from crime_record cr, crime_type ct where cr.offence_type = ct.id \
          AND ' + field + '= "' + value + '";'

    cursor.execute(sql)
    results = cursor.fetchall()
    records = cursor.rowcount
    for row in results:
        print(row)
    if records < 1:
        print('Record not found \n\n\n ')
    wait = input('\n\n\nPress any key to continue......')    
    
def report_menu():
    
    clear()
    print(' C R I M E  R E C O R D  R E P O R T S  ')
    print('1.  Crime date \n')
    print('2.  Offence Type  \n')
    print('3.  Complaint By  \n')
    print('4.  Address  \n')
    print('5.  Phone No  \n')
    print('6.  Status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'c_date'
    if choice == 2:
        field = 'offence_type'
    if choice == 3:
        field = 'compaint_by'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'phone_no'
    if choice == 6:
        field = 'status'
    value = input('Enter value  :')

    if choice ==2:
        sql = 'select cr.id,c_date,offence_name,compaint_by,address,phone_no,status,update_date \
          from crime_record cr, crime_type ct where cr.offence_type = ct.id \
          AND ' + field + '= ' + value + ';'
    else:
        sql = 'select cr.id,c_date,offence_name,compaint_by,address,phone_no,status,update_date \
          from crime_record cr, crime_type ct where cr.offence_type = ct.id \
          AND ' + field + '= "' + value + '";'

    cursor.execute(sql)
    results = cursor.fetchall()
    records = cursor.rowcount
   
    page = 1
    total_pages = records//20
    if records % 20 != 0:
        total_pages += 1
    if records < 1:
        print('Record not found \n\n\n ')
    else:
        clear()
        print('Report on :',field,':',value )
        print('Page :',page,'/',total_pages)
        print('-'*100)
        print('{} {} {} {} {} {} {} {}'.format('id','Crime Date','Crime','Complaint By','Address','Phone','Status','Update On'))
        print('-'*100)
        line=1
        for row in results:
            print('{} {} {} {} {} {} {} {}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            line = line+1
            if line>=21:
                wait = input('Press any key to continue.........')
                line = 1
                page +=1
                print('Report on :', field, ':', value)
                print('Page :',page,'/',total_pages)
                print('-'*100)
                print('{} {} {} {} {} {} {} {}'.format('id', 'Crime Date', 'Crime',
                                                       'Complaint By', 'Address', 'Phone', 'Status', 'Update On'))
        print('-'*100)
    
    wait = input('\n\n\nPress any key to continue......')


def main_menu():
    clear()
    login()
    clear()
    
    while True:
      clear()
      print(' C R I M E   R E C O R D    I N F O R M A T I O N   S Y S T E M')
      print('*'*100)
      print("\n1.  Add New Record")
      print("\n2.  Add New Crime Type")
      print('\n3.  Modify Crime Type Record')
      print('\n4.  Modify Crime Record')
      print('\n5.  Search Crime Database')
      print('\n6.  Report menu')
      print('\n7.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_record()

      if choice == 2:
        add_crime_type()

      if choice == 3:
        modify_crime_type_record()
      
      if choice == 4:
        modify_record()

      if choice == 5:
        search_menu()

      if choice == 6:
        report_menu()
      
      if choice == 7:
        break
main_menu()

 
    
   
