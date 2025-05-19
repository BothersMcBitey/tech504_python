# Documenting GCP Stuff

Lookup the Google documentation on Identity-Aware Proxy (IAP) TCP forwarding and add it to your documentation. Note the steps to do with a firewall rule.

Make sure only ONE person in the group follows the steps to setup the firewall rule.
Explain: Why does only person need to do it?
- The firewall rules are set across a VPC, so if multiple people are using a VPC only one person needs to set it
  
Test SSH via the console works for you into so you can login to the VMs in your instance group.

Subtask: Stop the app running on one of your instances
Objective: Try and produce an unhealthy instance in your instance group

- SSH into one of your instances
- Stop the app running on that machine using commands
- Confirm the app is no longer running on the machine (see hints below on this if you need them)
- Check your instance group - if the health check is working as it should, it should be very quick to mark it "unhealthy" (probably 30-60 seconds) - check your health check settings to work out how long it should take
- Notice that the instance with no app running (instead responding with 502 Bad Gateway error) continues to be marked as healthy

### Use the command sudo lsof -i :3000 - find out what it does
It gives you a list of every service using the 3000 port.

### Use the command curl localhost - find out what it does
By default it asks the localhost (i.e. this machine) what's on the http port (80).


### Fix the issue that an instance is marked as healthy even though the app is stopped
Set the Health Check to use HTTP, not TCP

Subtask: Why are my instances now marked as unhealthy all the time?
Steps:

Change the health check settings back to the way they were when your instances were always marked as healthy (i.e. use TCP again) - this way, you instances will be marked as "healthy" allowing you to SSH into them
Select an instance and delete it
Allow the instance group to re-create the VM (it may take 8-10 min)
SSH into the new instance, check if the app is running
If it's not, give it a minute, then check again
Most likely, the app will not be running
After 6 min (no less), check if the app is running now
You will notice it is running
Check the processes and see how long between when the kernel processes started up compared to when the PM2 and the app run - what's the difference in time?
This means that with instances created by the instance group, there is a time delay in running the Startup Script AFTER the VM boots up Linux. Note down the time delay and Edit the instance group to allow for this:
In the "Initialization period": Instead of 60 seconds - add on the time delay and make this the new figure
Under Auto-healing "Initial delay": Instead of 120 seconds - add on the time delay and make this the new figure
Make sure "On failed health check" is on Repair instance
Save your instance group
Change your health check to use the setting you came up with the last subtask (so NOT "TCP)

Subtask: Test out your instance group
SSH into an instance now and stop the app running - check after about 30-60 seconds - has it been marked as "healthy" and does it get replaced?
Delete a VM - does it create a new "healthy" instance now after about 8-10 min?
Re-start all instances (through the instance group) - should we expect them to come back as "healthy"? What will happen if you leave them there like that?
Replace all the instances (through the instance group) - should we expect them come back as "healthy"? How long will it take for them to come up as "healthy" and why?

Clean-up once you've finished documenting

