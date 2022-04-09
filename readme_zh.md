# Waifu duel py

给 Master Duel 替换卡图的工具

[中文文档](./readme_zh.md)

## 使用方法

#### 1. [**建议**] 备份所有数据

```shell
waifu-duel backup-all
```

备份游戏目录里所有卡图数据，用于备份。强烈建议在第一次使用的时候，进行一次全部备份。

> 注意，一旦替换过游戏数据，该命令备份的数据也将是被修改后的数据。

#### 2. 创建一个工作目录

工作目录可以作为一个主题进行区分每个主题包，比如你可以新建一个目录作为手坑主题。

#### 3. 准备替换的卡图，并进行重命名

将替换的卡图放入工作目录，并命名为对应替换卡片的`card id`。

可以使用 `waifu-duel search [keyword]` 检索卡片信息和 `card id`（支持日文、中文、英文，数据来源：[ygocdb](https://ygocdb.com/)）

> 图片格式建议，512x512 像素, PNG 图片格式, RGBA 彩色通道
> 
> 从 v0.2.0 起，可以自动调整图片到合适的大小，请确保图片的长、宽相同

#### 4. [**建议**] 备份被替换的资源文件

```shell
waifu-duel backup [work directory]
```

将要被替换的资源文件备份到工作目录下，所备份的文件会根据你提供的 card id 进行选择。

如果游戏中的资源文件已被替换过，可以通过以下命令从 “步骤1” 中备份的文件中提取备份。

```shell
waifu-duel backup [work directory] [backup-all directory]
```

#### 5. 生成资源包

```shell
waifu-duel build [work directory]
```

将你提供的图片压缩成资源文件，并按结构输出到 `output` 目录下。

#### 6. 安装数据

```shell
waifu-duel install [work directory]
```

复制工作目录下 `output` 文件夹里所有数据到 `steam/steamapps/common/Yu-Gi-Oh! Master Duel/LocalData/xxxxx/0000`


## 已知问题

+ 生成的资源文件偏大，可能是图片压缩算法的问题

## 免责声明

资源替换是修改客户端的行为，请使用者自行判断并承担相应后果。
