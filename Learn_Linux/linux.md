# Learn Linux

## Reirection and Appending
#### What does > do?
The > char will send the input to a new file or overwrite an existing file.
#### How is appending different?
Using >>  will send the input to a new file or *append it to* an existing file.
#### Give an example of a command where it appends to a file
```bash
echo "This is text" >> log.txt
```

## Piping
####  What is piping?
Piping is a way of redirecting output from one command to the input of another. Piping allows for continous datastreams without having to write to temporary intermediate files.
#### How is piping different to redirection using > or >>?
The > and >> characters are used to redirect output to a file/stream, not to another command.
#### What character is used for piping?
```|```
#### Give an example of a command that using piping once
```bash
tree -L 3 | more
```
#### Give an example of a command that using piping twice
```bash
more file.txt | head -3 | tail -2
```
#### Give an example of a command that using piping twice, than sends the output to a file
 ```bash
more file.txt | head -3 | tail -2 > lines_2_and_3.txt
 ```

# Streams
#### What is a stream in Linux?
A fancy queue of data going between IO devices and software.
#### What are the 3 data streams?
stdin, stdout, and stderr 
#### Create a new file new.txt and run the command ls missing_directory new.txt - this should give output to two different streams. How can we direct each stream to a file (one at a time)?
```bash
ls missing_directory new.txt 1>log.txt 2>err_log.txt
```
#### How can we direct both 2 output streams to a file?
```bash
ls missing_directory new.txt 1>>log.txt 2>>log.txt
```
#### Which stream is directed to a file by default?
stdout
#### How can we direct both output streams to a file in one command?
```bash
ls missing_directory new.txt > log.txt 2>&1
```