# Fun with Very Basic Scraping of an HTML String - Incomplete
# utils.py 
def getHTML():
    ''' 
    This is just a quicker way of grabbing the contents of the file
      VeryBasicHTMLforVeryBasicWebPage.html .
      
    We can also edit this string without affecting the original file 
    '''
    return ' \
    <!DOCTYPE html> \
    <html xmlns="http://www.w3.org/1999/xhtml"> \
    <head><title> \
        I can be scraped \
    </title></head> \
    </head> \
    <body> \
        <form method="post" action="./default.aspx" id="form1"> \
            <div class="mainContainer"> \
                <span class="mySpanClass"> \
                    Label 01                \
                </span> \
                <span class="mySpanClass"> \
                    Label 02 \
                </span> \
                <span class="mySpanClass"> \
                    <span>Label 03</span> \
                    <span>Label 03a</span> \
                </span> \
                <span> \
                    Label 04 \
                </span> \
                <table> \
                    <tr> \
                        <td> \
                            Python \
                        </td> \
                        <td> \
                            C# \
                        </td> \
                        <td> \
                            Java \
                        </td> \
                    </tr> \
                </table> \
            </div> \
        </form> \
    </body> \
    </html>'