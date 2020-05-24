- Install Docker
- Start Docker Services
- Create A folder to store docker volumes
- Create required folder such as
  - `mosquitto/config/`
  - `mosquitto/log`
  - `mosquitto/data`
- And Files such as
  - `mosquitto/config/mosquitto.conf`
  - `mosquitto/log/mosquitto.log`
  - `mosquitto/password.txt`
  - `mosquitto/acl.acl`
- Add required config to `mosquitto/config/mosquitto.conf` file.
- Initial config:
```
# Managing persistence

persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log

#Authorization

allow_anonymous false
password_file /mosquitto/password.txt
acl_file /mosquitto/acl/acl
```
- Add username:password to `/mosquitto/passwords.txt `
  - Multiple enteries separated by new line
  - Use ```mosquitto_passwd -U password.txt``` to convert the file into encrypted form.
    - Can be done on separate system and then copied over.
- Add required fields to `acl.acl`
- Example:
```
# Give user1 full access to everything
user user1
topic readwrite ## Allow user2 read/write to topic foo/bar/baz
user user2
topic foo/bar/## Allow user3 read to topic foo/bar/baz
user user3
topic read foo/## Allow jaythree read/write to anything
user jaythree
topic #

```
- GO to folder which has `mosquitto` folder
- Run Docker Command: - `sudo  docker run -it  -p 1883:1883 -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto`
- Install mosquitto on local system to test

- PUB_SUB Example https://steve.fi/hardware/d1-pub-sub/
- Password Setup Example http://www.steves-internet-guide.com/mqtt-username-password-example/
- File Setup Example https://blog.feabhas.com/2020/02/running-the-eclipse-mosquitto-mqtt-broker-in-a-docker-container/
- ACL Setup Example https://medium.com/jungletronics/mosquitto-acls-ac062aea3f9