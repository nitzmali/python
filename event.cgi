#!/Python27/python
print("Location:http://localhost/python/reservations.html")
import cgi
import pymysql
import cgi, cgitb
cgitb.enable()


def htmltop():

    print"""Content-type: text/html\n\n
          <!DOCTYPE html>
          <html lang="en">
          <head>
          <meta charset="utf-8"/>
          <title> MyPythonWebpage </title>
          </head>
          <body>"""
def connectDB():
    db = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='dbmshotel')
    cursor = db.cursor()

    return db,cursor

def stock(db,cursor,eventname,noofparticipants,type):
    db=db
    cursor=cursor
    print eventname
    print noofparticipants
    print type
    sql = 'INSERT INTO `dbmshotel`.`eventcat`(`groupname`,`partno`,`type`)VALUES("%s","%s","%s")' %(eventname,noofparticipants,type)
    #sql ='INSERT INTO `dbmshotel`.`dbmscustomer`(`dbmscustomername`,`dbmscustomerage`,`dbmscustomeremail`,`dependent`)VALUES("%s","%s","%s","%s")' %(name,age,email,usrtel)
    cursor.execute(sql)
    #print cursor.fetchall()
    db.commit()
    print "below is"

def htmltail():

    print"""<p> Ending Html tail<p></body>

    </html>"""
if __name__=="__main__":
    try:
        htmltop()
        form = cgi.FieldStorage()
        eventname = form.getvalue('eventname')
        noofparticipants = form.getvalue('noofparticipants')
        type = form.getvalue('type')

        #print name
        #print age
        db,cursor = connectDB()
        stock(db,cursor,eventname,noofparticipants,type)

        htmltail()

    except:
        cgi_print_exception()
