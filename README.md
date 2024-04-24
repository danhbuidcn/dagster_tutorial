# Dagster

- Dagster là một công cụ mã nguồn mở được thiết kế để giúp các nhóm phát triển, triển khai, và quản lý các ứng dụng dựa trên dữ liệu và các luồng công việc dữ liệu (data workflows). 
- Dagster cung cấp một cách để xây dựng, chạy, và theo dõi các luồng công việc dựa trên dữ liệu một cách cấu trúc và mô-đun.

[refer](https://viblo.asia/p/dagster-la-gi-dagster-co-ban-cho-nguoi-moi-bat-dau-WR5JRvKdJGv)

`Dagster is an orchestrator that's designed for developing and maintaining data assets, such as tables, data sets, machine learning models, and reports.`


# Introduction to Software-defined assets (SDA)

- assets là một vật thể được lưu trữ lâu dài nhằm nắm bắt một số hiểu biết về thế giới. Nội dung có thể là bất kỳ loại đối tượng nào, chẳng hạn như:
  - Một table hoặc view trong database
  - Một file (như file trên máy local) hoặc lưu trữ blob như S3
  - Một model Machine Learning

# Building a DAG of assets

- Một tập hợp các asset tạo thành DAG (directed acyclic graph - biểu đồ chu kỳ có hướng), trong đó các cạnh tương ứng với sự phụ thuộc dữ liệu giữa các nội dung. DAG này giúp bạn:
  - Hiểu về sự liên quan giữa các asset.
  - Giúp làm việc với data pipeline dễ dàng, hiệu quả hơn.


# Install package

```
apt-get install python3 python3-dev python3-pip
pip install dagster dagster-webserver dagit
pip install pandas

# Thêm thư mục vào biến môi trường PATH
nano ~/.bashrc
export PATH="$PATH:/home/bui.van.thuong@sun-asterisk.com/.local/bin"
source ~/.bashrc
dagster --version
```

# Projects

## Creating Dagster project option 1 (tutorial project)

[full version](./tutorial/)

```
cd tutorial
dagster dev -p 3000
```

## Creating Dagster project option 2 (hello_dagster project)

[shortest version](/hello_dagster/)

```
cd hello_dagster
dagster dev -f hello_dagster.py -p 3001
```

## Creating dbt with Dagster project (tutorial-dbt-dagster project)

[tutorial-dbt-dagster](/tutorial-dbt-dagster/jaffle_shop)

# Note

* Trong Python, một hàm được định nghĩa với kiểu trả về là None có nghĩa là hàm đó không trả về bất kỳ giá trị nào.

# Dagster Essentials

[link](https://courses.dagster.io/courses/dagster-essentials)

# Dagster & dbt

[link](https://courses.dagster.io/courses/dagster-dbt)
