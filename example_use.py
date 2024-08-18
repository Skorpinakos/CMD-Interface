from CmdInterface import CmdInterface 
#     ^^^ replace with where file is located/named

# Initialize 

cmd=CmdInterface()



# Send commands and capture outputs
output_hello_world = cmd.send_command( "echo Hello, World!")
output_dir = cmd.send_command( "dir")
output_dir2 = cmd.send_command( "cd ..")
output_dir3 = cmd.send_command("dir")

# Output results
print("Output of 'Hello, World!':", ''.join(output_hello_world))
print("Output of 'dir':", ''.join(output_dir))
print("Output of 'dir2':", ''.join(output_dir2))
print("Output of 'dir3':", ''.join(output_dir3))

#more commands in docs