<p class="has-line-data" data-line-start="0" data-line-end="1">Automated Voice, SMS, and WhatsApp Messaging System</p>
<p class="has-line-data" data-line-start="3" data-line-end="5">Project Overview<br>
The Automated Voice, SMS, and WhatsApp Messaging System aims to develop a robust backend API that facilitates the sending of automated voice calls, SMS messages, and WhatsApp messages to specified phone numbers. Additionally, a user-friendly frontend form has been created to enable users to input the recipient’s phone number and select the type of message they wish to send.</p>
<p class="has-line-data" data-line-start="7" data-line-end="20">Backend Implementation<br>
Framework and Technologies Used<br>
The backend of this system is developed using Django, a powerful Python web framework. Twilio API is utilized for sending messages and WhatsApp messages to phone numbers.<br>
Twilio Integration<br>
Twilio Installation:<br>
Twilio API is installed to the project.<br>
Twilio Configuration:<br>
The Twilio API credentials, such as account_sid and auth_token, are stored securely.<br>
Backend Logic:<br>
In the whatsapp/views.py file, a function send_message(request) is defined.<br>
An if/else statement is used to handle incoming GET requests.<br>
The logic checks the message type received from the frontend form and sends the message accordingly using the Twilio API.<br>
The client object is created using Twilio credentials, and messages are sent using client.messages.create().</p>
<p class="has-line-data" data-line-start="30" data-line-end="31"><a href="http://views.py">views.py</a></p>
<p class="has-line-data" data-line-start="72" data-line-end="77">Frontend Implementation<br>
HTML (templates/index.html)<br>
Form Creation:<br>
A form is created with fields for the recipient’s phone number, message body, and a button to send the message.<br>
Html code</p>
<p class="has-line-data" data-line-start="110" data-line-end="114">CSS (Internal CSS)<br>
Styling:<br>
The CSS file is used to style the form for better user experience.<br>
CSS  Code :</p>
<p class="has-line-data" data-line-start="157" data-line-end="161">JavaScript (Internal scripts)<br>
sendMessage() Function:<br>
The JavaScript function sendMessage() is defined to handle the submission of the form and trigger the backend API for sending messages.<br>
Javascript code :</p>
<p class="has-line-data" data-line-start="176" data-line-end="178">API Endpoints<br>
<a href="http://urls.py">urls.py</a> (whatsapp-messages/messages.urls.py)</p>
<p class="has-line-data" data-line-start="182" data-line-end="186">API Parameters:<br>
phone_number (Query Parameter): The recipient’s phone number.<br>
message_type (Query Parameter): The type of message to be sent (voice, sms, or whatsapp).<br>
message_body (Query Parameter): The content of the message.</p>
<p class="has-line-data" data-line-start="189" data-line-end="191">Localhost<br>
<a href="http://127.0.0.1:8000/hello">http://127.0.0.1:8000/hello</a></p>
<p class="has-line-data" data-line-start="192" data-line-end="194">Ngrok<br>
https://25e7-2402-e280-2257-2ce-917d-318-a9b7-d67a</p>
<p class="has-line-data" data-line-start="195" data-line-end="197">Creating a secure tunnel  local web server and a public URL :<br>
In this project, my local web server to the Twilio API, which required internet access. My web server was running on localhost, which means it was only accessible from my own computer and not from the internet. However, the Twilio API was running on the internet, so I needed a way to communicate with it from my web server. To solve this problem, I used Ngrok, a tool that creates a secure tunnel between my local web server and a public URL that anyone can access. Ngrok also handled the communication between my web server and Twilio, so I could send and receive messages through the tunnel. Using Ngrok, I was able to host my web server online and use the Twilio API to send automated voice calls, SMS messages, and WhatsApp messages to phone numbers.</p>
<p class="has-line-data" data-line-start="201" data-line-end="202">Sandbox Configuration</p>
<p class="has-line-data" data-line-start="210" data-line-end="212">Expected Responses :<br>
Whatsapp :</p>
<p class="has-line-data" data-line-start="237" data-line-end="238">Voice Call :                                                            SMS :</p>
<p class="has-line-data" data-line-start="251" data-line-end="254">Conclusion<br>
The Automated Voice, SMS, and WhatsApp Messaging System combines the power of Django and Twilio API to provide a seamless solution for sending automated messages through various channels. The frontend form ensures a user-friendly experience, while the backend logic efficiently handles message types and content. Proper styling enhances the overall presentation of the messaging system.<br>
Feel free to extend and customize this documentation based on additional features or specific requirements for your project.</p>
