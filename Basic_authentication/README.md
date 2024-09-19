# Basic Authentication
## General
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

- authentication is the process of verifying user or device who they say ther are. Sometimes a requirement to access resources on information.
- Base64 is a binary, represents binary data  in ASCII string format, designed to carry data stored in binary format across the channels. 
- to encode string in Base64,you convert str into byte like objects. 
- Basic authentication is a method of user authentication involving sending username and password with each request to a server or service.
- Autherization header is send by encoding username and password using base64, add prefix "Basic: to encoded string, setting value of HTTP authorization header to final str.
