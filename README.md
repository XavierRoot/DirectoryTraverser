### Directory Traverser

该脚本用于遍历指定目录及其子目录下的所有文件，并将文件路径输出到文件中。

#### 使用方法

```shell
$ python3 directory_traverser.py directory_path [-o output_file] [-x excluded_extensions] [-e included_extensions]
```

- `directory_path`：要遍历的目录路径。
- `-o, --output_file`：输出文件的路径，默认为 "output.txt"。
- `-x, --excluded_extensions`：额外指定不希望输出的文件后缀，多个后缀以逗号分隔。
- `-e, --included_extensions`：指定只输出的文件后缀，多个后缀以逗号分隔。

注意：`-x`和`-e`选项是互斥的，不能同时使用。

#### 示例

- 遍历目录并输出到默认文件（output.txt）：

  ```shell
  $ python3 directory_traverser.py /path/to/directory
  ```

- 指定输出文件名：

  ```shell
  $ python3 directory_traverser.py /path/to/directory -o result.txt
  ```

- 排除指定文件后缀：

  ```shell
  $ python3 directory_traverser.py /path/to/directory -x png,jpg,svg
  ```

- 只输出指定文件后缀：

  ```shell
  $ python3 directory_traverser.py /path/to/directory -e php,jsp,html
  ```

#### 注意事项

- 请确保已安装Python 3和必要的依赖项（tqdm）。
- 确保具有对目标目录的读取权限。

#### 其他
- directory_traverser.py为主脚本
- getPaths.py 为写脚本的过程文件，实现主要功能
- getDirs.py 为补充脚本，只输出目录列表