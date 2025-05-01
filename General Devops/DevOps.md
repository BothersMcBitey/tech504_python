# General DevOps Notes

### Monolith vs 2-Tier Architecture
A monolith is a big ol system running everything on one machine. There may be multiple layers (e.g. ui, logic, database) in the monolith. It's hard to scale, and if you have a database you might have to rewrite a lot of code to have that work across multiple instances.