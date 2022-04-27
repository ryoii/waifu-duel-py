# Waifu duel py

A tool for replacing the card images in master duel.

[中文文档](./readme_zh.md)

## usage

#### 1. [**RECOMMEND**] backup all data

```shell
waifu-duel backup-all
```

It will back up all the game asset data that contain the card images for recovery.

It is important for you to back up the data when using this application for the first time.

> Pay attention that once you replaced the game data. This command will back up the changed data.

#### 2. Make a work directory

The work directory will be a pack for a single theme. For example, you can make a theme named hand-trap.

#### 3. Prepare the image for replacing and rename them

Put the images into the work directory and Rename the image to its card id.

Search card id by command `waifu-duel search [keyword]` (Japanese, Chinese, English are supported. Datasource: [ygocdb](https://ygocdb.com/))

> image format recommend: 512x512 pixels, format PNG, mode RGBA
> 
> Since v0.2.0, can auto-resize to appropriate size. Make sure every single image has the same width and height.

#### 4. [**RECOMMEND**] Backup the images will be replaced

```shell
waifu-duel backup [work directory] [backup-all directory]
```

Back up the asset data to work directory according to the card id you set in the work directory.

If your game asset data had been replaced, you can back up from the data that you had back up in step 1.

```shell
waifu-duel backup [work directory] [backup-all directory]
```

#### 5. Build your pack

```shell
waifu-duel build [work directory]
```

Compress your images into the asset data, and output to `output` directory.

#### 6. Install data

```shell
waifu-duel install [work directory]
```

Copy all files in `work direcoty/output` to game data location `steam/steamapps/common/Yu-Gi-Oh! Master Duel/LocalData/xxxxx/0000`


## Known issues

+ Asset data size becomes larger, but it works. It seems to be the problem of image compression algorithm.
