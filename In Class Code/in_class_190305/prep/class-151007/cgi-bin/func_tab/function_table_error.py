'''
Created on Oct 16, 2013

Error page for the function_table script


@author: ben
'''
##   func(Object... args)

def page(*messages):
    print( "Content-Type: text/html; charset=UTF-8")
    print( "")
    
    print( '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>{}</title>
            <link rel="stylesheet" type="text/css" href="/style1.css"/>
        </head>
        <body>
    '''.format("Function Table: Error"))

    print( "<h1>There was an input error!</h1>")
    
    for message in messages:
        print( "<h2 style='color:red'>", message, "</h2>")
        
    print( "<h3>Backup to the entry page and try again!</h3>")
    
    print( '''
      </body>
    </html>
    ''' )