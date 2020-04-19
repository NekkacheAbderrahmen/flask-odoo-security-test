import sqlite3

db_conn = sqlite3.connect('conpany.db')

db_conn.execute('''CREATE TABLE COMPANY_TAB1
            (user_names     CHAR        NOT NULL,
            s_keys          CHAR         NOT NULL);''')
db_conn.execute("INSERT INTO COMPANY_TAB1 (user_names,s_keys) \
      VALUES ('abderrahmen','1234')");

db_conn.execute("INSERT INTO COMPANY_TAB1 (user_names,s_keys) \
      VALUES ('nor','2345')");

db_conn.execute("INSERT INTO COMPANY_TAB1 (user_names,s_keys) \
      VALUES ('younes','3456')");

db_conn.execute("INSERT INTO COMPANY_TAB1 (user_names,s_keys) \
      VALUES ('mouhamed','4567')");
db_conn.commit() 