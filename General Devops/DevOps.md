# General DevOps Notes

### Monolith vs 2-Tier Architecture
A monolith is a big ol system running everything on one machine. There may be multiple layers (e.g. ui, logic, database) in the monolith. It's hard to scale, and if you have a database you might have to rewrite a lot of code to have that work across multiple instances.

### Reverse Proxy
 - Can be a server which sits in front of backend servers, redirecting traffic and shielding internal servers from attack
 - Allows a single domain to have multiple back-end servers by having the reverse-proxy redirecting traffic where it's needed
   - Single external IP allows for a "friendly" url -> no port numbers
 - The reverse proxy can do load-balancing
 - It can handle caching as well
 - Can handle SSL encrryption and user authentication