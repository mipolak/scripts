#!/bin/bash

sftp -oIdentityFile=~/.ssh/key_sftp sftp_user@sftp_host <<EOF
rename /from/filename /to/filename
ls -l /to/
exit
EOF