
from bottle import template
from functions import functionMap


page_template = """<!DOCTYPE html>
<html>
    <head>
        <title>Function Table</title>
        <link rel="Stylesheet" type="text/css" href="/static/style1.css"/>
    </head>
    <body>
        <h1>Function Table Application</h1>
        
        <p>
            This application will display chosen function values
            over a specified range.
        </p>
        
        <form method="get" action="http://localhost:8001/generate">
            <h2>Range</h2>
            <p>
                Choose the range of values to display
                and the number of rows in the table.
            </p>
            <div class="data-grid">
                <div>
                    <span>Start</span>
                    <span>
                        <input type="number" name="start" value="1" min="0"/>
                    </span>
                </div>
                <div>
                    <span>End</span>
                    <span>
                        <input type="number" name="end" value="10"/>
                    </span>
                </div>
                <div>
                    <span>Number of Rows</span>
                    <span>
                        <input type="number" name="numrows" value="11" min='2'/>
                    </span>
                </div>
            </div>
        
            <h2>Functions</h2>
            <p>
                Choose the functions to display.
            </p>
            
            <div class=" data-grid">
                %  for f in functions:
                    % v = functions[f]
                    <div>
                        <span>{{v[0]}}</span>
                        <span><input type="checkbox" name="function" value="{{f}}"/></span>
                    </div>
                % end
                
            </div>
            
            <p>
            <input type="submit" value="Create Table" />
            </p>
        </form>



    </body>
</html>"""


def page():

    rtval = template(page_template, functions=functionMap)
    return rtval
