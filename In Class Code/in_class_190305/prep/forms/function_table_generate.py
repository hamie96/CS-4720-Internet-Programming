

# import requests
# from json_with_dates import loads
from bottle import run, route, static_file, request, template
# from forms import function_table_error, function_table_entry
import function_table_entry
import function_table_error
# import math
from functions import functionMap


PORT = 8001

page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Function Table</title>
    <link href="/static/style1.css" rel="stylesheet"/>
</head>
<body>

<!--
<p>start: {{start}} </p>
<p>end: {{end}}</p>
<p>number_of_rows: {{number_of_rows}}</p>
-->

<h1>Function Table</h1>
<h2>
{{number_of_rows}} rows, 
Argument range from {{start}} to {{end}}
</h2>

<table class='grid'>
    <tr>
        % for h in headers:
            <th title='{{h[1]}}'>{{h[0]}}</th>
        % end
    </tr>


    % for row in data:
        <tr>
        % for x in row:
            <td>{{x}}</td>
        % end
        </tr>
    %end
</table>

<!--<p> {{data}}</p>-->

</body>
</html>
"""

#
# functionMap = {"cube": ("Cube", "Cube function",
#                         lambda x: x*x*x),
#                "square": ("Square", "Square function",
#                           lambda x:  x*x),
#                "ln":     ("Ln", "Natural logarithm",
#                           lambda x: math.log(x)),
#                "log2":   ("Log2", "Binary log, base 2 logarithm",
#                           lambda x: math.log(x,2)),
#                "atan":   ("ArcTan", "Arctangent",
#                           lambda x: math.atan(x))
#                }


@route('/generate')
def send_request_data():
    try:
        # get values entered by user on the web page
        start = float(request.query["start"])
        end = float(request.query["end"])
        number_of_rows = int(request.query["numrows"])
        function_list = request.query.getall("function")

        func_info = [functionMap[f] for f in function_list if f in functionMap]

        # create row of headers
        headers = [('x', 'function argument')]
        for fi in func_info:
            headers.append((fi[0], fi[1]))

        # create rows of data
        # step = (end - start) / (number_of_rows - 1)
        page_data = []
        step = (end - start) / (number_of_rows - 1)
        for row in range(0, number_of_rows):
            x = row * step + start
            row_data = ["{:.3f}".format(x)]
            for fi in func_info:
                row_data.append("{:.3f}".format(fi[2](x)))

            # row_data = [x, "{:.3f}".format(fi[2](x)) for fi in funcInfo]
            # for f in functionList:
            #     if f in functionMap:
            #         row_data.append("{:.3f}".format(functionMap[f][2](x)))
            page_data.append(row_data)

        rtval = template(page_template, start=start, end=end, number_of_rows=number_of_rows,
                         data=page_data, headers=headers)
        return rtval
    except ValueError as ve:
        return function_table_error.page("One of the values you entered did not convert properly", ve)


@route('/')
def data_entry():
    # return static_file('function-entry.html', root='static')
    return function_table_entry.page()


@route('/static/<filepath:path>')
def send_static(filepath):
    print("send_static", filepath)
    return static_file(filepath, root='static')


run(host='localhost', port=PORT, debug=True)
