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

`tg conf tgcloud -h` manages the tgcloud account credentials ( used by `tg cloud login`)

| argument | description | accepted values | default |
| -------- | ----------- | --------------- | ------- |
| -email | The email address associated with your TigerGraph Cloud account | string containing user email address | "" |
| -password | The password associated with your TigerGraph Cloud account | string containing user password | "" |

Example : 

```
tg conf tgcloud -email <mail@domain.com> -password <password>
```

### Machines ( refered to as box ) Configuration list

`tg conf list -h` lists all the configuration 
 
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
 
### Add a Machine/Box 

`tg conf add -h` add a machine to the configuration store

```
usage: tg conf add [-h] [-alias ALIAS] [-user USER] [-password PASSWORD] [-host [HOST]] [-gsPort [GSPORT]]
                   [-restPort [RESTPORT]] [-default [{y,n}]]

optional arguments:
  -h, --help            show this help message and exit
  -alias ALIAS          the name used for referring to the tigergraph Box
  -user USER            tigergraph user ( default : tigergraph )
  -password PASSWORD    tigergraph password ( default : tigergraph )
  -host [HOST]          tigergraph host ( default : http://127.0.0.1 )
  -gsPort [GSPORT]      GSQL Port ( default : 14240 )
  -restPort [RESTPORT]  Rest++ Port ( default : 9000 )
  -default [{y,n}]      Set default alias conf (y/n) ( default : n )

```


| argument | description | accepted values | default |
| -------- | ----------- | --------------- | ------- |
| -alias | The name given to the box for using it later | string  | "" |
| -user | tigergraph user by defaulttigergraph  | string  | tigergraph |
| -password | tigergraph user's password  | string  | tigergraph |
| -host | host value for tigergraph  | string  | http://127.0.0.1 |
| -gsPort | GSQL Port for tigergraph instance | string  | 14240 |
| -restPort | RestPP Port for tigergraph instance | string  | 9000 |
| -default | y/n parameter to set this configuration as default box | string  | n |

