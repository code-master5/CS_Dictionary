import sqlite3
import re

def regexp(expr,item):
    reg = re.compile(expr)
    return reg.search(item) is not None


def main(adv_res,query):

    mydb = sqlite3.connect("db_gen/cs_terms.db")
    mydb.create_function("REGEXP", 2, regexp)
    cur = mydb.cursor()
    res_set = set()

    if adv_res==0:
        #start only search results
        regex = r'''"^%s"'''%(query.capitalize())
        cur.execute('select * from term_def where term REGEXP %s' %(regex))
        results = cur.fetchall()
        res_set = set(results)

        regex = r'''"^%s"'''%(query.lower())
        cur.execute('select * from term_def where term REGEXP %s' %(regex))
        results = cur.fetchall()
        res_set = set.union(res_set,set(results))

        regex = r'''"^%s"'''%(query.upper())
        cur.execute('select * from term_def where term REGEXP %s' %(regex))
        results = cur.fetchall()
        res_set = set.union(res_set,set(results))

    else:
        #advanced search results
        regex = r'''"%s"'''%(query.capitalize())
        cur.execute('select * from term_def where term REGEXP %s' %(regex))
        results = cur.fetchall()
        res_set = set(results)

    	regex = r'''"%s"'''%(query.lower())
        cur.execute('select * from term_def where term REGEXP %s' %(regex))
        results = cur.fetchall()
        res_set = set.union(res_set,set(results))

	regex = r'''"%s"'''%(query.upper())
        cur.execute('select * from term_def where term REGEXP %s' %(regex))
        results = cur.fetchall()
        res_set = set.union(res_set,set(results))

	mydb.commit()
	mydb.close()
    res_set = list(res_set)
    return res_set


