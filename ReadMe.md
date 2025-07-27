# How to Run the Discord Bot Script

To run the Discord bot script in the background, use the following command:

```bash
nohup ./discord_RObot/scripts/RUN.sh > /dev/null 2>&1 & disown
```

build docker image

```bash
docker build -t stu70048/discord_robot .
```

tag docker image

```bash
docker tag stu70048/discord_robot stu70048/discord_robot:tagname
```

tag docker image(copy origin docker and rename)

```bash
docker tag discord_robot stu70048/discord_robot:tagname
```

export docker image

```bash
docker save stu70048/discord_robot:tagname | gzip > discord_robot_tagname.tar.gz
```

push docker image to repo

```bash
docker push stu70048/discord_robot:tagname
```
