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

```
- Add username:password to `/mosquitto/passwords.txt `
  - Multiple enteries separated by new line
  - Use ```mosquitto_passwd -U password.txt``` to convert the file into encrypted form.
    - Can be done on separate system and then copied over.

- GO to folder which has `mosquitto` folder
- Run Docker Command: - `sudo  docker run -it  -p 1883:1883 -v $(pwd)/mosquitto:/mosquitto/ eclipse-mosquitto`
- Install mosquitto on local system to test
- PUB_SUB Example https://steve.fi/hardware/d1-pub-sub/
- Password Setup Example http://www.steves-internet-guide.com/mqtt-username-password-example/
- File Setup Example https://blog.feabhas.com/2020/02/running-the-eclipse-mosquitto-mqtt-broker-in-a-docker-container/
