Web Stack

As a software engineer it's crucial to have a solid understanding of how the web stack works on top of the internet. Understanding the workflow behind typing "https://www.google.com" in your browser and pressing Enter. In this blog post, we will break down the various steps involved in this process including;
DNS request
TCP/IP
Firewall
HTTPS/SSL
Load-balancer
Web server
Application server
Database













DNS Request:
When you type "https://www.google.com" in your browser and press Enter, the first step is a DNS (Domain Name System) request. DNS is responsible for translating human-readable domain names such as "www.google.com" into IP addresses, which are unique numeric addresses that identify a specific server on the internet. Your browser sends a DNS request to a DNS server, which looks up the IP address associated with "www.google.com" and returns it to your browser.
TCP/IP:
Once your browser has the IP address of "www.google.com," it establishes a TCP/IP connection with the web server hosting the Google website. TCP/IP (Transmission Control Protocol/Internet Protocol) is a set of protocols that enable communication over the internet. TCP ensures that the data sent between your browser and the web server is reliable and error-free while IP is responsible for routing the data packets across the internet.
Firewall:
Before the TCP/IP connection is established, the web server's firewall may verify if the incoming request is legitimate and allow access to the web server. A firewall acts as a barrier that filters incoming and outgoing network traffic based on predefined rules, ensuring the security of the network.

HTTPS/SSL:
Once the TCP/IP connection is established, your browser and the web server initiate a process called a handshake to establish a secure connection using HTTPS (Hypertext Transfer Protocol Secure). HTTPS encrypts the data transmitted between your browser and the web server, ensuring that it is protected from eavesdropping or tampering. This is achieved through SSL (Secure Sockets Layer) or its successor TLS (Transport Layer Security) protocols.

Load-Balancer:
If the website you're accessing, such as Google, receives a high volume of traffic, it may be distributed across multiple web servers for load balancing. A load balancer distributes incoming network traffic across multiple servers to ensure that no single server is overwhelmed with too much load, improving the website's availability and performance.

Web Server:
Once the TCP/IP connection is established, and the SSL handshake is completed, your browser sends an HTTP request to the web server. The web server is responsible for handling the HTTP request, processing the request, and generating an HTTP response that contains the HTML, CSS, JavaScript, and other resources needed to render the web page in your browser.

Application Server:
In some cases, the web server may delegate some of the processing to an application server. An application server is a server that runs software applications, such as server-side scripts or APIs, to generate dynamic content for the web page. The application server processes the request, communicates with databases or other services, and generates the response that is sent back to the web server.

Database:
If the web page you're accessing requires data from a database, the application server communicates with the database to retrieve the necessary data. The database may contain various types of data, such as user information, search results, or product listings, which are then used to generate the dynamic content displayed on the web page.

In conclusion, when you type "https://www.google.com" in your browser and press Enter, a series of complex steps take place behind the scenes and within a millisecond.














