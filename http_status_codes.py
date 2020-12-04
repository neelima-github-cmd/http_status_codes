#Program to display http status codes

Main_Classification_dict = {
#Broad classification
"1xx": "Informational",
"2xx": "Success",
"3xx": "Redirection",
"4xx": "Client Error",
"5xx": "Server Error"
}

#-------------------------------------
_1xx_Informational_dict = {
#1xx Informational sub classification
"100": "Continue",
"101": "Switching Protocols",
"102": "Processing (WebDAV)"
}

#-----------------------------------
_2xx_Success_dict = {
#2xx Success sub classification
"200": "OK",
"201": "Created",
"202": "Accepted",
"203": "Non-Authoritative",
"204": "No Content",
"205": "Reset Content",
"206": "Partial Content",
"207": "Multi status",
"208": "Already Reported(WebDAV)",
"226": "IM Used"
}
#-------------------------------------
_3xx_Redirection_dict = {
#3xx Redirection
"300": "Multiple Choices",
"301": "Moved Permanently",
"302": "Found",
"303": "See Other",
"304": "Not Modified",
"305": "Use Proxy",
"306": "(Unused)",
"307": "Temporary Redirect",
"308": "Permanent Redirect (experimental)"
}

#--------------------------------------
_4xx_Client_Error_dict = {
#4xx Client Error
"400": "Bad Request",
"401": "Unauthorized",
"402": "Payment Required",
"403": "Forbidden",
"404": "Not Found",
"405": "Method not allowed",
"406": "Not Acceptable",
"407": "Proxy Authentication Required",
"408": "Request Timeout",
"409": "Conflict",
"410": "Gone",
"411": "Length Required",
"412": "Precondition Failed",
"413": "Request Entity too large",
"414": "Request UR Too long",
"415": "Unsupported Media Type",
"416": "Requested Range Not Satisfiable",
"417": "Expectation failed",
"418": "I'm a teapot(RFC 2324)",
"420": "Enhance your Calm(Twitter)",
"422": "Unprocessable Entity(WebDAV)",
"423": "Locked(WebDAV)",
"424": "Failed Dependancy(WebDAV)",
"425": "Reserved for WebDAV",
"426": "Upgrade Required",
"428": "Precondition required",
"429": "Too Many requests",
"431": "Request Header fields too large",
"444": "No Response(Nginx)",
"449": "Retry with (Microsoft)",
"450": "Blocked by Windows Parental Controls(Microsoft)",
"451": "Unavailable for Legal resons",
"499": "Client Closed Request(Nginx)"
}

#--------------------------------------------
_5xx_Server_Error_dict = {
"500": "Internal Server Error",
"501": "Not Implemented",
"502": "Bad Gateway",
"503": "Service Unavailable",
"504": "Gateway Timeout",
"505": "HTTP Version Not Supported",
"506": "Variant Also Negotiates (Experimental)",
"507": "Insufficient Storage(WebDAV)",
"508": "Loop Detected(WebDAV)",
"509": "Bandwidth Limit Exceeded(Apache)",
"510": "Not Extended",
"511": "Network authentication Required",
"598": "Network read timeout error",
"599": "Network connect timeout error"
}

print("\nMain Classification",Main_Classification_dict)
#Read input from user
http_code = str(input("\nPlease enter HTTP code: "))

#print the http code 
print("\nThe entered HTTP code is:",http_code)

print("\nDetails for the code is:")

#print("\n")
if http_code in _1xx_Informational_dict :
    print(http_code,":",_1xx_Informational_dict[http_code])
elif http_code in _2xx_Success_dict :
    print(http_code,":",_2xx_Success_dict[http_code])
elif http_code in _3xx_Redirection_dict :
    print(http_code,":",_3xx_Redirection_dict[http_code])
elif http_code in _4xx_Client_Error_dict :
    print(http_code,":",_4xx_Client_Error_dict[http_code])
elif http_code in _5xx_Server_Error_dict :
    print(http_code,":",_5xx_Server_Error_dict[http_code])
else :
    print("Invalid http code entered")


