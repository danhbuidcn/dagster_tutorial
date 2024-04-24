# Tutorial Template Project

```
dagster project from-example --example tutorial

cd tutorial
pip install --upgrade pip setuptools
pip install -e .
pip install -e ".[dev]"
dagster dev -p 3000
```

- Lệnh cài đặt các gói có thể không cần thiết cho mọi dự án Dagster
  - requests sẽ được sử dụng để tải dữ liệu từ internet
  - pandas là một thư viện phổ biến để làm việc với dữ liệu dạng bảng
  - matplotlib giúp dễ dàng tạo biểu đồ bằng Python
  - dagster_duckdb quản lý cách Dagster có thể đọc và ghi vào DuckDB, một kho dữ liệu đang xử lý tương tự như SQLite mà bạn sẽ sử dụng cho hướng dẫn này
  - dagster_duckdb_pandas cho phép tải dữ liệu từ DuckDB vào Pandas DataFrames
  - Faker là thư viện tạo dữ liệu giả

## Writing your first asset

- Ingest data from the Hacker News API
- Turn that ingestion into an asset
- Explore the Dagster UI
- Launch your first Dagster run manually

### Step 1: Write your first asset (topstory_ids)

### Step 2: Materialize your asset

- `Materialize [məˈtɪr.i.ə.laɪz] a Software-defined asset means to create or update it. Dagster materializes assets by executing the asset's function or triggering an integration.`

- Materialize là tạo hoặc cập nhật một Software-defined asset. Dagster hiện thực hóa nội dung bằng cách thực thi chức năng của nội dung hoặc kích hoạt tích hợp.

## Building an asset graph

- Add more assets to your Dagster project
- Connect them to finish creating the pipeline
- Give users more knowledge about the assets by adding metadata and logging

### Step 1: Adding the DataFrame asset (topstories)

- Nhập dữ liệu Hacker News story IDs và tạo DataFrame từ câu chuyện đó. Bạn sẽ kết nối nội dung hiện tại của mình với nội dung mới này để thiết lập các mối phụ thuộc và tạo biểu đồ nội dung.

### Step 2: Creating an unstructured data asset (most_frequent_words)

- Cùng với dữ liệu có cấu trúc như bảng, Dagster's asset cũng có thể là dữ liệu phi cấu trúc, chẳng hạn như tệp hoặc hình ảnh JSON.

### Step 3: Educating users with metadata (most_frequent_words)

- Software-defined Assets có thể được làm phong phú bằng các loại siêu dữ liệu (metadata) khác nhau. Mọi thứ đều có thể được sử dụng làm siêu dữ liệu cho một asset. Các chi tiết phổ biến cần thêm là:
    - Thống kê về dữ liệu, chẳng hạn như số lượng hàng hoặc hồ sơ dữ liệu khác
    - Kết quả kiểm tra hoặc khẳng định về dữ liệu
    - Hình ảnh hoặc bản xem trước dạng bảng của asset
    - Thông tin về người sở hữu asset, nơi nó được lưu trữ và liên kết đến tài liệu bên ngoài

- Metadata and Markdown
    - DataFrame đã được nhúng vào asset's metadata bằng Markdown. 
    - Mọi đoạn mã Markdown hợp lệ đều có thể được lưu trữ và hiển thị trong giao diện người dùng Dagster, bao gồm cả hình ảnh. 
    - Bằng cách nhúng biểu đồ thanh (bar chart) gồm các từ được sử dụng thường xuyên nhất làm metadata, bạn và nhóm của mình có thể trực quan hóa và phân tích nội dung most_frequent_words mà không cần rời khỏi giao diện người dùng Dagster.

## Scheduling your pipeline

- Structure your project with code locations and jobs
- Refresh your assets periodically with schedules

### Step 1: Defining what assets to update (define_asset_job)

- Job
    - Một job cho phép bạn nhắm mục tiêu lựa chọn assets để cụ thể hóa (materialize) chúng thành một hành động duy nhất. 
    - Assets có thể thuộc về nhiều job

- define_asset_job
    - tutorial/__init__.py được sử dụng làm định nghĩa cấp cao nhất cho dự án của bạn.
    - Cập nhật mã trong tệp này để thêm công việc bằng hàm define_asset_job

- About definitions
    - Dagster definitions là các thực thể mà Dagster tìm hiểu bằng cách nhập mã của bạn. Vừa rồi bạn đã sử dụng một loại definition khác: a job definition.
    - Khi dự án phát triển có thể có nhiều definition như schedules, jobs, sensors 
    - Để kết hợp các định nghĩa và giúp chúng nhận biết lẫn nhau, Dagster cung cấp một tiện ích gọi là `Definitions` object.

### Step 2: Scheduling the materializations

- ScheduleDefinition
    - Sau khi xác định được job, nó có thể được gắn vào một schedule. 
    - Trách nhiệm của schedule là bắt đầu thực hiện job được giao vào một thời điểm nhất định. 
    - Schedule được thêm vào bằng lớp ScheduleDefinition.

- Other ways to automate your pipelines -> [automation guide](https://docs.dagster.io/concepts/automation):
    - Schedule
    - Sensors

## Connecting to external services

- Việc quản lý các kết nối bên ngoài có thể gặp khó khăn, `resource` được khuyến nghị để quản lý các kết nối ra bên ngoài trong Dagster
- Resources là các Dagster object kết nối với các dịch vụ bên ngoài như Slack, Snowfake, Amazon S3.Chúng ta sẽ tìm hiểu các phần sau:
    - Xác định một resource và sử dụng nó trong một asset
    - Cấu hình resource
    - Tùy chỉnh một resource dựa trên môi trường Dagster đang chạy

### Why use resources?

- Trong topstory_ids, topstories assets, ta đã sử dụng library để liên lạc với API Hacker News. Mã này sẽ khó bảo trì hơn nếu
    - Các kết nối cần được chia sẻ trên nhiều asset
    - Bạn cần xác thực bằng dịch vụ bên ngoài một các an toàn 
    - Cấu hình cần nhất quán trong quá trình sử dụng
- Ngoài sự phức tạp của việc định cấu hình chúng, việc xây dựng data pipeline còn tạo ra nhiều kết nối với các dịch vụ bên ngoài. Việc hiểu asset nào sử dụng kết nối nào hoặc tần suất sử dụng kết nối trở nên khó khăn.

- Nên sử dụng `resource` để quản lý việc liên lạc với dịch vụ bên ngoài vì:
    - Cho phép linh hoạt trong cấu hình
    - Chuẩn hóa cách sử dụng kết nối giữa các nội dung
    - Tạo một nguồn duy nhất để giám sát các kết nối trong giao diện người dùng Dagster

### Step 1: Setting up a resource

### Step 2: Using the resource

### Step 3: Configuring the resource

### Configuring based on the environment

- use `.env` file