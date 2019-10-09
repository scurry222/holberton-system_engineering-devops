# 0x19. Postmortem
This is a fake postmortem for the [0x17-web_stack_debugging](https://github.com/scurry222/holberton-system_engineering-devops/tree/master/0x17-web_stack_debugging_3) project, made for practice. 

## Issue Summary 
00:00 (10-01-2019, 12:11 am GMT-7) through 00:37 (10-01-2019, 12:48 am GMT-7) -  recently pushed server configuration led to all servers returning 500 error on all requests. This was caused by a mistype in the wordpress settings file. All users could not access the website while update was active.

## Timeline
00:00 - Lead developer noticed webpage returning 500 error.

00:02 - ticket 0x19 was opened by developer. Servers reverted to most recent working change until error is resolved.

00:06 - ticket was responded by junior developer Scout Curry.

00:10 - `ps auxf` shown that processes are running. Testing with attaching `strace` to process IDs starts.

00:25 - after attaching `strace` to apache2 process and sending a simple get request to the server, one of the php files returned a `-1 ENOENT` error. The php file was referred to by `phpp`.

00:27 -  After using `grep` in the file location looking for the `phpp` error, it was discovered that the `wp-settings.php` file was the culprit for the incorrect reference.

00:30 - `wp-setting.php` file was manually changed to fix typo. After change and restarting apache, server now returned 200 and displayed correct website.

00:35 - Puppet script was created to remove typo using `sed` from remaining servers, and ran `puppet apply` to enact script.

00:37 - Servers were updated with new change.

## Corrective/Preventative measures
Through unittests or testing code before pushing, this problem could have been avoided. Integrate pretesting before pushing code to production.

Or, commit small changes so you can look though the change history easily on GitHub
