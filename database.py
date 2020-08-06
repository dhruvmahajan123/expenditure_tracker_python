import sqlite3 as db

def init(name):
    conn=db.connect(("{xyz}.db").format(xyz=name,))
    cur=conn.cursor()
    sql = '''
    create table if not exists credit(
    date string,
    title string,
    amount number
    )
    '''
    sql2 = '''
    create table if not exists debit(
    date string,
    title string,
    amount number
    )
    '''
    cur.execute(sql)
    cur.execute(sql2)
    conn.commit()

def addCredit(name,title,amount):
    conn=db.connect(("{xyz}.db").format(xyz=name,))
    cur=conn.cursor()
    from datetime import date
    date = str(date.today())
    sql='''
    insert into credit values(
        '{}',
        '{}',
         {}
        )
    '''.format(date, title, amount)
    cur.execute(sql)
    conn.commit()

def addDebit(name,title,amount):
    conn=db.connect(("{xyz}.db").format(xyz=name,))
    cur=conn.cursor()
    from datetime import date
    date = str(date.today())
    sql='''
    insert into debit values(
        '{}',
        '{}',
         {}
        )
    '''.format(date, title, amount)
    cur.execute(sql)
    conn.commit()

def viewCredit(name):
    conn=db.connect(("{xyz}.db").format(xyz=name,))
    cur=conn.cursor()
    sql='''
        select * from credit
        '''
    cur.execute(sql)
    data= cur.fetchall()
    #cur.execute(sql2)
    #totalCredit= cur.fetchone()[0]
    conn.commit()

    return data

def viewDebit(name):
    conn=db.connect(("{xyz}.db").format(xyz=name,))
    cur=conn.cursor()

    sql='''
        select * from debit
        '''

    cur.execute(sql)
    data= cur.fetchall()
    #cur.execute(sql2)
    #totalDebit= cur.fetchone()[0]
    conn.commit()

    return data

init('xyz')
addCredit('xyz','anc',100)
print (viewCredit('xyz'))