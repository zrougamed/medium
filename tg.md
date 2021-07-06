# TigerGraph CLI project layout

At a high level, these areas make up the `tgcli` project:
- [`conf`]  - configration Manger
- [`cloud`] - Cloud Manager
- [`box`] - TigerGraph Instance Manager

## Command-line help text

Running `tg <module> -h` displays help text for a topic. 

Example : `tg cloud -h` 

In this case, we are getting the cloud's command help 

```
usage: tg cloud [-h] {login,start,stop,terminate,archive,list,create} ...

positional arguments:
  {login,start,stop,terminate,archive,list,create}
    login               Login to tgcloud.io
    start               Start a tgcloud instance
    stop                Stop a tgcloud instance
    terminate           Terminate a tgcloud instance
    archive             Archive a tgcloud instance
    list                List all tgcloud instance
    create              Create a tgcloud instance

optional arguments:
  -h, --help            show this help message and exit
```

# How TigerGraph CLI works

## Configuration Manager


`tg conf -h` Use this command to manage TigerGraph Cloud and Instances configuration.

```
usage: tg conf [-h] {tgcloud,add,delete,list} ...

positional arguments:
  {tgcloud,add,delete,list}
    tgcloud             tgcloud user Configuration
    add                 add Configuration
    delete              delete Configuration
    list                list Configuration

optional arguments:
  -h, --help            show this help message and exit

```

### tgcloud account 

`tg cloud tgcloud -h` manages the tgcloud account credentials ( used by `tg cloud login`)

| argument | description | accepted values | default |
| -------- | ----------- | --------------- | ------- |
| -email | The email address associated with your TigerGraph Cloud account | string containing user email address | "" |
| -password | The password associated with your TigerGraph Cloud account | string containing user password | "" |

Example : 

```
tg conf tgcloud -email <mail@domain.com> -password <password>
```

### Machines ( refered to as box ) Configuration list

`tg cloud list -h` lists all the configuration 
 
 Example :
 ```
=======    tgCloud Account  ======
username: myaccount@gmail.com
password: mypassword
======= TigerGraph Instances ======
Machine: alias = defaultConf  (default)  
 host: http://localhost
 user: tigergraph
 password: tigergraph
 GSQL Port: 14240
 REST Port: 9000
Machine: alias = Machine2
 host: https://machine.i.tgcloud.io
 user: tigergraph
 password: tigergraph
 GSQL Port: 14240
 REST Port: 9000
 ```
 

 