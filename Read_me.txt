Step 1 : Place the "file_tranfer_sftp.py" on the server(share the path).

Step 2 : Open command prompt, move to the location where the "file_tranfer_sftp.py" is placed.

         COMMAND : cd <location_of_file>\file_tranfer_sftp.py 

Step 3 : Run the command to tranfer the file local file path along with file and remote file.

         COMMAND : python file_tranfer_sftp.py <path_of_file_to_be_shared> <location_of_remote_path_along_with_file>
                  
          Example: python file_tranfer_sftp.py "/home/yashaggrawal/Desktop/testing_sftp.txt" "/CODESET/ready/testing_sftp_file.txt"

Note: location for remote path "/CODESET/ready/<same_name_as_file_in_local>"

<location_of_remote_path_along_with_file> is nothing but this code "/CODESET/ready/<same_name_as_file_in_local>"
